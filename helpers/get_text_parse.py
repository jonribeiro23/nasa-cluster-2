from flask_restful import reqparse

get_text = reqparse.RequestParser()

get_text.add_argument('word',
                          type=str,
                          required=True,
                          help='Inform the key word')