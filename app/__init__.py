import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # Configuración de la aplicación
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///miniblog.db')
    app.config['SECRET_KEY'] = 'tu_secret_key_aqui'  # Asegúrate de configurar una clave secreta

    # Inicialización de la base de datos y migraciones
    db.init_app(app)
    migrate.init_app(app, db)

    # Configuración de Flask-Login
    login_manager.init_app(app)
    login_manager.login_view = 'login'  # Asegúrate de tener una vista 'login'

    @login_manager.user_loader
    def load_user(user_id):
        from app.models import Usuario  # Importa tu modelo de Usuario aquí
        return Usuario.query.get(int(user_id))

    # Importar vistas dentro de la función para evitar importaciones circulares
    with app.app_context():
        from app.views.usuario_view import UsuarioView
        from app.views.entrada_view import EntradaView
        from app.views.comentario_view import ComentarioView
        from app.views.categoria_view import CategoriaView

        # Configuración de rutas
        app.add_url_rule('/usuarios/', view_func=UsuarioView.as_view('usuario_view'), methods=['GET', 'POST'])
        app.add_url_rule('/usuarios/<int:user_id>', view_func=UsuarioView.as_view('usuario_detail_view'), methods=['GET', 'PUT', 'DELETE'])

        app.add_url_rule('/entradas/', view_func=EntradaView.as_view('entrada_view'), methods=['GET', 'POST'])
        app.add_url_rule('/entradas/<int:entrada_id>', view_func=EntradaView.as_view('entrada_detail_view'), methods=['GET', 'PUT', 'DELETE'])

        app.add_url_rule('/comentarios/', view_func=ComentarioView.as_view('comentario_view'), methods=['GET', 'POST'])
        app.add_url_rule('/comentarios/<int:comentario_id>', view_func=ComentarioView.as_view('comentario_detail_view'), methods=['GET', 'PUT', 'DELETE'])

        app.add_url_rule('/categorias/', view_func=CategoriaView.as_view('categoria_view'), methods=['GET', 'POST'])
        app.add_url_rule('/categorias/<int:categoria_id>', view_func=CategoriaView.as_view('categoria_detail_view'), methods=['GET', 'PUT', 'DELETE'])

    return app
