import RPi.GPIO as IO
import time
IO.setmode(IO.BCM)
IO.setwarnings(False)

sensor_right = 17
IO.setup(sensor_right, IO.IN, pull_up_down=IO.PUD_UP)

sensor_left = 27
IO.setup(sensor_left, IO.IN, pull_up_down=IO.PUD_UP)

IO.setup(7,IO.OUT) # Mortor1 Forward
IO.setup(8,IO.OUT) # Motor 1 Backward

p = IO.PWM(7, 50)
q = IO.pwm(8,50)

p.start(0)
q.start(0)

IO.setup(10.IO.OUT) # Motor2 Forward
IO.setup(9,IO.OUT) # Motor 2 Backward

x = IO.PWM(10,50)
y = IO.PWM(9,50)

x.start(0)
y.start(0)

v = 70 # desired speed
w = 70

while True:
    current_right = IO.input(sensor_right)
    current_left = IO.input(sensor_left)
    print("right sensor: ", current_right, "left sensor: ", current_left)
    if (current_left ==0 and current_right == 0): #both while move foward
        p.ChangeDutyCycle(w)
        x.ChangeDutyCycle(v)
    elif(current_left == 1 and current_right == 0): #turn right
        p.ChangeDutyCycled(w)
        xChangeDutyCycle(0)
    elif(current_left == 0 and current_right == 1): #turn left
        p.ChangeDutyCycle(0)
        x.ChangeDutyCycle(v)
    else: #stay sill
        p.ChangeDutyCycle(0)
        x.ChangeDutyCycle(0)
IO.cleanup()

