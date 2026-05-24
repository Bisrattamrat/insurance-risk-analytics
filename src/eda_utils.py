import pandas as pd

def missing_values(df):
    """
    Returns missing values count.
    """
    return df.isnull().sum()

def descriptive_stats(df):
    """
    Returns descriptive statistics.
    """
    return df.describe()