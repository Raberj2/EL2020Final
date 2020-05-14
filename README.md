# EL2020Final<br />
Repository for Embedded Linux Final Project<br />
Jared Raber<br />
Joshua Raber<br />
Haley Rosenblatt Niggl<br />

## Prerequisite installations:<br />

## Circuit Description:<br />

## Software Description:<br />
This section will describe the diffent pieces of software and how they work together in order to produce a functioning design. The two major pieces of code are in detec.py and flaskServer.py:<br />
  ###### detec.py:<br />
  This python script handles the detection, logging, and vocalization of sensors, and it's subsequential data. Data is logged                in a database located in the logs/ directory from the applications root directory in the sensor.db file. When this script is            active, a single touch on the digital touch sensor wil activate the system. Each time a sensor activates, it will log the                data and play a sound on the speaker to alert that a sensor has been triggered. This script also waits detects if the system            is deactivated from the flaskServer.py<br />
  ###### flaskServer.py:<br />
   flaskServer.py handles a lot of the other processes that goes on in this project. It handles the webserver hosting, data                displaying, deactivation, and log in and registration system. Starting with the login and registration system, this is done              using various html files in the tempates/ directory, including login.html and register.html, as well as assistance from                  models.py which gets imported as dbHandler. <br />
           
 ###### models.py:<br />


Workload Breakdown:<br />
