# Read csv objects using dictionary
import csv

fileobj = open('example.csv')
readerobj = csv.DictReader(fileobj, ['Date', 'fruit', 'amount'])
#  TODO: add DictReader method and keys for access column

for i in readerobj:
    print(i['Date'], i['fruit'], i['amount'])

#
# OUTPUT
# 4/5/2015 13:34 Apples 73
# 4/5/2015 3:41 Cherries 85
# 4/6/2015 12:46 Pears 14
# 4/8/2015 8:59 Oranges 52
# 4/10/2015 2:07 Apples 152
# 4/10/2015 18:10 Bananas 23
# 4/10/2015 2:40 Strawberries 98
