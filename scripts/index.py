import os 

default = os.getcwd()

exec(open("./get_movies_data.py").read())
os.chdir(default)
exec(open("./concat_watched_watchlist.py").read())
os.chdir(default)
exec(open("./download_imdb_tables.py").read())
os.chdir(default)
exec(open("./download_name_data.py").read())
os.chdir(default)
exec(open("./concat_info_movie.py").read())
os.chdir(default)
exec(open("./get_ratings.py").read())
os.chdir(default)
exec(open("./clean_data.py").read())
os.chdir(default)
