import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from datetime import date

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id=Column(Integer, primary_key=True)
    username=Column(String,unique=True,nullable=False)
    firstname=Column(String,nullable=False)
    lastname=Column(String,nullable=False)
    email=Column(String,unique=True)
    posts = relationship ('posts', backref="users")
    followers = relationship ('followers', backref="users")
    comments= relationship ('coments', backref="users")

class Post(Base):
    __tablename__= "posts"
    id=Column(Integer, primary_key=True)
    title=Column(String(400))
    user_id=Column(Integer, ForeignKey("users.id"))
    media_type=relationship ('medias', backref="posts")
    Comment=relationship ('comments', backref="posts")

class Media(Base):
    __tablename__= "medias"
    id=Column(Integer, primary_key=True)
    type=Column(Enum('imagen','video'))
    url= Column(String(400))
    post_id=Column(Integer,ForeignKey("posts.id"))

class Comment(Base):
    __tablename__="comments"
    id=Column(Integer,primary_key=True)
    comment_text=Column(String(250))
    author_id=Column(Integer, ForeignKey("users.id"))
    post_id=Column(Integer,ForeignKey("posts.id"))

class Follower(Base):
    __tablename__="followers"
    id=Column(Integer, primary_key=True)
    user_from_id=Column(Integer, ForeignKey("users.id"))
    user_to_id=Column(Integer,ForeignKey("users.id"))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e




# Fallower
# -------
# user_from_id integer FK >- User.ID
# user_to_id integer FK >- User.ID

# User
# -----
# ID PK integer
# username string  unique
# firstname string
# lastname string
# email string unique

# Post
# ----
# ID PK integer
# user_id integer FK >- User.ID

# Media
# ------
# ID PK integer
# type enum("imagen","video")
# url string
# post_id int FK >- Post.ID

# Comment
# -----
# ID PK integer
# comment_text string
# author_id integer FK >- User.ID
# post_id integer FK >- Post.ID

# # Direct
# # --
# # ID_chat PK integer
# # mensaje string
# # sender_id integer
# # addressee_id integer