from app import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    entradas = db.relationship('Entrada', backref='autor', lazy='dynamic')

    def __repr__(self):
        return f'<Usuario {self.username}>'
