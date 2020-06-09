import csv
with open('Data/portfoliodate.csv') as f:
    rows = csv.reader(f)
    headers = next(rows)
    selection = ['name', 'shares', 'price']
    indices = [headers.index(colname) for colname in selection]
    pf = [ {colname: row[index] for colname, index in zip(selection, indices)} for row in rows]

print(pf)