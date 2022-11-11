import pandas as pd

#export movies dataset
print("Getting information together")
export_df = pd.read_csv("../data/created/exported_tmdb_final.csv")
print(f"Dataframe exported successfully\nDataframe size: {export_df.shape[0]}\n")
print("Dropping duplicated ids...")
export_df = export_df.drop_duplicates(subset=["imdb_id"])
print(f"Refreshed data size: {export_df.shape[0]}\n")

#export info about movies in dataset
print("Exporting movies information")
title_ratings = pd.read_csv("../data/imdb/title.ratings.tsv.gz.csv")
title_crew = pd.read_csv("../data/imdb/title.crew.tsv.gz.csv")
directors_name = pd.read_csv("../data/imdb/name.basics.tsv.gz_directors.csv")
directors_name = directors_name.loc[:, ["nconst", "primaryName"]]
writers_name = pd.read_csv("../data/imdb/name.basics.tsv.gz_writers.csv")
merged_crew = pd.merge(title_ratings, title_crew, on="imdb_id")
merged_crew = merged_crew.drop(["tconst_y"], axis=1)
print("Done.\n")

#merging data
print("Merging information with exported dataset")
df = pd.merge(merged_crew, export_df, on='imdb_id', how='left')
print(f"Merged complete. \nDataframe size: {df.shape[0]}")

#mapping directors and writers names
dir_map = {}
wri_map = {}

for i in range(len(directors_name)):
    dir_map[directors_name.loc[i, "nconst"]] = directors_name.loc[i, "primaryName"]

for i in range(len(writers_name)):
    wri_map[writers_name.loc[i, "nconst"]] = writers_name.loc[i, "primaryName"]

df["directors_name"] = df["directors"].map(dir_map)
df["writers_name"] = df["writers"].map(wri_map)

df = df.drop(["tconst_x", 'directors', 'writers', 'id'],axis=1)
df = df.rename(columns={"Date" : "date_watched", "Name" : "title", "Year" : "release_year"})

df_watched = df.loc[df["Watched"] == 1]
df_watchlist = df.loc[df["Watched"] == 0]

df.to_csv(f"../data/clean/movies_watched_watchlist.csv",header=True, index = False)
print(f"Movies watched size: {df_watched.shape[0]}.\nWatchlist size: {df_watchlist.shape[0]}")
df_watched.to_csv(f"../data/clean/watched_movies.csv",header=True, index = False)
df_watchlist.to_csv(f"../data/clean/watchlist_movies.csv",header=True, index = False)
