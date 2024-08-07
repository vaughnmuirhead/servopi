# Analogue thermostat smart conversion

This project uses a 3d printed linear actuator apparatus, a raspberry pi and a servo to convert an analogue thermostat to a smart thermostat.

- Download and 3d print the following
  - linear actuator apparatus here: https:/www.tinkercad.com/things/b8V2VNzX3zA-linearactuator
  - Power bank holder <https://www.tinkercad.com/things/3N6urT88Hxt>

- Get the following parts
  - Servo <https://core-electronics.com.au/df05bb-standard-servo-5kg.html>
  - Rasperry pi zero wh <https://core-electronics.com.au/catalogsearch/result/?q=pi+zero+wh>
  - SD card <https://core-electronics.com.au/sd-microsd-memory-card-16gb-class-10.html>
  - Jumper wires <https://core-electronics.com.au/jumper-wires-7-8-f-m-high-quality-30-pack.html>
  - Micro USB cable <https://core-electronics.com.au/micro-usb-cable.html>
  - USB power bank <https://core-electronics.com.au/usb-power-bank-fast-charge-30000mah.html>

- Setup your Raspberry pi with the pi os <https://www.raspberrypi.com/documentation/computers/getting-started.html#using-raspberry-pi-imager>
- Get your pi connected to wifi <https://www.raspberrypi-spy.co.uk/2017/04/manually-setting-up-pi-wifi-using-wpa_supplicant-conf/>
- Wire up the servo to the gpio pins on your pi. Diagram here <https://www.raspberrypi-spy.co.uk/2012/06/simple-guide-to-the-rpi-gpio-header-and-pins/>)
  - Red to +5v board pin 2
  - Orange to board pin 11
  - Black to ground board pin 6
- Clone this git repo to your pi user home directory
- Download the ssh button app for your Android phone <https://play.google.com/store/apps/details?id=com.pd7l.sshbutton&hl=en_AU&gl=US>
  - Configure a new ssh button to run the servo.py script with each of the following commands:

    ```ssh
      # Turn heat on to preset interval
      python3 servopi/servo.py on

      # Turn heat on to lower preset interval
      python3 servopi/servo.py lesswarm

      # Turn heat off
      python3 servopi/servo.py off

      # Turn heat on to higher preset interval
      python3 servopi/servo.py warmer

      # Move the temp up by preset interval
      python3 servopi/servo.py up

      # Move the temp down by preset interval
      python3 servopi/servo.py down

      # Set a delay in seconds before executing the command (this example can be used to set a delay for any other command as well.)
      nohup python3 servopi/servo.py off 3600 >> nohup.out 2>&1 &

    ```

- You may need to calibrate the angle of the servo for your particular thermostat and temperature preferences. Just modify the servo.py script angle variables to an angle between 0 and 180.
- Stick the apparatus to the wall with double sided mounting tape <https://www.bunnings.com.au/moroday-6mm-x-10m-grey-double-sided-body-mounting-tape_p0057719?store=6037>
- stick the battery holder to the wall with the same tape and put the battery in.
- Plug in your pi and enjoy!

## Working on integration with Google Assistant for Google Home voice command control

This make it more complicated but quite a bot cooler. Will try to make sure the simple version still works as well.

- In order to install the needed Google Firebase packages, I found I needed to increase the swap memory size on my raspberry pi as I am using the zero for this project

### Steps to increase swap size

    ```bash
    # Turn off swap
    sudo dphys-swapfile swapoff

    # edit swap config to increase to 2048 (CONF_SWAPSIZE=2048)
    sudo nano /etc/dphys-swapfile

    # Reload swap config
    sudo dphys-swapfile setup

    # Re-enable swap
    sudo dphys-swapfile swapon
    ```

### Installation

#### Firebase setup

* Note: This Google Home integration is a work in progress and basically hacked to work from the Google codelabs smarthome-washer code example. This works now but requires some major cleanup and secure implemenation.

    ```bash
    # These steps basically come from here https://developers.home.google.com/codelabs/smarthome-washer
    cd firebase
    npm install -g firebase-tools
    npm install -g firebase-tools
    firebase login --no-localhost
    firebase use <gcp-project-id>
    firebase init  # Choose Realtime Database, Functions, and Hosting options
    firebase deploy. # Use firebase deploy --only functions if you only want to deploy the functions
    ```
#### pi setup

    ```bash
    # CD to servopi directory
    # install python packages
    pip3 install -r requirements.txt

    # Setup servopi_service
    sudo cp servopi_service.service /etc/systemd/system/

    # Enable the service
    sudo systemctl enable servopi_service

    # Start the service
    sudo systemctl start servopi_service
    ```
