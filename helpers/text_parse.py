from flask_restful import reqparse

text = reqparse.RequestParser()

text.add_argument('content',
                          type=str,
                          required=True,
                          help='Text need be fullfilled')
text.add_argument('study_id',
                          type=str,
                          required=True,
                          help='ID need be fullfilled')
text.add_argument('title',
                          type=str,
                          required=True,
                          help='Title need be fullfilled')