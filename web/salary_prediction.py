import pickle
from functools import reduce
import numpy as np
import pandas as pd


class SalaryModel:
    def __init__(self, path='salary_model.pcl'):
        self.models = None
        with open(path, 'rb') as f:
            self.models = pickle.load(f)
        self.prod = lambda x, y: x * y
        self.cols = ['Q11_Part_1', 'Q11_Part_2', 'Q11_Part_3', 'Q11_Part_4', 'Q11_Part_5', 'Q11_Part_6',
                     'age_18-21', 'age_22-24', 'age_25-29', 'age_30-34', 'age_35-39', 'age_40-44', 'age_45-49',
                     'age_50-54', 'age_55-59', 'age_60+',
                     'country_Australia', 'country_Brazil', 'country_Canada', 'country_China', 'country_France',
                     'country_Germany', 'country_India', 'country_Italy',
                     'country_Japan', 'country_Mexico', 'country_Other', 'country_Russia', 'country_Spain',
                     'country_United Kingdom of Great Britain and Northern Ireland', 'country_United States of America',
                     'role_Business Analyst', 'role_Consultant', 'role_Data Analyst', 'role_Data Engineer',
                     'role_Data Scientist', 'role_Other', 'role_Research Scientist', 'role_Software Engineer',
                     'role_Student',
                     'employer_industry_Academics/Education', 'employer_industry_Accounting/Finance',
                     'employer_industry_Computers/Technology', 'employer_industry_Government/Public Service',
                     'employer_industry_Insurance/Risk Assessment',
                     'employer_industry_Medical/Pharmaceutical',
                     'employer_industry_Online Service/Internet-based Services', 'employer_industry_Other',
                     'years_experience_0-1', 'years_experience_1-2', 'years_experience_10-15', 'years_experience_15+',
                     'years_experience_2-3', 'years_experience_3-4', 'years_experience_4-5', 'years_experience_5-10']
        self.n_cols = len(self.cols)

        self.q11_map = {"None of these activities are an important part of my role at work": "Q11_Part_6",
                        "Do research that advances the state of the art of machine learning": "Q11_Part_5",
                        "Build prototypes to explore applying machine learning to new areas": "Q11_Part_4",
                        "Build and/or run the data infrastructure that my business uses for storing, analyzing, and operationalizing data": "Q11_Part_3",
                        "Build and/or run a machine learning service that operationally improves my product or workflows": "Q11_Part_2",
                        "Analyze and understand data to influence product or business decisions": "Q11_Part_1"}

    def form_input_to_sample(self, age, country, industry, role, experience, q11):
        sample = pd.DataFrame(np.zeros((1, self.n_cols)), columns=self.cols)
        sample['age_' + age] = 1
        sample['country_' + country] = 1
        sample['employer_industry_' + industry] = 1
        sample['role_' + role] = 1
        sample['years_experience_' + experience] = 1

        for value in q11:
            sample[self.q11_map[value]] = 1
        return sample

    def predict(self, sample):
        """
        Given list of binary classifiers and a sample, predict the most probable category index and the distribution
        """
        binary_probabilities = [mod.predict_proba(sample) for mod in self.models]
        neg_probs = [p[0][0] for p in binary_probabilities]
        pos_probs = [p[0][1] for p in binary_probabilities]
        bin_probabilities = []
        for i in range(len(self.models)):
            bin_prob = [p for p in pos_probs[:i]] + [neg_probs[i]]
            reduced = reduce(self.prod, bin_prob)
            bin_probabilities.append(reduced)
        bin_probabilities.append(reduce(self.prod, pos_probs))
        return np.argmax(bin_probabilities), bin_probabilities
