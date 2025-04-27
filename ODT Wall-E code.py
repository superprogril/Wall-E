from machine import Pin, PWM
import time
import random
neck_base = PWM(Pin(19)) #neck 1
neck_stretch = PWM(Pin(23)) #neck 2
eyes_horizontal = PWM(Pin(4)) #eyes pt 1
eyes_vertical = PWM(Pin(14)) #eyes pt 2
arm = PWM(Pin(5)) #arm

sens = Pin(27, Pin.IN)

en = PWM(Pin(15)) #configuring dc motor
eb = PWM(Pin(18))
IN1 = Pin(12, Pin.OUT) #left wheel
IN2 = Pin(13, Pin.OUT) #" "
IN3 = Pin(32, Pin.OUT) #right wheel
IN4 = Pin(33, Pin.OUT) #" "

#setting dc motor frequencies
en.freq(1000)
en.duty(1023)
eb.freq(1000)
eb.duty(1023)

neck_base.freq(50)
neck_stretch.freq(50)
eyes_horizontal.freq(50)
eyes_vertical.freq(50)
arm.freq(50)

# define function of dc motors
def clockwise(): #wheel 1
    IN1.value(1)
    IN2.value(0)
def anticlockwise(): #wheel 1
    IN1.value(0)
    IN2.value(1)

def clockwise2(): #wheel 2
    IN3.value(1)
    IN4.value(0)

def anticlockwise2(): #wheel 2
    IN3.value(0)
    IN4.value(1)

def stop_motors(): #pause all motors
    IN1.value(0)
    IN2.value(0)
    IN3.value(0)
    IN4.value(0)

#defining first action
def wave():
    arm.duty(30)
    time.sleep(0.5)
    arm.duty(85)
    time.sleep(0.5)

# Combined function to move both neck servos simultaneously
def neck_action():
    # Generate random values for both servos
    x = random.randint(25, 50)
    x1 = random.randint(25, 40)

    y = random.randint(25, 50)
    y1 = random.randint(25, 40)

    #Move both servos to first position simultaneously
    neck_base.duty(x)
    neck_stretch.duty(y)
    time.sleep(1)

    #Move both servos to second position simultaneously
    neck_base.duty(x1)
    neck_stretch.duty(y1)
    time.sleep(1)

while True:
    # Read the sensor value
    value_of_sensor = sens.value()
    print(value_of_sensor)

    if value_of_sensor == 1:
        wave()
        print("hello!")
        wave()
        time.sleep(1)

        clockwise()
        clockwise2()
        time.sleep(1)

        anticlockwise()
        anticlockwise2()
        time.sleep(1)

        stop_motors()
        time.sleep(1)

        neck_action()  #Run combined neck movement
        print("how are you today?")
        time.sleep(1)

        clockwise()
        anticlockwise2()
        stop_motors()
        neck_action()  #Run combined neck movement again
        wave()
        clockwise()
        print("wow")
        time.sleep(2)
        print("i really like these things called...plants!")
        stop_motors()

        clockwise()
        wave()
        stop_motors()
        print("thank you! Take care of yourself")
        anticlockwise2()
        clockwise2()
        stop_motors()

    time.sleep(0.2)
