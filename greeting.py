# Importing package
import time
import os
import onionGpio

os.system('omega2-ctrl gpiomux set uart1 gpio')
os.system('omega2-ctrl gpiomux set pwm0 pwm')

LampPin=1; FoggerPin=45; StirPin=15;
LampObj=onionGpio.OnionGpio(LampPin)
StirObj=onionGpio.OnionGpio(StirPin)
FoggerObj=onionGpio.OnionGpio(FoggerPin) 
LampVal=False

os.system('onion pwm 0 0 1000')
LampObj.setOutputDirection(LampVal)
FoggerObj.setOutputDirection(0)
StirObj.setOutputDirection(1)

while True:
	LampObj.setOutputDirection(LampVal)
	
	for i in range(0, 11+(2*LampVal-1)*4):
		FoggerObj.setOutputDirection(1)
		os.system('onion pwm 0 85 1000')
		StirObj.setOutputDirection(1)
		time.sleep(120)
		FoggerObj.setOutputDirection(0)
		os.system('onion pwm 0 0 1000')
		StirObj.setOutputDirection(0) 
		time.sleep(3480)

	LampVal=not LampVal
	print('Lamp Toggled')

