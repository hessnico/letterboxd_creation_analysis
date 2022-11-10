import os
import requests
import pandas as pd

def download_file(url):
    filename = url.split("/")[-1]
    os.chdir("../data/") 
    print(f"Temporary .gz file will start downloading in directory {os.getcwd()}")
    with open(filename, "wb") as f:
        r = requests.get(url)
        f.write(r.content)
        f.close()

def extract_and_join(filename):
    print("Unzip started")
    tmp = pd.read_csv(filename, compression='gzip', header=0, sep="\t", quotechar='"')
    print("Unzip finished, file opened as 'tmp'.")
    return tmp
    
def merge_exported_downloaded(exported_name, tmp):
    print("Merge started")
    odf = pd.read_csv(exported_name)
    odf = odf.loc[:, ["imdb_id"]]
    total_size = odf.shape[0]
    df = odf.merge(tmp, how='inner', left_on='imdb_id', right_on='tconst')
    print(f"Inner join finished. \nOriginal data size: {total_size}\nData size now: {df.shape[0]}\n...")
    return df, total_size-df.shape[0]

def verify_not_valid(exported_name, tmp):
    print("Not valid values verification started")
    odf = pd.read_csv(exported_name)
    odf_not_valid = odf.loc[:, ["imdb_id", "Name"]]
    not_valid = pd.merge(odf_not_valid, tmp, left_on='imdb_id', right_on='tconst', how="outer", indicator=True
            ).query('_merge=="left_only"')
    print("Verification completed, returning dataset as 'not_valid'")
    return not_valid

def start_download(value):
    print(f"\nStarting now {value} download and merge\n...")
    url = f"https://datasets.imdbws.com/{value}"
    download_file(url)
    filename = url.split("/")[-1]
    tmp = extract_and_join(filename)
    exported_name = "../data/created/exported_tmdb.csv"
    df, not_valid = merge_exported_downloaded(exported_name, tmp)
    if not_valid > 0:
        not_valid = verify_not_valid(exported_name, tmp)
        not_valid.to_csv(f"../data/imdb/{filename}_id_not_found.csv",header=True, index = False)
    try:    
        df.to_csv(f"../data/imdb/{filename}.csv",header=True, index = False)
        print("Dataframe with ids saved")
        try:
            os.remove(f"./{filename}")
            print("Download deleted")
        except:
            print("Wasn't able to remove downloaded file.")
    except:
        print("Error.")