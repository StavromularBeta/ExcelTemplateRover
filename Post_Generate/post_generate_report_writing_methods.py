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
        self.combine_headers_tables_and_footers()
        return self.finished_reports_dictionary

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
                    p{\dimexpr0.20\textwidth-2\tabcolsep-\arrayrulewidth\relax}|
                    p{\dimexpr0.20\textwidth-2\tabcolsep-\arrayrulewidth\relax}|
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
                    self.sig_fig_and_rounding_for_values(data_value_ppm) +\
                    " & " +\
                    blank_value +\
                    " & " +\
                    self.sig_fig_and_rounding_for_values(loq_value) +\
                    " & " +\
                    self.sig_fig_and_rounding_for_values(reference_recovery_value) + r" \\"
                if row_counter in [40, 80]:
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
            split_list_counter = 0
            jobnumber = samples[0][0][0:6]
            split_list = self.multi_table_splitter(samples)
            loq_types_list = self.multi_table_loq_fetcher(split_list)
            table_headers = self.multi_table_header_creator(split_list, loq_types_list)
            for sub_list in split_list:
                row_counter = 0
                row_list = [table_headers[split_list_counter]]
                while row_counter <= 109:
                    analyte_name = str(self.sample_data['pesticides/toxins list'].loc[row_counter])
                    reference_recovery_value = self.sig_fig_and_rounding_for_values(str(self.sample_data["Curve Recovery"].loc[row_counter]))
                    sample_string = "& "
                    for sample in sub_list:
                        sample_string += self.sig_fig_and_rounding_for_values(str(self.sample_data[sample[0]].loc[row_counter])) + " &"
                    loq_string = "& "
                    for item in loq_types_list[split_list_counter]:
                        loq_identifier_string = "LOQ (" + item + ")"
                        loq_value = self.sig_fig_and_rounding_for_values(str(self.sample_data[loq_identifier_string].loc[row_counter]))
                        loq_string += loq_value + " &"
                    multi_table_row = analyte_name + sample_string + " ND " + loq_string + reference_recovery_value + r" \\"
                    if row_counter in [40, 80]:
                        end_table_line = r"""\end{tabular}
                    \end{table}
                    \newpage
                    \newgeometry{head=65pt, includehead=true, includefoot=true, margin=0.5in}"""
                        row_list.append(end_table_line)
                        row_list.append(table_headers[split_list_counter])
                        row_list.append(multi_table_row)
                    else:
                        if row_counter >= 3:
                            row_list.append(multi_table_row)
                        else:
                            pass
                    row_counter += 1
                else:
                    row_list.append(r'\end{tabular}\end{table}')
                    self.table_row_lists_dictionary[jobnumber] = row_list
                    split_list_counter += 1

    def generate_footer(self):
        footer_string = r"""
    *Analysis includes all 96 target compounds on the Health Canada Mandatory List Oct 2018\newline
    **Trace = presence \& identity of compound verified, value below limit of quantification\newline
    As per international standards, all observed values are reported even if they are below LOQ's.\newline
    LOQ or MDL's are interpretative \& given as guidance only \& do not affect reported results.\newline\newline
    Method: Sample is solvent extracted, then cleaned using SPE (QuEChERS) methods. Multi-\newline
    residue analysis is carried out using UPLC-ESI-MS/MS/APCI \& GC-MS: SPME. Detection of\newline
    compounds meet or exceed HC requirements. Procedure ref AOAC 2007.01; USP <561><565>, eu 2.0813.\newline
    methods fully validated.
    \newline\newline\newline
    R. Bilodeau \phantom{aaaaaaaaaaaaaaaaaaaaaaaaaxaaaaaasasssssssssssss}H. Hartmann\\ Analytical Chemist: \underline{\hspace{3cm}}{ \hspace{3.2cm} Sr. Analytical Chemist: \underline{\hspace{3cm}}       
    \fancyfoot[C]{\textbf{MB Laboratories Ltd.}\\ \textbf{Web:} www.mblabs.com}
    \fancyfoot[R]{\textbf{Mail:} PO Box 2103\\ Sidney, B.C., V8L 356}
    \fancyfoot[L]{\textbf{T:} 250 656 1334\\ \textbf{E:} info@mblabs.com}
    \end{document}
     """
        return footer_string

    def combine_headers_tables_and_footers(self):
        for key, value in self.table_row_lists_dictionary.items():
            header = self.latex_header_and_sample_list_dictionary[key[0:6]]
            footer = self.generate_footer()
            table_string = ''
            for item in value:
                table_string += item + '\n'
            report = header + table_string + footer
            self.finished_reports_dictionary[key] = report

    def sig_fig_and_rounding_for_values(self, value):
        check = self.sig_fig_rounder_pre_filter(value)
        if check == "okay":
            value = float(value)
            string_value = str(value)
            split_string = string_value.split('.')
            pre_decimal = split_string[0]
            if len(pre_decimal) >= 3:
                value = int(round(value))
            elif len(pre_decimal) >= 2:
                value = round(value, 1)
            elif len(pre_decimal) == 1:
                if int(pre_decimal[0]) == 0:
                    value = round(value, 3)
                    if len(str(value)) == 4:
                        value = str(value) + '0'
                else:
                    value = round(value, 2)
                    if len(str(value)) == 3:
                        value = str(value) + '0'
            if value == 0.0:
                value = 'ND'
            return str(value)
        else:
            return check

    def sig_fig_rounder_pre_filter(self, value):
        if value == '-':
            return value
        elif value == 'nan':
            return "ND"
        elif value in ["Bud", "batch std", "Oil", "Isolate", "%rec", "Rosin", "Paper"]:
            return value
        elif "-" in value:
            return value
        elif "ng/ml" in value:
            return value
        elif "ng/g" in value:
            return value
        elif "LOQ" in value:
            return value
        else:
            return "okay"

    def multi_table_splitter(self, samples):
        counter = 0
        split_list = []
        small_list = []
        for item in samples:
            if counter == 3:
                small_list.append(item)
                split_list.append(small_list)
                counter = 0
            else:
                small_list.append(item)
                counter += 1
        if small_list:
            split_list.append(small_list)
        return split_list

    def multi_table_loq_fetcher(self, split_list):
        list_of_loq_lists = []
        loq_list = []
        for job in split_list:
            for sample in job:
                loq_list.append(sample[1][0])
            loq_list = list(set(loq_list))
            list_of_loq_lists.append(loq_list)
            loq_list = []
        return list_of_loq_lists

    def multi_table_header_creator(self, split_list, loq_types_list):
        header_strings = []
        item_counter = 0
        header_string_1 = r"""\newline
\renewcommand{\arraystretch}{0.9}
\begin{table}[h!]\centering
\small
\begin{tabular}{p{\dimexpr0.20\textwidth-2\tabcolsep-\arrayrulewidth\relax}|"""
        header_string_2 = r"""p{\dimexpr0.10\textwidth-2\tabcolsep-\arrayrulewidth\relax}|
p{\dimexpr0.10\textwidth-2\tabcolsep-\arrayrulewidth\relax}
}"""
        for item in split_list:
            columns_required = len(item) + len(loq_types_list[item_counter])
            space_per_column = 0.60 / columns_required
            extra_column_string = r"""p{\dimexpr""" +\
                                  str(space_per_column) +\
                                  r"""\textwidth-2\tabcolsep-\arrayrulewidth\relax}|"""
            for number in range(columns_required):
                header_string_1 += extra_column_string
            header_string_1 += header_string_2
            header_strings.append(header_string_1)
            first_row_string = r"\textbf{Analyte} & "
            second_row_string = r"& "
            for subitem in item:
                sample_number = subitem[0][-1]
                first_row_string += "Sample " + str(sample_number) + " & "
                second_row_string += "(ng/g) & "
            for item in loq_types_list[item_counter]:
                loq_string = "LOQ ( " + item + " )"
                first_row_string += r"\textbf{\small " + loq_string + "} & "
                second_row_string += r"(ng/g) & "
            first_row_string += r"\textbf{\small Blank} & "
            second_row_string += r"(ng/g) & "
            first_row_string += r" \textbf{\small \% Ref} \\"
            second_row_string += r" (Recovery) \\"
            header_strings[item_counter] += '\n' + first_row_string + '\n' + second_row_string
            item_counter += 1
        return header_strings

            


