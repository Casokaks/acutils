"""
acutils normalize
==================================
Library implementing some utility functions on normalization.

Created on Oct 18 2019
Author: Andrea Casati, andrea1.casati@gmail.com

"""


import numpy as np
import pandas as pd


def normalize_zero_fixed(x, scale=1):
    """
    Returns a normalized version of input.
    Normalization between -scale and +scale keeping original zero as zero.
    """
    if isinstance(x, pd.Series) or isinstance(x, pd.DataFrame):
        scale_max = x.abs().max().max()
    else:
        scale_max = max(abs(np.array(x)))
    scale_min = -scale_max
    y = (x - scale_min) / (scale_max - scale_min)
    return (2 * scale * y) - scale


def normalize_series(series, multiplier=1):
    """
    Returns the input series normalized between [0,1] and multiplied by multiplier.
    """
    smax = series.max()
    smin = series.min()
    return multiplier * (series-smin) / (smax-smin)


if __name__ == '__main__':
    x_ = pd.DataFrame({'one': [1, 3, 4, 9, 90, -1, -100, 0],
                       'two': [1, 3, 4, 9, 90, -1, -200, 0]})
    x_ = np.array([1, 3, 4, 9, 90, -1, -100, 0])
    scale_ = 100
    y_ = normalize_zero_fixed(x=x_, scale=scale_)
    print('input = ', x_)
    print('scale = ', scale_)
    print('output = ', y_)
