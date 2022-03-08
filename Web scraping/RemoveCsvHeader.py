# Project: Removing the Header from CSV Files
import csv, os
os.makedirs('HeaderRemoved', exist_ok=True)  # creating the directory to store the file
#  loop through every file in directory and select which have .csv extension
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue
    # selects the only file that has .csv file extension

    print('Remove the header from '+ csvFilename+'......')

    # TODO: Read the CSV file in (skipping first row).
    csvRows = []  # here will add all rows except first row
    fileObj = open(csvFilename)
    readObj = csv.reader(fileObj)
    for row in readObj:
        if readObj.line_num == 1: # here we are using loop to scan the reader Object
            continue                  # and if first line we have to skip that line
        csvRows.append(row)
    fileObj.close()

    # TODO: Write out the CSV file
    fileObj = open(os.path.join('HeaderRemoved', csvFilename), 'w',newline = '')
    writerObj = csv.writer(fileObj)
    for row in csvRows:
        writerObj.writerow(row)
    fileObj.close()

