from flask import Flask, json, jsonify, Response, request

import config
from models import Book
from exts import db
# 转换成json
import myutils
# 跨域
from flask_cors import CORS


app = Flask(__name__)
app.config.from_object(config)

'''可以返回ascII 中文字符'''
app.config['JSON_AS_ASCII'] = False

db.init_app(app)

# 可以进行跨域
# enable CORS
CORS(app)


@app.route('/')
def hello():
    return 'hello'

@app.route('/books')
def getbooks():
    if request.method == 'GET':
        sql = 'select * from vue_books;'
        books = db.session.execute(sql)
        books = Book.query.all()
        books = myutils.to_json(books)
        return jsonify(books)

@app.route('/add', methods=['GET', 'POST'])
def add():
    data = request.get_json()
    author = data['author']
    title = data['title']
    read = data['read']
    book = Book(author=author, title=title, read=read)
    db.session.add(book)
    db.session.commit()
    return jsonify(data)

@app.route('/showbooks/<book_id>')
def get_book(book_id):
    book = Book.query.filter(Book.id == book_id)
    book = myutils.to_json(book)
    return jsonify(book)


@app.route('/editbooks/<book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    data = request.get_json()
    author = data['author']
    title = data['title']
    read = data['read']
    book = Book.query.filter(Book.id == book_id).first()
    book.title = title
    book.author = author
    book.read = read
    db.session.commit()
    book = Book.query.filter(Book.id == book_id)
    book = myutils.to_json(book)
    return jsonify('success')

@app.route('/delete/<book_id>', methods=['GET', 'POST'])
def delete_book(book_id):
    book = Book.query.filter(Book.id == book_id).first()
    db.session.delete(book)
    db.session.commit()
    return jsonify('删除博客成功')


# 测试接口
@app.route('/ping')
def ping():
    return jsonify('ping')



if __name__ == "__main__":
    app.run()