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

from Pre_Generate.PreGenerateController import PreGenerateController as PreGenControl


class HomepageWindow(Tk.Frame):
    def __init__(self, parent, **kwargs):
        Tk.Frame.__init__(self, parent, **kwargs)
        self.parent = parent
        self.select_button_font = tkFont.Font(size=18, weight='bold')

    def homepage(self):
        select_button_pest_toxin_excel = Tk.Button(self, text="Pesticides/Toxins Batch",
                                                   command=lambda: self.browse_button("PestToxinExcel"),
                                                   font=self.select_button_font)
        select_button_pest_toxin_excel.grid(row=0, column=1, sticky=Tk.W, padx=10, pady=10)

    def start_data_processing(self, file_name, instrument_type):
        pre_gen_control = PreGenControl(file_name, instrument_type)
        sample_dictionary = pre_gen_control.sample_dictionary
        header_dictionary = pre_gen_control.header_dictionary
        self.parent.display_batchpage(sample_dictionary, header_dictionary)

    def browse_button(self, instrument_type):
        filename = filedialog.askopenfilename(
            initialdir=r"T:\ANALYST WORK FILES\Peter\ExcelTemplateRover\ExcelTemplates")
        self.start_data_processing(filename, instrument_type)




