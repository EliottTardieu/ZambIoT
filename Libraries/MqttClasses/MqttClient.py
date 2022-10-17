from typing import Callable
from paho.mqtt.client import Client


class MqttClient:
    """Class that manages the MQTT communication (sending and receiving). \n
    The method on_connect is called when the client is connected to the broker (server).
    """
    def __init__(self, topic: str, client_id: str, mqtt_username: str, mqtt_password: str, mqtt_ip_broker: str, mqtt_port: int):
        """
        :param topic: the topic is the name/path of the data we want to retrieve (example: learningmqtt/test/sensors)
        :param client_id: the name of the client
        :param mqtt_username: to be set if an account system is implemented inside the broker
        :param mqtt_password: to be set if an account system is implemented inside the broker
        :param mqtt_ip_broker: the ip of the mqtt server, called a broker (example: "broker.hivemq.com" or "192.168.1.3")
        :param mqtt_port: the port of the mqtt server
        """
        self.__topic = topic
        self.__client_id = client_id
        self.__mqtt_username = mqtt_username
        self.__mqtt_password = mqtt_password
        self.__mqtt_ip_broker = mqtt_ip_broker
        self.__mqtt_port = mqtt_port

        self.__client: Client = Client(self.__client_id)
        self.__on_connect: Callable[[Client, object, dict, int], None] = self.__default_on_connect

    @property
    def client_id(self):
        return self.__client_id

    @property
    def topic(self):
        return self.__topic

    @property
    def mqtt_username(self):
        return self.__mqtt_username

    @property
    def mqtt_password(self):
        return self.__mqtt_password

    @property
    def mqtt_ip_broker(self):
        return self.__mqtt_ip_broker

    @property
    def mqtt_port(self):
        return self.__mqtt_port

    @property
    def client(self):
        return self.__client

    @property
    def on_connect(self):
        return self.__on_connect

    @on_connect.setter
    def on_connect(self, method):
        assert (method is Callable[[Client, object, dict, int], None])
        self.__on_connect = method

    def connect_mqtt(self):
        self.__client.username_pw_set(self.__mqtt_username, self.__mqtt_password)
        self.__client.on_connect = self.on_connect
        self.__client.connect(self.__mqtt_ip_broker, self.__mqtt_port)

    # Method called when the client is connected
    @staticmethod
    def __default_on_connect(client: Client, userdata, flag: dict, rc: int):
        # The value of rc (the connection result) indicates success or not
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)