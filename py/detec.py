#Libraries
import RPi.GPIO as GPIO
import time
import sqlite3 as sql
import os
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN) #touch
GPIO.setup(5, GPIO.IN) #sound
GPIO.setup(21, GPIO.IN) #vibration
GPIO.setup(26, GPIO.IN) #Infrared
GPIO.setup(22, GPIO.IN)
GPIO.setup(24, GPIO.OUT)

onState = False
vibrationState = False
soundState = False
infState = False

def deactivate():
	vibrationState = False
	soundState = False
	infState = False
	GPIO.output(24, False)
	print("System is now offline")
	subprocess.call(['flite','-voice','slt','-t',"System is now Offline"])

try:
	con = sql.connect("../logs/sensor.db")
	cur = con.cursor()
	GPIO.output(24, False)
	while True:
		if GPIO.input(20) == True:
			print("System on")
			time.sleep(1)
			cur.execute("INSERT INTO sensor (Date, Sensor) VALUES (?,?)", (time.strftime("%Y-%m-%d %H:%M:%S"),"Touch Sensor"))
			con.commit()
			vibrationState = True
			soundState = True
			infState = True
			GPIO.output(24, True)
			subprocess.call(['flite','-voice','slt','-t',"System is now Active"])
			time.sleep(2)

		if GPIO.input(22) == True:
			if GPIO.input(21) == True:
#				vibrationState = False
				print("Vibration Detected")
				cur.execute("INSERT INTO sensor (Date, Sensor) VALUES (?,?)", (time.strftime("%Y-%m-%d %H:%M:%S"),"Vibration Sensor"))
                        	con.commit()
				time.sleep(.5)
				subprocess.call(['flite','-voice','slt','-t',"Vibration Sensor Tripped"])
				time.sleep(2)
			if GPIO.input(5) == True:
#				soundState = False
				print("Sound Detected")
                                cur.execute("INSERT INTO sensor (Date, Sensor) VALUES (?,?)", (time.strftime("%Y-%m-%d %H:%M:%S"),"Sound Sensor"))
                                con.commit()
				time.sleep(.5)
				subprocess.call(['flite','-voice','slt','-t',"Sound Has Been Detected"])
				time.sleep(5)
			if GPIO.input(26) == True:
#				infState = False
				print("Infrared Motion Detected")
                                cur.execute("INSERT INTO sensor (Date, Sensor) VALUES (?,?)", (time.strftime("%Y-%m-%d %H:%M:%S"),"IR Motion Sensor"))
                                con.commit()
				time.sleep(.5)
				subprocess.call(['flite','-voice','slt','-t',"Infra red motion sensor has been tripped"])
				time.sleep(2)
except KeyboardInterrupt:
	pass
	GPIO.cleanup()
	con.close()
