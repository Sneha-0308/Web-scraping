import csv
fileObj = open('output.csv', 'w', newline='')  # creating the csv file object
# why newline=' ' passed as an argument to the open function
# if you forget to set the newline argument, the rows in output.csv
# will be double-spaced

outputwriter = csv.writer(fileObj)
outputwriter.writerow(['spam', 'egg', 'bacon', 'ham'])
outputwriter.writerow(['Hello, World!', 'eggs', 'bacon', 'ham'])
outputwriter.writerow([1, 2, 3.14353, 4])

fileObj.close()

# STEPS TO WRITE OBJECTS IN CSV FILE
# 1] create csv file object in open() method pass file.csv, mode, newline=''
# 2] writer object for that file object
# 3] insert data using list by writerow function
# 4] close file object

