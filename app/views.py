from app import app
from flask import render_template,redirect,flash,url_for,session,request
from .form import LoginForm,AddSensorForm,EditSensorForm
from  app.models import User,Sensor,Sensor_History
from app import db
from flask import jsonify
from flask import request,abort
#import xlwt
import random

#登录路由
@app.route('/',methods=['GET','POST'])
@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        name=form.User.data
        password=form.password.data
        user=User.query.filter_by(name=name).first()
        #print(user.password)
        if user is None:
            flash('对不起，此用户不存在')
        if user.password == password :
            return redirect(url_for('SensorHistory'))
            #return render_template('glzx.html')
        else:
            flash('对不起，邮箱或密码错误')
        #flash('消息','flag')
    return render_template('login.html',t='登录界面',form=form)

#系统借入借出管理路由
@app.route('/Sensorhistory',methods=['GET','POST'])
def SensorHistory():
    page = request.args.get('page', type=int, default=1)
    query = Sensor_History.query.filter_by()
    paginate = query.order_by(Sensor_History.id.desc()).paginate(page=page, per_page=10, error_out=False)

    return render_template('glzx.html', paginate=paginate)

#接受传感器数据的路由
@app.route('/sensor/<int:sid>/data',methods=['GET','POST'])
def data(sid):
    sensor=Sensor.query.filter_by(id=sid).first()
    if sensor is None:
        return jsonify({'status':404, 'info':'找不到你的设备'})
    if request.json is None:
        return jsonify({'status': 404, 'info': '找不到你的数据'})
    if 'data' not in request.json.keys():
        return jsonify({'status': 404, 'info': '没有上传数据成功'})
    data_history=request.json.get('data')
    for i in data_history:
        print(i)
    sensor_history=Sensor_History()
    sensor_history.SensorName=sensor.SensorName
    sensor_history.SensorTime=data_history[1]
    sensor_history.SensorOP=data_history[0]
    sensor_history.sensor_id=sensor.id
    if data_history[0]=='归还':
        sensor.SensorState=1
    else:
        sensor.SensorState=0
    db.session.add_all([sensor_history,sensor])
    db.session.commit()
    return jsonify({'status': 200,'info':'OK'})

#设备信息管理路由
@app.route('/Sensornews',methods=['GET','POST'])
def SensorNews():
    page = request.args.get('page', type=int, default=1)
    query = Sensor.query.filter_by()
    paginate = query.order_by(Sensor.id.desc()).paginate(page=page, per_page=5, error_out=False)

    return render_template('sensor.html',paginate=paginate)

#增加设备
@app.route('/add_sensor',methods=['GET','POST'])
def AddSensor():
    form=AddSensorForm()
    if form.validate_on_submit():
        sensor=Sensor()
        sensor.SensorName=form.SensorName.data
        sensor.SensorState=form.SensorState.data
        db.session.add(sensor)
        db.session.commit()
        return redirect(url_for('.SensorNews'))
    return render_template('add_sensor.html',form=form)


#删除设备
@app.route('/delete_sensor',methods=['GET','POST'])
def Delete_sensor():
    sid=request.args.get('sid')
    if sid is None:
        print('此设备ID不存在')
    sensor=Sensor.query.filter_by(id=sid).first()
    if sensor is None:
        print('此设备不存在')
    db.session.delete(sensor)
    db.session.commit()
    return redirect(url_for('SensorNews'))

#修改设备
@app.route('/edit_sensor',methods=['GET','POST'])
def Edit_sensor():
    sid = request.args.get('sid')
    if sid is None:
        print('此设备ID不存在')
    sensor=Sensor.query.filter_by(id=sid).first()
    if sensor is None:
        print('此设备不存在')
    form = EditSensorForm()
    if form.validate_on_submit():
        sensor.SensorName = form.SensorName.data
        sensor.SensorState = form.SensorState.data
        db.session.add(sensor)
        db.session.commit()
        return redirect(url_for('.SensorNews'))
    form.SensorName.data=sensor.SensorName
    form.SensorState.data=sensor.SensorState
    return render_template('edit_sensor.html', form=form)