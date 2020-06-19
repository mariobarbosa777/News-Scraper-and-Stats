from scraper import get_tree, get_links, create_urlnews, get_details_dict
from config import get_config
import pandas as pd
from datetime import datetime


def run():
    config=get_config()
    for newspaper in config["newspaperlist"]:
        newspaper_dict = config["newspaperlist"][newspaper]
        details_dict = config["newspaperlist"][newspaper]["XPATH_news_details"]

        links= get_links(newspaper_dict)
        news_urls = create_urlnews(newspaper_dict,links)

        arraynews=[]
        for news_url in news_urls:
            arraynews.append(get_details_dict(details_dict,news_url))

        dfnews=pd.DataFrame(arraynews)
        dfnews.dropna(inplace=True)

        dfnews.to_csv(f"{config['newspaperlist'][newspaper]['name']} at {datetime.now().strftime(' %Y, %m, %d - %H-%M-%S')}.csv",encoding='utf-8-sig', index=False)




if __name__ == "__main__":
    
    run()


  # 
  # 