import pandas as pd

def clean_dataframe(df, name):
    print(f"General {name} data cleaning starting now...")
    df.rename(columns={'Unnamed: 0' : 'index', 'averageRating' : 'imdb_rating', 'numVotes' : 'imdb_total_votes', 'vote_average' : 'tmdb_rating', 'vote_count' : 'tmdb_total_votes', 'directors_name' : 'directors', 'writers_name' : 'writers', 'Rating' : 'my_rating'}, inplace=True)
    df = df.drop(['imdb_id', 'original_title', 'popularity', 'homepage', 'spoken_languages_full', 'date_watched'], axis=1)
    df["genres"] = df["genres"].str[:].str.split(',').tolist()
    df["spoken_languages"] = df["spoken_languages"].str[:].str.split(',').tolist()
    df["production_companies"] = df["production_companies"].str[:].str.split(',').tolist()
    df['production_countries'] = df['production_countries'].str[:].str.split(',').tolist()
    df["title"] = df["title"].astype('string')
    df["budget"] = df["budget"].astype('float')
    df["revenue"] = df["revenue"].astype('float')
    if 'my_rating' in df.columns:
        df["my_rating"] = df["my_rating"] * 2
    print("Done.")
    try:
        df.to_csv(f"../data/clean/clean_{name}.csv")
    except:
        print("Error on exportation.")

if __name__ == '__main__':
    dataframe1 = pd.read_csv("../data/clean/dirty_watched.csv")
    dataframe2 = pd.read_csv("../data/clean/watchlist_movies.csv")
    clean_dataframe(df=dataframe1, name='watched')
    clean_dataframe(df=dataframe2, name='watchlist')
