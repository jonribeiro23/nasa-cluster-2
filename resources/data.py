from pprint import pprint
from flask_restful import Resource
from models.text_analysis_GeneLab import TAGeneLab
from models.DB import DB
from helpers.text_parse import text
from helpers.get_text_parse import get_text
ta = TAGeneLab()
db = DB()


class MostCommomWords(Resource):
    def put(self):
        keyword = get_text.parse_args()
        data = db.get_related_study(keyword['word'])
        if data:
            return {'message': 'ok', 'content': data}, 200
        return {'message': 'err'}, 500

    def post(self):
        to_analyze = text.parse_args()
        data = ta.most_commom_words(to_analyze)
        if not db.save(data):
            return {'message': 'err'}, 501
        data.pop('_id') if '_id' in data.keys() else ''
        return {'message': 'ok', 'content': data}, 201


class MostCommomWordsPopulation(Resource):
    def get(self):
        try:
            pass
        except Exception as e:
            return {'message': e}, 501
        else:
            return {'message': 'ok'}, 200
        
