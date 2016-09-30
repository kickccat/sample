import sys
import csv
from pprint import pprint
# read the csv file
path_file = r'C:\Users\yzhou\Documents\Workspace\Daten\data\test.txt'
#dest_file = r'C:\Users\yzhou\Documents\Workspace\Daten\data\testCopy.csv'

#===============================================================================
# with open(path_file, 'rb') as csvFile1:
#     testData = csv.reader(csvFile1)
#     headers = testData.next()
#     column = {h:[] for h in headers}
#     for row in testData:
#         for h, v in zip(headers, row):
#             column[h].append(v)
#     pprint(column)
#===============================================================================
csv.register_dialect(
                     'mydialect',
                     delimiter = '\t',
                     quotechar = '"',
                     doublequote = True,
                     skipinitialspace = True,
                     lineterminator = '\r\n',
                     quoting = csv.QUOTE_MINIMAL)

with open(path_file, 'rb') as csvFile1:
    testData = csv.reader(csvFile1, dialect = 'mydialect')
    for row in testData:
        print row
print row[1]

#===============================================================================
# f2 = open(dest_file, 'w+')
# f2.write('\n')
# f2.writelines(rString)
# f2.seek(0)
# rString = f2.readlines()
# print rString
# f2.close()
#===============================================================================
