import pandas as pd
import numpy as np


def map_params(age, country, industry, role, experience, q11):
    # global cols
    col_num = 5  # len(cols)
    sample = pd.DataFrame(np.zeros((1, col_num)))
    # sample.columns=features.columns
    sample['age_' + age] = 1
    sample['country_' + country] = 1
    sample['employer_industry_' + industry] = 1
    sample['role_' + role] = 1
    sample['years_experience_' + experience] = 1

    # for value in q11:
    #     sample[q11_map[value]] = 1
    return sample
