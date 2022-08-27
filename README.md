## DS18B20 Setup
**Wiring to Raspberry Pi**

|DS18B20|Raspberry Pi  |
|--|--|
|GND (Black wire) |Raspberry Pi GND |
|DQ (Yellow wire)|Raspberry Pi GPIO17|
|VDD (Red wire)|Resistor 4,7k ohm|
|Resistor|Raspberry Pi 3v3|

See wiring diagram at Design folder or at Documentation for RL application

**Enable 1-Wire**

 - Open terminal, type `sudo raspi-config`
 - Select *Interfacing Option*
 - Enable *1-Wire*
 - Back to terminal, type `sudo modprobe w1_gpio` then `sudo modprobe w1_therm`
 - Edit config.txt file, type `sudo nano /boot/config.txt`
 - Append new line, and type `dtoverlay=w1-gpio-pullup,gpiopin=17`

**Read Temperature**

 - Change directory to /sys/bus/w1/devices, type `cd /sys/bus/w1/devices`
 - Check the directory using `ls` It should contain folder *28-xxxxxxxxxxxx*
 - Hop into that folder
 - Read the temperature using `cat w1-slave`
 - The YES in the first line indicates CRC check success (Data Valid). The number following t= is the temperature
 
**Script Read Temperature**

Here we are using Python to show the temperature. In the *Script* folder, for DS18B20 there are two Python scripts, one (temperature.py) contains all necessary functions to read temperature for the sensor, another one (maintem.py) contains function to read and some logic to determine health based on body temperature.

**How to Use**

 - Copy the script (maintem.py and temperature.py) to Raspberry Pi. *All the scripts must be put in one folder!*
 - Hold the sensor using one of your hands
 - In Raspberry Pi, run terminal, navigate to where you put the script
 - Run the script by typing `sudo python maintem.py` *Note: this script must be run by the root user*


## Max30102

**Wiring to Raspiberry Pi**
|Max30102|Raspberry Pi  |
|--|--|
|VIN|Raspberry Pi 3v3  |
|GND|Raspberry Pi GND|
|SCL|Raspberry Pi GPIO3|
|SDA|Raspberry Pi GPIO2|
|INT|Raspberry Pi GPIO4|


See wiring diagram at Design folder or at Documentation for RL application

**Enable I2C**

 - Open terminal, type `sudo raspi-config`
 - Select *Interfacing Option*
 - Enable *I2C*
 - Back to terminal, then reboot system `sudo reboot`

**Install Required Python Library**

 - Open terminal, type `sudo apt-get update` then `sudo apt-get install python-smbus python3-smbus python-dev python3-dev i2c-tools` This will install *smbus python library*
 - If that doesn't work, try `sudo apt-get update` then `sudo apt-get install python3-smbus python3-dev i2c-tools`
 - You also need *rpi.gpio module*, if it's not already installed, type `sudo apt-get update` then `sudo apt-get install rpi.gpio`

**Script**

Here we are using Python to read the sensor. All functions that are needed for the sensor to run are inside *Oksi.py* file. Running the file dirrectly will get and show sensor's data. You can also import this to another file to perform more complex logic.

**How to Use**

 - Run terminal and navigate to script folder, type `sudo python Oksi.py`
 - Touch Max30102 using your finger and wait until the program is complete

## Wiring Diagram
![wiring diagram](https://github.com/MuhammadNauvalDwiAfandi/sic-ta-w10/blob/master/Images/Schematic_bb.png)

## Result

After collecting data from sensor, data will be posted to Ubidots

![Ubidots](https://github.com/MuhammadNauvalDwiAfandi/sic-ta-w10/blob/master/Images/Screenshot%202022-08-27%20125554.png)

