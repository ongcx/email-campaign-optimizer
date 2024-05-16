# src/experiment.py
import numpy as np
from scipy.stats import ttest_ind

class ABTest:
    def __init__(self, data):
        self.data = data
        self.control_group = None
        self.treatment_group = None

    def assign_groups(self, group_size):
        subscribers = self.data['subscriber_id'].sample(frac=1).reset_index(drop=True)
        self.control_group = subscribers[:group_size]
        self.treatment_group = subscribers[group_size:]

    def analyze_results(self):
        control_open_rate = self.data.loc[self.data['subscriber_id'].isin(self.control_group), 'opened'].mean()
        treatment_open_rate = self.data.loc[self.data['subscriber_id'].isin(self.treatment_group), 'opened'].mean()

        control_conv_rate = self.data.loc[self.data['subscriber_id'].isin(self.control_group) & (self.data['converted'] == 1), 'converted'].mean()
        treatment_conv_rate = self.data.loc[self.data['subscriber_id'].isin(self.treatment_group) & (self.data['converted'] == 1), 'converted'].mean()

        open_rate_pvalue = ttest_ind(
            self.data.loc[self.data['subscriber_id'].isin(self.control_group), 'opened'],
            self.data.loc[self.data['subscriber_id'].isin(self.treatment_group), 'opened']
        )[1]

        conv_rate_pvalue = ttest_ind(
            self.data.loc[self.data['subscriber_id'].isin(self.control_group) & (self.data['converted'] == 1), 'converted'],
            self.data.loc[self.data['subscriber_id'].isin(self.treatment_group) & (self.data['converted'] == 1), 'converted']
        )[1]

        return {
            'control_open_rate': control_open_rate,
            'treatment_open_rate': treatment_open_rate,
            'control_conv_rate': control_conv_rate,
            'treatment_conv_rate': treatment_conv_rate,
            'open_rate_pvalue': open_rate_pvalue,
            'conv_rate_pvalue': conv_rate_pvalue
        }
