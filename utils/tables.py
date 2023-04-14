from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# 定義資料模型
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    userid = Column(Integer, primary_key=True)
    username = Column(String(20))
    email = Column(String(50))