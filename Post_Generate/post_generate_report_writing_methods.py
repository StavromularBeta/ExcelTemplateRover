import pandas as pd


class ReportMethods:

    def __init__(self,
                 sample_data,
                 updates,
                 latex_header_and_sample_list_dictionary,
                 single_reports_dictionary,
                 multiple_reports_dictionary):
        self.updates = updates
        self.sample_data = sample_data
        self.latex_header_and_sample_list_dictionary = latex_header_and_sample_list_dictionary
        self.single_reports_dictionary = single_reports_dictionary
        self.multiple_reports_dictionary = multiple_reports_dictionary
        self.finished_reports_dictionary = {}
        self.single_list = []
        self.multi_list = []

    def generate_pesticide_reports(self):
        self.split_reports_into_single_or_multi()
        self.make_single_tables()

    def split_reports_into_single_or_multi(self):
        for sample in self.single_reports_dictionary.items():
            self.single_list.append(sample)
        for key in self.sample_data["Job List"]:
            matching = [(bob, marley) for bob, marley in self.multiple_reports_dictionary.items() if
                        str(key)[0:6] in str(bob)]
            if len(matching) == 1:
                self.single_list.append(matching)
            else:
                self.multi_list.append(matching)

    def make_single_tables(self):
        print(self.single_list)
        print(self.sample_data['pesticides/toxins list'])
        row_counter = 0
        for sample in self.single_list:
            for item in self.sample_data[sample[0][0]]:
                print(str(self.sample_data['pesticides/toxins list'].loc[row_counter]) + '=' + str(item))
                row_counter += 1
