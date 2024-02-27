import numpy as np
import pandas as pd

from bonum_logging import log

input_file = '1__FY24_Product_Sales_Slicer.Catalog_&_Item_Detail.csv'
output_file = 'product.csv'
log.info(f'Transforming {input_file} to {output_file}')
# transform: product.csv
df = pd.read_csv('1__FY24_Product_Sales_Slicer.Catalog_&_Item_Detail.csv', dtype=str)
'''
 Model                                                25270BUTCHER
For Vlookup                                          25270BUTCHER#
Description                 12" x 46" Single Bench (Butcher Block)
SEP 2022 List Price*                                        1053.0
QTY Sold                                                      31.0
Extended List                                              32643.0
Extended Cost                                              4644.83
Average Material Cost                           149.83322580645162
Inbound Freight                                 16.931154516129034
Import Duty                                      7.641494516129033
Labor                                           27.119813870967743
Variable Overhead                                16.48165483870968
Fixed Overhead                                   32.36397677419355
Total Cost                                      250.37132032258066
Extended Total Cost                                     7761.51093
Cost Factor                                     0.2377695349692124
Pricing Threshold Category                                   Other
Catalog Category                              Planner Studio Bench
Product Group                                         Single Bench
Sales By Product Report                       Planner Studio Bench

'''
names = {' Model': 'Internal Reference',
         'Description': 'Name',
         'Product Group': 'Product Type',
         'SEP 2022 List Price*': 'Sales Price',
         'Extended Total Cost': 'Cost'}
df.loc[df[' Model'].isnull(), ' Model'] = df['For Vlookup']
dfnew = df[names.keys()]
dfnew = dfnew.rename(columns=names)
dfnew['Sales Price'] = dfnew['Sales Price'].astype(float)
dfnew['Sales Price'] = dfnew['Sales Price'].fillna(0)
dfnew = dfnew.sort_values(by=['Sales Price'])
dfnew = dfnew.drop_duplicates(subset=['Internal Reference'], keep='last')

# dedup
idx_remove = dfnew['Internal Reference'].duplicated() & (dfnew['Sales Price'] == 0)
dfnew = dfnew[~idx_remove].reset_index(drop=True)
dfnew['element'] = dfnew.index + 1
dfnew['External ID'] = dfnew.apply(lambda x: f'product_template_{x.element}', axis=1)
dfnew['Barcode'] = np.nan
dfnew['Weight'] = np.nan
dfnew['Sales Description'] = dfnew['Name']
dfnew = dfnew.drop(columns=['element'])
columns = ['External ID', 'Name', 'Product Type', 'Internal Reference', 'Barcode', 'Sales Price', 'Cost', 'Weight', 'Sales Description']
dfnew = dfnew[columns]
dfnew.to_csv('product.csv', index=False)

# sales people
