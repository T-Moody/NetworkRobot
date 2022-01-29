import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


# Motor class for initializing the motors.
class Motor():
    # __init__ takes in GPIO pin numbers and sets them up
    # as outputs.
    def __init__(self, EnaA, In1A, In2A, EnaB, In1B, In2B):
        self.EnaA = EnaA
        self.In1A = In1A
        self.In2A = In2A
        self.EnaB = EnaB
        self.In1B = In1B
        self.In2B = In2B
        GPIO.setup(self.EnaA, GPIO.OUT)
        GPIO.setup(self.In1A, GPIO.OUT)
        GPIO.setup(self.In2A, GPIO.OUT)
        GPIO.setup(self.EnaB, GPIO.OUT)
        GPIO.setup(self.In1B, GPIO.OUT)
        GPIO.setup(self.In2B, GPIO.OUT)

        # Set frequency to 100 and set duty cycle to 0.
        self.pwmA = GPIO.PWM(self.EnaA, 100)
        self.pwmA.start(0)
        self.pwmB = GPIO.PWM(self.EnaB, 100)
        self.pwmB.start(0)

    # Takes in a speed and a time and moves motors forward.
    def move(self, speed=0.5, turn=0, time=0):

        # Convert values to pwm values.
        speed *= 100
        turn *= 100
        left_speed = speed - turn
        right_speed = speed + turn

        # Set min value to -100 and Max to 100.
        if left_speed > 100:
            left_speed = 100
        elif left_speed < -100:
            left_speed = -100
        if right_speed > 100:
            right_speed = 100
        elif right_speed < -100:
            right_speed = -100

        # Set speed on motors.
        self.pwmA.ChangeDutyCycle(abs(left_speed))
        self.pwmB.ChangeDutyCycle(abs(right_speed))

        # Set direction of turn.
        if left_speed > 0:
            GPIO.output(self.In1A, GPIO.HIGH)
            GPIO.output(self.In2A, GPIO.LOW)
        else:
            GPIO.output(self.In1A, GPIO.LOW)
            GPIO.output(self.In2A, GPIO.HIGH)
        if right_speed > 0:
            GPIO.output(self.In1B, GPIO.HIGH)
            GPIO.output(self.In2B, GPIO.LOW)
        else:
            GPIO.output(self.In1B, GPIO.LOW)
            GPIO.output(self.In2B, GPIO.HIGH)

        sleep(time)

    # Sets duty cycle to 0 to stop motors.
    def stop(self, time=0):
        self.pwmA.ChangeDutyCycle(0)
        self.pwmB.ChangeDutyCycle(0)
        sleep(time)


def main():
    motor1.move(0.6, 0, 1)
    motor1.stop(1)


if __name__ == '__main__':
    motor1 = Motor(2, 3, 4, 22, 17, 27)
    main()
