import config
import pandas as pd
import sys
sys.path.append("../")
from modules import get_movies_module as gmm

api_key = config.tmdb_api_key
df1 = pd.read_csv("../data/letterboxd/watchlist.csv")
df2 = pd.read_csv("../data/letterboxd/watched.csv")
gmm.get_movie_data(api_key=api_key, df=df1, csv_name='watchlist')
gmm.get_movie_data(api_key=api_key, df=df2, csv_name='watched')