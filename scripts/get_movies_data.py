import config
import sys
sys.path.append("../")
from modules import get_movies_module as gmm

api_key = config.tmdb_api_key
gmm.get_movie_data(api_key=api_key)