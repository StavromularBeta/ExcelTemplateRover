import pandas as pd
import datetime
import re
import sys


class PreGenerateHeaderParsing:

    def __init__(self, sample_dictionary):
        self.sample_dictionary = sample_dictionary
        self.current_month_directory = ''
        self.last_month_directory = ''
        self.header_contents_dictionary = {}

#       This is for development - allows me to see the full DataFrame when i print to the console, rather than a
#       truncated version. This is useful for debugging purposes and ensuring that methods are working as intended.
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', -1)

#       This is a list of the abbreviations given to the directories where the header files are stored for a given month
        self.date_dict = {1: 'JAN',
                          2: 'FEB',
                          3: 'MAR',
                          4: 'APR',
                          5: 'MAY',
                          6: 'JUN',
                          7: 'JUL',
                          8: 'AUG',
                          9: 'SEP',
                          10: 'OCT',
                          11: 'NOV',
                          12: 'DEC'}

    def header_parsing_controller(self):
        self.get_current_and_last_month_directory()
        self.get_header_information_from_unique_jobs_list()
        return self.header_contents_dictionary

    def get_current_and_last_month_directory(self):
        self.current_month_directory = 'U:\\TXT-' + self.date_dict[datetime.datetime.now().month] + "\\"
        self.last_month_directory = 'U:\\TXT-' + self.date_dict[int(datetime.datetime.now().month)-1] + "\\"

    def get_header_information_from_unique_jobs_list(self):
        for item in self.sample_dictionary["Job List"]:
            current_month_file_path = self.current_month_directory + 'W' + item + '.TXT'
            last_month_file_path = self.last_month_directory + 'W' + item + '.TXT'
            header_contents = ''
            print("HEADER INFORMATION")
            print("attempting to find header for " + item)
            try:
                header = open(current_month_file_path, 'r')
                header_contents = header.read()
                print(item + " header found.")
            except FileNotFoundError:
                try:
                    header = open(last_month_file_path, 'r')
                    header_contents = header.read()
                    print(item + " header found.")
                except FileNotFoundError:
                    print("ERROR: header not found. Dummy header made up in place.")
                    header_contents = "Header not found"
#                   sys.exit()
#                   uncommenting will allow user to exit upon a missing header, rather than adding a dummy header.
            self.header_contents_dictionary[item] = self.header_parser_V2(header_contents)

    def header_parser_V2(self, header_contents):
        if header_contents == "Header not found":
            parsed_header_contents = ['no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no',
                                      'no', 'no', 'no', 'no']
            return parsed_header_contents
        name1 = header_contents[0:55].strip()
        date = header_contents[55:66].strip()
        time = header_contents[66:84].strip()
        w_number = header_contents[84:98].strip()
        remainder_of_header = header_contents[98:].strip().split("   ")
        remainder_of_header = [word for word in remainder_of_header if len(word) >= 1]
        if remainder_of_header[0][0] == "*":
            attn = remainder_of_header[0].strip()
            sample_type = re.sub('[\n]', '', remainder_of_header[1]).strip()
            address_1 = remainder_of_header[2].strip()
            sample_subtype = re.sub('[\n]', '', remainder_of_header[3]).strip()
            address_2 = remainder_of_header[4].strip()
            number_of_samples = re.sub('[\n]', '', remainder_of_header[5]).strip()
            postal_code = re.sub('[\n]', '', remainder_of_header[6]).strip()
        else:
            attn = "*"
            address_1 = remainder_of_header[0].strip()
            sample_type = re.sub('[\n]', '', remainder_of_header[1]).strip()
            address_2 = remainder_of_header[2].strip()
            sample_subtype = re.sub('[\n]', '', remainder_of_header[3]).strip()
            postal_code = re.sub('[\n]', '', remainder_of_header[4]).strip()
            number_of_samples = re.sub('[\n]', '', remainder_of_header[5]).strip()
        email = "can't find email"
        payment_information = "can't find payment information"
        arrival_temp = "can't find arrival temperature"
        sampler = "can't find sampler information"
        phone_number = "can't find phone number"
        for item in remainder_of_header:
            if "TEL:" in item:
                phone_number = re.sub('[\n]', '', item).strip()
            elif "@" in item:
                email = re.sub('[\n]', '', item).strip()
            elif "group" in item:
                email = re.sub('[\n]', '', item).strip()
            elif "Arrival temp" in item:
                arrival_temp = re.sub('[\n]', '', item).strip()[16:]
            elif "Pd" in item:
                payment_information = re.sub('[\n]', '', item).strip()
        parsed_header_contents = [name1,
                                  date,
                                  time,
                                  w_number,
                                  address_1,
                                  address_2,
                                  postal_code,
                                  sample_type,
                                  sample_subtype,
                                  number_of_samples,
                                  arrival_temp,
                                  phone_number,
                                  email,
                                  'phantom{a}',
                                  payment_information,
                                  attn,
                                  'phantom{a}']
        return parsed_header_contents
