# Reading Data from reader Objects in a for Loop

import csv

fileobj = open('example.csv')
readerobj = csv.reader(fileobj)

for i in readerobj:
    print('Row #' + str(readerobj.line_num) + ' ' + str(i))

# i holds the content of each list
# readerobject.line_num gives the which list content it is belong to
