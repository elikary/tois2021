from __future__ import division
import numpy as np
from common_variables import user_column, item_colum, rating_column, threshold, k
from metrics import precision, antiprecision, recall, fallout, ndcg_k, ndcl_k, mean_reciprocal_rank, anti_mean_reciprocal_rank
from utils import change_relevance
from statistics import mean


def count_positive_hits(data, column, threshold):
    ratings = get_ratings_set(data)
    return data[data[column].isin([i for i in ratings if i > threshold])][column].count()


def count_negative_hits(data, column, threshold):
    ratings = get_ratings_set(data)
    return data[data[column].isin([i for i in ratings if i <= threshold])][column].count()


def get_ratings_set(data):
    return data[rating_column].unique()


def get_test_ratings_rec(recommendation, testdata):
    recommendation = set_new_index(recommendation, user_column, item_colum)
    testdata = set_new_index(testdata, user_column, item_colum)
    recommendation[rating_column] = testdata[rating_column]
    return recommendation


def get_topk(data):
    return data.groupby(user_column).head(k).reset_index(drop=True)


def set_new_index(df, col1, col2):
    df.set_index(df[col1].map(str) + '_' + df[col2].map(str), inplace=True)
    return df


def get_number_users(data):
    return data[user_column].unique()


def find_user_data(data, u):
    return data.loc[data[user_column] == u]


def metrics_one_user(rec_user, user_test, iscondensed):
    tp_user = count_positive_hits(rec_user, rating_column, threshold)
    fp_user = count_negative_hits(rec_user, rating_column, threshold)

    relevants_user = count_positive_hits(user_test, rating_column, threshold)
    nonrelevants_user = count_negative_hits(user_test, rating_column, threshold)

    if iscondensed == False:

        return recall(tp_user, relevants_user), precision(tp_user, k), \
               fallout(fp_user, nonrelevants_user), antiprecision(fp_user, k)

    else:
        return recall(tp_user, relevants_user), precision(tp_user, tp_user + fp_user), \
               fallout(fp_user, nonrelevants_user), antiprecision(fp_user, tp_user + fp_user)


def metrics_all_users(recommendation, testdata, iscondensed):
    recall_list = []
    fallout_list = []
    precision_list = []
    antiprecision_list = []

    users_test = get_number_users(testdata)

    for u in users_test:
        recommendation_user = find_user_data(recommendation, u)
        testdata_user = find_user_data(testdata, u)

        recall, precision, fallout, antiprecision = metrics_one_user(recommendation_user, testdata_user, iscondensed)

        recall_list.append(recall)
        fallout_list.append(fallout)
        precision_list.append(precision)
        antiprecision_list.append(antiprecision)

    recall = np.mean(recall_list)
    fallout = np.mean(fallout_list)
    precision = np.mean(precision_list)
    antiprecision = np.mean(antiprecision_list)

    return [recall, precision, fallout, antiprecision]


def full_metrics(recommendation, testdata):
    recommendation = get_test_ratings_rec(recommendation, testdata)  # match ratings test with rec totaldatset
    return metrics_all_users(recommendation, testdata, False)


def condensed_metrics(recommendation, testdata):
    recommendation = get_test_ratings_rec(recommendation, testdata)  # match ratings test with rec totaldatset
    condensed_recommendation = recommendation[recommendation.rating.notnull()]
    rec_at_k = get_topk(condensed_recommendation)
    return metrics_all_users(rec_at_k, testdata, True)


def ndcg_ndcl(dataset, recommendation, testdata, k):
    usersin_test = testdata['user_id'].unique()

    total_ndcg = []
    total_ndcl = []

    recommendation['useritem'] = (recommendation['user_id'].map(str) + '_' + recommendation['item_id'].map(str))
    recommendation.set_index('useritem', inplace=True)

    testdata['useritem'] = (testdata['user_id'].map(str) + '_' + testdata['item_id'].map(str))
    testdata.set_index('useritem', inplace=True)

    recommendation['ratings'] = testdata['rating']
    recommendation['ratings'].fillna(0, inplace=True)

    recommendation, testdata = change_relevance(dataset, recommendation, testdata)

    for u in usersin_test:

        userInfo = recommendation.loc[recommendation['user_id'] == u]
        userRecArray = userInfo['rating_changed'].values

        if userInfo.size:

            userTest = testdata.loc[testdata['user_id'] == u]
            userTestArray_p = userTest['ideal_rank_p'].values
            userTestArray_n = userTest['ideal_rank_n'].values

            total_ndcg.append(ndcg_k(userRecArray, userTestArray_p, k))
            total_ndcl.append(ndcl_k(userRecArray, userTestArray_n, k))
        else:
            print(u)

    return [mean(total_ndcg), mean(total_ndcl)]


def compute_mrrs(recommendation, testdata):
    mrr_list = []
    recommendation = get_test_ratings_rec(recommendation, testdata)
    recommendation[rating_column].fillna(-1, inplace=True)  # shouldn't do this for condensed lists
    recommendation[rating_column] = recommendation.apply(
        lambda row: 0 if row[rating_column] == 0 else 1 if row[rating_column] == 2 or row[rating_column] == 1 \
            else -1, axis=1
    )  # check this depends on test data ratings 012, wont work for 543

    users_test = get_number_users(testdata)

    for u in users_test:
        recommendation_user = find_user_data(recommendation, u)
        if recommendation_user[rating_column].values.size:  # empty means users from test not in rec?
            mrr_list.append(recommendation_user[rating_column].values)

    mrr = mean_reciprocal_rank(mrr_list)
    anti_mrr = anti_mean_reciprocal_rank(mrr_list)

    return [mrr, anti_mrr]