# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy.random as np
import sys
import matplotlib
from IPython.core.pylabtools import figsize

print 'System info:\n'
print '###################################################################'
print '# Python version ' + sys.version
print '# Pandas Version ' + pd.__version__
print '# Matplotlib version ' + matplotlib.__version__
print '###################################################################'
print '\n'
print 'Program result: \n'

# Path of file
pathExcelFile = r'C:\Users\yzhou\Documents\Workspace\neonWorkspace\pandasStudy\src\Lesson3.xlsx'

# Parse a specific sheet
df = pd.read_excel(pathExcelFile, 0, index_col='Status Date')
# print df['State'].unique()

# Clean State column and convert to upper case
df['State'] = df.State.apply(lambda x: x.upper())

# Only grab where Status == 1
mask = df.State == 'BER'
df.loc[mask, 'State'] = 'BRA'
# print df['State'].unique()

# Sort the index of State
# sortDF = df[df['State']=='BRA'].sort_index(axis=0)
daily = df.reset_index().groupby(['State', 'Status Date']).sum()
del daily['Status']
#===============================================================================
# # print daily
# daily.loc['BAD']['2016'].plot()
# plt.show()
#===============================================================================

stateYearMonth = daily.groupby([daily.index.get_level_values(0), daily.index.get_level_values(1).year,
                                daily.index.get_level_values(1).month])
# Set the basic quantile as .25 for the outlier test
daily['Lower'] = stateYearMonth['Customer Count'].transform(lambda x:
                                                            x.quantile(q=.25) - 1.5 * (x.quantile(q=.75) - x.quantile(q=.25)))
daily['Upper'] = stateYearMonth['Customer Count'].transform(lambda x:
                                                            x.quantile(q=.75) + 1.5 * (x.quantile(q=.75) - x.quantile(q=.25)))
daily['Outlier'] = (daily['Customer Count'] < daily['Lower']) | (daily['Customer Count'] > daily['Upper'])

# Remove Outliers
daily = daily[daily['Outlier'] == False]

# Combine all markets

# Get the max customer count by Date
allMarkets = pd.DataFrame(daily['Customer Count'].groupby(daily.index.get_level_values(1)).sum())
# allMarkets.columns = ['Customer Count'] # Rename the column
yearMonth = allMarkets.groupby([lambda x: x.year, lambda x: x.month])
# print yearMonth.head(5)
# Find the max customer count per year and month
allMarkets['Max'] = yearMonth['Customer Count'].transform(lambda x: x.max())

# Create the BHAG(Big Hairy Annual Goal) dataframe
data = [2000, 3000, 4000]
idx = pd.date_range(start='1/1/2013', end='6/30/2016', freq='A')
BHAG = pd.DataFrame(data, index=idx, columns=['BHAG'])

# Combine the BHAG and the allMarkets data set
combined = pd.concat([allMarkets, BHAG], axis=0)
combined = combined.sort_index(axis=0)

fig, axe = plt.subplots(figsize=(12, 6))

#===============================================================================
# combined['BHAG'].fillna(method='pad').plot(color='green', label='BHAG')
# combined['Max'].plot(color='blue', label='All Markets')
# plt.legend(loc='best')
# plt.show()
#===============================================================================

# Group by year and get the max value per year
year = combined.groupby(lambda x: x.year).max()

# Add a column representing the percent change per year
year['YR_PCT_Change'] = year['Max'].pct_change(periods=1)
#===============================================================================
# print (1 + year.ix[2016, 'YR_PCT_Change']) * year.ix[2016, 'Max']
#===============================================================================

# Graph
allMarkets['Max'].plot(figsize=(15,6))
plt.title('All Markets')

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20,12))
fig.subplots_adjust(hspace=1.0) # Create space between plots

daily.loc['BRA']['Customer Count']['2016':].fillna(method='pad').plot(ax=axes[0, 0])
daily.loc['BAD']['Customer Count']['2016':].fillna(method='pad').plot(ax=axes[0, 1])
daily.loc['BAY']['Customer Count']['2016':].fillna(method='pad').plot(ax=axes[1, 0])
daily.loc['NRD']['Customer Count']['2016':].fillna(method='pad').plot(ax=axes[1, 1])

# Add titles
axes[0, 0].set_title('Bradenburg')
axes[0, 1].set_title('Baden')
axes[1, 0].set_title('Bayern')
axes[1, 1].set_title('Nord Western')
plt.show()