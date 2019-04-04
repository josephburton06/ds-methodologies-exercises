import seaborn as sns
import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

# ignore warnings
import warnings
warnings.filterwarnings("ignore")

import env

def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_titanic_data():
    return pd.read_sql('SELECT * FROM passengers', get_connection('titanic_db'))

def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_iris_data():
    return pd.read_sql('SELECT m.*, s.species_name FROM measurements as m JOIN species as s ON m.species_id = s.species_id', get_connection('iris_db'))

