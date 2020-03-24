#存放数据模型

from exts import db
import pymysql

class Book(db.Model):
    __tablename__ = 'vue_books'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50),nullable=False)
    author = db.Column(db.String(50),nullable=False)
    read = db.Column(db.Boolean,nullable=False)