import csv

# delimiter used to separate the each column
#  lineterminator is used to add lines between rows

fileObj = open('Keywordargs.csv', 'w', newline='')
filewriter = csv.writer(fileObj, delimiter='\t', lineterminator='\n\n')
filewriter.writerow(['apple', 'orange', 'grapes'])
filewriter.writerow(['eggs', 'bacon', 'ham'])
filewriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])
fileObj.close()