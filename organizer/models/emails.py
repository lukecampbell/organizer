from models.base import Base,BaseModel
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, backref

class Email(Base,BaseModel):
    __tablename__ = 'emails'
    id      = Column(Integer, primary_key = True)
    path    = Column(String)
    subject = Column(String)
    date    = Column(Date)

    thread_topic = Column(String, ForeignKey('threads.topic'))

    thread = relationship('Thread', backref=backref('emails', order_by=id))

    def __init__(self, path, subject, date):
        self.path    = path
        self.subject = subject
        self.date    = date

    def open(self):
        from sh import open as shopen
        shopen(self.path)

