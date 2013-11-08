from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def sqlite_engine(path, echo=True):
    conn_str = 'sqlite:///%s' % path
    engine = create_engine(conn_str, echo=echo)
    return engine

def sqlite_session(engine):
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    return session

