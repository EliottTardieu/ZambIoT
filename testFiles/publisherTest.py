import time

from Libraries.MqttClasses.MqttPublisher import MqttPublisher

publisher: MqttPublisher = MqttPublisher("polytech/test", "2", "192.168.1.118", 1883)
publisher.connect_mqtt()

publisher.publish("Hello World")
