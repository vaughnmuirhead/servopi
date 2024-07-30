"""servopy module"""

import time
import sys
import logging
from pathlib import Path
try:
    import RPi.GPIO as GPIO
except ImportError as err:
    raise ImportError('Import error') from err

logging.basicConfig(level=logging.NOTSET,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

logger.info('Starting script...')

INCREMENT = 4
state_file = Path(__file__).with_name('servostate.txt')

def main():
    """Main function"""

    mode = sys.argv[1]
    if len(sys.argv) > 2: #  Check for existence of second param representing delay
        logger.info('Delay argument found.')
        delay = int(sys.argv[2])
        logger.info('Sleeping for %s seconds...', delay)
        time.sleep(delay)

    logger.info('Mode is %s.', mode)

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
            logger.info('Servo is already at upper bound: %s', state)
    elif mode == 'down':
        state = get_state()
        if state < 180:
            angle = state + INCREMENT
        else:
            logger.info('Servo is already at lower bound: %s', state)
    else:
        angle = 0

    set_servo(180) # Set servo to 180 first
    set_servo(angle)
    set_state(angle)

def set_servo(angle):
    """Function sets servo angle"""

    logger.info('Moving servo...')

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11,GPIO.OUT)
    servo1 = GPIO.PWM(11,50)
    servo1.start(0)

    try:
        servo1.ChangeDutyCycle(2+(angle/18))
        time.sleep(0.5)
        servo1.ChangeDutyCycle(0)
        logger.info('Mode switched to %s.', angle)

    except Exception as e:
        logger.info('Caught exception: %s', e)

    finally:
        logger.debug('Cleaning up.')
        servo1.stop()
        GPIO.cleanup()

def set_state(state):
    """Set state of servo"""

    logger.info('Setting state: %s', state)
    f = open(state_file, "w", encoding="utf-8")
    f.write(str(state))

def get_state():
    """Get state of servo"""
    f = open(state_file, "r", encoding="utf-8")
    state = f.read()
    logger.info('Returning state: %s', state)
    return int(state)

if __name__ == '__main__':
    main()
