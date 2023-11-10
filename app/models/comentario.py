from app import db

class Comentario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cuerpo = db.Column(db.String(500))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    entrada_id = db.Column(db.Integer, db.ForeignKey('entrada.id'))

    def __repr__(self):
        return f'<Comentario {self.cuerpo[:15]}>'
