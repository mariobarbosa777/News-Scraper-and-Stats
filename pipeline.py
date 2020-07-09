from scraper.scraper import get_tree, get_links, create_urlnews
from config import get_config
import pandas as pd
from datetime import datetime
from stats.LangStats import NewsStats

def get_details_dict(details_dict,url):
    status, tree = get_tree(url)
    new_dict = {}
    if status:
        for details in details_dict:
            new_dict[details] = " ".join(tree.xpath(details_dict[details])).strip()
            if new_dict["Title"] =="":
                return {}

    print(f"{url} scraped OK")

    new_dict["url"] = url
    return new_dict


def get_data_news(exportCSV = True):
    config=get_config()
    for newspaper in config["newspaperlist"]:
        newspaper_dict = config["newspaperlist"][newspaper]
        details_dict = config["newspaperlist"][newspaper]["XPATH_news_details"]

        links= get_links(newspaper_dict)
        news_urls = create_urlnews(newspaper_dict,links)

        arraynews = []
        arraynews_stats = []

        for news_url in news_urls:
            news_details_dict = get_details_dict(details_dict,news_url)
            if news_details_dict:
                arraynews.append(news_details_dict)
                arraynews_stats.append(get_news_stats(news_details_dict))
           
        dfnews = pd.DataFrame(arraynews)
        dfnews.dropna(inplace=True)

        dfstats = pd.DataFrame(arraynews_stats)
        dfstats.dropna(inplace=True)

        if exportCSV:
            dfnews.to_csv(f"News {config['newspaperlist'][newspaper]['name']} at {datetime.now().strftime(' %Y, %m, %d %H-%M-%S')}.csv",encoding='utf-8-sig', index=False)
            dfstats.to_csv(f"Stats {config['newspaperlist'][newspaper]['name']} at {datetime.now().strftime(' %Y, %m, %d %H-%M-%S')}.csv",encoding='utf-8-sig', index=False)

    return  arraynews

def join_text_from_dict(news_details_dict):
    textofull=[]
    for key in news_details_dict:
        textofull.append(news_details_dict[key])

    return  " ".join(textofull)

def get_news_stats(news_details_dict):
    Stats = NewsStats(text =join_text_from_dict(news_details_dict))

    news_stats_dict = { }

    news_stats_dict["Tittle"] = news_details_dict["Title"]
    news_stats_dict["url"] = news_details_dict["url"]

    news_stats_dict["Vocabulary_len-No_StopWords"] = Stats.GetVocabularyLen()
    news_stats_dict["Vocabulary_len-No_StopWords"] = Stats.GetVocabularyLen()
    news_stats_dict["Vocabulary_len-With_StopWords"] = Stats.GetVocabularyLen(includestopwords=True)
    
    news_stats_dict["Common_words"] = Stats.GetMostCommonWords()
    news_stats_dict["Lexical_wealth"] = Stats.GetLexicalWealth()
    news_stats_dict["Bigrams_PMI"] = Stats.GetBigramswithPMI()
    news_stats_dict["Trigrams_PMI"] = Stats.GetTrigramswithPMI()


    return news_stats_dict

def run():
    get_data_news()



if __name__ == "__main__":
    run()
