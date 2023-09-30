from os import environ

class Config:
    r'''

    Config class for all env variables 
    '''
    DATABASE_URL = environ.get("DATABASE_URL","sqlite:///./test.db")