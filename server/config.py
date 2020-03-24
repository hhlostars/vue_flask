# 存放配置文件

import os
import pymysql

DEBUG = True

SECRET_KEY = os.urandom(24)

DB_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/vueflask'

SQLALCHEMY_DATABASE_URI = DB_URI
