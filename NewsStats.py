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

class NewsStats:
    
    def __init__(self,text,lenguaje="spanish"):
        self.text = text
        self._stopwordsES = stopwords.words(lenguaje) 

    def GetTokens(self):
        self._tokens = nltk.regexp_tokenize(self.text.lower(), pattern)
        return  self._tokens

    def GetAlphaNumTokensFromText(self):
        text=re.sub(r'\W',' ', self.text.lower())
        self._alphaNumTokens = nltk.regexp_tokenize(text,pattern)
        
        return self._alphaNumTokens
    
    def GetTokenNonStopWords(self):
        stopWd = stopwords.words("spanish")
        self._tokensNonStopWd = [word for word in self._tokens if word.lower() not in self._stopwordsES]
        return self._tokensNonStopWd

    def GetTokenNonStopAlphaNumTokens(self):
        self.GetAlphaNumTokensFromText()
        self._tokensNonStopAlphaNum = [ word for word in self._alphaNumTokens if word.lower() not in  self._stopwordsES]
        return self._tokensNonStopAlphaNum   

    def MostCommonWords(self,num=10):
        fdist= nltk.FreqDist(self._tokens)
        return fdist.most_common(num)

    def MostCommonNoStopWords(self,num=10):
        fdist= nltk.FreqDist(self._tokensNonStopAlphaNum)
        return fdist.most_common(num)


    def VocabularyWordsProportion(self):
        "Riqueza Lexica"
        return len(list(set(self._tokens)))/len(self._tokens)    
    

if __name__ == "__main__":
    pass
