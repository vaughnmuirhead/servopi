import RPi.GPIO as GPIO
import time
import sys

mode = sys.argv[1]
if mode == 'on':
  angle = 110
elif mode == 'off':
  angle = 180
elif mode == 'warmer':
  angle = 105
else:
  angle = 0
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50)

servo1.start(0)
try:
#  while True:
  #angle = float(input('Enter angle between 0 & 180: '))
  servo1.ChangeDutyCycle(2+(angle/18))
  time.sleep(0.5)
  servo1.ChangeDutyCycle(0)

finally:
  servo1.stop()
  GPIO.cleanup()
