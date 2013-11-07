from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel:
    @classmethod
    def create(cls, engine):
        Base.metadata.create_all(bind=engine, tables=[cls.__table__])

    @classmethod
    def drop(cls, engine):
        Base.metadata.drop_all(bind=engine, tables=[cls.__table__])

