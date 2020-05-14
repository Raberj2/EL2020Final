# EL2020Final<br />
Repository for Embedded Linux Final Project<br />
Jared Raber<br />
Joshua Raber<br />
Haley Rosenblatt Niggl<br />

## How to run:<br />
In one putty terminal run detec.py and in another run flaskServer.py. Both scripts are located in the py/ directory.
To login, in web browser, go to the pi address at port 2020. If you do not have a login already you can register a new one. After new user is registered, simply return to the login screen and enter credential then press deactivate.

## Prerequisite installations:<br />

## Circuit Description:<br />

## Software Description:<br />
This section will describe the diffent pieces of software and how they work together in order to produce a functioning design. The two major pieces of code are in detec.py and flaskServer.py:<br />
  ###### detec.py:<br />
  This python script handles the detection, logging, and vocalization of sensors, and it's subsequential data. Data is logged                in a database located in the logs/ directory from the applications root directory in the sensor.db file. When this script is            active, a single touch on the digital touch sensor wil activate the system. Each time a sensor activates, it will log the                data and play a sound on the speaker to alert that a sensor has been triggered. This script also waits detects if the system            is deactivated from the flaskServer.py<br />
  ###### flaskServer.py:<br />
   flaskServer.py handles a lot of the other processes that goes on in this project. It handles the webserver hosting, data                displaying, deactivation, and log in and registration system. Starting with the login and registration system, this is done              using various html files in the tempates/ directory, including login.html and register.html, as well as assistance from                  models.py which gets imported as dbHandler. This script is also the deactivation of detec.py, by turning of a port that detec.py turns on in order to run, it stops the sensor detection until the touch sensor is reactivated.<br />
           
 ###### models.py:<br />
  models.py is used exclusively to be imported in flaskServer.py to be used as dbHandler. This script is responsible for managing the database that is used for keeping track of user information in logs/users2.db. This allows the flaskServer.py to handle logins with usernames and passwords that are located on that database file as well as register new users by adding to that file. It also checks if the name being registered already exists on the file in order to prevent duplicate users with the same login information.<br />

## Workload Breakdown:<br />
