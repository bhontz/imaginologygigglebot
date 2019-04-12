from microbit import *
from gigglebot import *
import radio

display.show(Image.YES)
radio.on()
radio.config(group=16, power=6)
set_speed(40,40)
while True:
    msg = radio.receive()
    if msg and msg == "up":
        display.show(Image.ARROW_N)       
        drive(BACKWARD, 1000)
    elif msg and msg == "down":
        display.show(Image.ARROW_S)
        drive(FORWARD, 1000)
    elif msg and msg == "left":
        display.show(Image.ARROW_E)
        turn(LEFT, 1000)
    elif msg and msg == "right":
        display.show(Image.ARROW_W)
        turn(RIGHT, 1000)
        
    display.show(Image.HEART)
    sleep(500)
    display.show(Image.HEART_SMALL)
    sleep(500)