from microbit import *
import radio

lstgesture = ["up", "down", "left", "right"]

radio.on()
radio.config(group=16, power=6)
display.show(Image.YES)

while True:
    for g in lstgesture:
        if accelerometer.was_gesture(g):
            radio.send(g)
            display.scroll(g)
            break
    sleep(100)