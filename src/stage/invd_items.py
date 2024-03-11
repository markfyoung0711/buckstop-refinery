import re
import sys

import pandas as pd

def parse(input_filename, sheet_name='''Inv'd Items Report'''):
    '''
    open xlsx file for sheet name, parse it and return as df

    Parameters:
    -----------
    input_filename: str, XLSX filename
    sheet_name: str, sheet name in XLSX file

    '''
    xls = pd.ExcelFile(input_filename)
    df = pd.read_excel(xls, sheet_name=sheet_name)

    renames = {}

    # columns that have int as column value
    int_cols = [x for x in list(df.columns) if isinstance(x, int)]
    for col in int_cols:
        renames[col] = 'int' + str(col)

    # columns that have float as column value
    for col in list(df.columns):
        try:
            float_val = float(col)
            renames[col] = 'float' + str(float_val)
        except Exception:
            pass

    # columns that have odd characters in them, e.g. newline
    for weird_char in ['\n']:
        for col in list(df.columns):
            if str(weird_char) in str(col):
                renames[col] = re.sub(weird_char, ' ', col)

    return df.rename(columns=renames)

if __name__ == '__main__':
    df = parse(sys.argv[1], sys.argv[2])
    df.to_csv(sys.stdout, index=False)
