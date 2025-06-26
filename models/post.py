
from email.policy import default
from sqlalchemy import Boolean
from sqlalchemy.orm import declarative_base, Column, 
Base=declarative_base()

class Post(Base):
    __table__name=="posts"
    id=Column(Integer, primanry_key=True)
    title=Column(String,nullable=False)
    body=Column(String,nullable=False)
    is_published=Column(Boolean,default=False)
    author_id=Column(Integer,)