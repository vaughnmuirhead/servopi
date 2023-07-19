import RPi.GPIO as GPIO
import time
import sys
import logging

logger = logging.getLogger(__name__)

logger.debug('Starting script...')

def main():
  mode = sys.argv[1]
  logger.debug(f'Mode is {mode}')

  if mode == 'on':
    logging.info(f'mode received is: {mode}')
    angle = 108
  elif mode == 'off':
    logging.info(f'mode received is: {mode}')
    angle = 180
  elif mode == 'warmer':
    logging.info(f'mode received is: {mode}')
    angle = 103
  elif mode == 'lesswarm':
    logging.info(f'mode received is: {mode}')
    angle = 113
  elif mode == 'up':
    logging.info(f'mode received is: {mode}')
    state = get_state()
    angle = int(state) - 2
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
  f.write(state)

def get_state():
  f = open("servostate.txt", "r")
  state = f.read()
  logging.info(f'Returning state: {state}')
  return state

if __name__ == '__main__':
    main()
