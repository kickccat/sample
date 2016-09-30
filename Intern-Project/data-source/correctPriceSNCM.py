# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib
import time
import sys
from matplotlib import pyplot
from pandas import options
from numpy import float64

# Set the plot surroundings
matplotlib.pyplot.style.use('default')
# Always display all the columns
pd.set_option('display.width', 5000)
pd.set_option('display.max_columns', 60)

# Estimate the spending time
startTime = time.time()

# Check system info
print 'System info:\n'
print '###################################################################'
print '# Python version ' + sys.version
print '# Pandas Version ' + pd.__version__
print '# Matplotlib version ' + matplotlib.__version__
print '###################################################################'
print '\n'

# Set the files path
pathFile = r'C:\Users\yzhou\Documents\Workspace\Daten\oeCSVVer1.1.csv'
destFile = r'C:\Users\yzhou\Documents\Workspace\Daten\oeCSVVer1.2.csv'
destFileExcel = r'C:\Users\yzhou\Documents\Workspace\oeExcelVer1.2.xlsx'
tempPath = [r'C:\Users\yzhou\Documents\Workspace\Daten\oeCSVDiscount.csv', r'C:\Users\yzhou\Documents\Workspace\Daten\oeCSVSalesprice.csv',
            r'C:\Users\yzhou\Documents\Workspace\Daten\oeCSVNetAmount.csv', r'C:\Users\yzhou\Documents\Workspace\Daten\oeCSVCostprice.csv',
            r'C:\Users\yzhou\Documents\Workspace\Daten\oeCSVMargin.csv']

# Read the csv file into the dataframe and roughly handle the Na or NaN values
# naValues = [np.nan, '?', 'N/A', 'n/a', 'nan' 'NULL', None, '#NA', '#NAME', 'NaN', 'NA', 'Na']
# Important: thousand point to be set
try:
    dataFrameOE = pd.read_csv(pathFile, sep=';', header=0, decimal=',', na_values='default',
                              converters={'SalesPrice': (lambda x: float((x.replace('.', '')).replace(',', '.')))})
except UnicodeDecodeError, err:
    print 'Error: ', err
    exit()
else:
    print 'Read: \n', repr(dataFrameOE)

print 'Read end! \n'
print '#####################################################'
print 'Program start: '
print '#####################################################\n'

# Remove the .0 in the column 'HcmWorkerRecId'
longHcmWorkerRecId = dataFrameOE['HcmWorkerRecId'].str.len() > 2
dataFrameOE.loc[longHcmWorkerRecId, 'HcmWorkerRecId'] = dataFrameOE.loc[longHcmWorkerRecId, 'HcmWorkerRecId'].map(lambda x: x[:10])

#===============================================================================
# # Remove the .0 in the column 'SalesQty'
# pointZeroSalesQty = dataFrameOE['SalesQty'].str[-2:]=='.0'
# dataFrameOE.loc[pointZeroSalesQty, 'SalesQty'] = dataFrameOE.loc[pointZeroSalesQty, 'SalesQty'].map(lambda x: x.rstrip('.0'))
#===============================================================================

# Abs function check if values bigger than 100 return boolean
def compareHundred(numericVector):
    return numericVector.abs() > 100

# Divide 10e6 according to the label
def divideResult(someDataframe, labelString):
    compared = compareHundred(someDataframe[labelString])
    return someDataframe.loc[compared, labelString].map(lambda x: x/1000000)

# Divide 10e6 for the numbers in the columns 'Discount', 'SalesPrice', 'NetAmount', 'CostPrice', 'SalesMargin'
labelList = ['Discount', 'SalesPrice', 'NetAmount', 'CostPrice', 'SalesMargin']
i = 0
for labelText in labelList:
    comparision = compareHundred(dataFrameOE[labelText])
    dataFrameOE.loc[comparision, labelText] = divideResult(dataFrameOE, labelText)
    dataFrameOE[comparision][['Unnamed: 0', labelText]].to_csv(tempPath[i], sep=';', decimal=',', index=False)
    i += 1

#===============================================================================
# # Check the absolute values in the column 'Discount' if bigger than 100 then divide 10e6
# biggerDiscount = compareHundred(dataFrameOE['Discount'])
# dataFrameOE.loc[biggerDiscount, 'Discount'] = dataFrameOE.loc[biggerDiscount, 'Discount'].map(lambda x: x/1000000)
# print dataFrameOE[biggerDiscount]['Discount']
#===============================================================================

#===============================================================================
# # Divide 10e6 for the numbers in the columns 'SalesPrice', 'NetAmount', 'CostPrice', 'SalesMargin'
# biggerSalesprice = compareHundred(dataFrameOE['SalesPrice'])
# dataFrameOE.loc[biggerSalesprice, 'SalesPrice'] = dataFrameOE.loc[biggerSalesprice, 'SalesPrice'].map(lambda x: x/1000000)
# print dataFrameOE[biggerSalesprice]['SalesPrice']
#===============================================================================

#===============================================================================
# biggerNetamount = compareHundred(dataFrameOE['NetAmount'])
# dataFrameOE.loc[biggerNetamount, 'NetAmount'] = dataFrameOE.loc[biggerNetamount, 'NetAmount'].map(lambda x: x/1000000)
# print dataFrameOE[biggerNetamount]['NetAmount']
#===============================================================================

#===============================================================================
# biggerCostprice = compareHundred(dataFrameOE['CostPrice'])
# dataFrameOE.loc[biggerCostprice, 'CostPrice'] = dataFrameOE.loc[biggerCostprice, 'CostPrice'].map(lambda x: x/1000000)
# print dataFrameOE[biggerCostprice]['CostPrice']
#===============================================================================

#===============================================================================
# biggerMargin = compareHundred(dataFrameOE['SalesMargin'])
# dataFrameOE.loc[biggerMargin, 'SalesMargin'] = dataFrameOE.loc[biggerMargin, 'SalesMargin'].map(lambda x: x/1000000)
# print dataFrameOE[biggerMargin]['SalesMargin']
#===============================================================================


dataFrameOE.to_csv(destFile, sep=';', decimal=',', index=False)





# Total handeling time
endTime = time.time()
print "total time is %s seconds." %(endTime-startTime)