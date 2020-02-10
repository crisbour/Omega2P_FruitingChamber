#! /usr/bin/python

# Importing package
import time
import os
import onionGpio
from temperatureSensor import TemperatureSensor
import oneWire
from datetime import datetime

dayStart=9; dayFinish=21;

oneWireGpio=11
def strTemp(sensor):
	value=sensor.readValue()
	print("T= "+str(value) +" C")

os.system('omega2-ctrl gpiomux set uart1 gpio')
os.system('omega2-ctrl gpiomux set pwm0 pwm')

LampPin=1; FoggerPin=45; StirPin=15;
LampObj=onionGpio.OnionGpio(LampPin)
StirObj=onionGpio.OnionGpio(StirPin)
FoggerObj=onionGpio.OnionGpio(FoggerPin) 

#1-Wire Init
if not oneWire.setupOneWire(str(oneWireGpio)):
	print("Kernel mdule could not be inserted. Try again!")
sensorAddress=oneWire.scanOneAddress()
sensor=TemperatureSensor("oneWire",{"address":sensorAddress,"gpio":oneWireGpio})
if not sensor.ready:
	print("Sensore was not set up correctly.")

os.system('onion pwm 0 0 1000')
LampObj.setOutputDirection(0)
FoggerObj.setOutputDirection(0)
StirObj.setOutputDirection(1)

foggSet=True

now=datetime.now()
if(dayStart<=now.hour<dayFinish):
	dayBool=False
else:
	dayBool=True

print("Current time: "+ now.strftime("%c"));

while True:
	now=datetime.now() 

	if(dayStart<=now.hour<dayFinish):
		LampObj.setOutputDirection(1)
		if(not dayBool):
			print("It's day time!");
			dayBool=True
	else:
		LampObj.setOutputDirection(0)
		if(dayBool):
			print("It's night time!");
			dayBool=False

	if 45<=now.minute<50 and (not foggSet) :
		FoggerObj.setOutputDirection(1)
		StirObj.setOutputDirection(1)
		os.system('onion pwm 0 90 1000')
		print('Misting')
		foggSet=True
	if not(45<=now.minute<50) and foggSet :
		FoggerObj.setOutputDirection(0)
		StirObj.setOutputDirection(0)
		os.system('onion pwm 0 0 1000')
		print('Pause')
		foggSet=False
    		
	if(now.minute%10==0 and now.second==0):
    		strTemp(sensor)
