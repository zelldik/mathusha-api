from flask_restful import Resource, abort
from flask import g, jsonify, request

from keycloak_integration import authenticate
from misc import user_things_generation
from data import db_session
from data.users import User
from data.topics import Topic


class TopicListResource(Resource):
    @staticmethod
    @authenticate
    def get():
        session = db_session.create_session()
        user = session.query(User).filter(User.id == g.user_id).first()
        if not user:
            user = User(
                id=g.user_id
            )
            session.add(user)
            user_things_generation(session, g.user_id)
        res = []
        topics = session.query(Topic).all()
        if topics is None:
            abort(404, message="Topics not found")
        for i in topics:
            d = {
                'id': i.id,
                'name': i.name,
                'image': i.image,
            }
            res.append(d)
        session.commit()
        return jsonify(res)


class TopicDescriptionResource(Resource):
    @staticmethod
    @authenticate
    def get():
        id_ = request.json['id']
        session = db_session.create_session()
        topic = session.query(Topic).filter(Topic.id == id_).first()
        if topic is None:
            abort(404, message=f"Topic with id [{id_}] is not found")
        return jsonify({
            'description': topic.description
        })
