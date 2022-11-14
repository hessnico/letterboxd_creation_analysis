import pandas as pd
import os
import sys
sys.path.append("../")
from modules import clean_dataframe as clear

dataframe1 = pd.read_csv("../data/clean/dirty_watched.csv")
dataframe2 = pd.read_csv("../data/clean/watchlist_movies.csv")
clear.clean_dataframe(df=dataframe1, name='watched')
clear.clean_dataframe(df=dataframe2, name='watchlist')
os.remove("../data/clean/dirty_watched.csv")
os.remove("../data/clean/watchlist_movies.csv")
