from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField,IntegerField,SubmitField,PasswordField,SelectField
from wtforms.validators import DataRequired,Length

#用户表单
class LoginForm(FlaskForm):
    User=StringField(validators=[DataRequired()],default='用户名')
    password=PasswordField(validators=[DataRequired(),Length(6,64)])
    submit = SubmitField(label='登录')

#设备表单
class AddSensorForm(FlaskForm):
    SensorName=StringField(label='设备名称',validators=[DataRequired()])
    SensorState=SelectField(
        label='设备状态',

        render_kw={'class':'form-control'},
        choices=[(0,'借出'),(1,'归还')],
        default=0,
        coerce=int
                            )
    submit = SubmitField(label='提交')

#编辑设备表单
class EditSensorForm(FlaskForm):
    SensorName=StringField(label='设备名称',validators=[DataRequired()])
    SensorState=SelectField(
        label='设备状态',

        render_kw={'class':'form-control'},
        choices=[(0,'借出'),(1,'归还')],
        default=0,
        coerce=int
                            )
    submit = SubmitField(label='提交')
