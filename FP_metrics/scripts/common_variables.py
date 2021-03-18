"""
@author: Elisa Mena-Maldonado
"""

# for general evaluation

user_column = 'user_id'
item_colum = 'item_id'
rating_column = 'rating'
threshold = 0

# for general evaluation and main files

folds = range(1, 6)
k = 10
test_file_name = 'test012'
data_path = '../../librec-2.0.0/data/'
recommendation_path = '../../librec-2.0.0/result/'
evaluation_result_path = '../evaluation/'

recommendation_cols = ['user_id', 'item_id', 'score']

cols = ['user_id', 'item_id', 'rating']

result_cols = ['algorithm', 'dataset', 'recall', 'precision', 'fallout', 'antiprecision', 'cutoff']

data_sets = [
                'cm100k_true',
                'cm100k_observed',
                'cm100k_true_synthetic',
                'cm100k_observed_synthetic',
                'yahoo_true', 'yahoo_observed',
                'movielens1M',
                'movielens1M_time'
            ]

algorithms = [
                'mostpopular', 'itemknn',
                'listrankmf',  'randomguess',
                'slim', 'svdpp',
                'ranksgd','userknn',
                'smootheditemaverage',
                'optimalobservedprecision', 'optimalobservedantiprecision',
                'optimaltrueprecision', 'optimaltrueantiprecision',
                'optimaltrueprecisionrestricted', 'optimaltrueantiprecisionrestricted',
                'pnmf', 'eals', 'gbpr', 'plsa', 'bpoissmf', 'wrmf', 'wbpr'
              ]


# for condensed lists only

result_cols_condensed = ['algorithm', 'dataset', 'recall', 'precision', 'fallout', 'antiprecision', 'recall_c',
                         'precision_c', 'fallout_c', 'antiprecision_c', 'cutoff']


# for evaluation with ndcg and ndcl only

cols_time = ['user_id', 'item_id', 'rating', 'timestamp']
result_cols_ndcg = ['algorithm', 'dataset', 'ndcg', 'ndcl', 'cutoff']
test_file_name_ndcg = 'test543' #full rating scale

# for evaluation with mrr and antimrr only

result_cols_mrr = ['algorithm', 'dataset', 'mrr', 'antimrr', 'cutoff']

