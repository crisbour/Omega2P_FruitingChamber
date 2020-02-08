# Importing package
import time
import os
import onionGpio
from temperatureSensor import TemperatureSensor
import oneWire
from datetime import datetime

dayStart=9; dayFinish=6;

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

while True:
	now=datetime.now()

	if(dayStart<=now.hour<dayFinish):
		LampObj.setOutputDirection(1)
	else:
		LampObj.setOutputDirection(0)

	if(0<=now.minute<2):
		FoggerObj.setOutputDirection(1)
		os.system('onion pwm 0 85 1000')
		StirObj.setOutputDirection(1)
	else:
		FoggerObj.setOutputDirection(0)
		os.system('onion pwm 0 0 1000')
		StirObj.setOutputDirection(0)
    		
	if(now.minute%10==0):
    		strTemp(sensor)
