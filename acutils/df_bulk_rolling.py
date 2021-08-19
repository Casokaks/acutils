"""
acutils df_bulk_rolling
==================================
Library implementing bulk rolling execution of a generic method over a dataframe

Created on May 22 2020
Author: Andrea Casati, andrea1.casati@gmail.com

"""


import numpy as np
import pandas as pd
from .progresslib import print_progress
from .generic_function_execution import exec_func


def to_numpy(x):
    """
    Returns the numpy object of a pandas series or dataframe.
    """
    if isinstance(x, pd.DataFrame) or isinstance(x, pd.Series):
        return x.values
    else:
        return x


def to_pandas(x, index=None, columns=None, name=None):
    """
    Returns pandas dataframe or series given numpy array as input.
    """
    y = pd.DataFrame(x, index=index)
    if y.shape[1] > 1:
        if columns is not None:
            y.columns = columns
    else:
        y = y.iloc[:, 0]
        if name is not None:
            y.name = name
    return y


def fill_na(x, fill_na_with_zero=True):
    """
    Returns the numpy object with nans replaced by zeros.
    """
    if fill_na_with_zero:
        return np.nan_to_num(x)
    else:
        return x


def bulk_rolling(module_name, function_name, df, df_kwargs_name, rolling_window,
                 use_numpy=False, fill_na_with_zero=False, verbose=False, args=None, kwargs=None):
    """
    Returns the rolling execution of the input function over df dataframe.
    """
    # prep data
    _df = df.copy()
    if fill_na_with_zero:
        _df = _df.fillna(0)
    _df.reset_index(inplace=True, drop=True)
    _results_list = []
    tot = _df.shape[0]
    # iterate over rolling windows
    for i, _, in _df.iterrows():
        if ((i+1) - rolling_window) > 0:
            _df_iter_np = _df.iloc[((i+1) - rolling_window):(i+1), :]
            if use_numpy:
                _df_iter_np = to_numpy(x=_df_iter_np)
            # function execution
            kwargs[df_kwargs_name] = _df_iter_np
            _result = exec_func(
                module_name=module_name, function_name=function_name, args=args, kwargs=kwargs,
            )
            if isinstance(df, pd.DataFrame):
                _result = to_pandas(x=_result, index=df.columns)
            _results_list.append(_result)
        if verbose:
            print_progress(completed=i, total=tot)
    return pd.DataFrame(
        _results_list, columns=df.columns, index=df.index[rolling_window:],
    ).reindex(df.index)
