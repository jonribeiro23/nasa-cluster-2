from pprint import pprint
from models.text_analysis import TA
from models.search import TechPort
from bson import ObjectId
from pymongo import MongoClient
from tqdm import tqdm
import pymongo
import json
from api_key import DB_CONNECTION
ta = TA()
tp = TechPort()

class DB:
    def __init__(self):
        # self.cluster = MongoClient('mongodb://localhost:27017')
        # self.db = self.cluster['nasa']
        
        self.client = pymongo.MongoClient("mongodb://octopus:<password>@cluster0-shard-00-00.ckcoz.mongodb.net:27017,cluster0-shard-00-01.ckcoz.mongodb.net:27017,cluster0-shard-00-02.ckcoz.mongodb.net:27017/nasa?ssl=true&replicaSet=atlas-z81myr-shard-0&authSource=admin&retryWrites=true&w=majority")
        self.db = self.client['nasa']


    def save(self, data_Set):
        try:
            if self.if_exists(data_Set['article_id']):
                return True
            self.db['most_commom_words'].insert_one(data_Set)
        except Exception as e:
            print('='*30)
            print(e)
            print('='*30)
            return False
        else:
            return True

    def if_exists(self, _id):
        try:
            res = self.db['most_commom_words'].find({'article_id': _id}).count()
        except Exception as e:
            print(e)
        else:
            return res

    def get_related_study(self, keyword):
        try:
            res = self.db['most_commom_words'].find({
                'result': {
                    '$elemMatch': {
                        'word': {'$regex': keyword}
                    }
                }
                }, {'article_id': 1, '_id': 0})

        except Exception as e:
            print(e)
            return False
        else:
            return [i for i in res]


    
