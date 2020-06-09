# pcost.py

#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    path = 'Data/'+filename
    total = 0

    with open(path, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowid, row in enumerate(rows):
            record = dict(zip(headers, row))
            try:
                #row = row.split(',')
                nshares = int(record['shares'])
                cost_share = float(record['price'].strip())
                total = total + nshares*cost_share
            except ValueError:
                print(f'Row {rowid} : Could not convert {row} ')
    return round(total,2)

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost :', cost)
