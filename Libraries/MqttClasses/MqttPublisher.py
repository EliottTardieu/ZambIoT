import pickle
from paho.mqtt.client import MQTTMessageInfo
from typing import Callable

from Libraries.MqttClasses.MqttClient import MqttClient


class MqttPublisher(MqttClient):
    """Mqtt client used for sending objects. \n
    The method when_published is called when a message is published. \n
    The method on_connect is called when the client is connected to the broker (server)."""
    def __init__(self, topic: str, client_id: str, mqtt_username: str, mqtt_password: str, mqtt_ip_broker: str, mqtt_port: int):
        """
        :param topic: the topic is the name/path of the data we want to retrieve (example: learningmqtt/test/sensors)
        :param client_id: the name of the client
        :param mqtt_username: to be set if an account system is implemented inside the broker
        :param mqtt_password: to be set if an account system is implemented inside the broker
        :param mqtt_ip_broker: the ip of the mqtt server, called a broker (example: "broker.hivemq.com" or "192.168.1.3")
        :param mqtt_port: the port of the mqtt server
        """
        super().__init__(topic, client_id, mqtt_username, mqtt_password, mqtt_ip_broker, mqtt_port)
        # Method called when a message is published
        self.__when_published: Callable[[MQTTMessageInfo, bytearray], None] = self.__default_when_published

    @property
    def when_published(self):
        return self.__when_published

    @when_published.setter
    def when_published(self, method: Callable[[MQTTMessageInfo, bytearray], None]):
        self.__when_published = method

    # Used for sending messages, any objects can be sent
    def publish(self, message):
        # Necessary for sending message multiple times
        self.client.loop_start()
        # pickle.dumps() is for converting an object to a bytearray
        status = self.client.publish(self.topic, pickle.dumps(message))
        self.when_published(status, message)

    # Method called by default when the client publish
    @staticmethod
    def __default_when_published(status: MQTTMessageInfo, message):
        was_published = status[0]
        if was_published == 0:
            print(message, "sent")
        else:
            print("Failed to send message to topic ")
