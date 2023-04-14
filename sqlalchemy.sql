CREATE TABLE `users` (
  `userid` int NOT NULL AUTO_INCREMENT,
  `username` varchar(20),
  `email` varchar(50),
  PRIMARY KEY (`userid`)
);

-- 建立一個 user 'sqlalchemy'，只給他操作 test_sqlalchemy 這個資料庫的權限
CREATE USER 'sqlalchemy'@'%' IDENTIFIED BY 'test';
GRANT ALL PRIVILEGES ON test_sqlalchemy.* TO 'sqlalchemy'@'%';
