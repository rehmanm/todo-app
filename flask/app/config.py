import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    MAIL_SERVER = os.environ.get("MAIL_SERVER", "smtp.googlemail.com")
    MAIL_PORT = os.environ.get("MAIL_PORT", '587')
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS", 'true').lower() in ['true', 'on', '1']
    MAIL_USER_NAME = os.environ.get("MAIL_USER_NAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_SUBJECT = '[FLASK]'
    MAIL_SENDER = 'No Reply <flask@exmaple.com>'
    FLASK_ADMIN = os.environ.get("FLASK_ADMIN")
 


    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True


class TestConfig(Config):
    TESTING = True
 

class ProductionConfig(Config):
    PRODUCTION=True


config = {
    'development': DevelopmentConfig,
    'testing': TestConfig,
    'production' : ProductionConfig,
    'default': DevelopmentConfig
}