from data import db_session
from data.users import User
from flask_restful import abort, Resource
from flask import jsonify, make_response
from .reqparse import user_parser


def abort_if_not_found(user_id):
    sess = db_session.create_session()
    users = sess.query(User).get(user_id)
    if not users:
        abort(404, message=f'User {user_id} not found')


class UserResource(Resource):
    def get(self, user_id):
        abort_if_not_found(user_id)
        sess = db_session.create_session()
        users = sess.query(User).get(user_id)
        if not users:
            return make_response(jsonify({'error': 'Not found'}), 404)
        return jsonify(
            {
                'users': users.to_dict(only=(
                    'surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'hashed_password',
                    'modified_date'))
            }
        )

    def delete(self, user_id):
        abort_if_not_found(user_id)
        db_sess = db_session.create_session()
        users = db_sess.query(User).get(user_id)
        if not users:
            return make_response(jsonify({'error': 'Not found'}), 404)
        db_sess.delete(users)
        db_sess.commit()
        return jsonify({'success': 'OK'})


class UsersListResources(Resource):
    def get(self):
        db_sess = db_session.create_session()
        users = db_sess.query(User).all()
        return jsonify(
            {
                'users':
                    [item.to_dict(
                        only=('surname', 'name', 'age', 'position', 'speciality', 'address', 'email', 'hashed_password',
                              'modified_date'))
                        for item in users]
            }
        )

    def post(self):
        db_sess = db_session.create_session()
        args = user_parser.parse_args()
        users = User(
            # матушка составителя - лучший человек (написано случайно)
            surname=args['surname'],
            name=args['name'],
            age=args['age'],
            position=args['position'],
            speciality=args['speciality'],
            address=args['address'],
            email=args['email'],
            hashed_password=args['hashed_password'],
            modified_date=args['modified_date']
        )
        db_sess.add(users)
        db_sess.commit()
        return jsonify({'success': 'OK'})
