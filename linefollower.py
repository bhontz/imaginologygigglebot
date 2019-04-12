"""
    GSOC OC Fairgrounds Imaginology Robotic Line Follower
    Created for the 2019 event April 12/13
"""
from microbit import *
from gigglebot import *

button_a.was_pressed()
button_b.was_pressed()
display.show(Image.YES)
strip = init()
set_speed(40,40)
threshold = 30
lapcounter = 0
while True:
    if button_a.is_pressed() and button_b.is_pressed():
        right, left = read_sensor(LINE_SENSOR, BOTH)
        display.scroll(left)
        display.scroll(right)
        
    if button_a.is_pressed():
        while not button_b.is_pressed():
            right, left = read_sensor(LINE_SENSOR, BOTH)
            if left < threshold and right < threshold:
                strip[2] = (0, 255, 0)
                strip[8] = (0, 255, 0)
                strip.show()
                drive(FORWARD)
            elif right > threshold and left > threshold:
                stop()
                lapcounter = lapcounter + 1
                for i in range(0, 5):
                    drive(BACKWARD, 100)
                    set_smile(R=100,G=0,B=0)
                    sleep(500)
                    drive(FORWARD, 100)
                    set_smile(R=0,G=100,B=0)
                    sleep(500)
                    drive(BACKWARD, 100)
                    set_smile(R=0,G=0,B=100)
                    sleep(500)
                    drive(FORWARD, 100)
                set_smile(R=0,G=0,B=0)
                drive(FORWARD, 500)
                display.scroll(lapcounter)
            elif left > threshold and right < threshold:
                strip[2] = (0, 255, 0)
                strip[8] = (0, 0, 0)
                strip.show()
                turn(RIGHT)
            elif right > threshold and left < threshold:
                strip[2] = (0, 0, 0)
                strip[8] = (0, 255, 0)
                strip.show()
                turn(LEFT)
        stop()
        strip[2] = (0,0,0)
        strip[8] = (0,0,0)
        display.show(Image.YES)
        