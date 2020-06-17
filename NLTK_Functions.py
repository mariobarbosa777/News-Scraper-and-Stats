import nltk 
import re 
from nltk.corpus import stopwords

pattern = r'''(?x)                 # set flag to allow verbose regexps
              (?:[A-Z]\.)+         # abbreviations, e.g. U.S.A.
              | \w+(?:-\w+)*       # words with optional internal hyphens
              | \$?\d+(?:\.\d+)?%? # currency and percentages, e.g. $12.40, 82%
              | \.\.\.             # ellipsis
              | [][.,;"'?():-_`]   # these are separate tokens; includes ],
            '''



def GetTokens(text):

    tokens = nltk.regexp_tokenize(text.lower(),pattern)
    #tokens = nltk.regexp_tokenize(text,'\w')
    nltk.regexp_tokenize
    return  tokens

def GetAlphaNumTokensFromText(text):
    text=re.sub(r'\W',' ',text.lower())
    tokens = nltk.regexp_tokenize(text,pattern)
    return tokens

def GetTokenNonStopWords(tokens):
    stopWd = stopwords.words("spanish")

    tokensNonStopWd = [word for word in tokens if word.lower() not in  stopWd]
    
    return tokensNonStopWd

def GetTokenStopWords(tokens):
    stopWd = stopwords.words("spanish")

    tokensStopWd = [word for word in tokens if word.lower() in  stopWd]
    
    return tokensStopWd 

def StopwordsPercentaje(tokens):
    """
    tokens = List of words   ["Hello","World","Mommy","Happy"]
    """
    stopWd = stopwords.words("spanish")

    tokensStopWd = [word for word in tokens if word.lower() in stopWd]
    
    return len(tokensStopWd)/len(tokens)

def NonStopwordsPercentaje(tokens):

    return (1-StopwordsPercentaje(tokens))

def MostCommonWords(tokens,num=10):
    fdist= nltk.FreqDist(tokens)
    return fdist.most_common(num)

def VocabularyWordsProportion(tokens):
    "Riqueza Lexica"
    return len(list(set(tokens)))/len(tokens)

def TextLen(tokens):
    return len(tokens)

def Vocabulary(tokens):
    return sorted(set(tokens))

def VocabularyLen(tokens):
    return len(sorted(set(tokens)))


def GetBigrams(tokens,numbigrams=10,freqfilter=1):
    bigram_measure=nltk.collocations.BigramAssocMeasures()
    finder = nltk.collocations.BigramCollocationFinder.from_words(tokens)

    finder.apply_freq_filter(freqfilter)
    

    return finder.nbest(bigram_measure.pmi,numbigrams)

def GetBigramswithPMI(tokens,freqfilter=1):
    bigram_measure=nltk.collocations.BigramAssocMeasures()
    finder = nltk.collocations.BigramCollocationFinder.from_words(tokens)

    finder.apply_freq_filter(freqfilter)

    return finder.score_ngrams(bigram_measure.pmi)

def GetTrigrams(tokens,numbigrams=10,freqfilter=1):
    Trigram_measure=nltk.collocations.TrigramAssocMeasures()
    finder = nltk.collocations.TrigramCollocationFinder.from_words(tokens)
    finder.apply_freq_filter(freqfilter)
    
    return finder.nbest(Trigram_measure.pmi,numbigrams)

def GetTrigramswithPMI(tokens,freqfilter=1):
    Trigram_measure=nltk.collocations.TrigramAssocMeasures()
    finder = nltk.collocations.TrigramCollocationFinder.from_words(tokens)
    finder.apply_freq_filter(freqfilter)

    return finder.score_ngrams(Trigram_measure.pmi)



if __name__ == "__main__":

    texto = """ En Hola Mundo salvaje Ayer cuando sea el rey del Hola mundo (imaginaba él en su cabeza) no tendré que  preocuparme por estas bobadas. 
            Era solo un niño de 7 años, pero pensaba con la cabeza, que podría ser cualquier cosa que  Hola Mundo su imaginación le permitiera 
            visualizar Hola Mundo salvaje en su cabeza...""" 

    
    tokens=GetTokens(texto)
    print(GetBigrams(tokens,freqfilter=2))