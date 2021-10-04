from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from resources.data import (
    MostCommomWords,
    MostCommomWordsPopulation
)

app = Flask(__name__)
CORS(app)

app.config['DEBUG'] = True
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
app.secret_key = 'node.js'
api = Api(app)


api.add_resource(MostCommomWords, '/commom-words')
api.add_resource(MostCommomWordsPopulation, '/populate')



if __name__ == '__main__':
    app.run(port=5002)
