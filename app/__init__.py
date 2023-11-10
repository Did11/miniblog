# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.views.usuario_view import UsuarioView
from app.views.entrada_view import EntradaView
from app.views.comentario_view import ComentarioView
from app.views.categoria_view import CategoriaView

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///miniblog.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Configuración de rutas
app.add_url_rule('/usuarios/', view_func=UsuarioView.as_view('usuario_view'), methods=['GET', 'POST'])
app.add_url_rule('/usuarios/<int:user_id>', view_func=UsuarioView.as_view('usuario_detail_view'), methods=['GET', 'PUT', 'DELETE'])

app.add_url_rule('/entradas/', view_func=EntradaView.as_view('entrada_view'), methods=['GET', 'POST'])
app.add_url_rule('/entradas/<int:entrada_id>', view_func=EntradaView.as_view('entrada_detail_view'), methods=['GET', 'PUT', 'DELETE'])

app.add_url_rule('/comentarios/', view_func=ComentarioView.as_view('comentario_view'), methods=['GET', 'POST'])
app.add_url_rule('/comentarios/<int:comentario_id>', view_func=ComentarioView.as_view('comentario_detail_view'), methods=['GET', 'PUT', 'DELETE'])

app.add_url_rule('/categorias/', view_func=CategoriaView.as_view('categoria_view'), methods=['GET', 'POST'])
app.add_url_rule('/categorias/<int:categoria_id>', view_func=CategoriaView.as_view('categoria_detail_view'), methods=['GET', 'PUT', 'DELETE'])

# Importar modelos
from app.models import usuario, entrada, comentario, categoria
