from marshmallow import Schema, fields

class UsuarioSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    # No incluyo el password_hash

usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)