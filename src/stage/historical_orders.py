import pandas as pd
import re

sharepoint_filename = '3. FY24 Order Analysis.xlsx'
sheet_name = 'Historical Orders'

xls = pd.ExcelFile(sharepoint_filename)
df = pd.read_excel(xls, sheet_name=sheet_name)

df['Order Date'] = pd.to_datetime(df['Order Date'])

# bad data in Ship Date: 01-31-2020, Mfg Date : 01-30-2020
idx = df['Ship Date'].str.contains('Mfg Date')
df.loc[idx, 'Ship Date'] = df.loc[idx, 'Ship Date'].apply(lambda x: re.sub(', Mfg Date.*$', '', x))
df['Ship Date'] = pd.to_datetime(df['Ship Date'])
df['Cust No'] = df['Cust No'].fillna(0).astype(int)

# there are column names with just integers which breaks Postgres ingestion (SQL fields cannot be all digits)
int_cols = [x for x in list(df.columns) if isinstance(x, int)]
for colname in int_cols:
    new_colname = 'int' + str(colname)
    df = df.rename({colname: new_colname}, axis=1)

df.to_csv('HistoricalOrders.csv', index=False)
