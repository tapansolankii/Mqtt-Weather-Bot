import paho.mqtt.client as mqtt

brokerURL = "broker.hivemq.com"
brokerPort = 1883 # port number for unencrypted connections

def on_connect(client, userdata, flags, rc):
   print("Connected with result code "+str(rc))

def on_message(client, userdata, message):
   print("Received message '" + str(message.payload) + "' on topic '"
        + message.topic + "' with QoS " + str(message.qos))

def on_disconnect(client, userdata, rc):
    print("Client Got Disconnected")

mqttclient = mqtt.Client() #create cliet object

mqttclient.on_connect = on_connect
mqttclient.on_disconnect = on_disconnect
mqttclient.on_message = on_message

mqttclient.connect(brokerURL, brokerPort) #call connect function with URL and port number

mqttclient.subscribe("M_IOT/Tapan", qos=1)

mqttclient.loop_start()
# now we can publish topics in the console#

mqttclient.publish(topic="M_IOT/Tapan", payload="another hello", qos=0, retain=False)

# to stop use mqttclient.loop_stop()

#Try sending messages: mqttclient.publish("TestingTopic", "Hello")