# -*- coding: utf-8 -*-
"""
General analysis functions.

Try to write all methods such that they take a dataframe as input
and return a dataframe or list of dataframes.
"""

import datetime as dt


def daily(df, agg, starttime=dt.time.min, endtime=dt.time.max):
    """

    Parameters
    ----------
    df : pandas.DataFrame
        With pandas.DatetimeIndex and one or more columns
    agg : str
        'min', 'max', or another aggregation function
    starttime, endtime : datetime.time objects
        For each day, only consider the time between starttime and endtime
        If None, use begin of day/end of day respectively

    Returns
    -------
    df_day : pandas.DataFrame with daily datetimeindex and aggregated result
    """
    if df.empty:
        return df

    df = df[(df.index.time >= starttime) & (df.index.time < endtime)]
    df = df.resample('D', how=agg)
    return df


def daily_min(df, starttime=dt.time.min, endtime=dt.time.max):
    return daily(df=df, agg='min', starttime=starttime, endtime=endtime)


def daily_max(df, starttime=dt.time.min, endtime=dt.time.max):
    return daily(df=df, agg='max', starttime=starttime, endtime=endtime)
