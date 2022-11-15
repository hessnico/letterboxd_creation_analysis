import os 
import subprocess

default = os.getcwd()

folders = ["clean", "created", "imdb", "letterboxd"]
for folder in folders:
    target_dir = f"../data/{folder}"
    if os.path.exists(target_dir) == False:
        os.mkdir(target_dir)

files = ["./get_movies_data.py", "./concat_watched_watchlist.py", "./download_imdb_tables.py", "./download_imdb_tables.py", "./download_name_data.py", "./concat_info_movie.py", "./get_ratings.py", "./clean_data.py"]
files = []

for file in files:
    os.chdir(default)
    exec(open(file).read())

os.chdir(default)
subprocess.call("create_pdf_notbook.bat")