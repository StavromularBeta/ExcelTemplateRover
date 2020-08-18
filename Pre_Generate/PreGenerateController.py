import os, sys, inspect
import pandas as pd
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, currentdir)

from Pre_Generate.PreGenerateDataManipulation import PreGenerateDataManipulation as Pdm
from Pre_Generate.PreGenerateHeaderParsing import PreGenerateHeaderParsing as Php

class PreGenerateController:
    """This class controls the methods in the pre_generate folder. It runs the data_manipulation routines, and then runs
     the header_parsing routines."""

    def __init__(self, target_file, batch_type):
        self.target_file = target_file
        self.batch_type = batch_type
        if self.batch_type == 'PestToxinExcel':
            self.data_manipulation = Pdm(target_file)
            self.sample_dictionary = self.data_manipulation.data_manipulation_controller()
            self.header_parsing = Php(self.sample_dictionary)
            self.header_dictionary = self.header_parsing.header_parsing_controller()



