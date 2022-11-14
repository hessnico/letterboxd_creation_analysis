import pandas as pd 
import numpy as np
import warnings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestRegressor
import sklearn.metrics as metrics
from datetime import datetime
from sklearn.preprocessing import MinMaxScaler
warnings.simplefilter(action='ignore', category=pd.errors.PerformanceWarning)

def encode_variables(dataset, row_name):
    dataset.loc[:, row_name] = dataset.loc[:, row_name].str.replace("[", '', regex=False)
    dataset.loc[:, row_name] = dataset.loc[:, row_name].str.replace("]", '', regex=False)
    dataset.loc[:, row_name] = dataset.loc[:, row_name].str.replace(" ", '')
    dataset.loc[:, row_name] = dataset.loc[:, row_name].str.replace("'", '')
    dataset[row_name] = dataset[row_name].astype('string')
    for i in range(len(dataset)):
      lst = dataset.loc[i, row_name].split(",")
      for j in range(len(lst)):
        dataset.loc[i, f"{row_name}_{lst[j]}"] = 1
    return dataset

def encode_year(dataset, row_name):
    dataset[row_name] = dataset[row_name].astype('string')
    for i in range(len(dataset)):
      lst = dataset.loc[i, row_name].split(",")
      for j in range(len(lst)):
        dataset.loc[i, f"{row_name}_{lst[j]}"] = 1
    return dataset

def classify_fit_predict(classifier, X_train, Y_train, X_test):
    '''classifier/regression algorithm, fit him to x axis train set and y axis train set and later, predict with x axis test set'''
    
    start_time = datetime.now()
    
    cl = str(classifier)
    tmp = cl.find("(")
    print("Calculating predictions for", cl[:tmp])
    
    clf = classifier
    model = clf.fit(X_train, Y_train)
    y_pred = model.predict(X_test)
    
    print(f"{cl[:-2]} is ready... \nCalculation finished in {datetime.now()-start_time}")
    
    return model, y_pred

print("Training the model started...")
watched = pd.read_csv("../data/clean/clean_watched.csv")
watched = watched.drop(["Unnamed: 0", "name_year", "Date", "Name", "Year", "tmdb_total_votes", "tmdb_rating", "production_companies", "production_countries", "release_date"], axis=1)
watched["release_year"] = watched["release_year"].astype('string')
watched = watched.dropna()
watched = watched.reset_index()
watched=watched.drop(["index", "level_0"], axis=1)
print(watched.columns)

lst = [watched]

for value in lst:
    value = encode_variables(value, 'genres')
    value = encode_variables(value, 'original_language')
    value = encode_variables(value, 'spoken_languages')
    value = encode_year(value, 'release_year')

watched = watched.drop(["genres", "original_language", 'spoken_languages', 'release_year'], axis=1)
watched = watched.fillna(0)

numerical_data = watched.loc[:, ['imdb_rating', 'imdb_total_votes', 'budget', 'revenue',
       'runtime']]

text_data = watched.loc[:, ["overview"]]

remaining_data = watched.drop(['imdb_rating', 'imdb_total_votes', 'budget', 'revenue',
       'runtime'],axis=1)

tfidf = TfidfVectorizer(stop_words='english')
tfidf_plot = tfidf.fit_transform(watched['overview'])
words = pd.DataFrame(tfidf_plot.toarray())

scaler = MinMaxScaler()
standardized_df = scaler.fit_transform(numerical_data)
standardized_df = pd.DataFrame(standardized_df, columns=numerical_data.columns)

watched = standardized_df.merge(remaining_data, left_index=True, right_index=True)
watched = watched.merge(words, left_index=True, right_index=True)

x_data = watched.drop(["my_rating", "title", "overview", "Watched"], axis=1)
y_data = watched.loc[:, "my_rating"]

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, random_state=111, test_size=0.2)

classifiers = [ 
    RandomForestRegressor()
]

models = []

for classifier in classifiers:
    cfp = classify_fit_predict(classifier, x_train.values, y_train.values, x_test.values)
    models.append(cfp)

for i in range(len(models)):
    mae = metrics.mean_absolute_error(models[i][1], y_test.values)
    mse = metrics.mean_squared_error(models[i][1], y_test.values)
    rmse = np.sqrt(mse)
    r2 = metrics.r2_score(models[i][1],y_test)

    print(f"\n{str(models[i][0])[:-2]} got scored at: {(models[i][0].score(x_test.values, y_test.values))*100:.2f}% ")
    print("Results of sklearn.metrics:")
    print("MAE:",mae)
    print("MSE:", mse)
    print("RMSE:", rmse)
    print("R-Squared:", r2)
    print("\n")