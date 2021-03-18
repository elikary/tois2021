"""
@author: Elisa Mena-Maldonado
"""

import common_variables as cmv


def remove_optimals(df):
    return df.loc[~df['algorithm'].isin(cmv.optimals)]


def retrieve_nicks(series):
    values = []
    for a in series:
        if a in cmv.nick_names:
            values.append(cmv.nick_names[a])
    return values


