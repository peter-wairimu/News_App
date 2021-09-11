import os


class Config:
    '''
    General configuration parent class
    '''


    BASE_URL ='https://newsapi.org/v2/top-headlines/sources?apiKey=7d4e000c27af4d38ab95a716258769a8'
    MOVIE_API_KEY ='NEWS_API_KEY'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    




class ProdConfig(Config):
    '''
    Pruduction  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    
    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}