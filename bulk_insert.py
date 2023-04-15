from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import pandas as pd
from utils.tables import User
from utils.connection import connect_db


# 创建数据库连接
engine = connect_db()

# 创建Session
Session = sessionmaker(bind=engine)
session = Session()

# 模拟生成一批数据
data = []
for i in range(10500):
    user = {'username': f'user_{i}', 'email': f'user_{i}@example.com'}
    data.append(user)

# 每累积10000条数据，执行一次批量插入
batch_size = 10000
for i in range(0, len(data), batch_size):
    batch = data[i:i+batch_size]
    session.bulk_insert_mappings(User, batch)
    session.commit()

# 剩余的数据不足批量插入的数量时，使用单独插入
if len(data) % batch_size > 0:
    remaining_batch = data[len(data) - len(data) % batch_size:]
    session.bulk_insert_mappings(User, remaining_batch)
    session.commit()
