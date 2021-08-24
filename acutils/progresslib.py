"""
acutils progresslib
==================================
Library including some utility functions.

Created on feb 27th 2020
Author: Andrea Casati, andrea1.casati@gmail.com

"""

def print_progress(completed, total, percentage=True, digits=3):
    i = (completed+1) * 100 if percentage else (completed+1)
    print("Progress {}%                         ".format(round(i/total, digits)), end="\r", flush=True)
