import RPi.GPIO as GPIO

class MotorController:
    def __init__(self):
        self.ENA = 22
        self.IN1 = 17
        self.IN2 = 27
        self.ENB = 25
        self.IN3 = 23
        self.IN4 = 24

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)  # Disable GPIO warnings

        GPIO.setup(self.ENA, GPIO.OUT)
        GPIO.setup(self.IN1, GPIO.OUT)
        GPIO.setup(self.IN2, GPIO.OUT)
        GPIO.setup(self.ENB, GPIO.OUT)
        GPIO.setup(self.IN3, GPIO.OUT)
        GPIO.setup(self.IN4, GPIO.OUT)

        self.pwm_A = GPIO.PWM(self.ENA, 100)
        self.pwm_B = GPIO.PWM(self.ENB, 100)
        self.pwm_A.start(0)
        self.pwm_B.start(0)

    def forward(self):
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.HIGH)
        GPIO.output(self.IN4, GPIO.LOW)
        self.pwm_A.ChangeDutyCycle(75)
        self.pwm_B.ChangeDutyCycle(75)

    def backward(self):
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.HIGH)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.HIGH)
        self.pwm_A.ChangeDutyCycle(75)
        self.pwm_B.ChangeDutyCycle(75)

    def left(self):
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.HIGH)
        GPIO.output(self.IN3, GPIO.HIGH)
        GPIO.output(self.IN4, GPIO.LOW)
        self.pwm_A.ChangeDutyCycle(75)
        self.pwm_B.ChangeDutyCycle(75)

    def right(self):
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.HIGH)
        self.pwm_A.ChangeDutyCycle(75)
        self.pwm_B.ChangeDutyCycle(75)

    def stop(self):
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.LOW)
        GPIO.output(self.IN3, GPIO.LOW)
        GPIO.output(self.IN4, GPIO.LOW)
        self.pwm_A.ChangeDutyCycle(0)
        self.pwm_B.ChangeDutyCycle(0)

    def cleanup(self):
        self.pwm_A.stop()
        self.pwm_B.stop()
        GPIO.cleanup()
