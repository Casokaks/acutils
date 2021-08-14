"""
Library to import and execute functions
Created on Oct 27 2017
Author: Andrea Casati, andrea1.casati@gmail.com
"""


from importlib import import_module
import sys
sys.path.insert(0, 'C:/Users/caso8/Google Drive/Python Scripts/acpylibs/datatrader/')


def exec_func(module_name, function_name, args=None, kwargs=None):
    """
    Execute the function_name form module_name passing args and kwargs as input parameters.
    :param string module_name: name of the module containing the function, eg. talib
    :param string function_name: name of the function to execute, eg EMA
    :param list args: list of values passed to the function as input params, eg. [[1,2,3,4,5],5]
    :param dict kwargs: dictionary of values passed to the function as input params,
    eg. {'timeperiod':5, 'real':close_['AAPL']}
    :return ?: whatever the function returns
    """
    if args is None:
        args = []
    if kwargs is None:
        kwargs = {}
    module = import_module(module_name)
    return getattr(module, function_name)(*args, **kwargs)


def main():
    x = 1
    y = exec_func(module_name='numpy', function_name='log', args=[1], kwargs={})
    print('log({}) = {}'.format(x, y))


if __name__ == '__main__':
    main()
