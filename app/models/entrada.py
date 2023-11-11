from app import db

class Entrada(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(140))
    cuerpo = db.Column(db.String(1000))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id', name='fk_usuario_id'))
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id', name='fk_categoria_id'))  # Nombre asignado

    def __repr__(self):
        return f'<Entrada {self.titulo}>'
