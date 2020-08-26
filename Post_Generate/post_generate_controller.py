import os, sys, inspect
import pandas as pd
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, currentdir)
from post_generate_header_methods import HeaderMethods
from post_generate_organize_methods import OrganizeMethods


class ReportWriter:

    def __init__(self, sample_data, header_data, updates):
        self.sample_data = sample_data
        self.header_data = header_data
        self.updates = updates
        self.latex_header_dictionary = {}
        self.latex_header_and_sample_list_dictionary = {}
        self.single_reports_dictionary = {}
        self.multiple_reports_dictionary = {}

#       This is for development - allows me to see the full DataFrame when i print to the console, rather than a
#       truncated version. This is useful for debugging purposes and ensuring that methods are working as intended.
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', -1)

#       Helper classes
        self.header_methods = HeaderMethods(header_data)
        self.organize_methods = OrganizeMethods(updates, sample_data)

    def post_generate_controller(self):
        self.latex_header_dictionary = self.header_methods.generate_job_latex_headers()
        self.latex_header_and_sample_list_dictionary = self.header_methods.generate_samples_list()
        self.single_reports_dictionary, self.multiple_reports_dictionary = \
            self.organize_methods.split_samples_into_single_or_multi()
        print(self.sample_data)
        print(self.header_data)
        print(self.updates)



