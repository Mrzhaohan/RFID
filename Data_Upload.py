import serial
import re
import time
from urllib.request import urlopen
import json
import requests

#接受并转化为gbk编码的硬件数据的函数
def get_data():
    s = serial.Serial(port='COM3', baudrate=9600)
    d = {}
    flag = 0
    for i in s:
        #print(i)
        if len(i) > 40:
            b = i.decode('gbk',errors='ignore')
            time=re.findall('txt="(.*)"biao', b)
            ID_card=re.findall('pic 80,60,([0-9])',b)
            time="".join(time)
            ID_card="".join(ID_card)
            SensorState=time[0:2]
            time=time[2:-1]
            if int(ID_card)==0 or int(ID_card)== 1 :
                sensor_name='示波器'
            elif int(ID_card)==2 or int(ID_card)== 3 :
                sensor_name = '显微镜'
            elif int(ID_card) == 4 or int(ID_card) == 5 :
                sensor_name = '稳压电源'
            elif int(ID_card) == 6 or int(ID_card) == 7 :
                sensor_name = '光谱仪'
            print('借出入情况：'+SensorState)
            print('时间:'+time)
            print('设备名称:'+sensor_name)
            sensornew=[SensorState,time,sensor_name]
            return sensornew
        else:
            pass

#数据传输至网站的函数
def upload_data(sen_id, value) :
    header = {'content-type':'application/json'}
    url = 'http://127.0.0.1:5000/sensor/{}/data'
    url = url.format(sen_id)
    d = {'data':value}
    response = requests.post(url, headers=header,  data=json.dumps(d), timeout=1)
    print(response.content)

#程序启动的死循环
while True :
    temp=get_data()
    for i in temp:
        print('1111111')
    if temp[2] == '示波器':
        number=1
    elif temp[2] =='显微镜':
        number=2
    elif temp[2] =='稳压电源':
        number=3
    elif temp[2] =='光谱仪':
        number=4
    upload_data( number, temp)
    #time.sleep(1)




