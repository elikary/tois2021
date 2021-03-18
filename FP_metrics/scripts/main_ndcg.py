"""
@author: elisa mena-maldonado

We used test sets with ranking values of [1,2,3,4,5] for movielens and yahoo, and [1,2,3,4] for cm100k
"""

import pandas as pd
from evaluation import ndcg_ndcl
import common_variables as cmv
from utils import load_data, save_results, remove_trueoptimals


def compute_evaluation(data_set_name, num_fold):
    print(data_set_name)
    result_list = []

    test = load_data(cmv.data_path, data_set_name + '/fold' + str(num_fold), cmv.test_file_name_ndcg + '.txt', '\t',
                     cols=cmv.cols)
    for a in cmv.algorithms:
        recommendation = load_data(cmv.recommendation_path, data_set_name + '/fold' + str(num_fold), a, ',',
                                   cols=cmv.recommendation_cols)
        print(a)

        rec_per_k = recommendation.groupby('user_id').head(cmv.k).reset_index(drop=True)
        result_list.append([a, data_set_name] + ndcg_ndcl(data_set_name, rec_per_k, test, cmv.k) + [cmv.k])
        print(cmv.k)

    results = pd.DataFrame(result_list)
    results.columns = cmv.result_cols_ndcg
    return results


def main():
    for d in cmv.data_sets:
        if d == 'movielens1M_time':
            cmv.folds = [1]
            remove_trueoptimals()
        for f in cmv.folds:
            results = compute_evaluation(data_set_name=d, num_fold=f)
            result_file_name = cmv.evaluation_result_path + d + '/' + d + '_fold' + str(
                f) + '_' + 'ndcg' + '.csv'
            save_results(results, result_file_name)


if __name__ == "__main__":
    main()
