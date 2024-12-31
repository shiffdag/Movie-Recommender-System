# Movie-Recommender-System

### To set up repository:
- `pyenv virtualenv 3.10.13 recommender`
- `pyenv activate recommender`
- `poetry install`
- `pre-commit install`
- If you have the kaggle utility installed, run the following to download the data:
  - `mkdir data && cd data`
  - `kaggle competitions download -c recsys-20181-cfmr`
  - `unzip recsys-20181-cfmr.zip`
