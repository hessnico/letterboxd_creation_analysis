import sys
sys.path.append("../")
import modules.download_imdb_modules as dim

if __name__ == "__main__":
    to_download = ['title.crew.tsv.gz','title.ratings.tsv.gz']
    for value in to_download:
        dim.start_download(value)