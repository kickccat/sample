# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib
import time
import sys
from matplotlib import pyplot
from numpy import dtype
from pandas import options
options.io.excel.xlsx.writer = 'xlsxwriter'

# Set the plot surroundings
matplotlib.pyplot.style.use('default')
# Always display all the columns
pd.set_option('display.width', 5000)
pd.set_option('display.max_columns', 60)

pathFile = r'C:\Users\yzhou\Documents\Workspace\Daten\revenueVer0.csv'
destFile = r'C:\Users\yzhou\Documents\Workspace\Daten\revenueVer1.csv'
destFileExcel = r'C:\Users\yzhou\Documents\Workspace\revenueVer1.xlsx'

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

# Read the csv file into the dataframe
naValues = [np.nan, '?', 'N/A', 'n/a', ' ', '', '0', 'NULL', None]
try:
    dataFrameOE = pd.read_csv(pathFile, na_values=naValues, dtype={'grecid': str, 'CustAccount': str, 'projid': str, 'pmcat1': str,
                                                             'pmcat3': str,
                                                             'targetA': str, 'targetB': str,
                                                             'HcmWorkerRecId': str,
                                                             'ItemId': str, 'SalesQty': dtype,
                                                             'CostCenter': str}, sep=';', decimal='.',
                                                             encoding='latin1', warn_bad_lines=True)
except UnicodeDecodeError, err:
    print 'Error: ', err
    exit()
else:
    print 'Read: \n', repr(dataFrameOE)

print 'Read end! \n'
print 'Program start: \n'
# Drop the blank columns
# dataFrameOE = dataFrame.drop(dataFrame.columns[range(35, 52)], axis=1)
dataFrameOE = dataFrameOE.dropna(axis=1, how='all')

#===============================================================================
# print dataFrameOE
# dataFrameOE.to_csv(destFile, sep=',')
# dataFrameOE.to_excel(destFileExcel, encoding='utf-8')
#===============================================================================

#===============================================================================
# # Map 'CustAccount' to 'AccountName'
# def mapIdentify(someDataFrame):
#     tempDF = someDataFrame[]
#===============================================================================

#===============================================================================
# tempDF = dataFrameOE[['CustAccount', 'AccountName']].dropna(axis=0, how='all')
# tempDF = tempDF.drop_duplicates('AccountName')
# tempDF = tempDF.dropna(subset=['AccountName'])
# tempDF = tempDF.sort_values(['AccountName', 'CustAccount'], ascending=False)
# valuesCompare = np.where(tempDF['AccountName'] == tempDF['CustAccount'], 'True', 'False')
# tempDF = tempDF[valuesCompare=='False']
# tempDF.to_excel(r'C:\Users\yzhou\Documents\Workspace\Daten\mapping1.xlsx')
# #print valuesCompare
#
# print tempDF
#
# endTime = time.time()
# print "total time is %s seconds." %(endTime-startTime)
# exit()
#===============================================================================

# Casting to the float value
def toFloat(someArray):
    for i in range(len(someArray)):
        if ~isinstance(someArray[i], float):
            someArray[i] = float(str(someArray[i]).replace(',', '.'))
            if abs(someArray[i]) > 1000000:
                someArray[i] /= 1000000

# Correct the price point position
priceSales = dataFrameOE['SalesPrice'].values
toFloat(priceSales)
# print priceSales

#===============================================================================
# # Find the saletype 'RMA', 'IC' and 'Sales Order'
# saletypeRMADF = dataFrameOE['SalesType'].str.match('RMA', case=False).fillna(False)
# print dataFrameOE[saletypeRMADF]
# dataFrameOE[saletypeRMADF].to_csv(destFile, index=False, encoding='utf-8')
# # dataFrameOE[saletypeRMADF].to_excel(destFileExcel, index=False)
#===============================================================================

#===============================================================================
# saletypeICDF = dataFrameOE['SalesType'].str.match('IC', case=False).fillna(False)
# print dataFrameOE[saletypeICDF]
# dataFrameOE[saletypeICDF].to_csv(destFile, index=False, encoding='utf-8')
# # dataFrameOE[saletypeRMADF].to_excel(destFileExcel, index=False)
#===============================================================================

saletypeSalesOrderDF = dataFrameOE['SalesType'].str.match('Sales Order', case=False).fillna(False)
print dataFrameOE[saletypeSalesOrderDF]['CustAccount'].unique()
# dataFrameOE[saletypeSalesOrderDF].to_csv(destFile, index=False, encoding='utf-8', sep=',', decimal='.', float_format='%.3f')
# dataFrameOE[saletypeRMADF].to_excel(destFileExcel, index=False)


# Spended time
endTime = time.time()
print "total time is %s seconds." %(endTime-startTime)