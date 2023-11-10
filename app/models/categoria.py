from app import db

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True)
    entradas = db.relationship('Entrada', backref='categoria', lazy='dynamic')

    def __repr__(self):
        return f'<Categoria {self.nombre}>'
