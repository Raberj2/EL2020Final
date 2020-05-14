# EL2020Final<br />
Repository for Embedded Linux Final Project<br />
Jared Raber<br />
Joshua Raber<br />
Haley Rosenblatt Niggl<br />

## How to run:<br />
In one putty terminal run detec.py and in another run flaskServer.py. Both scripts are located in the py/ directory.
To login, in web browser, go to the pi address at port 2020. If you do not have a login already you can register a new one. After new user is registered, simply return to the login screen and enter credential then press deactivate.

## Prerequisite installations:<br /

## Circuit Description:<br />
Components Needed: <br />
- Digital Touch Sensor [1]<br />
- Vibration Sensor Module [1]<br />
- Sound Detection Sensor [1]<br />
- HC-SR501 Infrared PIR Motion Sensor Module [1]<br />
- Speaker w/ 3.5mm Audiojack cord [1]<br />

GPIO Extension Board Pin Requirements:<br />
- 3V3<br />
- GND<br />
- GPIO22<br />
- GPIO5<br />
- GPIO26<br />
- GPIO24<br />
- GPIO20<br />
- GPIO21<br />

Also Needed:<br />
- Male-to-Male wires<br />
- Male-to-Female wires<br />

Wiring:<br />

First off, start by attaching the GPIO Extension Board to the breadboard.<br />

Next, let take a male-to-male wire and attach one end into the "+" line of the breadboard, while attaching the other end to the "3V3" Pin on the 
GPIO Extension board. This will act as the voltage line.<br />

Similarly, attach one end of a male-to-male wire in the "-" line of the breadboard, with the other end placed in the "GND" pin on the Extension board.
This will serve as the ground line.<br />

Taking a male-to-male wire, place one end in the GPIO22 pin and place the other end in the GPIO24. The reason for this will be explained in the 
software section.<br />

In seperate breadboard lines, plug in the Digital Touch Sensor, Vibration Sensor, and the Sound Sensor. Leave the Infrared Sensor to the side for now.<br />

On each of the three sensors that were just installed into the breadboard, locate the "GND" pin, and place an end of a male-to-male wire into a connected
pin. [Note: Each GND pin of the board get a separate wire.] The other end of those three wires should be placed in the "-" line where the wire connecting
to GND pin of the Extension board is located.<br />

Likewise, do the same thing for all the VCC pins, but instead of connecting it into the "-" line, connect the VCC pins to "+" line, where the extension
board is connected via the "3V3" pin.<br />

Repeat these last two steps with the Infrared Sensor with the exception of instead of using Male-to-Male wires, use male-to-female wires. Also, it should be noted that if the sensor is upside down, with the leads closer to you, the VCC is the Left lead, and the GND is the Right Lead. The OUT Lead is in the middle.<br />

For the Touch sensor, connect one end of a male-to-male wire to the "SIG" pin, and connect the other end to the "GPIO20" pin.<br />

For the Sound Sensor, connect one end of a male-to-male wire to the "OUT" Pin and the other end to the GPIO5 pin.<br />

For the Vibration Sensor, connect the "DO" pin to GPIO21 with a male-to-male wire.<br />

For the IR Motion Sensor, connect the middle pin to GPIO26 with a male-to-female wire.<br />

## Software Description:<br />
This section will describe the diffent pieces of software and how they work together in order to produce a functioning design. The two major pieces of code are in detec.py and flaskServer.py:<br />
  ###### detec.py:<br />
  This python script handles the detection, logging, and vocalization of sensors, and it's subsequential data. Data is logged                in a database located in the logs/ directory from the applications root directory in the sensor.db file. When this script is            active, a single touch on the digital touch sensor wil activate the system. Each time a sensor activates, it will log the                data and play a sound on the speaker to alert that a sensor has been triggered. This script also waits detects if the system            is deactivated from the flaskServer.py<br />
  ###### flaskServer.py:<br />
   flaskServer.py handles a lot of the other processes that goes on in this project. It handles the webserver hosting, data                displaying, deactivation, and log in and registration system. Starting with the login and registration system, this is done              using various html files in the tempates/ directory, including login.html and register.html, as well as assistance from                  models.py which gets imported as dbHandler. This script is also the deactivation of detec.py, by turning of a port that detec.py turns on in order to run, it stops the sensor detection until the touch sensor is reactivated.<br />
           
 ###### models.py:<br />
  models.py is used exclusively to be imported in flaskServer.py to be used as dbHandler. This script is responsible for managing the database that is used for keeping track of user information in logs/users2.db. This allows the flaskServer.py to handle logins with usernames and passwords that are located on that database file as well as register new users by adding to that file. It also checks if the name being registered already exists on the file in order to prevent duplicate users with the same login information.<br />

## Workload Breakdown:<br />
