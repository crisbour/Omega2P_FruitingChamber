# Importing package
import time
import onionGpio
from OmegaExpansion import pwmExp

LampPin=1; FoggerPin=45;
LampObject=onionGpio.OnionGpio(LampPin)
FoggerObj=onionGpio.OnionGpio(FoggerPin) 
LampVal=True

LampObj.setOutputDirection(LampVal)
FoggerObj.setOutputDirection(0)

while status==0:
	LampVal=not LampVal
	status = LampObject.setOutputDirection(LampVal)
	print('Lamp Toggled')
	time.sleep(4)

