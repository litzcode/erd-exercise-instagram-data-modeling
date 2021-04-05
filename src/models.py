import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    uid = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    lastname = Column(String(50))
    username = Column(String(50))
    email = Column(String(50), nullable=False)
    posts = relationship("Post", back_populates="user") # One to Many. One user can have many posts
    comments = relationship("Comment", back_populates="user") # One to Many. One user can have many comments

    # Defining a method inside the class is OPTIONAL
    # The %s operator lets you add a value into a Python string
    def serialize(self):
        return "<User(name='%s', lastname='%s', username='%s')>" % (self.name, self.lastname, self.username)


class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    post_content = Column(String(250), nullable=False)
    date = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey("user.uid")) # One to Many. One user can have many posts
    comments = relationship("Comment", back_populates="post") #One to Many. One post can have many comments


class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    date = Column(String(50), nullable=False)
    author_id = Column(Integer, ForeignKey("user.uid")) # One to Many. One user can have many comments
    post_commented = Column(Integer, ForeignKey("post.id")) #One to Many. One post can have many comments
        

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')