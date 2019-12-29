__all__ = ['configure_app']








class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "secret_key"
    USER = "root"
    PASSWORD = "root123"
    DATABASE_NAME = "inventory"
    HOST = "localhost"

class Production_config(Config):
    pass

class Development_config(Config):
    DEBUG = True

class Testing_config(Config):
    TESTING = True




