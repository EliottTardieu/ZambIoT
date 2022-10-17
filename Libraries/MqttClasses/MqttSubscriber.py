import pickle
from paho.mqtt.client import MQTTMessage, Client
from typing import Callable

from Libraries.MqttClasses.MqttClient import MqttClient


# Mqtt client used for receiving objects
class MqttSubscriber(MqttClient):
    """Mqtt client used for receiving objects. \n
    The method on_message is called when a message is received. \n
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
        self.__on_message: Callable[[Client, object, MQTTMessage], None] = self.__default_on_message

    @property
    def on_message(self):
        return self.__on_message

    @on_message.setter
    def on_message(self, method: Callable[[Client, object, MQTTMessage], None]):
        self.__on_message = method

    # Used for receiving all new messages
    # This method is usually called in a while(true) loop
    # If this is not the case, change in_loop to false
    def subscribe(self, in_loop: bool = True):
        self.client.subscribe(self.topic)
        self.client.on_message = self.on_message
        if in_loop:
            # Necessary to get all the message within the while loop
            self.client.loop_forever()

    # Used to get the object from the bytearray in message
    @staticmethod
    def get_object_from_message(message: MQTTMessage):
        return pickle.loads(message.payload)

    # Method called when the client receive a message
    # The message sent need is a bytearray (use pickle.dumps(object) method)
    @staticmethod
    def __default_on_message(client: Client, userdata, message: MQTTMessage):
        # pickle.loads is for converting a bytearray to the original object
        print("Received : \"", MqttSubscriber.get_object_from_message(message), "\" from", message.topic)