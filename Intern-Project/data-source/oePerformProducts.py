# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib
import time
import sys
import calendar
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
pathFile = r'C:\Users\yzhou\Documents\Workspace\Daten\oeCSVVer1.4.csv'
destFile = r'C:\Users\yzhou\Documents\Workspace\Daten\oePP1.csv'
destFileExcel = r'C:\Users\yzhou\Documents\Workspace\oePP1.xlsx'
tempPath = r'C:\Users\yzhou\Documents\Workspace\Daten\oePP1Check.csv'
unvalidItemPath = r'C:\Users\yzhou\Documents\Workspace\Daten\unvalidProductId.csv'

# Read the csv file into the dataframe
# Important: thousand point to be set
dateParse = lambda x: pd.datetime.strptime(x, '%d.%m.%Y')
try:
    dataFrameOE = pd.read_csv(pathFile, sep=';', header=0, decimal=',', parse_dates=['Date'], date_parser=dateParse, warn_bad_lines=True)

except UnicodeDecodeError, err:
    print 'Error: ', err
    exit()
else:
    print 'Read: \n', repr(dataFrameOE)

print 'Read end! \n'
print '#####################################################'
print 'Program start: '
print '#####################################################\n'

# Version 1.3
#===============================================================================
# dataFrameOE = dataFrameOE[['InvoicedId', 'Day', 'SalesType', 'SalesStatus', 'AccountName', 'SalesRep', 'BusinessUnit', 'LineOfBusiness',
#                              'pmcat3', 'CustClassificationId', 'ItemId', 'SalesQty', 'SalesPrice', 'Discount', 'NetAmount',
#                              'CostPrice', 'SalesMargin', 'Productmanager', 'Notes']]
#
# names = ['InvoicedId', 'Date', 'SalesType', 'SalesStatus', 'CustomerCompany', 'SalesRepresentative', 'Agency', 'BusinessPart',
#          'ProdCatalog', 'CustomerStatus', 'ProductId', 'Quantity', 'OriginalPrice', 'Discount', 'PriceAmount',
#          'ProductCost', 'MarginAmount', 'Productmanager', 'Description']
#
# # Change the column names
# dataFrameOE.columns = names
#
# # Drop the unvalid Invoice 'Target' in the column 'InvoicedId'
# unvalidInvoice = dataFrameOE['InvoicedId'] == 'Target'
# dataFrameOE = dataFrameOE[~unvalidInvoice]
#
# # Drop the unvalid Products in the column 'ProductId'
# try:
#     dataFrameTemp = pd.read_csv(unvalidItemPath, header=0, warn_bad_lines=True)
#
# except UnicodeDecodeError, err:
#     print 'Error: ', err
#     exit()
# else:
#     print 'Read: \n', repr(dataFrameTemp)
# unvalidList = list(dataFrameTemp['ProductId'].unique())
# dropProduct = dataFrameOE['ProductId'].isin(unvalidList)
# dataFrameOE = dataFrameOE[~dropProduct]
#===============================================================================

#===============================================================================
# # Concatenate prodCatalog
# concatValues = dataFrameOE.apply(lambda x:'%s %s %s' %(x['ProdCatalog1'] if pd.notnull(x['ProdCatalog1']) else '',
#                                                                        x['ProdCatalog2'] if pd.notnull(x['ProdCatalog2']) else '',
#                                                                        x['ProdCatalog3']), axis=1)
# idx1 = dataFrameOE.columns.get_loc('ProdCatalog1')
# idx2 = dataFrameOE.columns.get_loc('ProdCatalog2')
# idx = dataFrameOE.columns.get_loc('ProdCatalog3')
# dataFrameOE.insert(idx+1, 'ProdCatalog', concatValues)
# dataFrameOE = dataFrameOE.drop(dataFrameOE.columns[[idx1, idx2, idx]], axis=1)
#===============================================================================

# Version 1.4
#===============================================================================
# # Business part transaction between the branches will be ignored
# interTransaction = dataFrameOE['BusinessPart'] == 'IC'
# dataFrameOE = dataFrameOE[~interTransaction]
# customerIntern = dataFrameOE['CustomerStatus'] == 'IC'
# dataFrameOE = dataFrameOE[~customerIntern]
#
# # Ignore the intern demand
# internDemand = dataFrameOE['Agency'] == 'HQ'
# dataFrameOE = dataFrameOE[~internDemand]
#
# # Ignore the margin equal zero because of the additional service or additional hard- or software
# zeroMargin = dataFrameOE['MarginAmount'] == 0
# dataFrameOE = dataFrameOE[~zeroMargin]
#===============================================================================


# Apart the date as day, month, year
dataFrameOE['Day'] = dataFrameOE['Date'].dt.day
dataFrameOE['Month'] = dataFrameOE['Date'].dt.month
dataFrameOE['Monthname'] = dataFrameOE['Month'].apply(lambda x: calendar.month_name[x])
dataFrameOE['Year'] = dataFrameOE['Date'].dt.year
dataFrameOE['Month-Year'] = dataFrameOE.apply(lambda x: str(x['Month']) + '-' + str(x['Year']), axis=1)
dataFrameOE.to_csv(tempPath, sep=';', decimal=',', index=False)
print 'done!'
exit()


dataFrameOE.to_csv(tempPath, sep=';', decimal=',', index=False)
print 'done!'







# Total handeling time
endTime = time.time()
print "total time is %s seconds." %(endTime-startTime)