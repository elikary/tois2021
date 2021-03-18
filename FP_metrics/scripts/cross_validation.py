"""
@author: Elisa Mena-Maldonado
"""

import pandas as pd
import common_variables as cmv
from utils import load_data, save_results, remove_trueoptimals
import sys


def concat_allfolds(data_set, metric):
    eval_files = []

    for f in cmv.folds:
        eval_data = load_data(cmv.evaluation_result_path, data_set,
                              data_set + '_fold' + str(f) + '_' + metric + '.csv',
                              ',', head=0)
        print(data_set + ' fold' + str(f))
        eval_files.append(eval_data)

    eval_all = pd.concat(eval_files)

    return eval_all


def compute_mean_allfolds(eval_all, k, algorithms, data_set):
    eval_final = pd.DataFrame(columns=eval_all.columns)

    for a in algorithms:
        eval_all_at_k = eval_all.loc[(eval_all['cutoff'] == k) & (eval_all['algorithm'] == a)]
        all_means = eval_all_at_k.mean()

        all_means = all_means.append(pd.Series([a, data_set], index=['algorithm', 'dataset']))
        eval_final = eval_final.append(all_means, ignore_index=True)

    return eval_final


def main():
    metric = sys.argv[1] #mrr, ndcg, or prec
    for d in cmv.data_sets:
        if d == 'movielens1M_time':
            continue
        results = compute_mean_allfolds(concat_allfolds(d, metric), cmv.k, cmv.algorithms, d)
        result_file_name = cmv.evaluation_result_path + d + '/' + d + '_' + str(cmv.k) + '_' + metric + '.csv'
        save_results(results, result_file_name)


if __name__ == "__main__":
    main()
