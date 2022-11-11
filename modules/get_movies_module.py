import pandas as pd
import json
import requests 
from modules import get_info_modules

def get_movie_data(api_key, df, csv_name):
    print(f"Colleting data from {csv_name}.csv")
    df = df.drop(["Letterboxd URI"], axis=1)

    df['id'] = 0
    df['original_title'] = 0 

    for i in range(0, len(df)):
        title = format(df.loc[i, "Name"])
        print(f"Trying to collect from {title}")
        search_movie = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={title}"
        response =  requests.get(search_movie)
        if response.status_code == 200:
            raw_json_format = json.loads(response.text)
            json_format = get_info_modules.find_movie(raw_json_format, df.loc[i, "Year"])
            if json_format == None:
                i = i + 1
                print(f"json_format None for {title} indexed {i}")
            else:
                df.loc[i, 'id'] = str(json_format['id'])
                df.loc[i, 'original_title'] = str(json_format['original_title'])
                print(f"Initial data collected from {title}")

    for i in range(0, len(df)):
        title = format(df.loc[i, "original_title"])
        print(f"{i} - Trying to collect complete data from {title}")
        id = df.loc[i, "id"]
        movie_info = f"https://api.themoviedb.org/3/movie/{id}-{title}?api_key={api_key}"
        response = requests.get(movie_info)
        if response.status_code == 200:
            json_format = json.loads(response.text)
            df.loc[i, 'imdb_id'] = str(json_format['imdb_id'])
            df.loc[i, 'original_language'] = str(json_format['original_language'])
            df.loc[i, 'overview'] = str(json_format['overview'])
            df.loc[i, 'popularity'] = str(json_format['popularity'])
            df.loc[i, 'budget'] = str(json_format['budget'])
            df.loc[i, 'genres'] = get_info_modules.get_info(json_format, "genres", "name")
            df.loc[i, 'homepage'] = str(json_format['homepage'])
            df.loc[i, 'release_date'] = str(json_format['release_date'])
            df.loc[i, 'revenue'] = str(json_format['revenue'])
            df.loc[i, 'runtime'] = str(json_format['runtime'])
            df.loc[i, 'spoken_languages'] = str(json_format['spoken_languages'])
            df.loc[i, 'vote_average'] = str(json_format['vote_average'])
            df.loc[i, 'vote_count'] = str(json_format['vote_count'])
            df.loc[i, 'production_companies'] = get_info_modules.get_info(json_format, "production_companies", "name")
            df.loc[i, 'production_countries'] = get_info_modules.get_info(json_format, "production_countries", "iso_3166_1")
            df.loc[i, 'spoken_languages']= get_info_modules.get_info(json_format, "spoken_languages", "iso_639_1")
            df.loc[i, 'spoken_languages_full'] = get_info_modules.get_info(json_format, "spoken_languages", "english_name")
            print(f"Data collected data from {title}")

    df.to_csv(f"../data/created/exported_tmdb_{csv_name}.csv",header=True, index = False)