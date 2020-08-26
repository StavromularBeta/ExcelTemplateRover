import os, sys, inspect
import pandas as pd
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, currentdir)


class ReportWriter:

    def __init__(self, sample_data, header_data, updates):
        self.sample_data = sample_data
        self.header_data = header_data
        self.updates = updates

#       This is for development - allows me to see the full DataFrame when i print to the console, rather than a
#       truncated version. This is useful for debugging purposes and ensuring that methods are working as intended.
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', -1)

    def post_generate_controller(self):
        print(self.sample_data)
        print(self.header_data)
        print(self.updates)



