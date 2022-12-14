# we need to have   Our Separate Database(our engine for our test database)
from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# from typing import List
from main import app
from item.database import Base, get_db

# import databases
import sqlalchemy

# from fastapi import FastAPI


# SQLAlchemy specific code, as with any other app
DATABASE_URL = "sqlite:///./test.db"
# DATABASE_URL = "postgresql://user:password@postgresserver/db"


metadata = sqlalchemy.MetaData()
Base = declarative_base()

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# To assure whenever the test begins the tables dropped and REcreated again
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# As for doc API we may want to Overwrite a  dependency during the testing
# we Don't  dont want the  original depency to run nor any of the sub dependencies it might have
# instead w want to  provide a different dependency   that will be used ondly during tests (Possibly some specific tests)
def override_get_db():

    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db()
