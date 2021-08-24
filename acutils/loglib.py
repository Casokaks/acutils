"""
acutils loglib
==================================
Library exporting light logging utilities to write output to both terminal and file.

Created on aug 23rd 2021
Author: Andrea Casati, andrea1.casati@gmail.com

"""

import sys

class Logger(object):
    """
    How to use:
    - initialize by: 
        import sys
        sys.stdout = Logger(file="path/to/file/logname.log") 
    - just use normal prints to write outputs to both standard output and logfile: 
        print("Hello")
    """
    
    def __init__(self, file="logfile.log"):
        self.terminal = sys.stdout
        self.log = open(file, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)  

    def flush(self):
        #this flush method is needed for python 3 compatibility.
        #this handles the flush command by doing nothing.
        #you might want to specify some extra behavior here.
        pass    
