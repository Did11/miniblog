from flask import request, jsonify
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

    def put(self, comentario_id):
        comentario_schema = ComentarioSchema()
        comentario = Comentario.query.get(comentario_id)

        if not comentario:
            return jsonify({"mensaje": "Comentario no encontrado"}), 404

        try:
            datos = comentario_schema.load(request.json)
            for key, value in datos.items():
                setattr(comentario, key, value)
            db.session.commit()
            return comentario_schema.dump(comentario), 200
        except ValidationError as err:
            return err.messages, 400

    def delete(self, comentario_id):
        comentario = Comentario.query.get(comentario_id)

        if not comentario:
            return jsonify({"mensaje": "Comentario no encontrado"}), 404

        db.session.delete(comentario)
        db.session.commit()
        return jsonify({"mensaje": "Comentario eliminado"}), 200