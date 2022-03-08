import csv
exampleobj = open('example.csv') # we have to create csv file object
exampleReader = csv.reader(exampleobj) # we have to create file object reader
exampleData = list(exampleReader)   # then convert it into list
print(exampleData) # print the content
# [['4/5/2015 13:34', 'Apples', '73'], ['4/5/2015 3:41', 'Cherries', '85'],
# ['4/6/2015 12:46', 'Pears', '14'], ['4/8/2015 8:59', 'Oranges', '52'],
# ['4/10/2015 2:07', 'Apples', '152'], ['4/10/2015 18:10', 'Bananas', '23'], ['4/10/2015 2:40', 'Strawberries', '98']]

# STEPS TO READ THE CSV OBJECT
# 1] create csv file object
# 2] create reader object for tht file object
# 3] convert the reader object content into list
# 4] print that list

print(exampleData[1][2])  # output is 85
