import pandas as pd
import warnings
from pprint import pprint
import json
import re
import nltk
from nltk.stem import WordNetLemmatizer
from collections import Counter
# from fill_db import FillDB

# db = FillDB()

nltk.download('wordnet')
stop_words_file = 'models/stop_list.txt'
# stop_words_file = 'stop_list.txt'
stop_words = []

with open(stop_words_file, "r") as f:
    for line in f:
        stop_words.extend(line.split()) 
        
stop_words = stop_words  


warnings.filterwarnings('ignore')
class TAGeneLab:

    @staticmethod
    def preprocess(raw_text):
    
        #regular expression keeping only letters 
        letters_only_text = re.sub("[^a-zA-Z]", " ", raw_text)

        # convert to lower case and split into words -> convert string into list ( 'hello world' -> ['hello', 'world'])
        words = letters_only_text.lower().split()

        cleaned_words = []
        lemmatizer = WordNetLemmatizer() #plug in here any other stemmer or lemmatiser you want to try out
        
        # remove stopwords
        for word in words:
            if word not in stop_words:
                cleaned_words.append(word)
        
        # stemm or lemmatise words
        stemmed_words = []
        for word in cleaned_words:
            word = lemmatizer.lemmatize(word)   #dont forget to change stem to lemmatize if you are using a lemmatizer
            stemmed_words.append(word)
        
        # converting list back to string
        return " ".join(stemmed_words)

    def most_commom_words(self, txt):
        df = pd.read_json(json.dumps([txt]))
        data = df['content'].apply(TAGeneLab.preprocess)
        res = self._format_most_commom_words(Counter(" ".join(data).split()).most_common(5), txt['study_id'])
        return res

    def _format_most_commom_words(self, data, _id):
        res = {}
        temp = []
        res['article_id'] = _id
        for x in data:
            temp.append( {
                    'word': x[0],
                    'repeat': x[1]
            })
        res['result'] = temp
        return res

