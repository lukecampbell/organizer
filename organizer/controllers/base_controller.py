from sqlalchemy.orm import sessionmaker
from organizer.models.base import Base

class BaseController:
    def __init__(self, engine):
        self.engine = engine
        self.session = self.get_session()
    
    def get_session(self):
        Session = sessionmaker()
        Session.configure(bind=self.engine)
        session = Session()
        return session

    def create_all(self, *tables):
        Base.metadata.create_all(bind=self.engine, tables=tables)

    def drop_all(self, *tables):
        Base.metadata.drop_all(bind=self.engine, tables=tables)
    
