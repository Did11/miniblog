from marshmallow import Schema, fields

class CategoriaSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)

categoria_schema = CategoriaSchema()
categorias_schema = CategoriaSchema(many=True)