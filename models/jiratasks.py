from models.base import Base,BaseModel
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, backref

class JiraTask(Base,BaseModel):
    __tablename__ = 'jiratasks'
    assignee   = Column(String)
    component  = Column(String)
    created    = Column(Date)
    fixversion = Column(String)
    key        = Column(Integer, primary_key=True)
    link       = Column(String)
    parent     = Column(Integer)
    priority   = Column(Integer)
    project    = Column(String)
    reporter   = Column(String)
    resolution = Column(Integer)
    status     = Column(Integer)
    summary    = Column(String)
    title      = Column(String)
    task_type  = Column(Integer)
    updated    = Column(Date)

    def open(self):
        from sh import open as shopen
        shopen(self.link)
