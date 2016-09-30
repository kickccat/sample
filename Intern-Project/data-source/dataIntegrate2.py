# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib
import time
import sys
from matplotlib import pyplot
from pandas import options

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
pathFile = r'C:\Users\yzhou\Documents\Workspace\Daten\revenueCSVVer0.csv'
destFile = r'C:\Users\yzhou\Documents\Workspace\Daten\revenueCSVVer1.csv'
destFileExcel = r'C:\Users\yzhou\Documents\Workspace\revenueExcelVer1.xlsx'
tempPath = r'C:\Users\yzhou\Documents\Workspace\Daten\margin.csv'

# Read the csv file into the dataframe and roughly handle the Na or NaN values
# naValues = [np.nan, '?', 'N/A', 'n/a', 'nan' 'NULL', None, '#NA', '#NAME', 'NaN', 'NA', 'Na']
try:
    dataFrameRev = pd.read_csv(pathFile, na_values='default', sep=';', header=0, decimal=',',
                              warn_bad_lines=True)

except UnicodeDecodeError, err:
    print 'Error: ', err
    exit()
else:
    print 'Read: \n', repr(dataFrameRev)

print 'Read end! \n'
print '#####################################################'
print 'Program start: '
print '#####################################################\n'

# Define the search list start with 'SL', 'obi' or 'TG' in the column 'grecid'
searchStr = ['SL', 'obi', 'TG']

# Rename the columns
names=['grecid', 'RechnungsNr.', 'Year', 'Month', 'Day', 'SalesType', 'InvoiceId', 'CustAccount', 'ProjId', 'AccountName',
                                     'SalesRep', 'HcmWorkerRecId', 'Company', 'BusinessUnit', 'LineOfBusiness', 'pmcat1', 'pmcat2', 'pmcat3', 'TargetType',
                                     'TargetEnum', 'CostCenter', 'CustClassificationId', 'CustCreateMonth', 'ItemId', 'SalesQty', 'SalesPrice', 'Discount',
                                     'NetAmount', 'CostPrice', 'SalesMargin', 'targetA', 'targetB', 'Productmanager', 'Manufacturer', 'Remarks', 'Notes']

# Drop some useless columns 'projid', 'pmcat1', 'pmcat2', 'targetA', 'targetB' if OE file
if ('SalesStatus' in list(dataFrameRev.columns.values)):
    print 'OE Daten: '
    dataFrameRev = dataFrameRev.drop(['projid', 'pmcat1', 'pmcat2', 'targetA', 'targetB'], axis=1)
else:
    # Clean up the ',' token in the first position of the string in the column 'grecid'
    print 'Revenue Daten: '
    dataFrameRev['grecid'] = dataFrameRev['grecid'].map(lambda x: x.lstrip(' ,').strip(','))

# Drop the blank rows
dataFrameRev = dataFrameRev.dropna(axis=0, how='all')
dataFrameRev = dataFrameRev[dataFrameRev['grecid'] != '']


# Combine the text with NaN values in the last several columns to the column set with 'Notes'
for i in range(36, len(dataFrameRev.columns)):
    dataFrameRev.iloc[:, 35] = dataFrameRev.iloc[:, 35].fillna('') + '; ' + dataFrameRev.iloc[:, i].fillna('')

# Remove the last several columns till 'Notes' column
dataFrameRev = dataFrameRev.drop(dataFrameRev.columns[36 : len(dataFrameRev.columns)], axis=1)

# Remove the whole semicomma token cells in the column 'Notes'
dataFrameRev[dataFrameRev.columns[35]] = dataFrameRev[dataFrameRev.columns[35]].map(lambda x: x.strip(' ;'))

# Reset the columns name
dataFrameRev.columns = names

# Check the begin four prefix sign in the column 'grecid'
allStrGrecid = dataFrameRev['grecid'].apply(lambda x: x[:3])
prefixStr = allStrGrecid.unique()
searchList = prefixStr # Search list start with '**', 'obi' or 'TG' in the column 'grecid'

