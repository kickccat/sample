# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib
import time

matplotlib.pyplot.style.use('default')
# Always display all the columns
pd.set_option('display.width', 5000)
pd.set_option('display.max_columns', 60)

pathFile = r'C:\Users\yzhou\Documents\Workspace\neonWorkspace\pandasStudy\Service_Requests_firstQuarter2016.csv'
destFile = r'C:\Users\yzhou\Documents\Workspace\neonWorkspace\pandasStudy\Service_Requests_firstQuarter2016_Final.csv'
destFileExcel = r'C:\Users\yzhou\Documents\Workspace\neonWorkspace\pandasStudy\Service_Requests_firstQuarter2016_Final.xlsx'

startTime = time.time()
naValues = ['UNKNOWN', np.nan, '?', 'N/A', 'NO CLUE', '0', None]
requests = pd.read_csv(pathFile, na_values=naValues, dtype={'Incident Zip': str}, encoding='utf-8', low_memory=False)
# print requests['Incident Zip'].unique()

#===============================================================================
# print np.dtype(requests['Incident Zip'])
# requests.to_excel(destFileExcel)
# #print requests['Incident Zip'].unique()
#===============================================================================

#===============================================================================
# # Find the zip number with dash token
# rowsWithDashes = requests['Incident Zip'].str.contains('-').fillna(False)
# print len(requests[rowsWithDashes])
# print requests[rowsWithDashes]['Incident Zip'].str.find('-')
# print requests[rowsWithDashes]
#===============================================================================

# Find the zipcode longer than 6 and check if the dash token is at the 4th position or 'AIRPORT' is in the string
longZipCodes = requests['Incident Zip'].str.len() > 6
notStrZipCode = requests['Incident Zip'][longZipCodes].str.find('AIRPORT')==-1
dashAt4thPosition = requests['Incident Zip'][longZipCodes].str.find('-')==4
# print requests['Incident Zip'][longZipCodes].unique()

# Direct copy makes SettingWithCopyWarning and the labelbased parameter will be used to set the new value
# (sequence as condition then labels in the index)
# Set the valid zip code values
requests.loc[longZipCodes & notStrZipCode, 'Incident Zip'] = requests.loc[longZipCodes & notStrZipCode, 'Incident Zip'].str.slice(0, 5)
requests.loc[longZipCodes & dashAt4thPosition, 'Incident Zip'] = requests.loc[longZipCodes & dashAt4thPosition, 'Incident Zip'].str.slice(0, 4)

# print requests[requests['Incident Zip'] == '00000']
# Find the zip code with no meaning number '00000' or '000000'
zeroZips = ((requests['Incident Zip'] == '00000') | (requests['Incident Zip'] == '000000'))
requests.loc[zeroZips, 'Incident Zip'] = np.nan

#===============================================================================
# # Find and sort the unique zip codes
# uniqueZips = requests['Incident Zip'].unique()
# uniqueZips.sort()
# print uniqueZips
#===============================================================================

# Estimate the accuracy depending on the zip codes and ignore the NaN or None values
zips = requests['Incident Zip']
isClose = zips.str.startswith('0') | zips.str.startswith('1')
isFar = (~(isClose.fillna(True).astype(bool))) & (pd.notnull(zips))
# print zips[isFar]
# print requests[isFar][['Incident Zip', 'Descriptor', 'City']].sort_values(by='Incident Zip')
# print requests['City'].str.upper().value_counts()
print requests['Incident Zip'].unique()

endTime = time.time()
print "total time is %s seconds." %(endTime-startTime)