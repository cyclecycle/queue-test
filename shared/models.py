from sqlalchemy import Column, Integer, String, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    query = Column(String, index=True)
    fetched_data = Column(String)  # Simplified for example purposes
    processed_data = Column(String)
    processed = Column(Boolean, default=False)
