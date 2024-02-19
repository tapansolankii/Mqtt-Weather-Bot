import dht
import network
import machine

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.scan()
wlan.connect('Wokwi-GUEST','')
wlan.isconnected()

d = dht.DHT22(machine.Pin(4)) #connection to the dht22
d.measure()
d.temperature()
print('-----------------------------')
print(d.temperature())
d.humidity()