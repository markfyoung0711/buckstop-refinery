import pandas as pd
import re

# config what to read in xlsx file.
sharepoint_filename = '1. FY24 Product Sales Slicer.xlsx'
sheet_name = '''Inv'd Items Report'''

xls = pd.ExcelFile(sharepoint_filename)
df = pd.read_excel(xls, sheet_name=sheet_name)

# renames of int named columns, e.g. 1
renames = {}
int_cols = [x for x in list(df.columns) if isinstance(x, int)]
for col in int_cols:
    renames[col] = 'int' + str(col)

for col in list(df.columns):
    try:
        float_val = float(col)
        renames[col] = 'float' + str(float_val)
    except Exception:
        pass

df = df.rename(columns=renames)

# renames of other weirdly named columns
renames = {}
for weird_char in ['\n']:
    for col in list(df.columns):
        if weird_char in col:
            renames[col] = re.sub(weird_char, ' ', col)

df = df.rename(columns=renames)

df.to_csv('InventoriedItemsReport_2024.csv', index=False)
