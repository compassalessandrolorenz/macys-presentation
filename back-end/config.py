import os
from datetime import timedelta

class Config:
    """Configurações da aplicação"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ai_markethub_secret_key'
    DEBUG = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    
    # Configurações de CORS
    CORS_ORIGINS = ['http://localhost:3000', 'http://127.0.0.1:3000', 'http://localhost:8080', 'http://localhost:5173', 'http://127.0.0.1:5173' 'http://localhost:5174', 'http://127.0.0.1:5174']
    
    # Configurações de token
    TOKEN_EXPIRATION_DAYS = 1
    
    # Configurações de email (simulado)
    EMAIL_ENABLED = True
    EMAIL_FROM = 'noreply@markethub.com'

    # Configurações do SQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
