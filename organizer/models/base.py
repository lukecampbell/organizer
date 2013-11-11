from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class BaseModel:
    @classmethod
    def create(cls, engine):
        Base.metadata.create_all(bind=engine, tables=[cls.__table__])

    @classmethod
    def drop(cls, engine):
        Base.metadata.drop_all(bind=engine, tables=[cls.__table__])

class Association:
    __tablename__ = 'emails'
    id = Column(Integer, primary_key=True)
    from_type = Column(String, nullable=True)
    from_id = Column(Integer, nullable=True)
    to_type = Column(String, nullable=True)
    to_id = Column(Integer, nullable=True)

