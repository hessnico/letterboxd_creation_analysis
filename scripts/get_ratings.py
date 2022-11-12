import pandas as pd
print("Getting movie's ratings")
df = pd.read_csv("../data/clean/watched_movies.csv")
ratings = pd.read_csv("../data/letterboxd/ratings.csv")

ratings["Year"] = ratings["Year"].map(str)
df["release_year"] = df["release_year"].map(str)

ratings['name_year'] = ratings['Name'] + ' ' + ratings['Year']
df["name_year"] = df["title"] + ' '+ df["release_year"]

total = df.merge(ratings, on='name_year', how='left').drop(["Name", "name_year", "Date", "Year", "Letterboxd URI"], axis=1)
total.to_csv("../data/clean/ratings_watched.csv")
print("Done")