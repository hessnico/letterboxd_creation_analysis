# Letterboxd data creation and extraction, creation of hashmaps with IMDb's datasets and cleaning of data 
<a name="readme-top"></a>
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#Outputs">Usage</a></li>
	<li><a href="#Final conclusions">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
# About The Project
The ideia of the project is to automate extraction, cleaning and exploratory data analysis of my logged movies in Letterboxd.
The project consists in the extraction of data utilizing TMDB's API from my `watched.csv` exported in Letterboxd's site, the automatic creation of hashmaps from IMDb's open datasets, and finally, in the cleaning of data using, mostly, the Pandas library from Python. 
Lastly, the cleaned data can be used for exploratory data analysis, for data regression and a lot more. 

### Built With

<ul>
    <li>Pandas</li>
    <li>Sklearn</li>
	<li>Json</li>
    <li>Requests</li>
	<li>Seaborn</li>
	<li>Matplotlib</li>
	<li>Datatime</li>
</ul>

<!-- GETTING STARTED -->
## Getting Started

An TMDB's API key is needed, also some Python libraries.

### Prerequisites

For installation of Python library, try
* Check if pip is installed
  ```sh
  pip help 
  ```
* If not, try downloadind pip in [pip's installation guide](https://pip.pypa.io/en/stable/installation/)

### Installation

1. Get a free API Key at [https://www.themoviedb.org/documentation/api](https://www.themoviedb.org/documentation/api)
2. Clone the repo
   ```sh
   git clone https://github.com/hessnico/letterboxd_creation_analysis
   ```
3. Enter your API in `config.py`
   ```python
	tmdb_api_key = ""
   ```
4. Export your data `ratings.csv`, `watched.csv` and `watchlist.csv` from [Letterboxd site](https://letterboxd.com/settings/data/) and them put it inside `/data/letterboxd/` file.
5. Run index file
	```sh
	python index.py
	```

<!-- Outputs -->
## Outputs 
During the execution of `index.py` is generated a lot of csv tables.  Generated in `/data/imdb` is the two hashmaps called `directors_dataset.csv` and `writers_directors.csv`, they have the persons id in IMDb and name, also in the same folder is the two tables with not found or invalid movie's ids. <br>
Generated in `/data/created` is the data extracted in the `get_movies_data.py` with TMDB's API. <br>
For the last folder, is the `/data/clean` with the cleaned and ready to use data. Data with name `*_watched` or `*_watchlist` means that the data was separed in the watched movies section or movies in watchlist. This was made because with the creation of a good regression model (if possible, cinema is subjective) there can be made some predictions in the movie ratings.

<!-- Final conclusions -->
## Final conclusions
The initial idea was to automate data extraction and cleaning, which was successfully done. In the end, I took the liberty to try and create an regression algorithm for finding patterns in my ratings, found in `/scripts/data_regression.py`, and, if so, creating predictions for my watchlist movies. I got a plus 50% score and a small, but positive, R squared value, which, I didn't expected. 
This is an open source project, feel free to clone and try it with your personal data. 

<!-- CONTACT -->
## Contact

In case for any suggestions, check out my [Linkedin profile](https://www.linkedin.com/in/hessnico/)

<p>(<a href="#readme-top">back to top</a>)</p>