"""
acutils timelib
==================================
Library including some date and time utility functions.

Created on aug 23rd 2021
Author: Andrea Casati, andrea1.casati@gmail.com

"""

from datetime import datetime

def now_to_string():
    """Returns string with datetime now."""
    return datetime.now().strftime("%Y-%m-%d|%H:%M:%S")
