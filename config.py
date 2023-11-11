import os

class Config(object):
    # Configuración de la base de datos
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///minidb.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Clave secreta para la seguridad de la sesión
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # JWT Secret Key (si estás usando JWT)
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')

    # Otras configuraciones
    DEBUG = True  # Activa el modo de depuración para ver errores y mensajes de Flask
    # Más configuraciones según tus necesidades...
