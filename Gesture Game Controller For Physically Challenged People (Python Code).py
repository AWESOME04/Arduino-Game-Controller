import serial                                         #Install Pyserial Packages

from pynput.keyboard import Key, Controller           #Install Pynput Packages

ser = serial.Serial('COM9', 9600)                     #Enter Arduino Port Number

keyboard = Controller()

while True:
    data = ser.readline()
    
    if data.decode().strip() == "LEFT":
        keyboard.press("a")
        keyboard.release("a")
    

    if data.decode().strip() == "RIGHT":
        keyboard.press("d")
        keyboard.release("d")
    

    if data.decode().strip() == "UP":
        keyboard.press("w")
        keyboard.release("w")
    

    if data.decode().strip() == "DOWN":
        keyboard.press("s")
        keyboard.release("s")    
