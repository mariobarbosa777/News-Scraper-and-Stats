import yaml
import requests
import pandas as pd
from lxml import html
from urllib.parse import urljoin

def get_config(configFileName="config.yaml"):
    with open("config.yaml", 'r') as f:
        _config = yaml.safe_load(f)
    return _config


def get_links(newspaper_dict):
    status, tree = get_tree(newspaper_dict["website"])
    if status:
        links=tree.xpath(newspaper_dict["XPATH_links"])
        
        return links

    else:
        return []


def get_tree(url):
    try:
        pageContent = requests.get(url)
        if pageContent.status_code ==200:
            tree=html.fromstring(pageContent.content.decode("utf-8"))
            return True, tree
        else:
            print(f"Error Scrapping URL {url} \n")
            print(f"Status Code = {pageContent.status_code}")
            return False, None
    except Exception as e:
        print(f"Error Scrapping URL: {url} \n")
        print(e)
        return False, None

def create_urlnews(newspaper_dict, links):
    news_urls = [ ]
    for link in links:
        news_urls.append(urljoin(newspaper_dict["website"],link))

    return news_urls

def get_details_dict(details_dict,url):
    status, tree = get_tree(url)
    new_dict = {}
    if status:
        for details in details_dict:
            new_dict[details] = " ".join(tree.xpath(details_dict[details])).strip()

    print(f"{url} scraped OK")

    new_dict["url"] = url
    return new_dict 
    
    



        


if __name__ == "__main__":
    
    config=get_config()
    for newspaper in config["newspaperlist"]:
        newspaper_dict = config["newspaperlist"][newspaper]
        details_dict = config["newspaperlist"][newspaper]["XPATH_news_details"]

        links= get_links(newspaper_dict)
        news_urls = create_urlnews(newspaper_dict,links)

        arraynews=[]
        for news_url in news_urls:
            arraynews.append(get_details_dict(details_dict,news_url))
        #for news_url in news_urls:

        dfnews=pd.DataFrame(arraynews)
        dfnews.to_csv("pruebaFinal.csv",encoding='utf-8-sig')
    print(dfnews)
