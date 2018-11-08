#!/Users/yuzhang/anaconda3/bin/python
# Filename: Autocorrelation.py
# Description:  This is a python script that has the function to calculated 
#               autocorrelation function of a set of data. This function uses
#               NIST's definition of autocorrelation, which can be found at
#               https://www.itl.nist.gov/div898/handbook/eda/section3/autocopl.htm
# Dates:    11-08-2018  Created

import numpy as np

def autocorr(data, norm = True):
    '''This function calculate the exact autocorrelation function using NIST 
    definition. If norm is set to false, no normalization.
    
    Input
        data: numpy.array. It turns out that list also works for current version 
            3.6.4 because when doing math operations with numpy variables, the 
            list will autimatically be convertedto numpy array.
        norm: boolean, default is True.
    return
        numpy.array
    '''
    if norm:
        r = [1]
        # avg and var are numpy.float64
        avg = np.mean(data)
        var = np.var(data)
        for i in range(1, len(data)):
            r.append(sum((data[:-i]-avg)*(data[i:]-avg))/var/len(data))
            break
    else:
        r = [np.sum(data**2)]
        for i in range(1, len(data)):
            r.append(sum((data[:-i])*(data[i:])))
    return np.array(r)
