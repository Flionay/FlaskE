from flask_script import Manager
from apps import create_app
from flask_migrate import Migrate, MigrateCommand
from dao import db
from apps.user.model import User

app = create_app()
manager = Manager(app)  # 给app套了一个壳子，用来添加一些命令行操作，主要是数据库对应

# 命令工具
migrate = Migrate(app=app, db=db)  # 其实可以理解为将app和db交给migrate管理
manager.add_command('db', MigrateCommand)  # 是不是能理解为打开migrate里面的database相关命令行开关

if __name__ == '__main__':
    manager.run()
