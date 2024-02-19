import dht
import machine
import network
import time
from umqtt.simple import MQTTClient

wlan = network.WLAN(network.STA_IF) # create station interface
wlan.active(True)       # activate the interface
wlan.connect('Rechnernetze', 'rnFIW625') 
time.sleep(3)
print(wlan.ifconfig())

d = dht.DHT22(machine.Pin(15))
d.measure()
d.temperature() # eg. 23.6 (°C)
d.humidity()    # eg. 41.3 (% RH)
print("The Temp")

client=MQTTClient("Tapan","broker.hivemq.com")
client.connect()

while True:
    d.measure()
    client.publish("M_IoT/Tapan/temp",str(d.temperature()))
    client.publish("M_IoT/Tapan/humi",str(d.humidity()))
    print("The Temperature is: ",d.temperature())
    print("The Humidity is:",d.humidity())
    time.sleep(15)