class Config(object):
    SQLALCHEMY_DATABASE_URI = 'YOUR_DATABASE'
    SECRET_KEY = 'SECRET_KEY'
    

class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    
    
app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': ProductionConfig
}
