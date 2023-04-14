from sqlalchemy.orm import sessionmaker
# 從 utils/tables.py 模組中匯入 User 類別
from utils.tables import User
from utils.connection import connect_db


# 建立資料庫連接
engine = connect_db()

# 建立 Session
Session = sessionmaker(bind=engine)
session = Session()


# 新增一筆資料
new_user = User(username='Adler', email='john@example.com')
session.add(new_user)
session.commit()

# 更新資料
user = session.query(User).filter_by(username='Adler').first()
user.email = 'huadlerben@gmail.com'
session.commit()

# 查詢資料
users = session.query(User).all()
for user in users:
    print(f'User ID: {user.userid}, Name: {user.username}, Email: {user.email}')


# 刪除資料
# user = session.query(User).filter_by(username='John').first()
# session.delete(user)
# session.commit()
