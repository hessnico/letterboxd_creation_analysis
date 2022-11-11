import pandas as pd

print("Joining watched movies with your watchlist")
watched = pd.read_csv("../data/created/exported_tmdb_watched.csv")
watchlist = pd.read_csv("../data/created/exported_tmdb_watchlist.csv")

watched['Watched'] = 1
watchlist['Watched'] = 0

df = pd.concat([watched, watchlist], axis=0)
print(df)
df.to_csv(f"../data/created/exported_tmdb_final.csv",header=True, index = False)
print("Done.\n")