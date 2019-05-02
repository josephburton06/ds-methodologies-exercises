import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np

def encode_gender(df):
    encoder = LabelEncoder()
    encoder.fit(df.gender)
    df = df.assign(gender_encoded = encoder.transform(df.gender))
    return df



def get_outliers(df, k):
    q1, q3 = df.quantile([.25, .75])
    iqr = q3 - q1
    upper_bound = q3 + 1.5 * iqr
    lower_bound = q1 - 1.5 * iqr
    upper = df.apply(lambda x: max([x - upper_bound, 0]))
    lower = df.apply(lambda x: min([x + lower_bound, 0]))
    return(upper, lower)

def add_outlier_columns(df, k):
    for col in df.select_dtypes('number'):
        df[col + '_upper_outliers'] = get_upper_outliers(df[col], k)
        df[col + '_lower_outliers'] = get_lower_outliers(df[col], k)
    return df

