from app import app
from flask_script import Shell,Manager
from app import views
import pymysql
from app import db
from app.models import User,Sensor,Sensor_History

#数据库连接配置
pymysql.install_as_MySQLdb()
manager=Manager(app)


def make_shell_context():
    return dict(app=app,db=db,User=User,Sensor=Sensor,Sensor_History=Sensor_History,views=views)
manager.add_command('shell',Shell(make_context=make_shell_context()))
#manager.run()

#项目启动
#我改动了一个注释
#我又改动了
#我又又改动了
app.run(debug=True)
