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

        self.languages = ["Python", "R", "SQL", "Bash", "Java", "Javascript",
                         "Visual_Basic", "C", "Matlab", "Scala", "Julia", "Go",
                         "NET", "PHP", "Ruby", "STATA", "None", "Other"]
        self.lang_map = {l: 'Q16_' + l for l in self.languages}
        
        self.frameworks = ["Scikit_Learn", "TensorFlow", "Keras", "PyTorch", "Spark", "H20",
              "Fastai", "Mxnet", "Caret", "Xgboost", "mlr", "Prophet", "randomForest",
              "lightgbm", "catboost", "CNTK", "Caffe", "None", "Other"]
        
        self.framework_map = {f: 'Q19_' + f for f in self.frameworks}
        
        self.courses = ["Udacity", "Coursera", "edX", "DataCamp", "DataQuest", "Kaggle_learn",
           "Fast_AI", "developers_google", "Udemy", "TheSchool_AI", "Online_University_courses",
           "None", "Other"]
        
        self.course_map = {c: 'Q36_' + c for c in self.courses}
        
        self.sources = ['Twitter', 'Hacker_news', 'R_machine_learning', 'Kaggle_forum',
           'Fastai', 'SirajRaval', 'DataTau', 'Linear_Digression_podcast',
           'Cloud_AI_adventures', 'FiveThirtyEight', 'ArXiv', 'Journal_publication',
           'FastMLBlog', 'KDnuggets', 'OReilly_data', 'Partially_derivative_podcast',
             'Data_Skeptic_podcast', 'Medium_Blog', 'Torwards_data_science',
           'Analytics_Vidhya', "None", 'Other']
        
        self.source_map = {s: 'Q38_' + s for s in self.sources}

    def form_input_to_sample(self, languages=[], frameworks=[], courses=[], sources=[]):
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
    
    def summarize_distribution(self, probs):
        """ 1 - AUC of empirical cumulative distribution """
        return 1 - (np.cumsum(probs).sum() / len(probs))

    def get_recommendations(self, base_sample, top_n=None):
        base_pred, base_distr = self.predict(base_sample)
        base_sum = self.summarize_distribution(base_distr)

        pairs = []

        for c in self.languages:
            if c in ["None", "Other", "Bash", "Visual_Basic", "STATA"]:
                continue
            if base_sample[self.lang_map[c]].values == 0:
                candidate = base_sample.copy()
                candidate[self.lang_map[c]] = 1
                _, dist = self.predict(candidate)
                dist_sum = self.summarize_distribution(dist)
                relative_change = (dist_sum - base_sum) / base_sum
                pairs.append((c, relative_change))
        lang_sorted = sorted(pairs, key=lambda x:x[1], reverse=True)

        pairs = []
        for c in self.frameworks:
            if c in ["None", "Other", "Mxnet"]:
                continue
            if base_sample[self.framework_map[c]].values == 0:
                candidate = base_sample.copy()
                candidate[self.framework_map[c]] = 1
                _, dist = self.predict(candidate)
                dist_sum = self.summarize_distribution(dist)
                relative_change = (dist_sum - base_sum) / base_sum
                pairs.append((c, relative_change))     
        fw_sorted = sorted(pairs, key=lambda x:x[1], reverse=True)

        pairs = []
        for c in self.courses:
            if c in ["None", "Other"]:  # We shouldn't even evaluate those options
                continue
            if base_sample[self.course_map[c]].values == 0:
                candidate = base_sample.copy()
                candidate[self.course_map[c]] = 1
                _, dist = self.predict(candidate)
                dist_sum = self.summarize_distribution(dist)
                relative_change = (dist_sum - base_sum) / base_sum
                pairs.append((c, relative_change))
        course_sorted = sorted(pairs, key=lambda x:x[1], reverse=True)

        pairs = []

        for c in self.sources:
            if c in ["None", "Other", "FiveThirtyEight"]:
                continue
            if base_sample[self.source_map[c]].values == 0:
                candidate = base_sample.copy()
                candidate[self.source_map[c]] = 1
                _, dist = self.predict(candidate)
                dist_sum = self.summarize_distribution(dist)
                relative_change = (dist_sum - base_sum) / base_sum
                pairs.append((c, relative_change))  

        sources_sorted = sorted(pairs, key=lambda x:x[1], reverse=True)
        return lang_sorted, fw_sorted, course_sorted, sources_sorted