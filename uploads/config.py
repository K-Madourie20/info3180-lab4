import os

class Config(Object):
    DEBUG = False
    SECRET_KEY= os.environ.get('SECRET_KEY') or 'MyP@ssw0rd123'
    ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME') or 'admin'
    ADMIN_PASSWORD = 0s.environ.get('ADMIN_PASSWORD') or 'Password123'
    UPLOAD_FOLDER = ("./app/static/uploads")


    class DevelopmentConfig(Config):
        DEVELOPMENT = True
        DEBUG =True

    class ProductionConfig(Config):
        DEBUG = False
