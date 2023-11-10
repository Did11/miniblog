from flask import request, jsonify, abort
from flask.views import MethodView
from app import db
from app.models.categoria import Categoria
from app.schemas.categoria_schema import categoria_schema, categorias_schema

class CategoriaView(MethodView):

    def get(self, categoria_id=None):
        if categoria_id is None:
            categorias = Categoria.query.all()
            return jsonify(categorias_schema.dump(categorias))
        else:
            categoria = Categoria.query.get_or_404(categoria_id)
            return jsonify(categoria_schema.dump(categoria))

    def post(self):
        data = request.get_json()
        errors = categoria_schema.validate(data)
        if errors:
            abort(400, str(errors))
        categoria = Categoria(**data)
        db.session.add(categoria)
        db.session.commit()
        return jsonify(categoria_schema.dump(categoria)), 201

    def put(self, categoria_id):
        categoria = Categoria.query.get_or_404(categoria_id)
        data = request.get_json()
        errors = categoria_schema.validate(data)
        if errors:
            abort(400, str(errors))
        categoria.nombre = data.get('nombre', categoria.nombre)
        db.session.commit()
        return jsonify(categoria_schema.dump(categoria))

    def delete(self, categoria_id):
        categoria = Categoria.query.get_or_404(categoria_id)
        db.session.delete(categoria)
        db.session.commit()
        return jsonify({}), 204
