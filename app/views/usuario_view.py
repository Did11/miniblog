from flask import request, jsonify, abort
from flask.views import MethodView
from app import db
from app.models.usuario import Usuario
from app.schemas.usuario_schema import usuario_schema, usuarios_schema

class UsuarioView(MethodView):

    def get(self, user_id=None):
        if user_id is None:
            usuarios = Usuario.query.all()
            return jsonify(usuarios_schema.dump(usuarios))
        else:
            usuario = Usuario.query.get_or_404(user_id)
            return jsonify(usuario_schema.dump(usuario))

    def post(self):
        data = request.get_json()
        errors = usuario_schema.validate(data)
        if errors:
            abort(400, str(errors))
        usuario = Usuario(**data)
        db.session.add(usuario)
        db.session.commit()
        return jsonify(usuario_schema.dump(usuario)), 201

    def put(self, user_id):
        usuario = Usuario.query.get_or_404(user_id)
        data = request.get_json()
        errors = usuario_schema.validate(data)
        if errors:
            abort(400, str(errors))
        usuario.username = data.get('username', usuario.username)
        usuario.email = data.get('email', usuario.email)
        # Actualizar otros campos si es necesario
        db.session.commit()
        return jsonify(usuario_schema.dump(usuario))

    def delete(self, user_id):
        usuario = Usuario.query.get_or_404(user_id)
        db.session.delete(usuario)
        db.session.commit()
        return jsonify({}), 204
