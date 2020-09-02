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
        self.table_row_lists_dictionary = {}

    def generate_pesticide_reports(self):
        self.split_reports_into_single_or_multi()
        self.make_single_tables()
        print(self.table_row_lists_dictionary)

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
        for sample in self.single_list:
            row_list = []
            row_counter = 0
            type = sample[0][1][0]
            loq_string = "LOQ (" + type + ")"
            for item in self.sample_data[sample[0][0]]:
                data_value_ppm = str(item)
                analyte_name = str(self.sample_data['pesticides/toxins list'].loc[row_counter])
                reference_recovery_value = str(self.sample_data["Curve Recovery"].loc[row_counter])
                loq_value = str(self.sample_data[loq_string].loc[row_counter])
                blank_value = "ND"
                latex_table_row = analyte_name +\
                    " & " +\
                    data_value_ppm +\
                    " & " +\
                    blank_value +\
                    " & " +\
                    reference_recovery_value +\
                    " & " +\
                    loq_value + r" \\"
                row_list.append(latex_table_row)
                row_counter += 1
            self.table_row_lists_dictionary[sample[0][0]] = row_list

    def make_multi_tables(self):
        pass