# Clean the text in column "grecid" and append to the "Notes"
def cleanUnvalid(someDataFrame):
    # Distinguish the valid and unvalid rows in column 'grecid'
    if ('SalesStatus' in list(someDataFrame.columns.values)):
        markedValid = someDataFrame['grecid'].str.startswith(tuple(searchStr)).fillna(False)
        markedUnvalid = ~someDataFrame['grecid'].str.startswith(tuple(searchStr)).fillna(False)
    else:
        markedValid = someDataFrame['grecid'].str.startswith(tuple(searchList)).fillna(False)
        markedUnvalid = ~someDataFrame['grecid'].str.startswith(tuple(searchList)).fillna(False)

    tempDF = someDataFrame['grecid']
    validRow = tempDF[markedValid]
    unvalidRow = tempDF[markedUnvalid].fillna('') # unvalid text in the first column

    unvalidRowSecond = someDataFrame[markedUnvalid]['RechnungsNr.'].dropna(axis=0, how='all') # unvalid text in the second column
    #===========================================================================
    # print unvalidRowSecond
    # exit()
    #===========================================================================

    #===========================================================================
    # validRowPath = r'C:\Users\yzhou\Documents\Workspace\Daten\validRow.csv'
    # validRow.to_csv(validRowPath, sep=';')
    # exit()
    #===========================================================================

    #===========================================================================
    # unvalidRowPath = r'C:\Users\yzhou\Documents\Workspace\Daten\unvalidRow.csv'
    # unvalidRow.to_csv(unvalidRowPath, sep=';')
    # print unvalidRow.index
    # print len(unvalidRow)
    # exit()
    #===========================================================================

    #===========================================================================
    # # Test the unvalid values in the second column
    # unvalidRowSecond = someDataFrame[markedUnvalid][['grecid', 'RechnungsNr.']]
    # print unvalidRowSecond[pd.notnull(unvalidRowSecond['RechnungsNr.'])]
    # # tempUnvalidSecond = r'C:\Users\yzhou\Documents\Workspace\Daten\tempUnvalidSecond.csv'
    # # unvalidRowSecond.to_csv(tempUnvalidSecond, sep=';')
    # exit()
    #===========================================================================

    # Apart two parts valid and unvalid tables to insert
    someDataFrame['Notes'] = someDataFrame['Notes'].fillna('')
    try:
        i = 0 # Index of unvalidRow
        m = 0 # Index of unvalidRowSecond
        k = 0 # Index of validRow
        mark = []
        while i < len(unvalidRow):
            j = i # Step of unvalidRow
            try:
                # Compare the index between the valid table and unvalid table
                while validRow.index[k] < unvalidRow.index[j]:
                    k += 1
                mark.append(validRow.index[k-1])
                appendIndex = validRow.index[k-1]

                if (j == len(unvalidRow)-1):

                    if (unvalidRow.index[j] == unvalidRowSecond.index[m]):
                        unvalidRow.values[j] += "; " + unvalidRowSecond.values[m]
                    someDataFrame.loc[appendIndex, 'Notes'] = str(someDataFrame.loc[appendIndex, 'Notes']) + "; " + unvalidRow.values[j]
                    break

                while (unvalidRow.index[j] < validRow.index[k]):

                    # Check if some text at the second column and append it
                    if (m < len(unvalidRowSecond) and unvalidRow.index[j] == unvalidRowSecond.index[m]):

                        # print 'unvalidRowSecond.index[m %d]: %s %s' %(m, unvalidRowSecond.index[m], unvalidRowSecond.values[m])
                        unvalidRow.values[i] += "; " + unvalidRowSecond.values[m]
                        m += 1

                    # Check if more than one unvalidrow in the first column
                    if (unvalidRow.index[j+1] < validRow.index[k]):
                        unvalidRow.values[i] += "; " + unvalidRow.values[j+1]

                    j += 1

                someDataFrame.loc[appendIndex, 'Notes'] = str(someDataFrame.loc[appendIndex, 'Notes']) + "; " + unvalidRow.values[i]

                if (m >= len(unvalidRowSecond)):
                    m -= 1

            except TypeError, err:
                print 'Appended string type: %s\n' %type(unvalidRow.values[i])
                print 'Notes type: %s\n' %type(someDataFrame.loc[appendIndex, 'Notes'])
                print 'TypeError: ', err
                exit()

            # j += 1
            i = j

    except IndexError, err:
        print 'Error index: %d' %i
        print 'IndexError: ', err
        exit()

    someDataFrame = someDataFrame[markedValid]

    return someDataFrame
    #===========================================================================
    # # Check if remove the unvalid rows
    # print unvalidRow[unvalidRow.values != 'removed']
    # print len(unvalidRow[unvalidRow.values != 'removed'])
    #===========================================================================

dataFrameRev = cleanUnvalid(dataFrameRev)
print dataFrameRev
# dataFrameRev['SalesMargin'].to_csv(tempPath, sep=';', decimal=',')
dataFrameRev.to_csv(destFile, sep=';', decimal=',')

#===============================================================================
# # Save to excel
# # Change encode
# def changeencode(data, cols):
#     for col in cols:
#         data[col] = data[col].str.decode('iso-8859-1').str.encode('utf-8')
#     return data
#
# # Create a Pandas Excel writer using XlsxWriter as the engine.
# writer = pd.ExcelWriter(destFileExcel, engine='xlsxwriter')
#
# # Convert the dataframe to an XlsxWriter Excel object.
# dataFrameRev.to_excel(writer, index=False, encoding='utf-8')
#
# # Close the Pandas Excel writer and output the Excel file.
# writer.save()
#===============================================================================



# Total handeling time
endTime = time.time()
print "total time is %s seconds." %(endTime-startTime)