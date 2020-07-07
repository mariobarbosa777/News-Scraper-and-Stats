import requests
from lxml import html
from urllib.parse import urljoin

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

def get_links(newspaper_dict):
    status, tree = get_tree(newspaper_dict["website"])
    if status:
        links=tree.xpath(newspaper_dict["XPATH_links"])
        
        return list(set(links))

    else:
        return []

def create_urlnews(newspaper_dict, links):
    news_urls = [ ]
    for link in links:
        news_urls.append(urljoin(newspaper_dict["website"],link))

    return news_urls




    