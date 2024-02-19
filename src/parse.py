import click
import pandas as pd
import re

from dataclasses import dataclass

from bonum_logging import log


@dataclass
class CatalogEntry:
    sheet_filename: str
    shape: str
    xls_filename: str
    sheet_name: str

    def __repr__(self):
        return (f'{self.__class__.__name__} '
                f'(sheet_filename={self.sheet_filename}, '
                f'shape={self.shape}, '
                f'xls_filename={self.xls_filename},'
                f'sheet_name={self.sheet_name})')


# SmithSystem's Clay produces these files for Bill Schaad
sharepoint_files = {
    '1. FY24 Product Sales Slicer.xlsx': ["Inv'd Items Report",
                                          "Catalog & Item Detail",
                                          "SEP 2022 Price Book",
                                          "Inv'd Items FY23",
                                          "Sheet6",
                                          "Current Cost"],
    '2. FY24 Customer Sales Slicer.xlsx': ["customers",
                                           "Fiscal Calendar",
                                           "Order History",
                                           "Zip Codes",
                                           "Sales Journal",
                                           "Sales Journal 2023",
                                           "Sales Journal 2022"],
    '3. FY24 Order Analysis.xlsx': ["Zip Codes",
                                    "Order History",
                                    "All FY20 Orders",
                                    "All FY21 Orders",
                                    "All FY22 Orders",
                                    "All FY23 Orders",
                                    "All FY24 Orders",
                                    "Historical Orders",
                                    "Customer Master",
                                    "Dates"]
}


@click.command('parse')
@click.option("-i", "--input-directory", help="location of SmithSystem Clay files")
@click.option("-o", "--output-directory", help="location of parsed sheets")
def parse(input_directory, output_directory):
    '''
    The function parses the SmithSystem files called Clay's files from the Sharepoint
    shared by Andrea N.

    There are a limited set of sheets that are parsed because many are of unknown
    quality and/or are derivative sheets created from others, i.e. report datasets

    Parameters:
    -----------
    input-directory: str, the directory to where Sharepoint .xlsx files have been downloaded
    output-directory: str, the directory where the parsed sheets are saved

    the format of the filename in the output directory is roughly:
        <name of the xlsx file>.<name of sheet>.csv

    Note that the name of the file and sheet are edited to take out inconvenient characters
    such as "space" and "&" and ".xlsx" suffix

    So for an input file like:
        "1. FY24 Product Sales Slicer.xlsx"
    we end up with per-sheet csv files:
        1__FY24_Product_Sales_Slicer.Catalog_&_Item_Detail.csv
        1__FY24_Product_Sales_Slicer.Current_Cost.csv
        1__FY24_Product_Sales_Slicer.Inv_d_Items_FY23.csv
        1__FY24_Product_Sales_Slicer.Inv_d_Items_Report.csv
        1__FY24_Product_Sales_Slicer.SEP_2022_Price_Book.csv
        1__FY24_Product_Sales_Slicer.Sheet6.csv
    '''

    # catalog file is a text file that relates the original files to the parsed files
    catalog = []
    catalog_filename = 'catalog.txt'

    for xls_file_number, sharepoint_filename in enumerate(sharepoint_files.keys()):
        # sheets of interest
        sheets_of_interest = sharepoint_files[sharepoint_filename]
        num_sheets_of_interest = len(sheets_of_interest)
        # output filename: remove .xlsx suffix and substitute '.' "'", and space with "_"
        adjusted_sharepoint_filename = re.sub(r"\.xlsx", '', sharepoint_filename)
        adjusted_sharepoint_filename = re.sub(r"[\. ']", '_', adjusted_sharepoint_filename)

        # original input file, fully-qualified
        sharepoint_filename = f'{input_directory}/{sharepoint_filename}'
        log.info(f'Parsing file {sharepoint_filename}/...')
        xls = pd.ExcelFile(sharepoint_filename)
        sheets_of_interest = set(sheets_of_interest).intersection(set(xls.sheet_names))
        if len(sheets_of_interest) != num_sheets_of_interest:
            import ipdb; ipdb.set_trace()

        for sheet_number, sheet_name in enumerate(sheets_of_interest):
            log.info(f'Parsing sheet {sheet_name}...')
            df = pd.read_excel(xls, sheet_name=sheet_name)

            # column name repair.
            # 1. substitute newlines in column names with space
            edited_column_names = []
            for col in list(df.columns):
                col = str(col)
                col = re.sub('\n', ' ', col)
                edited_column_names.append(col)
            df.columns = edited_column_names

            # substitute '.' "'", and space with "_"
            new_sheet_name = re.sub(r"[\.  ']", '_', sheet_name)
            output_file = f'{output_directory}/{adjusted_sharepoint_filename}.{new_sheet_name}.csv'
            # check if # of columns parsed match # fields parsed
            df.to_csv(output_file)
            catalog.append(CatalogEntry(output_file, df.shape, sharepoint_filename, sheet_name))

    catalog_filename = 'catalog.txt'
    with open(catalog_filename, 'w') as catalog_file:
        for entry in catalog:
            catalog_file.write(str(entry) + '\n')

    log.info(f'check {catalog_filename} for parsed results')


if __name__ == "__main__":
    parse()
