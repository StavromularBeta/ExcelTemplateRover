import pandas as pd
import os, sys, inspect
import collections
import xlsxwriter
from math import floor, log10, isnan
# below 3 lines add the parent directory to the path, so that SQL_functions can be found.
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0, parentdir)


class PreGenerateDataManipulation:
    """This file controls the data manipulation processes occurring prior to generating latex files.
     Raw data -> Processed data."""

    def __init__(self, excel_file):
        self.excel_file = excel_file
        self.page_list = []
        self.sample_counter_list = []
        self.sample_dictionary = collections.OrderedDict()
        self.pt_data = pd.read_excel(self.excel_file)
#       This is for development - allows me to see the full DataFrame when i print to the console, rather than a
#       truncated version. This is useful for debugging purposes and ensuring that methods are working as intended.
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', -1)

    def data_manipulation_controller(self):
        self.page_splitter()
        self.sample_sorter()
        self.sample_dictionary_assembler()
        self.create_job_list()
        return self.sample_dictionary

    def page_splitter(self):
        counter = 1
        for item in self.pt_data.iloc[:, 2]:
            counter += 1
            if str(item) == "Targetlynx files:":
                self.pt_data = pd.read_excel(self.excel_file, skiprows=counter)
                break
        number_of_pages = range((self.pt_data.shape[0] % 113) + 1)
        page_counter = 0
        for item in number_of_pages:
            page = self.pt_data.loc[page_counter:page_counter + 112]
            page.reset_index(drop=True, inplace=True)
            page = page.drop([64, 65, 66])
            page.reset_index(drop=True, inplace=True)
            if self.sample_dictionary:
                pass
            else:
                self.sample_dictionary['pesticides/toxins list'] = page.iloc[:, 2]
            self.page_list.append(page)
            page_counter += 114

    def sample_sorter(self):
        for item in self.page_list:
            counter = 0
            sample_list = []
            for subitem in item.iloc[1]:
                if str(subitem) == 'nan':
                    counter += 1
                    pass
                else:
                    sample_list.append([subitem, counter, item.iloc[2, counter], item.iloc[0, counter]])
                    counter += 1
            self.sample_counter_list.append(sample_list)

    def sample_dictionary_assembler(self):
        counter = 0
        for item in self.sample_counter_list:
            for subitem in item:
                try:
                    if "batch std" in subitem[3] and subitem[2] == "%rec":
                        self.sample_dictionary["Curve Recovery"] = self.page_list[counter].iloc[:, subitem[1]]
                except TypeError:
                    pass
                if subitem[3] == "Bud" and subitem[2] == "%rec":
                    self.sample_dictionary["Spike (Bud)"] = self.page_list[counter].iloc[:, subitem[1]]
                elif subitem[3] == "Oil" and subitem[2] == "%rec":
                    self.sample_dictionary["Spike (Oil)"] = self.page_list[counter].iloc[:, subitem[1]]
                elif subitem[3] == "Paper" and subitem[2] == "%rec":
                    self.sample_dictionary["Spike (Paper)"] = self.page_list[counter].iloc[:, subitem[1]]
                elif "CS" in subitem[0] and subitem[2] == "%rec":
                    self.sample_dictionary["Curve Recovery"] = self.page_list[counter].iloc[:, subitem[1]]
                elif subitem[0] == "Bud" and subitem[2] == "LOQ (est.)":
                    self.sample_dictionary["LOQ (Bud)"] = self.page_list[counter].iloc[:, subitem[1]]
                elif subitem[0] == "Oil" and subitem[2] == "LOQ (est.)":
                    self.sample_dictionary["LOQ (Oil)"] = self.page_list[counter].iloc[:, subitem[1]]
                elif subitem[0] == "Paper" and subitem[2] == "LOQ (est.)":
                    self.sample_dictionary["LOQ (Paper)"] = self.page_list[counter].iloc[:, subitem[1]]
                else:
                    self.sample_dictionary[subitem[0]] = self.page_list[counter].iloc[:, subitem[1]]
            counter += 1

    def create_job_list(self):
        job_list = []
        sample_list = []
        for item in self.sample_dictionary.keys():
            try:
                if isinstance(int(item[0:6]), int):
                    job_list.append(item[0:6])
                    sample_list.append(item)
            except ValueError:
                pass
        job_list = list(set(job_list))
        sample_list = list(set(sample_list))
        self.sample_dictionary["Job List"] = job_list
        self.sample_dictionary["Sample List"] = sample_list

    def print_sample_dictionary(self):
        for key, value in self.sample_dictionary.items():
            print('XXXXXXXXXXXXXXXXXXXXXX')
            print(key)
            print('XXXXXXXXXXXXXXXXXXXXXX')
            print(value)
            print('XXXXXXXXXXXXXXXXXXXXXX')
