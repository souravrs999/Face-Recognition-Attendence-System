#! env/usr/bin python

''' Necessary Imports '''
import os

''' Function to create a directory if it does not exist '''
def mk_dir(directory):

    if not os.path.exists(directory):

        ''' Create the directory '''
        os.mkdir(directory)

