import pandas as pd


class OrganizeMethods:

    def __init__(self, updates, sample_data):
        self.updates = updates
        self.sample_data = sample_data
        self.single_reports_dictionary = {}
        self.multiple_reports_dictionary = {}

    def split_samples_into_single_or_multi(self):
        counter = 0
        for item in self.updates['single multi']:
            if item == 'Single':
                self.single_reports_dictionary[self.updates["sample numbers"][counter]] = \
                    [self.updates['sample type'][counter],
                     self.updates['report type'][counter]]
            else:
                self.multiple_reports_dictionary[self.updates["sample numbers"][counter]] = \
                    [self.updates['sample type'][counter],
                     self.updates['report type'][counter]]
            counter += 1
        return self.single_reports_dictionary, self.multiple_reports_dictionary
