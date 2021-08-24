"""
acutils timelib
==================================
Library including some date and time utility functions.

Created on aug 23rd 2021
Author: Andrea Casati, andrea1.casati@gmail.com

"""

from datetime import datetime

def now():
    """Returns now datetime."""
    return datetime.now()

def now_to_log():
    """Returns string with datetime now using format [%Y-%m-%d|%H:%M:%S]."""
    return now().strftime("[%Y-%m-%d|%H:%M:%S]")

def now_to_string():
    """Returns string with datetime now using format %Y/%m/%d %H:%M:%S."""
    return now().strftime("%Y/%m/%d %H:%M:%S")

def now_to_id():
    """Returns string with datetime now using format %Y%m%d%H%M%S."""
    return now().strftime("%Y%m%d%H%M%S")
