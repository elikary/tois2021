from __future__ import division
import numpy as np


def precision(tp, denominator):
    return tp / denominator


def antiprecision(fp, denominator):
    return fp / denominator


def recall(tp, relevants):
    if relevants == 0:
        return 0
    return tp / relevants


def fallout(fp, nonrelevants):
    if nonrelevants == 0:
        return 0
    return fp / nonrelevants

"""
based on https://gist.github.com/bwhite/3726239/b117d9657fb96d721b1f90616af41f812f5baf22
"""

def linear_dcg_at_k(r, k):
    # r = [(2**x)-1 for x in r] #exponential version
    r = np.asfarray(r)[:k]
    if r.size:
        return np.sum(np.maximum(r, 0) / np.log2(np.arange(2, r.size + 2)))


def linear_dcl_at_k(r, k):
    # r = [(2**x)-1 for x in r] #exponential version
    r = np.asfarray(r)[:k]
    if r.size:
        return np.sum(-np.minimum(r, 0) / np.log2(np.arange(2, r.size + 2)))
        # negative sign because we are working with negative numbers in the list
        # minimum between r and 0.
        # for dcl, the lower the better


def ndcg_k(predicted_scores, user_scores, k):
    idcg = linear_dcg_at_k(sorted(user_scores, reverse=True), k)
    return (linear_dcg_at_k(predicted_scores, k) / idcg) if idcg > 0.0 else 0.0


def ndcl_k(predicted_scores, user_scores, k):
    idcl = linear_dcl_at_k(sorted(user_scores, reverse=False),k)  # here it is important the ascendent list because the lower the idcl the better (lower ratings on top)
    return (linear_dcl_at_k(predicted_scores, k) / idcl) if idcl > 0.0 else 0.0

"""
based on https://gist.github.com/bwhite/3726239
"""
def mean_reciprocal_rank(rs):
    rs = (np.where(np.array(r) == 1)[0] for r in rs)
    return np.mean([1. / (r[0] + 1) if r.size else 0. for r in rs])


def anti_mean_reciprocal_rank(rs):
    rs = (np.where(np.array(r) == 0)[0] for r in rs)
    return np.mean([1. / (r[0] + 1) if r.size else 0. for r in rs])

