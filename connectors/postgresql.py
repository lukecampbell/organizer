from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def psql_engine(db_name):
    conn_str = 'postgresql+psycopg2://luke@localhost/%s' % db_name
    engine = create_engine(conn_str, echo=True)
    return engine

def psql_session(engine):
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    return session
