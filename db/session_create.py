"""this is create session for connect data base."""

from config import CONNECTION_FOR_ENGINE

from models.db import db

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine(CONNECTION_FOR_ENGINE)
Session = sessionmaker(bind=engine)

session: Session = Session()
