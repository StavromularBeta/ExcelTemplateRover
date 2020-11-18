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

        #LOQ_Dictionaries
        self.Bud_LOQ_Dictionary = {"Abamectin": 60.48,
                                   "Acephate": 18.00,
                                   "Acequinocyl": 26.30,
                                   "Acetamiprid": 6.09,
                                   "Alidcarb": 51.36,
                                   "Allethrin": 47.41,
                                   "Azadirachtin": 695,
                                   "Azoxystrobin": 7.34,
                                   "Benzovindiflupyr": 5.06,
                                   "Bifenazate": 7.25,
                                   "Bifenthrin": 9.28,
                                   "Boscalid": 7.63,
                                   "Buprofezin": 5.77,
                                   "Carbaryl": 48.85,
                                   "Carbofuran": 6.46,
                                   "Chlorantraniliprole": 7.77,
                                   "Chlorphenapyr": 40.40,
                                   "Chlorpyrifos": 8.57,
                                   "Clofentezine": 6.69,
                                   "Clothianidin": 6.62,
                                   "Coumaphos": 6.34,
                                   "Cyantraniliprole": 5.38,
                                   "Cyfluthrin": 180,
                                   "Cypermethrin": 53.07,
                                   "Cyprodinil": 9.74,
                                   "Daminozide": 89.70,
                                   "Deltamethrin": 20.70,
                                   "Diazinon": 6.97,
                                   "Dichlorvos": 9.19,
                                   "Dimethoate": 6.85,
                                   "Dimethomorph": 4.50,
                                   "Dinotefuran": 32.20,
                                   "Dodemorph": 10.00,
                                   "Endosulfan-alpha": 30.00,
                                   "Endosulfan-beta": 5.00,
                                   "Endosulfan sulfate": 5.00,
                                   "Ethoprophos": 7.35,
                                   "Etofenprox": 10.74,
                                   "Etoxazole": 6.80,
                                   "Etridiazole": 26.00,
                                   "Fenoxycarb": 7.18,
                                   "Fenpyroximate": 11.07,
                                   "Fensulfothion": 7.00,
                                   "Fenthion": 8.57,
                                   "Fenvalerate": 60.8,
                                   "Fipronil": 9.13,
                                   "Flonicamid": 7.45,
                                   "Fludioxonil": 15.47,
                                   "Fluopyram": 6.37,
                                   "Hexythiazox": 6.85,
                                   "Imazalil": 5.29,
                                   "Imidacloprid": 5.57,
                                   "Iprodione": 490,
                                   "Kinoprene": 50.00,
                                   "Kresoxim-methyl": 5.79,
                                   "Malathion": 11.88,
                                   "Metalaxyl": 8.28,
                                   "Methiocarb": 11.50,
                                   "Methomyl": 7.02,
                                   "Methoprene": 8.00,
                                   "Methyl parathion": 25.00,
                                   "Mevinphos": 7.02,
                                   "MGK-264": 22.80,
                                   "Myclobutanil": 6.80,
                                   "Naled (Dibrom)": 7.48,
                                   "Novaluron": 5.30,
                                   "Oxamyl": 26.30,
                                   "Paclobutrazol": 7.60,
                                   "Permethrin": 35.80,
                                   "Phenothrin": 45.40,
                                   "Phosmet": 10.40,
                                   "Piperonyl butoxide": 47.40,
                                   "Primicarb": 6.50,
                                   "Prallethrin": 17.85,
                                   "Propiconazole": 5.30,
                                   "Propoxur": 10.65,
                                   "Pyraclostrobin": 6.70,
                                   "Pyrethrin I": 19.80,
                                   "Pyrethrin II": 49.40,
                                   "Pyridaben": 7.70,
                                   "Quintozene": 20.00,
                                   "Resmethrin": 22.10,
                                   "Spinetoram": 6.70,
                                   "Spinosad": 6.60,
                                   "Spirodiclofen": 16.20,
                                   "Spiromesifen": 6.50,
                                   "Spirotetramat": 11.20,
                                   "Spiroxamine": 7.20,
                                   "Tebuconazole": 5.50,
                                   "Tebufenozide": 10.30,
                                   "Teflubenzuron": 7.80,
                                   "Tetrachlorvinphos": 6.70,
                                   "Tetramethrin": 72.20,
                                   "Thiacloprid": 6.60,
                                   "Thiamethoxam": 10.50,
                                   "Thiophanate-methyl": 6.60,
                                   "Trifloxystrobin": 6.30,
                                   "aflatoxin B1": 0.030,
                                   "aflatoxin B2": 0.015,
                                   "aflatoxin G1": 0.030,
                                   "aflatoxin G2": 0.015,
                                   "ochratoxin": 0.030,
                                   "zearalenone": 0.030
                                   }
        self.Oil_LOQ_Dictionary = {"Abamectin": 145.00,
                                   "Acephate": 45.00,
                                   "Acequinocyl": 65.70,
                                   "Acetamiprid": 15.20,
                                   "Alidcarb": 128.00,
                                   "Allethrin": 92.10,
                                   "Azadirachtin": 480,
                                   "Azoxystrobin": 8.90,
                                   "Benzovindiflupyr": 9.06,
                                   "Bifenazate": 8.50,
                                   "Bifenthrin": 23.00,
                                   "Boscalid": 9.20,
                                   "Buprofezin": 14.40,
                                   "Carbaryl": 24.00,
                                   "Carbofuran": 9.50,
                                   "Chlorantraniliprole": 19.40,
                                   "Chlorphenapyr": 101.00,
                                   "Chlorpyrifos": 21.40,
                                   "Clofentezine": 9.60,
                                   "Clothianidin": 16.60,
                                   "Coumaphos": 8.90,
                                   "Cyantraniliprole": 7.50,
                                   "Cyfluthrin": 451.00,
                                   "Cypermethrin": 133.00,
                                   "Cyprodinil": 9.81,
                                   "Daminozide": 224.00,
                                   "Deltamethrin": 52.00,
                                   "Diazinon": 17.00,
                                   "Dichlorvos": 23.00,
                                   "Dimethoate": 9.55,
                                   "Dimethomorph": 11.20,
                                   "Dinotefuran": 4.80,
                                   "Dodemorph": 25.00,
                                   "Endosulfan-alpha": 75.00,
                                   "Endosulfan-beta": 12.50,
                                   "Endosulfan sulfate": 12.50,
                                   "Ethoprophos": 9.40,
                                   "Etofenprox": 26.80,
                                   "Etoxazole": 17.00,
                                   "Etridiazole": 65.00,
                                   "Fenoxycarb": 9.22,
                                   "Fenpyroximate": 27.70,
                                   "Fensulfothion": 8.90,
                                   "Fenthion": 9.50,
                                   "Fenvalerate": 152.00,
                                   "Fipronil": 9.55,
                                   "Flonicamid": 18.60,
                                   "Fludioxonil": 9.40,
                                   "Fluopyram": 7.60,
                                   "Hexythiazox": 17.20,
                                   "Imazalil": 8.90,
                                   "Imidacloprid": 9.20,
                                   "Iprodione": 402.00,
                                   "Kinoprene": 125.00,
                                   "Kresoxim-methyl": 14.50,
                                   "Malathion": 8.90,
                                   "Metalaxyl": 9.20,
                                   "Methiocarb": 9.50,
                                   "Methomyl": 17.50,
                                   "Methoprene": 24.00,
                                   "Methyl parathion": 62.50,
                                   "Mevinphos": 17.60,
                                   "MGK-264": 264.00,
                                   "Myclobutanil": 9.80,
                                   "Naled (Dibrom)": 18.70,
                                   "Novaluron": 20.20,
                                   "Oxamyl": 65.70,
                                   "Paclobutrazol": 9.00,
                                   "Permethrin": 89.50,
                                   "Phenothrin": 113.00,
                                   "Phosmet": 26.00,
                                   "Piperonyl butoxide": 118.00,
                                   "Primicarb": 9.10,
                                   "Prallethrin": 44.60,
                                   "Propiconazole": 13.20,
                                   "Propoxur": 9.00,
                                   "Pyraclostrobin": 8.90,
                                   "Pyrethrin I": 49.50,
                                   "Pyrethrin II": 123.00,
                                   "Pyridaben": 19.00,
                                   "Quintozene": 50.00,
                                   "Resmethrin": 45.00,
                                   "Spinetoram": 9.80,
                                   "Spinosad": 8.10,
                                   "Spirodiclofen": 40.60,
                                   "Spiromesifen": 16.20,
                                   "Spirotetramat": 9.55,
                                   "Spiroxamine": 18.00,
                                   "Tebuconazole": 8.90,
                                   "Tebufenozide": 9.60,
                                   "Teflubenzuron": 19.50,
                                   "Tetrachlorvinphos": 9.77,
                                   "Tetramethrin": 180.00,
                                   "Thiacloprid": 9.40,
                                   "Thiamethoxam": 9.90,
                                   "Thiophanate-methyl": 16.50,
                                   "Trifloxystrobin": 8.50,
                                   "aflatoxin B1": 0.030,
                                   "aflatoxin B2": 0.015,
                                   "aflatoxin G1": 0.030,
                                   "aflatoxin G2": 0.015,
                                   "ochratoxin": 0.030,
                                   "zearalenone": 0.030
                                   }
        self.Analyte_Numbers = {"Abamectin": 1,
                                   "Acephate": 2,
                                   "Acequinocyl": 3,
                                   "Acetamiprid": 4,
                                   "Alidcarb": 5,
                                   "Allethrin": 6,
                                   "Azadirachtin": 7,
                                   "Azoxystrobin": 8,
                                   "Benzovindiflupyr": 9,
                                   "Bifenazate": 10,
                                   "Bifenthrin": 11,
                                   "Boscalid": 12,
                                   "Buprofezin": 13,
                                   "Carbaryl": 14,
                                   "Carbofuran": 15,
                                   "Chlorantraniliprole": 16,
                                   "Chlorphenapyr": 17,
                                   "Chlorpyrifos": 18,
                                   "Clofentezine": 19,
                                   "Clothianidin": 20,
                                   "Coumaphos": 21,
                                   "Cyantraniliprole": 22,
                                   "Cyfluthrin": 23,
                                   "Cypermethrin": 24,
                                   "Cyprodinil": 25,
                                   "Daminozide": 26,
                                   "Deltamethrin": 27,
                                   "Diazinon": 28,
                                   "Dichlorvos": 29,
                                   "Dimethoate": 30,
                                   "Dimethomorph": 31,
                                   "Dinotefuran": 32,
                                   "Dodemorph": 33,
                                   "Endosulfan-alpha": 34,
                                   "Endosulfan-beta": 35,
                                   "Endosulfan sulfate": 36,
                                   "Ethoprophos": 37,
                                   "Etofenprox": 38,
                                   "Etoxazole": 39,
                                   "Etridiazole": 40,
                                   "Fenoxycarb": 41,
                                   "Fenpyroximate": 42,
                                   "Fensulfothion": 43,
                                   "Fenthion": 44,
                                   "Fenvalerate": 45,
                                   "Fipronil": 46,
                                   "Flonicamid": 47,
                                   "Fludioxonil": 48,
                                   "Fluopyram": 49,
                                   "Hexythiazox": 50,
                                   "Imazalil": 51,
                                   "Imidacloprid": 52,
                                   "Iprodione": 53,
                                   "Kinoprene": 54,
                                   "Kresoxim-methyl": 55,
                                   "Malathion": 56,
                                   "Metalaxyl": 57,
                                   "Methiocarb": 58,
                                   "Methomyl": 59,
                                   "Methoprene": 60,
                                   "Methyl parathion": 61,
                                   "Mevinphos": 62,
                                   "MGK-264": 63,
                                   "Myclobutanil": 64,
                                   "Naled (Dibrom)": 65,
                                   "Novaluron": 66,
                                   "Oxamyl": 67,
                                   "Paclobutrazol": 68,
                                   "Permethrin": 69,
                                   "Phenothrin": 70,
                                   "Phosmet": 71,
                                   "Piperonyl butoxide": 72,
                                   "Primicarb": 73,
                                   "Prallethrin": 74,
                                   "Propiconazole": 75,
                                   "Propoxur": 76,
                                   "Pyraclostrobin": 77,
                                   "Pyrethrin I": 78,
                                   "Pyrethrin II": 79,
                                   "Pyridaben": 80,
                                   "Quintozene": 81,
                                   "Resmethrin": 82,
                                   "Spinetoram": 83,
                                   "Spinosad": 84,
                                   "Spirodiclofen": 85,
                                   "Spiromesifen": 86,
                                   "Spirotetramat": 87,
                                   "Spiroxamine": 88,
                                   "Tebuconazole": 89,
                                   "Tebufenozide": 90,
                                   "Teflubenzuron": 91,
                                   "Tetrachlorvinphos": 92,
                                   "Tetramethrin": 93,
                                   "Thiacloprid": 94,
                                   "Thiamethoxam": 95,
                                   "Thiophanate-methyl": 96,
                                   "Trifloxystrobin": 97,
                                   "aflatoxin B1": 1,
                                   "aflatoxin B2": 2,
                                   "aflatoxin G1": 3,
                                   "aflatoxin G2": 4,
                                   "ochratoxin": 5,
                                   "zearalenone": 6
                                   }

    def generate_pesticide_reports(self):
        self.split_reports_into_single_or_multi()
        self.make_single_tables()
        self.make_multi_tables()
        self.combine_headers_tables_and_footers()
        return self.finished_reports_dictionary

