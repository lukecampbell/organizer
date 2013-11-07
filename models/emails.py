from models.base import Base,BaseModel
from sqlalchemy import Column, Integer, String, Date

class Email(Base,BaseModel):
    __tablename__ = 'emails'
    id      = Column(Integer, primary_key = True)
    path    = Column(String)
    subject = Column(String)
    date    = Column(Date)

    def __init__(self, path, subject, date):
        self.path    = path
        self.subject = subject
        self.date    = date

