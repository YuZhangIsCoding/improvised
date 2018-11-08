# Autocorrelation function

Autocorrelation is the correlation of a signal/dataset with a delayed copy of itself as a function of delay. The analysis of autocorrelation can be used to find repeated patterns/seasonality. It's also used in signal processing for analyzing functions or series of values, such as time domain signals. This markdown file illustrates basics of autocorrelation. The [AutoCorrelation.ipynb](https://github.com/YuZhangIsCoding/improvised/blob/master/AutoCorrelation/AutoCorrelation.ipynb) in this repo walk you through examples and show some python implementations. And the [Autocorrelation.py](https://github.com/YuZhangIsCoding/improvised/blob/master/AutoCorrelation/Autocorrelation.py) is a python script that has brute-force implementation of calculating autocorrelation function given a numpy.array.

The exact formula can be defined as:

<img src="https://latex.codecogs.com/svg.latex?\hat{R}(k)=\frac{1}{(n-k)\sigma^2}\sum\limits_{t=1}^{n-k}(X_t-\mu)(X_{t+k}-\mu){\quad}for\,k%3Cn"/>

When the true mean &mu; and variance &sigma;<sup>2</sup> are known, this estimate is unbiased. In practise, there are several estimates when the true mean and variance are unknown:

1. If &mu; and &sigma;<sup>2</sup> are replaced by the standard formulae for sample mean and sample variance, then this is a biased estimate.
2. A periodogram-based estimate replaces *n-k* in the above formula with *n*. This estimate is always biased; however, it usually has a smaller mean squared error. This is said to be most widely used.
3. Another way is to treat the two protions of data {X<sub>1</sub>, X<sub>2</sub>, ..., X<sub>n-k</sub>} and {X<sub>k+1</sub>, X<sub>k+2</sub>, ..., X<sub>n</sub>} separately and calculating separate sample means and/or sample variance for use in defining the estimate.

There are many python functions that claim they compute/visualize autocorrelation function. These function deviates from each other though. Here, I list the functions I found as well as the estimates they used for computing:

* pandas.plotting.autocorrelation_plot: combines estimates 1 and 2, use sample mean and variance, also replace *n-k* with n.
* numpy.correlate: uses estimate 2 and is done without subtracting mean and dividing variance.
* matplotlib.pyplot.acorr: uses estimate 2 and is done without subtrcting mean and dividing variance.
* numpy.corrcoef: uses estimate 3, and is actually calculating pearson correlation coefficient between the subsets.
* pandas.autocorr: uses estimate 3, and is actually calculating Pearsono correlation coefficient between the subsets.
