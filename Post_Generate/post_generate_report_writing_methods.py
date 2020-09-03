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
        self.make_multi_tables()
        for key, value in self.table_row_lists_dictionary.items():
            print(key)
            for item in value:
                print(item)

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
            row_counter = 0
            type = sample[0][1][0]
            loq_string = "LOQ (" + type + ")"
            table_head_string = r"""\newline
    \renewcommand{\arraystretch}{0.9}
    \begin{table}[h!]\centering
    \small
    \begin{tabular}{p{\dimexpr0.20\textwidth-2\tabcolsep-\arrayrulewidth\relax}|
                    p{\dimexpr0.20\textwidth-2\tabcolsep-\arrayrulewidth\relax}|
                    p{\dimexpr0.20\textwidth-2\tabcolsep-\arrayrulewidth\relax}
                    p{\dimexpr0.20\textwidth-2\tabcolsep-\arrayrulewidth\relax}
                    p{\dimexpr0.20\textwidth-2\tabcolsep-\arrayrulewidth\relax}
                    }
    \textbf{Analyte} & \textbf{Sample 1}  & \textbf{\small Blank} &  $\mathbf{\small """ +\
                                loq_string + r"""}$ & \textbf{\small \% Ref} \\
    & (ng/g) & (ng/g) & (ng/g) & (Recovery) \\
    \hline
    \hline"""
            row_list = [table_head_string]
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
                    loq_value +\
                    " & " +\
                    reference_recovery_value + r" \\"
                if row_counter == 60:
                    end_table_line = r"""\end{tabular}
\end{table}
\newpage
\newgeometry{head=65pt, includehead=true, includefoot=true, margin=0.5in}"""
                    row_list.append(end_table_line)
                    row_list.append(table_head_string)
                    row_list.append(latex_table_row)
                else:
                    if row_counter >= 3:
                        row_list.append(latex_table_row)
                    else:
                        pass
                row_counter += 1
            row_list.append(r'\end{tabular}\end{table}')
            self.table_row_lists_dictionary[sample[0][0]] = row_list

    def make_multi_tables(self):
        for samples in self.multi_list:
            row_counter = 0
            row_list = []
            jobnumber = samples[0][0][0:6]
            while row_counter <= 109:
                analyte_name = str(self.sample_data['pesticides/toxins list'].loc[row_counter])
                reference_recovery_value = str(self.sample_data["Curve Recovery"].loc[row_counter])
                loq_types_list = []
                sample_string = "& "
                for sample in samples:
                    sample_string += str(self.sample_data[sample[0]].loc[row_counter]) + " &"
                    loq_types_list.append(sample[1][0])
                loq_types_list = list(set(loq_types_list))
                loq_string = "& "
                for item in loq_types_list:
                    loq_identifier_string = "LOQ (" + item + ")"
                    loq_value = str(self.sample_data[loq_identifier_string].loc[row_counter])
                    loq_string += loq_value + " &"
                multi_table_row = analyte_name + sample_string + " ND " + loq_string + reference_recovery_value + r" \\"
                if row_counter >= 3:
                    row_list.append(multi_table_row)
                row_counter += 1
            else:
                self.table_row_lists_dictionary[jobnumber] = row_list

