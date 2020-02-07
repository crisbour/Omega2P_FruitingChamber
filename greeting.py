# Importing package
import time
import onionGpio

LampPin=1; FoggerPin=45;
LampObject=onionGpio.OnionGpio(LampPin)
FoggerObj=onionGpio.OnionGpio(FoggerPin) 
LampVal=True

LampObj.setOutputDirection(LampVal)
FoggerObj.setOutputDirection(0)

while status==0:
	LampVal=not LampVal
	status = LampObject.setOutputDirection(LampVal)
	for i in range(0, 11):
    		FoggerObj.setOutputDirection(1)
			time.sleep(12)
			FoggerObj.setOutputDirection(0)
			time.sleep(384)
	print('Lamp Toggled')
	time.sleep(4)

