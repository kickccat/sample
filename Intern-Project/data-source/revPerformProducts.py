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
pathFile = r'C:\Users\yzhou\Documents\Workspace\Daten\revenueCSVVer1.2.csv'
destFile = r'C:\Users\yzhou\Documents\Workspace\Daten\revPP1.csv'
destFileExcel = r'C:\Users\yzhou\Documents\Workspace\revPP1.xlsx'
tempPath = r'C:\Users\yzhou\Documents\Workspace\Daten\revPP1Check.csv'
unvalidItemPath = r'C:\Users\yzhou\Documents\Workspace\Daten\unvalidProductId.csv'
productCatalog = r'C:\Users\yzhou\Documents\Workspace\Daten\productCatalog.csv'

# Read the csv file into the dataframe
# Important: thousand point to be set
dateParse = lambda x: pd.datetime.strptime(x, '%d.%m.%Y')
try:
    dataFrameRev = pd.read_csv(pathFile, sep=';', header=0, decimal=',', parse_dates=['Date'], date_parser=dateParse, warn_bad_lines=True)

except UnicodeDecodeError, err:
    print 'Error: ', err
    exit()
else:
    print 'Read: \n', repr(dataFrameRev)

print 'Read end! \n'
print '#####################################################'
print 'Program start: '
print '#####################################################\n'

# Till version 1.1
#===============================================================================
# dataFrameRev = dataFrameRev[['RechnungsNr.', 'Day', 'SalesType', 'InvoiceId', 'AccountName', 'SalesRep', 'BusinessUnit', 'LineOfBusiness',
#                              'pmcat1', 'pmcat2', 'pmcat3', 'CustClassificationId', 'ItemId', 'SalesQty', 'SalesPrice', 'Discount', 'NetAmount',
#                              'CostPrice', 'SalesMargin', 'Productmanager', 'Notes']]
#
# names = ['InvoicedNo.', 'Date', 'SalesType', 'OrderNo.', 'Customer', 'SalesRepresentative', 'Agency', 'BusinessPart',
#          'ProdCatalog1', 'ProdCatalog2', 'ProdCatalog3', 'CustomerStatus', 'ProductId', 'Quantity', 'OriginalPrice', 'Discount', 'PriceAmount',
#          'ProductCost', 'MarginAmount', 'Productmanager', 'Description']
#
# # Change the column names
# dataFrameRev.columns = names
#
# # Drop the unvalid Invoice 'Target' in the column 'InvoicedId'
# unvalidInvoice = dataFrameRev['InvoicedNo.'] == 'Target'
# dataFrameRev = dataFrameRev[~unvalidInvoice]
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
# dropProduct = dataFrameRev['ProductId'].isin(unvalidList)
# dataFrameRev = dataFrameRev[~dropProduct]
#
# # Concatenate prodCatalog
# concatValues = dataFrameRev.apply(lambda x:'%s %s %s' %(x['ProdCatalog1'] if pd.notnull(x['ProdCatalog1']) else '',
#                                                                        x['ProdCatalog2'] if pd.notnull(x['ProdCatalog2']) else '',
#                                                                        x['ProdCatalog3']), axis=1)
# idx1 = dataFrameRev.columns.get_loc('ProdCatalog1')
# idx2 = dataFrameRev.columns.get_loc('ProdCatalog2')
# idx = dataFrameRev.columns.get_loc('ProdCatalog3')
# dataFrameRev.insert(idx+1, 'ProdCatalog', concatValues)
# dataFrameRev = dataFrameRev.drop(dataFrameRev.columns[[idx1, idx2, idx]], axis=1)
#===============================================================================

# Version 1.2
#===============================================================================
# # Business part transaction between the branches will be ignored
# interTransaction = dataFrameRev['BusinessPart'] == 'IC'
# dataFrameRev = dataFrameRev[~interTransaction]
# customerIntern = dataFrameRev['CustomerStatus'] == 'IC'
# dataFrameRev = dataFrameRev[~customerIntern]
#
# # Ignore the intern demand
# internDemand = dataFrameRev['Agency'] == 'HQ'
# dataFrameRev = dataFrameRev[~internDemand]
#
# # Ignore the margin equal zero because of the additional service or additional hard- or software
# zeroMargin = dataFrameRev['MarginAmount'] == 0
# dataFrameRev = dataFrameRev[~zeroMargin]
#===============================================================================

# Version 1.2 Date
#===============================================================================
# # Apart the date as day, month, year
# dataFrameRev['Day'] = dataFrameRev['Date'].dt.day
# dataFrameRev['Month'] = dataFrameRev['Date'].dt.month
# dataFrameRev['Monthname'] = dataFrameRev['Month'].apply(lambda x: calendar.month_name[x])
# dataFrameRev['Year'] = dataFrameRev['Date'].dt.year
# dataFrameRev['Month-Year'] = dataFrameRev.apply(lambda x: str(x['Month']) + '-' + str(x['Year']), axis=1)
# dataFrameRev.to_csv(tempPath, sep=';', decimal=',', index=False)
# print 'done!'
# exit()
#===============================================================================

# Get the product catalog
searchFor = ('Options', 'Thin Client', 'Miete', 'Other', 'Entry', 'Midrange', 'Others', 'Components')
testFound = dataFrameRev[dataFrameRev['ProdCatalog'].str.endswith(searchFor)]['ProdCatalog']
print testFound
exit()
dataFrameRev['combinedCatalog'] = np.where(~dataFrameRev['ProdCatalog'].str.contains('|'.join(searchFor)), dataFrameRev['ProdCatalog'], \
                                           dataFrameRev['ProdCatalog'].fillna('') + '; ' + dataFrameRev['Description'].fillna(''))
combCata = dataFrameRev['combinedCatalog'].unique()
replaceCatalog = dataFrameRev['ProdCatalog'].str.contains('|'.join(searchFor))
dataFrameRev['Replacement'] = dataFrameRev[replaceCatalog]['ProdCatalog'].fillna('') + ' ' + dataFrameRev[replaceCatalog]['Description'].fillna('')
repCataFinal = dataFrameRev['Replacement'].unique()

pd.DataFrame(repCataFinal).to_csv(productCatalog, sep=';', decimal=',')
exit()





dataFrameRev.to_csv(tempPath, sep=';', decimal=',', index=False)
print 'done!'







# Total handeling time
endTime = time.time()
print "total time is %s seconds." %(endTime-startTime)