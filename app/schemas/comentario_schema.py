from marshmallow import Schema, fields

class ComentarioSchema(Schema):
    id = fields.Int(dump_only=True)
    cuerpo = fields.Str(required=True)
    usuario_id = fields.Int(load_only=True)
    entrada_id = fields.Int(load_only=True)

comentario_schema = ComentarioSchema()
comentarios_schema = ComentarioSchema(many=True)