# SINGLE AND MULTIPLE REPORT SPLITTING FUNCTIONS

    def split_reports_into_single_or_multi(self):
        for sample in self.single_reports_dictionary.items():
            self.single_list.append([sample])
        for key in self.sample_data["Job List"]:
            matching = [(bob, marley) for bob, marley in self.multiple_reports_dictionary.items() if
                        str(key)[0:6] in str(bob)]
            if len(matching) == 1:
                self.single_list.append(matching)
            else:
                self.multi_list.append(matching)

# SINGLE TABLE MAKING FUNCTIONS

    def make_single_tables(self):
        for sample in self.single_list:
            report_type = sample[0][1][2]
            row_counter = 0
            type = sample[0][1][0]
            loq_string = "LOQ (" + type + ")"
            table_head_string = r"""\newline
\renewcommand{\arraystretch}{1.1}
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
            end_table_line = r"""\end{tabular}
\end{table}
\textbf{continued on next page...}
\newpage
\newgeometry{head=65pt, includehead=true, includefoot=true, margin=0.5in}"""
            three_table_end_line = r'''\end{tabular}
\end{table}
\newpage
\newgeometry{head=65pt, includehead=true, includefoot=true, margin=0.5in}'''
            row_list = [table_head_string]
            for item in self.sample_data[sample[0][0]]:
                latex_table_row = self.make_single_table_row(item, row_counter, loq_string)
                row_addition_decision = self.single_table_row_inclusion_decider(row_counter, sample)
                if row_addition_decision == "END":
                    row_list.append(end_table_line)
                    row_list.append(table_head_string)
                    row_list.append(latex_table_row)
                elif row_addition_decision == "ADD":
                    row_list.append(latex_table_row)
                else:
                    pass
                row_counter += 1
            row_list.append(three_table_end_line)
            self.table_row_lists_dictionary[sample[0][0]] = [row_list, report_type]

    def make_single_table_row(self, data_value, row_counter, loq_string):
        bold_line = False
        data_value_ppm = str(data_value)
        try:
            if float(data_value_ppm) > 0:
                bold_line = True
        except ValueError:
            pass
        analyte_name = str(self.sample_data['pesticides/toxins list'].loc[row_counter])
        reference_recovery_value = str(self.sample_data["Curve Recovery"].loc[row_counter])
        loq_value = str(self.sample_data[loq_string].loc[row_counter])
        blank_value = "ND"
        if bold_line:
            latex_table_row = r"\textbf{" + analyte_name + \
                              " }& " + \
                              r"\textbf{" + self.sig_fig_and_rounding_for_values(data_value_ppm) + \
                              " }& " + \
                              r"\textbf{" + blank_value + \
                              " }& " + \
                              r"\textbf{" + self.sig_fig_and_rounding_for_values(loq_value) + \
                              " }& " + \
                              r"\textbf{" + self.sig_fig_and_rounding_for_values(reference_recovery_value) +\
                              r" }\\" + "\n" + r"\hline"
        else:
            latex_table_row = analyte_name + \
                              " & " + \
                              self.sig_fig_and_rounding_for_values(data_value_ppm) + \
                              " & " + \
                              blank_value + \
                              " & " + \
                              self.sig_fig_and_rounding_for_values(loq_value) + \
                              " & " + \
                              self.sig_fig_and_rounding_for_values(reference_recovery_value) +\
                              r" \\" + "\n" + r"\hline"
        return latex_table_row

    def single_table_row_inclusion_decider(self, row_counter, sample):
        toxins_status = sample[0][1][2]
        end_string = "END"
        denied_string = "NO"
        approved_string = "ADD"
        row_end_dictionary = {"Pesticides": 100,
                              "Toxins Only": 106,
                              "Both": 106}
        row_start_dictionary = {"Pesticides": 3,
                                "Toxins Only": 100,
                                "Both": 3}
        if row_counter in [40, 80]:
            if toxins_status == "Toxins Only":
                return denied_string
            else:
                return end_string
        else:
            if row_end_dictionary[toxins_status] > row_counter >= row_start_dictionary[toxins_status]:
                return approved_string
            else:
                return denied_string

# MULTI TABLE MAKING FUNCTIONS

    def make_multi_tables(self):
        for samples in self.multi_list:
            if not samples:
                break
            report_type = samples[0][1][2]
            split_list_counter = 0
            jobnumber = samples[0][0][0:6]
            split_list = self.multi_table_splitter(samples)
            loq_types_list = self.multi_table_loq_fetcher(split_list)
            table_headers = self.multi_table_header_creator(split_list, loq_types_list)
            end_table_line = r"""\end{tabular}
