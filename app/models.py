from app import db

#管理员用户数据表
class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64))#用户名
    password=db.Column(db.String(64))#密码

#设备信息数据表
class Sensor(db.Model):
    __tablename__='sensors'
    id=db.Column(db.Integer,primary_key=True)
    SensorName=db.Column(db.String(128))#设备名
    SensorState=db.Column(db.Boolean,default=False)#设备借阅状态
    Sensor_historys=db.relationship('Sensor_History',backref='sensor')#反向关系

#设备历史数据表
class Sensor_History(db.Model):
    __tablename__='sensor_history'
    id=db.Column(db.Integer,primary_key=True)
    SensorName=db.Column(db.String(128))#设备名
    SensorOP= db.Column(db.String(128))  # 设备操作
    SensorTime=db.Column(db.String(128))#借出入时间
    sensor_id=db.Column(db.Integer,db.ForeignKey('sensors.id'))#设备的ID，外键关系