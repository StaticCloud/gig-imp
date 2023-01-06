from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# load our environmental variables
load_dotenv()

# engine manages connection to the database
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
# generates temporary connections for CRUD operations
Session = sessionmaker(bind=engine)
# base allows us to map models to real MySQL tables
Base = declarative_base()