\end{table}
\textbf{continued on next page...}
\newpage
\newgeometry{head=65pt, includehead=true, includefoot=true, margin=0.5in}"""
            for sub_list in split_list:
                row_counter = 0
                row_list = [table_headers[split_list_counter]]
                while row_counter <= 109:
                    multi_table_row = self.make_multi_table_row(row_counter,
                                                                split_list_counter,
                                                                sub_list,
                                                                loq_types_list)
                    row_addition_decision = self.multi_table_row_inclusion_decider(row_counter, sub_list)
                    if row_addition_decision == "END":
                        row_list.append(end_table_line)
                        row_list.append(table_headers[split_list_counter])
                        row_list.append(multi_table_row)
                    elif row_addition_decision == "ADD":
                        row_list.append(multi_table_row)
                    else:
                        pass
                    row_counter += 1
                else:
                    row_list.append(r'''\end{tabular}
\end{table}
\newpage
\newgeometry{head=65pt, includehead=true, includefoot=true, margin=0.5in}''')
                    try:
                        self.table_row_lists_dictionary[jobnumber][0] += row_list
                    except KeyError:
                        self.table_row_lists_dictionary[jobnumber] = [row_list, report_type]
                    split_list_counter += 1

    def make_multi_table_row(self, row_counter, split_list_counter, sub_list, loq_types_list):
        analyte_name = str(self.sample_data['pesticides/toxins list'].loc[row_counter])
        reference_recovery_value = self.sig_fig_and_rounding_for_values(
            str(self.sample_data["Curve Recovery"].loc[row_counter]))
        sample_string = " "
        bold_line = False
        for sample in sub_list:
            sample_string_value = self.sig_fig_and_rounding_for_values(
                str(self.sample_data[sample[0]].loc[row_counter]))
            try:
                if float(sample_string_value):
                    bold_line = True
                else:
                    pass
            except ValueError:
                pass
            if bold_line:
                sample_string += r'\textbf{' + sample_string_value + "} &"
            else:
                sample_string += sample_string_value + " &"
        loq_string = " "
        for item in loq_types_list[split_list_counter]:
            loq_identifier_string = "LOQ (" + item + ")"
            loq_value = self.sig_fig_and_rounding_for_values(
                str(self.sample_data[loq_identifier_string].loc[row_counter]))
            if bold_line:
                loq_string += r'\textbf{' + loq_value + "} &"
            else:
                loq_string += loq_value + " &"
        if bold_line:
            multi_table_row = r'\textbf{' + analyte_name + \
                              "}&" + \
                              sample_string + \
                              loq_string + \
                              r" \textbf{ND} & " + \
                              r'\textbf{' + reference_recovery_value + \
                              r"} \\" +\
                              "\n" + "\hline"
        else:
            multi_table_row = analyte_name +\
                              "&" +\
                              sample_string +\
                              loq_string +\
                              " ND & " +\
                              reference_recovery_value +\
                              r" \\" +\
                              "\n" + "\hline"
        return multi_table_row

    def multi_table_row_inclusion_decider(self, row_counter, sub_list):
        toxins_status = sub_list[0][1][2]
        end_string = "END"
        denied_string = "NO"
        approved_string = "ADD"
        row_end_dictionary = {"Pesticides": 100,
                              "Toxins Only": 106,
                              "Both": 106}
        row_start_dictionary = {"Pesticides": 3,
                                "Toxins Only": 100,
                                "Both": 3}
        if row_counter in [40, 80]:
            if toxins_status == "Toxins Only":
                return denied_string
            else:
                return end_string
        else:
            if row_end_dictionary[toxins_status] > row_counter >= row_start_dictionary[toxins_status]:
                return approved_string
            else:
                return denied_string

    def multi_table_splitter(self, samples):
        counter = 0
        split_list = []
        small_list = []
        for item in samples:
            if counter == 3:
                small_list.append(item)
                split_list.append(small_list)
                small_list = []
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
        for item in split_list:
            header_string_1 = r"""\newline
