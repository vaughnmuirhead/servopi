import RPi.GPIO as GPIO
import time
import sys
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logger.debug('Starting script...')

INCREMENT = 4

def main():
  mode = sys.argv[1]
  logger.debug(f'Mode is {mode}')

  if mode == 'on':
    angle = 108
  elif mode == 'off':
    angle = 180
  elif mode == 'warmer':
    angle = 103
  elif mode == 'lesswarm':
    angle = 113
  elif mode == 'up':
    state = get_state()
    if state > INCREMENT:
      angle = state - INCREMENT
    else:
      logger.info(f'Servo is already at upper bound: {state}')
  elif mode == 'down':
    state = get_state()
    if state < 180:
      angle = state + INCREMENT
    else:
      logger.info(f'Servo is already at lower bound: {state}')
  else:
    angle = 0
  
  set_servo(180) # Set servo to 180 first
  set_servo(angle)
  set_state(angle)

def set_servo(angle):
  logger.info(f'Moving servo...')

  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(11,GPIO.OUT)
  servo1 = GPIO.PWM(11,50)
  servo1.start(0)

  try:
    servo1.ChangeDutyCycle(2+(angle/18))
    time.sleep(0.5)
    servo1.ChangeDutyCycle(0)
    logger.info(f'Mode switched to {angle}.')

  except Exception as e:
    logging.info(f'Caught exception: {e}')

  finally:
    logging.debug('Cleaning up.')
    servo1.stop()
    GPIO.cleanup()

def set_state(state):
  logging.info(f'Setting state: {state}')
  f = open("servostate.txt", "w")
  f.write(str(state))

def get_state():
  f = open("servostate.txt", "r")
  state = f.read()
  logging.info(f'Returning state: {state}')
  return int(state)

if __name__ == '__main__':
    main()
