import csv
fileObje = open('outputdict.csv','w',newline='')
writeobj = csv.DictWriter(fileObje,['Name', 'Pet', 'Phone'], delimiter='\t', lineterminator='\n\n',)
#  TODO: just add DictWriter function and keys of dictinory
writeobj.writeheader()
# by using this code it will write all keys at the top of each column
writeobj.writerow({'Name':'ruby', 'Pet':'Dog', 'Phone':'12644'})
# TODO: extra is to user flower braces instead of square and use key will inserting values

fileObje.close()