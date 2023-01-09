from app.models import User
from app.db import Session, Base, engine

# drop then create tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)