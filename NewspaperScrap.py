# -*- coding: utf-8 -*-
import requests
from lxml import html
import pandas as pd 
import os.path
from os import path


class ScrapingEspectador:

    def __init__(self,url):
        self.url = url

    def GetTree(self):
        try:
            pageContent = requests.get(self.url)
        except Exception as e:
            print("Error Scrapping URL:",self.url)
            print("")
            print(e)
            return None
        
        if pageContent.status_code !=200:
            print("Error Scrapping URL {}".format(self.url))
            print("")
            print("Status Code = {}".format(pageContent.status_code))
            return None

        self.tree=html.fromstring(pageContent.content)

        return 1

    def GetNewsData(self):

        self.data={}

        #ID
        self.data["ID"] = self.url.split("-")[-1]
        self._ID = self.data["ID"]

        #URL
        self.data["URL"] = self.url

        #Date
        try:
            self.data["date"]=" ".join(self.tree.xpath('//div[@itemprop="datePublished"]/text()')).encode("latin-1").decode("utf-8",errors="replace").replace("�"," ").strip()
        except:
            self.data["date"]=" ".join(self.tree.xpath('//div[@itemprop="datePublished"]/text()')).strip()

        #Author
        try:
            self.data["author"]=" ".join(self.tree.xpath('//div[@itemprop="author"]/text()')).encode("latin-1").decode("utf-8").strip() 
        except:   
            self.data["author"]=" ".join(self.tree.xpath('//div[@itemprop="author"]/text()')).strip()
        
        #Title
        try:
            self.data["title"]=" ".join(self.tree.xpath('//div[@itemprop="name"]/h1/text()')).encode("latin-1").decode("utf-8",errors="replace").replace("�"," ").strip() 
        except:
            self.data["title"]=" ".join(self.tree.xpath('//div[@itemprop="name"]/h1/text()')).strip() 

        #Get Epigraf
        try:
            self.data["epigraf"]=" ".join(self.tree.xpath('//*[contains(@class,"teaser")]//text()')).encode("latin-1").decode("utf-8",errors="replace").replace("�"," ").strip() 
        except:
            self.data["epigraf"]=" ".join(self.tree.xpath('//*[contains(@class,"teaser")]//text()')).strip() 
        
        #Get Body
        try:
            self.data["body"]=" ".join(self.tree.xpath('//*[contains(@class,"body")]/p//text()')).encode("latin-1").decode("utf-8",errors="replace").replace("�"," ").strip() 
        except:
            self.data["body"]=" ".join(self.tree.xpath('//*[contains(@class,"body")]/p//text()')).strip() 

        #ImgURL
        self.data["imgURL"]="".join(self.tree.xpath('//*[contains(@class,"file-image")]/img/@src'))

        return self.data

    def ExportDatatoCSV(self, Filename="DataNews.csv"):
        df=pd.DataFrame([self.data])
        
        df.to_csv(Filename, index=False, mode = 'a', header = not(path.exists(Filename)),encoding='utf-8-sig')


# if __name__ == "__main__":
    
#     URLs = ["https://www.elespectador.com/economia/hertz-compania-de-alquiler-de-vehiculos-se-declara-en-bancarrota-en-eeuu-articulo-920973",
#             "https://www.elespectador.com/noticias/el-mundo/pentagono-se-desmarca-de-trump-y-no-apoya-propuesta-de-enviar-soldados-protestas-articulo-922459",
#             "https://www.elespectador.com/noticias/el-mundo/la-pandemia-desde-corea-del-sur-estudiante-colombiana-cuenta-su-experiencia-articulo-922379",
#             "https://www.elespectador.com/economia/que-se-debe-el-actual-frenesi-por-el-papel-higienico-articulo-909787",
#             "https://www.elespectador.com/coronavirus/asignacion-de-recursos-para-programa-de-apoyo-las-nominas-articulo-922458",
#             "https://www.elespectador.com/coronavirus/una-recuperacion-duradera-para-el-petroleo-articulo-922427",
#             "https://www.elespectador.com/economia/hertz-compania-de-alquiler-de-vehiculos-se-declara-en-bancarrota-en-eeuu-articulo-920973",
#             "https://www.elespectador.com/no-se-puso-en-duda-la-validez-de-la-condena-contra-arias-articulo-920903",
#             "https://www.elespectador.com/coronavirus-cartagena-su-pasado-y-la-otra-crisis-en-medio-de-la-pandemia-articulo-920906",   
#     ]

#     URLs = list(set(URLs))

#     for url in URLs:
#         myNews=ScrapingEspectador(url)
#         if myNews.GetTree():
#             myNews.GetNewsData()
#             myNews.ExportDatatoCSV()
#             print(f"Data got from: {url}")
#         else:
#             print(f"Error getting data from: {url}")    