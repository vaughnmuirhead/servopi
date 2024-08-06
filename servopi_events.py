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
logger.setLevel(logging.INFO)

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

if __name__ == '__main__':
    main()
