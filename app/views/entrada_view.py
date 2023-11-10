from flask import request, jsonify, abort
from flask.views import MethodView
from app import db
from app.models.entrada import Entrada
from app.schemas.entrada_schema import entrada_schema, entradas_schema

class EntradaView(MethodView):

    def get(self, entrada_id=None):
        if entrada_id is None:
            entradas = Entrada.query.all()
            return jsonify(entradas_schema.dump(entradas))
        else:
            entrada = Entrada.query.get_or_404(entrada_id)
            return jsonify(entrada_schema.dump(entrada))

    def post(self):
        data = request.get_json()
        errors = entrada_schema.validate(data)
        if errors:
            abort(400, str(errors))
        entrada = Entrada(**data)
        db.session.add(entrada)
        db.session.commit()
        return jsonify(entrada_schema.dump(entrada)), 201

    def put(self, entrada_id):
        entrada = Entrada.query.get_or_404(entrada_id)
        data = request.get_json()
        errors = entrada_schema.validate(data)
        if errors:
            abort(400, str(errors))
        entrada.titulo = data.get('titulo', entrada.titulo)
        entrada.cuerpo = data.get('cuerpo', entrada.cuerpo)
        db.session.commit()
        return jsonify(entrada_schema.dump(entrada))

    def delete(self, entrada_id):
        entrada = Entrada.query.get_or_404(entrada_id)
        db.session.delete(entrada)
        db.session.commit()
        return jsonify({}), 204
