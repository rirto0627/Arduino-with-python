import serial
import MySQLdb

db  =  MySQLdb . connect (
     host = "192.168.1.10" ,     #主機名
     user = "admin_DHT" ,          #用戶名
     passwd = "jihg2689" ,   #密碼
     db = "admin_ArduinoDHT" )         #數據庫名稱
# ser=serial.Serial(" /dev/ttyUSB0", 9600, timeout= 0.5 ) #使用USB連接串行口
# ser=serial.Serial(" /dev/ttyAMA0", 9600, timeout= 0.5 ) #使用樹莓派的GPIO口連接串行
ser = serial.Serial("COM4", 9600, timeout=1)
# winsows系統使用com1口連接串行口
# ser=serial.Serial("com1" , 9600, timeout= 0.5 )
# winsows系統使用com1口連接串行口
# ser=serial.Serial(" /dev/ttyS1 " , 9600, timeout= 0.5 )
# Linux系統使用com1口連接串行口
print(ser.name)
# 打印設備名稱
print(ser.port)
# 打印設備名
#ser.open()
# 打開端口
s = ser.read(10)
# 從端口讀10個字節
# ser.write"hello"
# 向端口些數據
#data = ser.read(20)  # 是讀20個字符
data = ser.readline().decode()
# 是讀一行，以/n結束，要是沒有/n就一直讀，阻塞。
#data = ser.readlines().encode('UTF-8')
while 1:
    print(data)
# 都需要設置超時時間
#ser.baudrate = 9600
# 設置波特率
ser.isOpen()  # 看看這個串口是否已經被打開

ser.close()
# 關閉端口