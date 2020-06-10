# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename, selection = None, types = [], has_headers = True, delim = ',' ):
    '''
    Parse a .csv file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter = delim)

        # File structure
        if has_headers:
            headers = next(rows)
        else:
            headers = []
            
        if selection:
            indices = [headers.index(colname) for colname in selection]
            headers = selection

        # Rows
        records = []
        for row in rows:
            if not row:
                continue

            if selection:
                row = [row[index] for index in indices]
            if types:
                row = [fun(val) for fun,val in zip(types, row)]
            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)

            records.append(record)
        
        return records

