import pickle
from functools import reduce
import numpy as np
import pandas as pd


class RecommenderModel:
    def __init__(self, path='recom_model.pcl'):
        self.models = None
        with open(path, 'rb') as f:
            self.models = pickle.load(f)
        self.prod = lambda x, y: x * y
        self.cols = ['Q16_Python', 'Q16_R', 'Q16_SQL', 'Q16_Bash', 'Q16_Java',
                       'Q16_Javascript', 'Q16_Visual_Basic', 'Q16_C', 'Q16_Matlab',
                       'Q16_Scala', 'Q16_Julia', 'Q16_Go', 'Q16_NET', 'Q16_PHP', 'Q16_Ruby',
                       'Q16_STATA', 'Q16_None', 'Q16_Other', 'Q19_Scikit_Learn',
                       'Q19_TensorFlow', 'Q19_Keras', 'Q19_PyTorch', 'Q19_Spark', 'Q19_H20',
                       'Q19_Fastai', 'Q19_Mxnet', 'Q19_Caret', 'Q19_Xgboost', 'Q19_mlr',
                       'Q19_Prophet', 'Q19_randomForest', 'Q19_lightgbm', 'Q19_catboost',
                       'Q19_CNTK', 'Q19_Caffe', 'Q19_None', 'Q19_Other', 'Q38_Twitter',
                       'Q38_Hacker_news', 'Q38_R_machine_learning', 'Q38_Kaggle_forum',
                       'Q38_Fastai', 'Q38_SirajRaval', 'Q38_DataTau',
                       'Q38_Linear_Digression_podcast', 'Q38_Cloud_AI_adventures',
                       'Q38_FiveThirtyEight', 'Q38_ArXiv', 'Q38_Journal_publication',
                       'Q38_FastMLBlog', 'Q38_KDnuggets', 'Q38_OReilly_data',
                       'Q38_Partially_derivative_podcast', 'Q38_Data_Skeptic_podcast',
                       'Q38_Medium_Blog', 'Q38_Torwards_data_science', 'Q38_Analytics_Vidhya',
                       'Q38_Other', 'Q38_None', 'Q36_Udacity', 'Q36_Coursera', 'Q36_edX',
                       'Q36_DataCamp', 'Q36_DataQuest', 'Q36_Kaggle_learn', 'Q36_Fast_AI',
                       'Q36_developers_google', 'Q36_Udemy', 'Q36_TheSchool_AI',
                       'Q36_Online_University_courses', 'Q36_None', 'Q36_Other']
        self.n_cols = len(self.cols)

#         self.q11_map = {"None of these activities are an important part of my role at work": "Q11_Part_6",
#                         "Do research that advances the state of the art of machine learning": "Q11_Part_5",
#                         "Build prototypes to explore applying machine learning to new areas": "Q11_Part_4",
#                         "Build and/or run the data infrastructure that my business uses for storing, analyzing, and operationalizing data": "Q11_Part_3",
#                         "Build and/or run a machine learning service that operationally improves my product or workflows": "Q11_Part_2",
#                         "Analyze and understand data to influence product or business decisions": "Q11_Part_1"}

    def form_input_to_sample(self, languages, frameworks, courses, sources):
        sample = pd.DataFrame(np.zeros((1, self.n_cols)), columns=self.cols)

        for v in languages:
            sample['Q16_' + v] = 1
        for v in frameworks:
            sample['Q19_' + v] = 1
        for v in courses:
            sample['Q36_' + v] = 1
        for v in sources:
            sample['Q38_' + v] = 1
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
