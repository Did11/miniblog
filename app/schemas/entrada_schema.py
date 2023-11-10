from marshmallow import Schema, fields

class EntradaSchema(Schema):
    id = fields.Int(dump_only=True)
    titulo = fields.Str(required=True)
    cuerpo = fields.Str(required=True)
    usuario_id = fields.Int(load_only=True)

entrada_schema = EntradaSchema()
entradas_schema = EntradaSchema(many=True)