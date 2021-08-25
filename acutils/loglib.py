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
        self.file = file
        self.log = open(file, "a")
        self.log.close()

    def write(self, message):
        # write to terminal
        self.terminal.write(message)
        # write to log file
        self.log = open(self.file, "a")
        self.log.write(message)
        self.log.close()

    def flush(self):
        #this flush method is needed for python 3 compatibility.
        #this handles the flush command by doing nothing.
        #you might want to specify some extra behavior here.
        pass    
