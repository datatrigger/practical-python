# report.py
#
# Exercise 2.4
# pcost.py

import csv

def read_portfolio(filename):
    '''Reads the portfolio and format it into a list of tuples'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            t = {'name':row[0], 'shares':int(row[1]), 'price':float(row[2]) }
            portfolio.append(t)
    return portfolio

def read_prices(filename):
    '''Reads the portfolio and format it into a list of tuples'''
    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        #headers = next(rows)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                print('Error : empty line. Proceeding to read the next line.')
    return prices

pf = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

# Cost
cost = 0.0
for s in pf:
    cost += s['shares']*s['price']

# Value
value = 0.0
for s in pf:
    value += s['shares']*prices[s['name']]

result = round(value - cost,2)
print('Cost :', cost, '\nValue :', value, '\nResult :', result)

def make_report(portfolio, prices):
    report = []
    for s in portfolio:
        #t = (s['name'], s['shares'], prices[s['name']], prices[s['name']] - s['price'] )
        t = (s['name'], s['shares'], '$'+str(round(prices[s['name']],2)), prices[s['name']] - s['price'] )
        report.append(t)
    return(report)

report = make_report(pf, prices)
headers = ('Name', 'Shares', 'Price', 'Change')

print('\n Full report of the portfolio : \n')
#print('%10s %10s %10s %10s' % headers)
print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print(('-' * 10 + ' ') * len(headers))
for name, shares, price, change in report:
        #print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
        print(f'{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')



