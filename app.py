from flask_script import Manager
from apps import create_app

app = create_app() 
manager = Manager(app) # 给app套了一个壳子

if __name__=='__main__':
    manager.run()