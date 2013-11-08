from models.base import Base,BaseModel
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref

class WunderTask(Base, BaseModel):
    __tablename__ = 'wundertasks'
    id           = Column(String, primary_key=True)
    starred      = Column(Integer)
    completed_at = Column(Date)
    title        = Column(String)
    note         = Column(String)
    list_id      = Column(String, ForeignKey('wunderlists.id'))

    wunderlist = relationship('WunderList', backref=backref('tasks', order_by=id))

class WunderList(Base, BaseModel):
    __tablename__ = 'wunderlists'
    id    = Column(String, primary_key=True)
    title = Column(String)

