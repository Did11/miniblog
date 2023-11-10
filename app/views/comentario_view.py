from flask import request, jsonify, abort
from flask.views import MethodView
from app import db
from app.models.comentario import Comentario
from app.schemas.comentario_schema import comentario_schema, comentarios_schema

class ComentarioView(MethodView):

    def get(self, comentario_id=None):
        if comentario_id is None:
            comentarios = Comentario.query.all()
            return jsonify(comentarios_schema.dump(comentarios))
        else:
            comentario = Comentario.query.get_or_404(comentario_id)
            return jsonify(comentario_schema.dump(comentario))

    def post(self):
        data = request.get_json()
        errors = comentario_schema.validate(data)
