import pandas as pd

def pd_read_csv(fname):
        f = pd.read_csv(fname)
        print(f)
        print(f['a'])
        print(list(f['a']))

        print(f[['a', 'b']])

        # f[['a', 'b']].to_csv('./test.csv.out')

        sorted = f[['a', 'b']].sort_values('a')
        print(sorted)

        # select rows
        print(sorted.iloc[[0, 1]])

pd_read_csv('./test.csv')