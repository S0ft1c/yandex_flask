from data import db_session
from data.news import News
from flask_restful import abort, Resource
from flask import jsonify, make_response
from .reqparse import parser


def abort_if_not_found(news_id):
    sess = db_session.create_session()
    news = sess.query(News).get(news_id)
    if not news:
        abort(404, message=f'News {news_id} not found')


class NewsResource(Resource):
    def get(self, news_id):
        abort_if_not_found(news_id)
        sess = db_session.create_session()
        news = sess.query(News).get(news_id)
        if not news:
            return make_response(jsonify({'error': 'Not found'}), 404)
        return jsonify(
            {
                'news': news.to_dict(only=(
                    'title', 'content', 'user_id', 'is_private'))
            }
        )

    def delete(self, news_id):
        abort_if_not_found(news_id)
        db_sess = db_session.create_session()
        news = db_sess.query(News).get(news_id)
        if not news:
            return make_response(jsonify({'error': 'Not found'}), 404)
        db_sess.delete(news)
        db_sess.commit()
        return jsonify({'success': 'OK'})


class NewsListResources(Resource):
    def get(self):
        db_sess = db_session.create_session()
        news = db_sess.query(News).all()
        return jsonify(
            {
                'news':
                    [item.to_dict(only=('title', 'content', 'user.name'))
                     for item in news]
            }
        )

    def post(self):
        db_sess = db_session.create_session()
        args = parser.parse_args()
        news = News(
            title=args['title'],
            content=args['content'],
            user_id=args['user_id'],
            is_private=args['is_private']
        )
        db_sess.add(news)
        db_sess.commit()
        return jsonify({'success': 'OK'})
