from LangStats import NewsStats
from NewspaperScrap import ScrapingEspectador


def jointextList(textlist):
    textofull=[]
    for text in textlist:
        textofull.extend(text)

    return " ".join(textofull)

def GetDataFromURLsElEspectador(URLs):

    URLs = list(set(URLs))
    data=[]

    Errors=0

    for url in URLs:
        myNews=ScrapingEspectador(url)
        if myNews.GetTree():
            data.append(myNews.GetNewsData())
            #myNews.ExportDatatoCSV(Filename="DatosNoticias.csv")
            print(f"Data got from: {url}")

        else:
            Errors+=1
            print(f"Error getting data from: {url}")
    
    print (f"Successful News Scrapper {len(URLs)-Errors}")
    print (f"Errors Scraping News {Errors}")

    return data
        
    







if __name__ == "__main__":

    URLs = ["https://www.elespectador.com/economia/hertz-compania-de-alquiler-de-vehiculos-se-declara-en-bancarrota-en-eeuu-articulo-920973",
            "https://www.elespectador.com/noticias/el-mundo/pentagono-se-desmarca-de-trump-y-no-apoya-propuesta-de-enviar-soldados-protestas-articulo-922459",
            "https://www.elespectador.com/noticias/el-mundo/la-pandemia-desde-corea-del-sur-estudiante-colombiana-cuenta-su-experiencia-articulo-922379",
            "https://www.elespectador.com/economia/que-se-debe-el-actual-frenesi-por-el-papel-higienico-articulo-909787",
            "https://www.elespectador.com/coronavirus/asignacion-de-recursos-para-programa-de-apoyo-las-nominas-articulo-922458",
            "https://www.elespectador.com/coronavirus/una-recuperacion-duradera-para-el-petroleo-articulo-922427",
            "https://www.elespectador.com/economia/hertz-compania-de-alquiler-de-vehiculos-se-declara-en-bancarrota-en-eeuu-articulo-920973",
            "https://www.elespectador.com/no-se-puso-en-duda-la-validez-de-la-condena-contra-arias-articulo-920903",
            "https://www.elespectador.com/coronavirus-cartagena-su-pasado-y-la-otra-crisis-en-medio-de-la-pandemia-articulo-920906",   
    ]

    data=GetDataFromURLsElEspectador(URLs)

    AppendDatos=[]
    for datos in data: 
        AppendDatos.append( [ datos["title"], datos["epigraf"], datos["body"] ])


    FullText = jointextList(AppendDatos)


    myStats = NewsStats(FullText)

    print (f"Bigramas: {myStats.GetBigramswithPMI(freqfilter=5, num=5)}")
    print(f"Trigramas: {myStats.GetTrigramswithPMI(freqfilter=5,num=5)}") 