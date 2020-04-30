import serial
import MySQLdb

db  =  MySQLdb . connect (
     host = "#" ,     #主機名
     user = "#" ,          #用戶名
     passwd = "#" ,   #密碼
     db = "#" )         #數據庫名稱

ser = serial.Serial("COM4", 9600, timeout=1)
s = ser.read(10)
data = ser.readline().decode()
while 1:
    print(data)
