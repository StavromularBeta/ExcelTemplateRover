import tkinter as Tk
from tkinter import font as tkFont
from tkinter import filedialog
import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0, parentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, currentdir)
from Post_Generate.post_generate_controller import ReportWriter as report


class BatchWindow(Tk.Frame):
    def __init__(self, parent, **kwargs):
        Tk.Frame.__init__(self, parent, **kwargs)
        self.parent = parent
        self.header_font = tkFont.Font(size=10, weight='bold')
        self.master_display_frame = Tk.Frame(self)
        self.sub_display_frame = Tk.Frame(self)
        self.recovery_data_frame = Tk.Frame(self.sub_display_frame)
        self.headers_data_frame = Tk.Frame(self.sub_display_frame)
        self.samples_checklist_frame = Tk.Frame(self.sub_display_frame)
        #Header info list
        self.header_information_list = []
        self.updated_header_information_list = []
        #Sample type list
        self.sample_type_option_list = []
        self.updated_sample_type_option_list = []
        #Report type list
        self.report_type_option_list = []
        self.updated_report_type_option_list = []
        #Single or multi list
        self.single_or_multi_list = []
        self.updated_single_or_multi_list = []
        #Sample name lists
        self.sample_name_list = []
        self.updated_sample_name_list = []
        #Update Dictionary
        self.updated_dictionary = {}
        #sample number list
        self.sample_number_list = []

    def batch(self, sample_dictionary, header_dictionary):
        self.create_scrollable_window()
        self.recovery_data_frame.grid(row=0, column=0, sticky=Tk.W, padx=10, pady=10)
        self.headers_data_frame.grid(row=1, column=0, sticky=Tk.W, padx=10, pady=10)
        self.samples_checklist_frame.grid(row=2, column=0, sticky=Tk.W, padx=10, pady=10)
        self.create_recovery_frame(sample_dictionary)
        self.create_header_frames(header_dictionary)
        self.create_samples_checklist_option_frame(sample_dictionary, header_dictionary)

    def create_scrollable_window(self):
        display_all_jobs_canvas = Tk.Canvas(self.master_display_frame,
                                            width=1280,
                                            height=700,
                                            scrollregion=(0, 0, 0, 15000))
        all_entries_scroll = Tk.Scrollbar(self.master_display_frame,
                                          orient="vertical",
                                          command=display_all_jobs_canvas.yview)
        display_all_jobs_canvas.configure(yscrollcommand=all_entries_scroll.set)
        all_entries_scroll.pack(side='right',
                                fill='y')
        display_all_jobs_canvas.pack(side="left",
                                     fill='y')
        display_all_jobs_canvas.create_window((0, 0),
                                              window=self.sub_display_frame,
                                              anchor='nw')
        self.master_display_frame.grid()

    def create_recovery_frame(self, sample_dictionary):
        #Analytes
        analytes_label = Tk.Label(self.recovery_data_frame, text="Analytes", font=self.header_font)
        analytes_label.grid(row=0, column=0, sticky=Tk.W)
        analytes_text = Tk.Text(self.recovery_data_frame, width=40, height=20)
        analytes_text.insert(Tk.END, sample_dictionary["pesticides/toxins list"].to_string())
        analytes_text.config(state="disabled")
        analytes_text.grid(row=1, column=0)
        #Bud Spike
        bud_recovery_label = Tk.Label(self.recovery_data_frame, text="Bud Spike", font=self.header_font)
        bud_recovery_label.grid(row=0, column=1, sticky=Tk.W)
        bud_recovery_text = Tk.Text(self.recovery_data_frame, width=20, height=20)
        try:
            bud_recovery_text.insert(Tk.END, sample_dictionary["Spike (Bud)"].to_string())
        except KeyError:
            bud_recovery_text.insert(Tk.END, "No bud spike.")
        bud_recovery_text.config(state="disabled")
        bud_recovery_text.grid(row=1, column=1)
        #Oil Spike
        oil_recovery_label = Tk.Label(self.recovery_data_frame, text="Oil Spike", font=self.header_font)
        oil_recovery_label.grid(row=0, column=2, sticky=Tk.W)
        oil_recovery_text = Tk.Text(self.recovery_data_frame, width=20, height=20)
        try:
            oil_recovery_text.insert(Tk.END, sample_dictionary["Spike (Oil)"].to_string())
        except KeyError:
            oil_recovery_text.insert(Tk.END, "No oil spike.")
        oil_recovery_text.config(state="disabled")
        oil_recovery_text.grid(row=1, column=2)
        #CS Spike
        cs_recovery_label = Tk.Label(self.recovery_data_frame, text="Curve Recovery", font=self.header_font)
        cs_recovery_label.grid(row=0, column=3, sticky=Tk.W)
        cs_recovery_text = Tk.Text(self.recovery_data_frame, width=40, height=20)
        cs_recovery_text.insert(Tk.END, sample_dictionary["Curve Recovery"].to_string())
        cs_recovery_text.config(state="disabled")
        cs_recovery_text.grid(row=1, column=3)

    def create_header_frames(self, header_dictionary):
        counter = 0
        column_counter = 1
        self.create_header_frame_labels(counter)
        for key, value in header_dictionary.items():
            header_frame_label = Tk.Label(self.headers_data_frame, text=key, font=self.header_font)
            header_frame_label.grid(row=counter, column=column_counter)
            counter += 1
            header_name_entry = Tk.Entry(self.headers_data_frame)
            header_name_entry.insert(Tk.END, value[0])
            header_name_entry.grid(row=counter, column=column_counter)
            counter += 1
            date_entry = Tk.Entry(self.headers_data_frame)
            date_entry.insert(Tk.END, value[1])
            date_entry.grid(row=counter, column=column_counter)
            counter += 1
            time_entry = Tk.Entry(self.headers_data_frame)
            time_entry.insert(Tk.END, value[2])
            time_entry.grid(row=counter, column=column_counter)
            counter += 1
            job_entry = Tk.Entry(self.headers_data_frame)
            job_entry.insert(Tk.END, value[3])
            job_entry.grid(row=counter, column=column_counter)
            counter += 1
            attention_entry = Tk.Entry(self.headers_data_frame)
            attention_entry.insert(Tk.END, value[15])
            attention_entry.grid(row=counter, column=column_counter)
            counter += 1
            address_entry = Tk.Entry(self.headers_data_frame)
            address_entry.insert(Tk.END, value[4])
            address_entry.grid(row=counter, column=column_counter)
            counter += 1
            address_entry_2 = Tk.Entry(self.headers_data_frame)
            address_entry_2.insert(Tk.END, value[5])
            address_entry_2.grid(row=counter, column=column_counter)
            counter += 1
            address_entry_3 = Tk.Entry(self.headers_data_frame)
            address_entry_3.insert(Tk.END, value[6])
            address_entry_3.grid(row=counter, column=column_counter)
            counter += 1
            sample_type_entry_1 = Tk.Entry(self.headers_data_frame)
            sample_type_entry_1.insert(Tk.END, value[7])
            sample_type_entry_1.grid(row=counter, column=column_counter)
            counter += 1
            sample_type_entry_2 = Tk.Entry(self.headers_data_frame)
            sample_type_entry_2.insert(Tk.END, value[8])
            sample_type_entry_2.grid(row=counter, column=column_counter)
            counter += 1
            number_of_samples_entry = Tk.Entry(self.headers_data_frame)
            number_of_samples_entry.insert(Tk.END, value[9])
            number_of_samples_entry.grid(row=counter, column=column_counter)
            counter += 1
            receive_temp = Tk.Entry(self.headers_data_frame)
            receive_temp.insert(Tk.END, value[10])
            receive_temp.grid(row=counter, column=column_counter)
            counter += 1
            additional_info_1 = Tk.Entry(self.headers_data_frame)
            additional_info_1.insert(Tk.END, value[11])
            additional_info_1.grid(row=counter, column=column_counter)
            counter += 1
            additional_info_2 = Tk.Entry(self.headers_data_frame)
            additional_info_2.insert(Tk.END, value[12])
            additional_info_2.grid(row=counter, column=column_counter)
            counter += 1
            additional_info_3 = Tk.Entry(self.headers_data_frame)
            additional_info_3.insert(Tk.END, value[13])
            additional_info_3.grid(row=counter, column=column_counter)
            counter += 1
            payment_info = Tk.Entry(self.headers_data_frame)
            payment_info.insert(Tk.END, value[14])
            payment_info.grid(row=counter, column=column_counter)
            counter += 1
            counter -= 17
            if column_counter >= 5:
                counter += 17
                self.create_header_frame_labels(counter)
                column_counter = 1
            else:
                column_counter += 1
            self.header_information_list.append((key, [header_name_entry,
                                                       date_entry,
                                                       time_entry,
                                                       job_entry,
                                                       address_entry,
                                                       address_entry_2,
                                                       address_entry_3,
                                                       sample_type_entry_1,
                                                       sample_type_entry_2,
                                                       number_of_samples_entry,
                                                       receive_temp,
                                                       additional_info_1,
                                                       additional_info_2,
                                                       additional_info_3,
                                                       payment_info,
                                                       attention_entry,
                                                       attention_entry]))

    def create_header_frame_labels(self, row):
        Tk.Label(self.headers_data_frame, text="Client Name", font=self.header_font).grid(row=row+1, column=0, sticky=Tk.W)
        Tk.Label(self.headers_data_frame, text="Date", font=self.header_font).grid(row=row+2, column=0, sticky=Tk.W)
        Tk.Label(self.headers_data_frame, text="Time", font=self.header_font).grid(row=row+3, column=0, sticky=Tk.W)
        Tk.Label(self.headers_data_frame, text="Job Number", font=self.header_font).grid(row=row+4, column=0, sticky=Tk.W)
        Tk.Label(self.headers_data_frame, text="Attention", font=self.header_font).grid(row=row+5, column=0, sticky=Tk.W)
        Tk.Label(self.headers_data_frame, text="Address 1", font=self.header_font).grid(row=row+6, column=0, sticky=Tk.W)
        Tk.Label(self.headers_data_frame, text="Address 2", font=self.header_font).grid(row=row+7, column=0, sticky=Tk.W)
        Tk.Label(self.headers_data_frame, text="Address 3", font=self.header_font).grid(row=row+8, column=0, sticky=Tk.W)
        Tk.Label(self.headers_data_frame, text="Sample Type 1", font=self.header_font).grid(row=row+9, column=0, sticky=Tk.W)
        Tk.Label(self.headers_data_frame, text="Sample Type 2", font=self.header_font).grid(row=row+10, column=0, sticky=Tk.W)
        Tk.Label(self.headers_data_frame, text="Number of Samples", font=self.header_font).grid(row=row+11, column=0, sticky=Tk.W)
        Tk.Label(self.headers_data_frame, text="Receive Temp.", font=self.header_font).grid(row=row+12, column=0, sticky=Tk.W)
        Tk.Label(self.headers_data_frame, text="Additional Info 1", font=self.header_font).grid(row=row+13, column=0, sticky=Tk.W)
        Tk.Label(self.headers_data_frame, text="Additional Info 2", font=self.header_font).grid(row=row+14, column=0, sticky=Tk.W)
        Tk.Label(self.headers_data_frame, text="Additional Info 3", font=self.header_font).grid(row=row+15, column=0, sticky=Tk.W)
        Tk.Label(self.headers_data_frame, text="Payment Info", font=self.header_font).grid(row=row+16, column=0, sticky=Tk.W)

    def create_samples_checklist_option_frame(self, sample_dictionary, header_dictionary):
        counter = 1
        Tk.Label(self.samples_checklist_frame, text="Samples", font=self.header_font).grid(row=0, column=0)
        Tk.Label(self.samples_checklist_frame, text="Type", font=self.header_font).grid(row=0, column=1)
        Tk.Label(self.samples_checklist_frame, text="Analyte List", font=self.header_font).grid(row=0, column=2)
        Tk.Label(self.samples_checklist_frame, text="single/multi", font=self.header_font).grid(row=0, column=3)
        for key, value in sample_dictionary.items():
            try:
                if isinstance(int(key[0:6]), int):
                    Tk.Label(self.samples_checklist_frame, text=key).grid(row=counter, column=0)
                    self.sample_number_list.append(key)
                    sample_type_string_variable = Tk.StringVar(self.samples_checklist_frame)
                    sample_type_choices = {'Bud', 'Oil', 'Paper', 'Rinse', 'Other'}
                    sample_type_string_variable.set('Bud')
                    sample_type_menu = Tk.OptionMenu(self.samples_checklist_frame,
                                                     sample_type_string_variable,
                                                     *sample_type_choices)
                    sample_type_menu.grid(row=counter, column=1)
                    self.sample_type_option_list.append((key, sample_type_menu, sample_type_string_variable))
                    report_type_string_variable = Tk.StringVar(self.samples_checklist_frame)
                    report_type_choices = {'Canada', 'Canada + USA'}
                    report_type_string_variable.set('Canada')
                    report_type_menu = Tk.OptionMenu(self.samples_checklist_frame,
                                                     report_type_string_variable,
                                                     *report_type_choices)
                    report_type_menu.grid(row=counter, column=2)
                    self.report_type_option_list.append((key, report_type_menu, report_type_string_variable))
                    multi_or_single_variable = Tk.StringVar(self.samples_checklist_frame)
                    multi_or_single_choices = {'Multi', 'Single'}
                    multi_or_single_variable.set('Multi')
                    multi_single_menu = Tk.OptionMenu(self.samples_checklist_frame,
                                                      multi_or_single_variable,
                                                      *multi_or_single_choices)
                    multi_single_menu.grid(row=counter, column=3)
                    self.single_or_multi_list.append((key, multi_single_menu, multi_or_single_variable))
                    sample_name_entry = Tk.Entry(self.samples_checklist_frame)
                    Tk.Label(self.samples_checklist_frame, text="   Sample name: ").grid(row=counter, column=4)
                    sample_name_entry.grid(row=counter, column=5)
                    self.sample_name_list.append((key, sample_name_entry))
                    counter += 1
            except ValueError:
                pass
        dict_list = (sample_dictionary, header_dictionary)
        Tk.Button(self.samples_checklist_frame,
                  text="Generate Batch",
                  command=lambda x=dict_list: self.generate_batch(x), font=self.header_font).grid(row=counter,
                                                                                                 column=0,
                                                                                                 padx=10,
                                                                                                 pady=20,
                                                                                                 sticky=Tk.W,
                                                                                                 columnspan=2)

    def generate_batch(self, dict_list):
        self.updated_sample_type_option_list = [var.get() for item, menu, var in self.sample_type_option_list]
        self.updated_report_type_option_list = [var.get() for item, menu, var in self.report_type_option_list]
        self.updated_single_or_multi_list = [var.get() for item, menu, var in self.single_or_multi_list]
        self.updated_header_information_list = [var.get()
                                                for key, variables in self.header_information_list for var in variables]
        self.updated_sample_name_list = [[item, var.get()] for item, var in self.sample_name_list]
        self.updated_dictionary['sample type'] = self.updated_sample_type_option_list
        self.updated_dictionary['report type'] = self.updated_report_type_option_list
        self.updated_dictionary['single multi'] = self.updated_single_or_multi_list
        self.updated_dictionary['headers'] = self.updated_header_information_list
        self.updated_dictionary['sample names'] = self.updated_sample_name_list
        self.updated_dictionary['sample numbers'] = self.sample_number_list
        self.post_generate_controller(dict_list[0], dict_list[1])

    def post_generate_controller(self, sample_data, header_data):
        counter = 0
        for key, value in header_data.items():
            for item in range(0, 17):
                header_data[key][item] = \
                    self.updated_dictionary['headers'][counter]
                counter += 1
            datestring = "Date: " + header_data[key][1] + " (" + header_data[key][2] + ")"
            sourcestring = "Source: " + header_data[key][7]
            subtype_string = "Type: " + header_data[key][8]
            samplenumberstring = "No. of Samples: " + header_data[key][9]
            arrivaltempstring = "Arrival temp: " + header_data[key][10]
            endinfo3string = header_data[key][14]
            self.lengthlist = [len(datestring),
                               len(sourcestring),
                               len(subtype_string),
                               len(samplenumberstring),
                               len(arrivaltempstring),
                               len(endinfo3string)]
            longest = max(self.lengthlist)
            lengthlist_counter = 0
            for item in self.lengthlist:
                if item != longest:
                    offset = longest - item - 1
                    offset = "x" * offset
                    offset = r'\phantom{' + offset + "}"
                    self.lengthlist[lengthlist_counter] = offset
                    lengthlist_counter += 1
                else:
                    offset = r'\phantom{}'
                    self.lengthlist[lengthlist_counter] = offset
                    lengthlist_counter += 1
            header_data[key].append(self.lengthlist)
        header_counter = 15
        counter = 0
        sample_names_master_list = []
        for key, value in header_data.items():
            jobnumber_to_match = value[3][1:]
            empty_list_for_matching = []
            for item in self.updated_dictionary['sample names']:
                if int(item[0][0:6]) == int(jobnumber_to_match):
                    if len(str(item[0])) == 6:
                        string = r'\textbf{1)} ' + item[1]
                        empty_list_for_matching.append(string)
                    elif len(str(item[0])) == 8:
                        string = r'\textbf{' + item[0][-1] + r')} ' + item[1]
                        empty_list_for_matching.append(string)
                    else:
                        string = r'\textbf{' + item[0][-2:] + r')} ' + item[1]
                        empty_list_for_matching.append(string)
                else:
                    pass
            sample_names_master_list.append(' '.join([i for i in empty_list_for_matching]))
        for key, value in header_data.items():
            header_data[key][header_counter] = sample_names_master_list[counter]
            counter += 1
        batch_report = report(sample_data, header_data, self.updated_dictionary)
        batch_report.post_generate_controller()

