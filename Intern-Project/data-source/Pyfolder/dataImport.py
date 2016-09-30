import sys
import csv

path_file = r'C:\Users\yzhou\Documents\Workspace\Daten\data\newData\withHeadline\oe.csv'
dest_file = r'C:\Users\yzhou\Documents\Workspace\Daten\data\newData\withHeadline\dest_oe.csv'

with open(path_file, 'rb') as f1:
    reader = csv.reader(f1)
    for row in reader:
        print row
    
f1.close()

#===============================================================================
# f2 = open(dest_file, 'w+')
# f2.write('\n')
# f2.writelines(rString)
# f2.seek(0)
# rString = f2.readlines()
# print rString
# f2.close()
#===============================================================================
