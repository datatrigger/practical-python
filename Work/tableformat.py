class TableFormatter:

    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data
        '''
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in HTML format.
    '''
    def headings(self, headers):
        print('<tr>', end = '')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>', end = '\n')

    def row(self, rowdata):
        print('<tr>', end = '')
        for row in rowdata:
            print(f'<th>{row}</th>', end='')
        print('</tr>', end = '\n')

class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

def create_formatter( fmt = 'txt '):
    if fmt == 'txt':
        formatter = TextTableFormatter()
    elif fmt == 'csv':
        formatter = CSVTableFormatter()
    elif fmt == 'html':
        formatter = HTMLTableFormatter()
    else:
        raise RuntimeError(f'Unknown format {fmt}')

    return formatter

def print_table(data, attributes = ['Name','Shares','Price','Change'], formatter = TextTableFormatter()):
    '''
    Print a nicely formated table from a list of attributes.
    '''
    formatter.headings(attributes)
    for d in data:
        rowdata = [ str(getattr(d, attribute)) for attribute in attributes ]
        formatter.row(rowdata)