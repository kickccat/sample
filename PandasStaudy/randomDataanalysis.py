# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy.random as np
import sys
import matplotlib

print 'Python version ' + sys.version
print 'Pandas Version ' + pd.__version__
print 'Matplotlib version ' + matplotlib.__version__

# Set seed
np.seed(111)

# Function to generate test data
def createDataSet(Number):
    output = []

    for i in range(Number):

        # Create a weekly(mondays) date range
        rng = pd.date_range(start='1/1/2013', end='30/6/2016', freq='W-MON')

        # Create random data
        data = np.randint(low=25, high=1000, size=len(rng))

        # Status pool
        status = [1, 2, 3]

        # Make a random list of statuses
        randomStatus = [status[np.randint(low=0, high=len(status))] for i in range(len(rng))]

        # State pool
        states = ['BRA', 'BER', 'BAD', 'BAY', 'NRD', 'SAX', 'HESS', 'ber']

        # Make a random list of states
        randomStates = [states[np.randint(low=0, high=len(states))] for i in range(len(rng))]

        output.extend(zip(randomStates, randomStatus, data, rng))
#    print 'range = ' + str(rng)
    return output

dataset = createDataSet(4)
df = pd.DataFrame(data=dataset, columns=['State', 'Status', 'Customer Count', 'Status Date'])
# print df.head()

# Save results to excel
df.to_excel('Lesson3.xlsx', index=False)
