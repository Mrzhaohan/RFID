from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

#生成app对象
app=Flask(__name__)
app.config.from_object('config')#为应用程序设计密钥

#生成bootstrap前端快速渲染对象
bootstrap=Bootstrap(app)

#生成数据库连接对象
db=SQLAlchemy(app)