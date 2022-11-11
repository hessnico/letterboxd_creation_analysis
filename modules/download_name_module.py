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
    os.chdir("../data/") 
    tmp = pd.read_csv(filename, compression='gzip', header=0, sep="\t", quotechar='"')
    print("Unzip finished, file opened as 'tmp'.")
    return tmp

def get_list_unique(dataset, value):
    print(f"Getting list of {value} data")
    unique_director = []
    for i in range(len(dataset[value])):
        lst = dataset.loc[i, value].split(",")
        for j in range(len(lst)):
            if unique_director.count(lst[j]) < 1:
                unique_director.append(lst[j])
                i += 1
    
    print(f"{value} data retrieved")
    return unique_director

def join_of_databases(unique_directors, tmp, value):
    print("Inner join started")
    dir = pd.DataFrame(unique_directors, columns=[f"id_{value}"])
    df = tmp.merge(dir, how='inner', left_on="nconst", right_on=f'id_{value}')
    total_size = dir.shape[0]
    print(f"Inner join finished. \nOriginal data size: {total_size}\nData size now: {df.shape[0]}\n...")
    return df


def start_download(to_download):
    print(f"\nStarting now {to_download} download and merge\n...")
    url = f"https://datasets.imdbws.com/{to_download}"
    download_file(url)
    tmp = extract_and_join(to_download)
    get_list = ['directors', 'writers']
    dataset_for_extraction = pd.read_csv("../data/imdb/title.crew.tsv.gz.csv")
    for value in get_list:
        unique_p = get_list_unique(dataset_for_extraction, value)
        unique_p.sort()
        df = join_of_databases(unique_p, tmp, value)
        try:    
            df.to_csv(f"../data/imdb/{to_download}_{value}.csv",header=True, index = False)
            print("Dataframe with ids saved")
        except:
            print("Error.")

    try:
        os.remove(f"./{to_download}")
        print("Download deleted")
    except:
        print("Wasn't able to remove downloaded file.")

'''
def verify_not_valid(unique_directors, tmp):
    print("Verifying not valid ids")
    dir = pd.DataFrame(unique_directors, columns=["id_directors"])
    not_valid = pd.merge(dir, tmp, left_on="id_directors", right_on="nconst", how="outer", indicator=True
            ).query('_merge=="left_only"')
    print("Verification completed, returning dataset as 'not_valid'")
    return not_valid
'''

'''
used the verify_not_valid and found this
Verifying not valid ids
Verification completed, returning dataset as 'not_valid'
id_directors nconst primaryName birthYear deathYear primaryProfession knownForTitles     _merge
0           N    NaN         NaN       NaN       NaN               NaN            NaN  left_only
'''

    