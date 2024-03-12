import pdb
import sys

import pandas as pd


def find_value(df, value):
    for col in df.columns:
        idx = df[col].astype(str).str.contains(value)
        if (count := idx.sum()) > 0:
            results = df[idx][col].value_counts()
            print(f'------\n{col} shows {count} {value}\n{results}')


def do(input_file):
    df = pd.read_csv(input_file, dtype=str)

    find_value(df, 'Oodle')

    pdb.set_trace()


if __name__ == '__main__':
    do(sys.argv[1])
