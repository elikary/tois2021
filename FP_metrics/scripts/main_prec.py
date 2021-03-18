"""
@author: Elisa Mena-Maldonado
"""

import pandas as pd
from evaluation import full_metrics, condensed_metrics
import common_variables as cmv
from utils import load_data, save_results


def compute_evaluation(data_set_name, num_fold, condensed):
    print(data_set_name)

    result_list = []

    test = load_data(cmv.data_path, data_set_name + '/fold' + str(num_fold), cmv.test_file_name + '.txt', '\t',
                     cols=cmv.cols)

    for a in cmv.algorithms:
        recommendation = load_data(cmv.recommendation_path, data_set_name + '/fold' + str(num_fold), a, ',',
                                   cols=cmv.recommendation_cols)
        recommendation_at_k = recommendation.groupby(cmv.user_column).head(cmv.k).reset_index(drop=True)
        if condensed:
            result_list.append([a, data_set_name] + full_metrics(recommendation_at_k, test) + \
                               condensed_metrics(recommendation, test) + [cmv.k])
        else:
            result_list.append([a, data_set_name] + full_metrics(recommendation_at_k, test) + [cmv.k])

        print('Finished processing metrics@' + str(cmv.k) + '\n')

    results = pd.DataFrame(result_list)

    if condensed:
        results.columns = cmv.result_cols_condensed
    else:
        results.columns = cmv.result_cols

    return results


def main():
    for d in cmv.data_sets:
        if d == 'movielens1M_time':
            cmv.folds = [1]
        for f in cmv.folds:
            condensed = False if d != 'movielens1M' else True

            results = compute_evaluation(data_set_name=d, num_fold=f, condesed=condensed)
            result_file_name = cmv.evaluation_result_path + d + '/' + d + '_fold' + str(
                f) + '_' + 'prec' + '.csv'
            save_results(results, result_file_name)


if __name__ == "__main__":
    main()
