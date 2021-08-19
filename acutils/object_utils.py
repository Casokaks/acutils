"""
acutils object_utils
==================================
Library implementing some utility functions for objects.

Created on May 212020
Author: Andrea Casati, andrea1.casati@gmail.com

"""


def dict_from_class(cls, excluded_keys_list):
    return dict(
        (key, value)
        for (key, value) in cls.__dict__.items()
        if key not in excluded_keys_list
    )
