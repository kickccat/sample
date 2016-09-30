# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.core.pylabtools import figsize
pd.set_option('display.mpl_style', 'default')
# Always display all the columns
pd.set_option('display.line_width', 5000)
pd.set_option('display.max_columns', 60)

pathFile = r'''C:\Users\yzhou\Documents\Workspace\neonWorkspace\pandasStudy\weather_082016.csv'''
destFile = r'''C:\Users\yzhou\Documents\Workspace\neonWorkspace\pandasStudy\weather_082016_Final.csv'''
destFileExcel = r'''C:\Users\yzhou\Documents\Workspace\neonWorkspace\pandasStudy\weather_082016_Final.xlsx'''
weather_aug2016 = pd.read_csv(pathFile, skiprows=16, index_col='Date/Time',
                              sep=',', parse_dates=True, encoding='latin1')

# Define the non-ASCII character
chars = {
    '\xc2\xb0': '°'  # Temperature sign
    }

# Repalce the non-ASCII character
def replace_chars(match):
    char = match.group(0)
    return chars[char]

# print weather_aug2016[u"Temp (\xb0C)"].values

# Set the weather dataframe where temperature are not null
weather_aug2016_TempRecords = weather_aug2016[pd.notnull(weather_aug2016[u"Temp (\xb0C)"])]

# print weather_aug2016_TempRecords
#===============================================================================
# print weather_aug2016_TempRecords[u"Temp (\xb0C)"]
# weather_aug2016_TempRecords[u"Temp (\xb0C)"].plot(figsize=(15, 10))
# plt.show()
#===============================================================================

# Set the dateaframe where all records in columns are not null
weather_aug2016_NotNullRecords = weather_aug2016.dropna(axis=1, how='all')

# Get rid of the redundant and useless columns
weather_aug2016_RemainRecords = weather_aug2016_NotNullRecords.drop(['Year', 'Month', 'Day', 'Time',
                                                                     'Data Quality'], axis=1)
weather_aug2016_RemainRecordsFinal = weather_aug2016_RemainRecords.dropna(axis=0, how='all')

#===============================================================================
# # Plot the daily tends of the temperature
# temperatures = weather_aug2016_RemainRecords[[u'Temp (\xb0C)']]
# temperatures.loc[:, ('Hour')] = weather_aug2016.loc[:, ('Time')]
# temperatures.groupby('Hour').aggregate(np.median).plot(figsize=(15,5))
# plt.show()
#===============================================================================

#===============================================================================
# # Save the modified file with csv and excel format
# weather_aug2016_RemainRecordsFinal.to_csv(destFile, encoding='utf-8', sep=',')
# weather_aug2016_RemainRecordsFinal.to_excel(destFileExcel)
#===============================================================================

# Find the fogged days on Aug.2016
weather_aug2016_Description = weather_aug2016_RemainRecordsFinal[pd.notnull(weather_aug2016_RemainRecordsFinal
                                                                            ['Weather'])]['Weather']
isFog = weather_aug2016_Description.str.contains('Fog')
#===============================================================================
# print isFog.astype(float).resample('D', how=np.mean)
# isFog.astype(float).resample('D', how=np.mean).plot(kind='bar') # Alternative use plot.bar()
# plt.show()
#===============================================================================

#===============================================================================
# # Find the median temperature on August 2016(Parameter 'D'=day, 'M'=month, 'Y'=year in method resample)
# weather_aug2016_TempRecords[u'Temp (\xb0C)'].resample('D', how=np.median).plot(kind='bar')
# plt.show()
#===============================================================================

temperatures = weather_aug2016_RemainRecordsFinal[u'Temp (\xb0C)'].resample('D', how=np.median)
fogged = isFog.astype(float).resample('D', how=np.mean)
temperatures.name = "Temperature"
fogged.name = "Fogday"
states = pd.concat([temperatures, fogged], axis=1)
print states
states.plot(kind='bar', subplots=True, figsize=(15,5))
plt.show()