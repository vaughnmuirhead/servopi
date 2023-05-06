import RPi.GPIO as GPIO
import time
import sys
import logging

logger = logging.getLogger(__name__)

logger.debug('Starting script...')

mode = sys.argv[1]
logger.debug(f'Mode is {mode}')

if mode == 'on':
  angle = 108
elif mode == 'off':
  angle = 180
elif mode == 'warmer':
  angle = 103
elif mode == 'lesswarm':
  angle = 90
else:
  angle = 0
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50)

servo1.start(0)
try:
  servo1.ChangeDutyCycle(2+(angle/18))
  time.sleep(0.5)
  servo1.ChangeDutyCycle(0)
  logger.info(f'Mode switched to {mode}.')

except Exception as e:
  logging.info(f'Caught exception: {e}')

finally:
  logging.debug('Cleaning up.')
  servo1.stop()
  GPIO.cleanup()
