from sqlalchemy import Column, String, Integer
from blask import db

class Post(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(32))
    contents = Column(String())
    def __init__(self, title: str, contents: str):
        self.title = title
        self.contents = contents