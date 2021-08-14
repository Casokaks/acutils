"""
Library implementing some utility functions
Created on Nov 26 2018
Author: Andrea Casati, andrea1.casati@gmail.com
"""


from collections.abc import Sequence


def dedup_list(my_list):
    """Remove duplicates from a list, while keeping the order. Especially useful for list of lists"""
    new_list = []
    for elem in my_list:
        if elem not in new_list:
            new_list.append(elem)
    return new_list


def get_shape(lst, shape=()):
    """
    returns the shape of nested lists similarly to numpy's shape.

    :param lst: the nested list
    :param shape: the shape up to the current recursion depth
    :return: the shape including the current depth
            (finally this will be the full depth)
    """
    if not isinstance(lst, Sequence):
        # base case
        return shape
    # peek ahead and assure all lists in the next depth
    # have the same length
    if isinstance(lst[0], Sequence):
        l = len(lst[0])
        if not all(len(item) == l for item in lst):
            msg = 'not all lists have the same length'
            raise ValueError(msg)

    shape += (len(lst), )
    # recurse
    shape = get_shape(lst[0], shape)
    return shape
