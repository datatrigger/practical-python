# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000
total_paid = 0.0
month = 0

while principal > 0:
    month = month + 1
    first_year = (month <= 12)
    principal = principal * (1+rate/12) - payment - (extra_payment * first_year)
    total_paid = total_paid + payment + extra_payment * first_year

print('Total paid', total_paid, 'Months', month)