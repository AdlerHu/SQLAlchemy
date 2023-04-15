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
for i, user in enumerate(data):
    session.bulk_insert_mappings(User, [user])
    if (i + 1) % batch_size == 0:
        session.flush()

# 提交事务
session.commit()

# 关闭Session
session.close()