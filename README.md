# News-Scraper-and-Stats

For each newspaper_X in config.yaml, a .csv is created with details in XPATH_news_details from newspaper home

This generate two .cvs per newspaper (News data and Stats) 

The stats are:
    Vocabulary len, Common words, Lexical wealth, Bigrams, Trigrams

#Use
    Clone this repository and move to folder

    python -m venv venv

    source venv/bin/activate  for linux or source venv/Scripts/Activate for windows

    pip install -r requirements.txt

    python pipeline.py