\renewcommand{\arraystretch}{1.1}
\begin{table}[h!]\centering
\small
\begin{tabular}{p{\dimexpr0.20\textwidth-2\tabcolsep-\arrayrulewidth\relax}|"""
            header_string_2 = r"""p{\dimexpr0.10\textwidth-2\tabcolsep-\arrayrulewidth\relax}|
p{\dimexpr0.10\textwidth-2\tabcolsep-\arrayrulewidth\relax}
}"""
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
                first_row_string += r"\textbf{Sample " + str(sample_number) + "} & "
                second_row_string += "(ng/g) & "
            for item in loq_types_list[item_counter]:
                loq_string = "LOQ ( " + item + " )"
                first_row_string += r"\textbf{\small " + loq_string + "} & "
                second_row_string += r"(ng/g) & "
            first_row_string += r"\textbf{\small Blank} & "
            second_row_string += r"(ng/g) & "
            first_row_string += r" \textbf{\small \% Ref} \\"
            second_row_string += r" (Recovery) \\"
            header_strings[item_counter] += '\n' +\
                                            first_row_string +\
                                            '\n' +\
                                            second_row_string +\
                                            '\n' + r'\hline\hline'
            item_counter += 1
        return header_strings

# SHARED FUNCTIONS

    def generate_footer(self):
        pesticides_footer_string = r"""
    *Analysis includes all 96 target compounds on the Health Canada Mandatory List Aug 2019\newline
    **Trace = presence \& identity of compound verified, value below limit of quantification\newline
    As per international standards, all observed values are reported even if they are below LOQ's.\newline
    LOQ or MDL's are interpretative \& given as guidance only \& do not affect reported results.\newline\newline
    Method: Sample is solvent extracted, then cleaned using SPE (QuEChERS) methods. Multi-\newline
    residue analysis is carried out using UPLC-ESI-MS/MS/APCI \& GC-MS: SPME. Detection of\newline
    compounds meet or exceed HC requirements. Procedure ref AOAC 2007.01; USP $<$561$><$565$>$, EU 2.0813.\newline
    methods fully validated.
    \newline\newline\newline
    R. Bilodeau \phantom{aaaaaaaaaaaaaaaaaaaaaaaaaxaaaaaasasssssssssssss}H. Hartmann\\ Analytical Chemist: \underline{\hspace{3cm}}{ \hspace{3.2cm} Sr. Analytical Chemist: \underline{\hspace{3cm}}       
    \fancyfoot[C]{\textbf{MB Laboratories Ltd.}\\ \textbf{Web:} www.mblabs.com}
    \fancyfoot[R]{\textbf{Mail:} PO Box 2103\\ Sidney, B.C., V8L 356}
    \fancyfoot[L]{\textbf{T:} 250 656 1334\\ \textbf{E:} info@mblabs.com}
    \end{document}
     """
        toxins_footer_string = r"""
    Method: Sample is solvent extracted, then cleaned using SPE (QuEChERS) methods. Multi-\newline
    residue analysis is carried out using UPLC-ESI-MS/MS/APCI \& GC-MS: SPME. Detection of\newline
    compounds meet or exceed HC requirements. Procedure ref AOAC 2007.01; USP $<$561$><$565$>$, EU 2.0813.\newline
    methods fully validated.
	\newline\newline
	So = Standard deviation at zero analyte concentration; method detection limit \newline
	ND = none detected n/a = not applicable \newline
	ppb = parts per billion (ng/g) \newline\newline
	Mycotoxin - Maximum Tolerance Levels -CFIA FAO Food \& Nutrition Paper 64, 1997\newline
	\phantom{aaaaaaaaaal} CFIA - Fact Sheet - Mycotoxins LL Charmley \& HL Trenholm May 2010 \newline\newline
	Afalatoxin:\phantom{aaaaaa} 15 ppb \phantom{aaaaa} nut products \phantom{la} Canada\newline
	\phantom{aaaaaaaaaaaaaala}	20 ppb \phantom{aaaaa} all foods \phantom{aaaala} USA\newline\newline
	Ochratoxin A: \phantom{aaa}20 ppb \phantom{aaaaa} Cannabis \phantom{aaaaa} Health Canada\newline
	\phantom{aaaaaaaaaaaaaaal}	5-10 ppb \phantom{aaal} food \& spices\phantom{al}  EU
    \newline\newline\newline
    R. Bilodeau \phantom{aaaaaaaaaaaaaaaaaaaaaaaaaxaaaaaasasssssssssssss}H. Hartmann\\ Analytical Chemist: \underline{\hspace{3cm}}{ \hspace{3.2cm} Sr. Analytical Chemist: \underline{\hspace{3cm}}       
    \fancyfoot[C]{\textbf{MB Laboratories Ltd.}\\ \textbf{Web:} www.mblabs.com}
    \fancyfoot[R]{\textbf{Mail:} PO Box 2103\\ Sidney, B.C., V8L 356}
    \fancyfoot[L]{\textbf{T:} 250 656 1334\\ \textbf{E:} info@mblabs.com}
    \end{document}
"""
        return [pesticides_footer_string, toxins_footer_string]

    def combine_headers_tables_and_footers(self):
        for key, value in self.table_row_lists_dictionary.items():
            header = self.latex_header_and_sample_list_dictionary[key[0:6]]
            footer = self.generate_footer()
            table_string = ''
            for item in value[0]:
                table_string += item + '\n'
            if value[1] == "Pesticides":
                report = header + table_string[:-82] + footer[0]
            elif value[1] == "Toxins Only":
                report = header + table_string[:-82] + footer[1]
            else:
                report = header + table_string[:-82] + footer[0]
            self.finished_reports_dictionary[key] = [report, value[1]]

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
        elif value in ["Bud",
                       "batch std",
                       "Oil",
                       "Isolate",
                       "%rec",
                       "Rosin",
                       "Paper",
                       "Fresh Leaf",
                       "CS4",
                       "Arabica gum",
                       "pallet",
                       "Candy",
                       "Cheesecloth",
                       "Cream",
                       "Syringe",
                       "na"]:
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
            


