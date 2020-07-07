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
        self._text = text
        self._stopwords = stopwords.words(lenguaje)

        # Tokens with pattern and regexp
        self._tokens = nltk.regexp_tokenize(self._text.lower(), pattern)
        
        # AlphaNum Tokens with pattern and regexp
        self._alphaNumTokens = nltk.regexp_tokenize(re.sub(r'\W',' ', self._text.lower()),pattern)

        #Tokens Without StopWorks 
        self._tokensWithoutStopWd = [word for word in self._tokens if word.lower() not in self._stopwords]
        
        #AlphaNum Tokens Without StopWorks 
        self._alphaNumTokensWithoutStopWd = [word for word in self._alphaNumTokens if word.lower() not in self._stopwords]
        self._fdist= nltk.FreqDist(self._alphaNumTokensWithoutStopWd)

        #Vocabulary 
        self._vocabulary = list(set(self._tokens))
        self._vocabularyWithoutStopWd = list(set(self._tokensWithoutStopWd))

    def GetTokens(self):
        return self._tokens

    def GetAlphaNumTokens(self):
        return self._alphaNumTokens

    def GetTokensWithoutStopWords(self):
        return self._tokensWithoutStopWd

    def GetAlphaNumTokensWithoutStopWords(self):
        return self._alphaNumTokensWithoutStopWd

    def GetMostCommonWords(self,num=10):
        return self._fdist.most_common(num)

    def GetVocabulary(self,includestopwords=False):
        if includestopwords:
            return self._vocabulary
        else : 
            return self._vocabularyWithoutStopWd

    def GetLexicalWealth(self,includestopwords=False):
        if includestopwords:
            return len(self._vocabulary)/len(self._tokens) 
        else:
            return len(self._vocabularyWithoutStopWd)/len(self._tokensWithoutStopWd) 


    def GetBigrams(self,num=10,freqfilter=1):
        bigram_measure=nltk.collocations.BigramAssocMeasures()
        finder = nltk.collocations.BigramCollocationFinder.from_words(self._tokens)
        finder.apply_freq_filter(freqfilter)
        
        return finder.nbest(bigram_measure.pmi,num)

    def GetBigramswithPMI(self,num=10,freqfilter=1):
        bigram_measure=nltk.collocations.BigramAssocMeasures()
        finder = nltk.collocations.BigramCollocationFinder.from_words(self._tokens)
        finder.apply_freq_filter(freqfilter)

        Bigramspmi = finder.score_ngrams(bigram_measure.pmi)

        if len(Bigramspmi) > num:
            return Bigramspmi[0:num]
        else :
            return Bigramspmi

    def GetTrigrams(self,num=10,freqfilter=1):
        Trigram_measure=nltk.collocations.TrigramAssocMeasures()
        finder = nltk.collocations.TrigramCollocationFinder.from_words(self._tokens)
        finder.apply_freq_filter(freqfilter)
        

        return finder.nbest(Trigram_measure.pmi,num)

    def GetTrigramswithPMI(self, num=10,freqfilter=1):
        Trigram_measure=nltk.collocations.TrigramAssocMeasures()
        finder = nltk.collocations.TrigramCollocationFinder.from_words(self._tokens)
        finder.apply_freq_filter(freqfilter)

        Trigramspmi = finder.score_ngrams(Trigram_measure.pmi)

        if len(Trigramspmi) > num:
            return Trigramspmi[0:num]
        else :
            return Trigramspmi








