import pandas as pd
import warnings
from pprint import pprint
from models.search import TechPort
# from search import TechPort
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
class TA:
    def json_to_df(self, _id):
        tech_port = TechPort()
        r = tech_port.search_project(_id)

        try:
            benefits = r['project']['benefits'].replace('<p>', '').replace('</p>', '') if r['project'].get('benefits') else ''
            exampleTechnologies = r['project']['primaryTaxonomyNodes'][0]['exampleTechnologies'] if 'exampleTechnologies' in r['project']['primaryTaxonomyNodes'][0].keys() else ''
            data = {
                'text': r['project']['primaryTaxonomyNodes'][0]['title'] +
                        r['project']['primaryTaxonomyNodes'][0]['definition'] +
                        r['project']['primaryTaxonomyNodes'][0]['exampleTechnologies'] +
                        benefits +
                        r['project']['description'].replace('<p>', '').replace('</p>', '')
            }
        except KeyError:
            data = {
                'text': r['project']['primaryTaxonomyNodes'][0]['title'] +
                        r['project']['primaryTaxonomyNodes'][0]['definition'] +
                        benefits +
                        r['project']['description'].replace('<p>', '').replace('</p>', '')
            }

        return pd.read_json(json.dumps([data]))

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

    def clean_df(self, _id):
        df = self.json_to_df(_id)
        df['prep'] = df['text'].apply(TA.preprocess)
        return df

    def most_commom_words(self, _id):
        df = self.clean_df(_id)
        res = self._format_most_commom_words(Counter(" ".join(df["prep"]).split()).most_common(10), _id)
        return res

    def _format_most_commom_words(self, data, _id):
        res = {}
        temp = []
        res['project_id'] = _id
        for x in data:
            temp.append( {
                'most_commom':{
                    'word': x[0],
                    'repeat': x[1]
                }  
            })
        res['result'] = temp
        return res


projects = [
    {
                "projectId": 103110,
                "lastUpdated": "2021-9-9"
            },
            {
                "projectId": 102784,
                "lastUpdated": "2021-9-9"
            },
            {
                "projectId": 102629,
                "lastUpdated": "2021-9-9"
            },
            {
                "projectId": 102602,
                "lastUpdated": "2021-9-9"
            },
            {
                "projectId": 103089,
                "lastUpdated": "2021-9-9"
            },
            {
                "projectId": 102352,
                "lastUpdated": "2021-9-9"
            },
            {
                "projectId": 102900,
                "lastUpdated": "2021-9-9"
            },
            {
                "projectId": 102023,
                "lastUpdated": "2021-9-9"
            },
            {
                "projectId": 102084,
                "lastUpdated": "2021-9-9"
            },
            {
                "projectId": 103068,
                "lastUpdated": "2021-9-9"
            },
            {
                "projectId": 102492,
                "lastUpdated": "2021-9-9"
            }
]
