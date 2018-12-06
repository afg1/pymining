# pymining
image based data mining in python/numpy

pymining implements a simple binary image based data mining approach, using a t-test per element of numpy arrays to produce a t-value map.

The statistic to determine global significance is in this case the most extreme t value.

The library should handle any dimensional data that numpy can give it, but will get slower for larger dimensions (obviously). 

When loading your data, make sure it is organised such that the samples are on the last axis, eg for 100 samples of 64x64 data, the shape should be (64,64,100).

Have fun!


## Requirements
numpy

## Nice to have 
tqdm - for nice progress bars in the permutation test


## Citations
