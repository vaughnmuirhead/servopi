"""Servopi Google Home Event Service"""
import logging
import time
import firebase_admin
from firebase_admin import credentials
# Import database module.
from firebase_admin import db
import servo

logging.basicConfig(level=logging.NOTSET,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logger.info('Starting servopi event listener service...')

cred = credentials.Certificate("servopi-7957-firebase-adminsdk-i9z6y-dfbe85274f.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://servopi-7957-default-rtdb.firebaseio.com'
})

def main():
    """Main function"""
    # create database doc event listener
    db.reference('/heater').listen(heater_event_listener)
    while True:
        logger.info('Listening for events...')
        time.sleep(5)

def heater_event_listener(event):
    """Handle database doc events"""
    logger.debug(event.data)
    if "on" in event.data:
        logger.info("Event received: %s", event.data)
        heater_state = event.data['on']
        if heater_state is True:
            logger.info("Heater True state recieved.")
            servo.handle_action("on")
        elif heater_state is False:
            logger.info("Heater False state recieved.")
            servo.handle_action("off")

    if "temperatureSetpointCelsius" in event.data:
        temp = event.data['temperatureSetpointCelsius']['temperature']
        logger.info("Received temperature set event: %s", temp)
        mode = get_mode(temp)
        if mode is not None:
            logger.info("Mode mapped to %s", mode)
            servo.handle_action(mode)

def get_mode(temp):
    """Maps temperataure input to device modes."""
    mode = None

    if temp < 17:
        mode = 'down'
    elif temp == 17:
        mode = 'lesswarm'
    elif temp == 18:
        mode = 'on'
    elif temp == 19:
        mode = 'warmer'
    elif temp >=20:
        mode = 'up'

    return mode

if __name__ == '__main__':
    main()
