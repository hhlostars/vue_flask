#管理文件 对数据库操作

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from library import app
from exts import db
from models import Book

manager = Manager(app)

#绑定migrate app db
migrate = Migrate(app, db)

#添加迁移脚本的命令到manager中
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()