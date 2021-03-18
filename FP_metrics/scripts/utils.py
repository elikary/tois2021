import pandas as pd
import common_variables as cmv


def load_data(path, data_set_name, file_name, separator, cols=None, head=None):
    print('------loading ' + file_name + ' ------ ' + '\n')

    try:
        if cols is None:
            if head is not None:
                data_df = pd.read_csv(path + data_set_name + '/' + file_name, sep=separator, encoding='latin-1',
                                      header=head)
            else:
                print('error! missing header parameter')
        else:
            data_df = pd.read_csv(path + data_set_name + '/' + file_name, sep=separator, encoding='latin-1', names=cols)
        print('done!')
        return data_df

    except FileNotFoundError as e:
        print(e)


def remove_trueoptimals():
    cmv.algorithms.remove("optimaltrueprecision")
    cmv.algorithms.remove("optimaltrueantiprecision")
    cmv.algorithms.remove("optimaltrueprecisionrestricted")
    cmv.algorithms.remove("optimaltrueantiprecisionrestricted")


def save_results(data, result_file_name):
    print(result_file_name)
    print(data.head(5))
    data.to_csv(result_file_name, header=True, index=None, sep=',', mode='w+')


"""
relevance change for nDCG and nDCL metrics  maybe change this to evaluation?
Please refer to the toy_examples.xlsx file to see how to compute them with binary relevance
"""


def change_relevance(dataset, recommendation, testdata):
    if dataset == 'cm100k_observed' or 'cm100k_true':
        testdata['ideal_rank_p'] = testdata['rating'].replace([4, 3, 2, 1], [2, 1, 0, 0])
        testdata['ideal_rank_n'] = testdata['rating'].replace([4, 3, 2, 1], [0, 0, -1, -2])
        recommendation['rating_changed'] = recommendation['ratings'].replace([4, 3, 2, 1], [2, 1, -1, -2])
    elif dataset == 'movielens1M' or 'movielens1M_time' or 'yahoo_observed' or 'yahoo_true':
        testdata['ideal_rank_p'] = testdata['rating'].replace([5, 4, 3, 2, 1], [2, 1, 0, 0, 0])
        testdata['ideal_rank_n'] = testdata['rating'].replace([5, 4, 3, 2, 1], [0, 0, -1, -2, -3])
        recommendation['rating_changed'] = recommendation['ratings'].replace([5, 4, 3, 2, 1], [2, 1, -1, -2, -3])

    return recommendation, testdata
