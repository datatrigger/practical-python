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
        next(rows)
        for row in rows:
            try:
                #row = row.split(',')
                nshares = int(row[1])
                cost_share = float(row[2].strip())
                total = total + nshares*cost_share
            except ValueError:
                print('Could not read the current line. Proceeding to read the next line.')
    return round(total,2)

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost :', cost)
