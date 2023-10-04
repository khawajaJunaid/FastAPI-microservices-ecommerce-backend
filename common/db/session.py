from common.config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from common.db.base import Base
import time

DATABASE_URL = Config.DATABASE_URL
MAX_RETRIES = 3  # Maximum number of retry attempts
RETRY_DELAY = 5  # Delay between retry attempts (in seconds)


def create_database_engine():
    return create_engine(DATABASE_URL)


def connect_to_database():
    for retry_attempt in range(MAX_RETRIES):
        try:
            engine = create_database_engine()
            Base.metadata.create_all(engine)
            SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
            return SessionLocal()
        except Exception as e:
            print(
                f"Database connection attempt {retry_attempt + 1} failed. Error: {str(e)}"
            )
            if retry_attempt < MAX_RETRIES - 1:
                print(f"Retrying in {RETRY_DELAY} seconds...")
                time.sleep(RETRY_DELAY)
            else:
                raise


# Dependency
def get_db():
    db = None
    try:
        db = connect_to_database()
        yield db
    finally:
        db.close()
