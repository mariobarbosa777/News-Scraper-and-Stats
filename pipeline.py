from scraper import get_tree, get_links, create_urlnews
from config import get_config
import pandas as pd
from datetime import datetime
from LangStats import NewsStats

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




def get_data_news():
    config=get_config()
    for newspaper in config["newspaperlist"]:
        newspaper_dict = config["newspaperlist"][newspaper]
        details_dict = config["newspaperlist"][newspaper]["XPATH_news_details"]

        links= get_links(newspaper_dict)
        news_urls = create_urlnews(newspaper_dict,links)

        arraynews=[]
        for news_url in news_urls:
            arraynews.append(get_details_dict(details_dict,news_url))
            get_newsstats(details_dict)

        dfnews=pd.DataFrame(arraynews)
        dfnews.dropna(inplace=True)

        dfnews.to_csv(f"{config['newspaperlist'][newspaper]['name']} at {datetime.now().strftime(' %Y, %m, %d %H-%M-%S')}.csv",encoding='utf-8-sig', index=False)


def jointextList(textlist):
    textofull=[]
    for text in textlist:
        textofull.extend(text)

    return " ".join(textofull)


def get_newsstats(details_dict):
    pass



def run():
     get_data_news()


if __name__ == "__main__":
    
    run()


  # 
  # 