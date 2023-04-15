from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import aliased
from sqlalchemy.sql import exists

# 建立資料庫連線及 Session
engine = create_engine('mysql://username:password@localhost/dbname')
Session = sessionmaker(bind=engine)
session = Session()

# 定義 User 資料模型
class User(Base):
    __tablename__ = 'users'
    userid = Column(Integer, primary_key=True)
    username = Column(String(20))
    email = Column(String(50))
    orders = relationship('Order', back_populates='user')

# 定義 Order 資料模型
class Order(Base):
    __tablename__ = 'orders'
    orderid = Column(Integer, primary_key=True)
    status = Column(String(20))
    user_id = Column(Integer, ForeignKey('users.userid'))
    user = relationship('User', back_populates='orders')

# 建立子查詢，查詢所有至少擁有一筆 Order 的 User 的 userid
subquery = session.query(Order.user_id).distinct()

# 使用子查詢進行主查詢，查詢所有擁有至少一筆 Order 的 User
users = session.query(User).filter(User.userid.in_(subquery)).all()
