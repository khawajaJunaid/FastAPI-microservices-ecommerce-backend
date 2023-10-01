from common.config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from common.db.base import Base

DATABASE_URL = Config.DATABASE_URL
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(engine)


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
