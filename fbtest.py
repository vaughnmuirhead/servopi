import firebase_admin
import time
from firebase_admin import credentials
# Import database module.
from firebase_admin import db
cred = credentials.Certificate("servopi-7957-firebase-adminsdk-i9z6y-dfbe85274f.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://servopi-7957-default-rtdb.firebaseio.com'
})

def heater_event_listener(event):
    print(event.data)

db.reference('/testobj').listen(heater_event_listener)

ref = db.reference('/testobj')
# dev_ref = ref.child('device_update')

import uuid

# get Current state of
#state = ref.get()
onoff = True

while True:
    onoff = not onoff
    nonce = uuid.uuid4().hex
    ref.update({
        "device_update": nonce,
        "TemperatureControl/temperatureSetpointCelsius": 18,
        "OnOff/on": onoff
        })
    time.sleep(3)
