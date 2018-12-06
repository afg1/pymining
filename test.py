"""

This test script performs a ttest using scipy's ttest_ind with unequal variance

The results should be identical (ish) to what pymining gives.

We get a p-value from the permutation test, rather than analytically though

"""



import numpy as np
from scipy.stats import ttest_ind

from pymining import imagesTTest, permutationTest

## generate some data
np.random.seed(12345678)
dataNonEvent = np.random.normal(loc=5, scale=10, size=500)

dataEvent = np.random.normal(loc=5, scale=10, size=500)

## Concatenate into one big array for pymining to work on
data = np.concatenate((dataNonEvent, dataEvent))

## pymining also needs labels
labels = np.concatenate((np.zeros((500,)), np.ones((500,))))

## Use scipy ttest, we should get the same result later
print(ttest_ind(dataEvent, dataNonEvent, equal_var=False, axis=0))


## Use pymining to get the t statistic
print(imagesTTest(data, labels).flatten()[0])


## Now use pymining to get a global p value. It should be similar to that from scipy
globalp, tthresh = permutationTest(data, labels)
print(globalp)
