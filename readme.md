# Analogue thermostat smart conversion

This project uses a 3d printed linear actuator apparatus, a raspberry pi and a servo to convert an analogue thermostat to a smart thermostat.

- Download and 3d print the following
    - linear actuator apparatus here: https://www.tinkercad.com/things/b8V2VNzX3zA-linearactuator
    - Power bank holder https://www.tinkercad.com/things/3N6urT88Hxt

- Get the following parts
    - Servo https://core-electronics.com.au/df05bb-standard-servo-5kg.html
    - Rasperry pi zero wh https://core-electronics.com.au/catalogsearch/result/?q=pi+zero+wh
    - SD card https://core-electronics.com.au/sd-microsd-memory-card-16gb-class-10.html
    - Jumper wires https://core-electronics.com.au/jumper-wires-7-8-f-m-high-quality-30-pack.html
    - Micro USB cable https://core-electronics.com.au/micro-usb-cable.html
    - USB power bank https://core-electronics.com.au/usb-power-bank-fast-charge-30000mah.html

- Setup your Raspberry pi with the pi os https://www.raspberrypi.com/documentation/computers/getting-started.html#using-raspberry-pi-imager
- Get your pi connected to wifi https://www.raspberrypi-spy.co.uk/2017/04/manually-setting-up-pi-wifi-using-wpa_supplicant-conf/
- Wire up the servo to the gpio pins on your pi. Diagram here https://www.raspberrypi-spy.co.uk/2012/06/simple-guide-to-the-rpi-gpio-header-and-pins/)
    - Red to +5v board pin 2
    - Orange to board pin 11
    - Black to ground board pin 6
- Clone this git repo to your pi user home directory
- Download the ssh button app for your Android phone https://play.google.com/store/apps/details?id=com.pd7l.sshbutton&hl=en_AU&gl=US
    - Configure a new ssh button to run the servo.py script with each of the following commands:
        ``` ssh
         python servopi/servo.py on
         python servopi/servo.py off
         python servopi/servo.py warmer
        ```
- You may need to calibrate the angle of the servo for your particular thermostat and temperature preferances. Just modify the servo.py script angle variables to an angle between 0 and 180.
- Stick the apparatus to the wall with double sided mounting tape https://www.bunnings.com.au/moroday-6mm-x-10m-grey-double-sided-body-mounting-tape_p0057719?store=6037
- stick the battery holder to the wall with the same tape and put the battery in.
- Plug in your pi and enjoy!