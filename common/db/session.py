
from common.config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL =  Config.DATABASE_URL
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
