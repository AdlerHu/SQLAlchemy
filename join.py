from utils.connection import connect_db
from sqlalchemy.orm import Session
from mymodels import User, Order  # 假設你已經定義了 User 和 Order 這兩個模型

# 建立資料庫連線
engine = connect_db()

# 建立 Session 物件
session = Session(engine)

# 執行 JOIN 查詢
# 查詢 User 和 Order 兩個表格中符合條件的記錄，並將結果放入 User 物件中

# SELECT users.*
# FROM users
# JOIN orders ON users.userid = orders.userid
# WHERE orders.status = 'completed';
users = session.query(User).join(Order, User.userid == Order.userid).filter(Order.status == 'completed').all()

# SELECT users.username
# FROM users
# JOIN orders ON users.userid = orders.userid
# WHERE orders.status = 'completed';
users = session.query(User.username).join(Order, User.userid == Order.userid).filter(Order.status == 'completed').all()



# 使用查詢結果
for user in users:
    print(f"User ID: {user.userid}, Username: {user.username}, Email: {user.email}")

# 關閉 Session
session.close()
