import serial

#create the serial port object
try:
    port = serial.Serial('/dev/ttyACM0', 9600,timeout=0.01) #Serial Setting
except:
    print('Serial Error')
    exit()

port.write(b's') #Serial write
_buffer = ''
while  True:
    try:
        msg = port.read(1) #Serial Read 1 คือจำตัวอักษรที่จะอ่าน

        if msg != b'':
            if msg == b'\n': #คำสั่ง printlnของ arduino มันจะพ่วง \r\n ต่อท้ายข้อมูลมาด้วย
                print(_buffer)
                _buffer = '' #
            else:
                _buffer += msg.decode('utf-8')
    except:
        print('Serial Error')
        exit()


    
        