from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_
# 從 utils/tables.py 模組中匯入 User 類別
from utils.tables import User
from utils.connection import connect_db


# 建立資料庫連接
engine = connect_db()

# 建立 Session
Session = sessionmaker(bind=engine)
session = Session()


# 新增一筆資料
# new_user = User(username='Adler', email='john@example.com')
# session.add(new_user)
# session.commit()

# 更新資料
# user = session.query(User).filter_by(username='Adler').first()
# user.email = 'huadlerben@gmail.com'
# session.commit()


# 執行複雜的 SELECT 查詢
# 查詢 username 為 'Adler'，且 email 為 'john@example.com' 或 'huadlerben@gmail.com' 的 User 記錄
users = session.query(User).filter(
    and_(User.username == 'Adler', or_(User.email == 'john@example.com', User.email == 'huadlerben@gmail.com'))
).all()

# 查詢資料
for user in users:
    print(f'User ID: {user.userid}, Name: {user.username}, Email: {user.email}')


# 刪除資料
# user = session.query(User).filter_by(username='John').first()
# session.delete(user)
# session.commit()

session.close()