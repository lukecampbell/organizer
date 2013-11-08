from organizer.models.base import Base,BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Thread(Base, BaseModel):
    __tablename__ = 'threads'
    topic = Column(String, primary_key = True)

    #emails = relationship("Email", order_by="Email.date", backref="thread")


    def __init__(self, topic):
        self.topic = topic


