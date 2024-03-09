from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('title', required=True)
parser.add_argument('content', required=True)
parser.add_argument('is_private', required=True, type=bool)
parser.add_argument('user_id', required=True, type=int)

user_parser = reqparse.RequestParser()
user_parser.add_argument('name', required=True)
user_parser.add_argument('about', required=True)
user_parser.add_argument('email', required=True)
