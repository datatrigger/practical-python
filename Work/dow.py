import csv
from pprint import pprint

def date_to_tuple(date):
    return tuple(map(int, date.split('/')))

with open('Data/dowstocks.csv') as f:
    rows = csv.reader(f)
    headers = next(rows)
    types = [str, float, date_to_tuple, str, float, float, float, float, int]
    ds = []
    for row in rows:
        ds.append(
            {name: function(value) for name, function, value in zip(headers, types, row)}
        )

pprint(ds)