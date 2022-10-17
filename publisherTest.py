import time

from Libraries.MqttClasses.MqttPublisher import MqttPublisher

publisher: MqttPublisher = MqttPublisher("testMqtt", "2", "", "", "broker.hivemq.com", 1883)
publisher.connect_mqtt()

time.sleep(3)

loop = True
while loop:
    message = input("New message : ")
    publisher.publish(message)
