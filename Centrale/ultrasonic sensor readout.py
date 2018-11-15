import serial

ser = serial.Serial('COM5', baudrate=19200, timeout=1) #COM port changes over time
afst = []
while 1:
    arduinoData = ser.readline().decode('utf-8')
    afst.append(arduinoData)

    print(arduinoData)
    print(afst)



