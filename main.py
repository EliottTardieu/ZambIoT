import time

from Libraries.MqttClasses.MqttPublisher import MqttPublisher
from gpiozero import CPUTemperature

if __name__ == '__main__':
    # On fait un nouveau publisher
    publisher: MqttPublisher = MqttPublisher(
        topic="polytech/mqtt",
        client_id="pub1",
        # Il faut remplacer cet ip par celle du broker (ou de la machine si le broker est sur un docker)
        mqtt_ip_broker="broker.hivemq.com",
        mqtt_port=1883,
        mqtt_username="admin",
        mqtt_password="password"
    )

    # On connecte le publisher au broker mqtt
    publisher.connect_mqtt()

    while True:
        # On récupère la température du CPU puis on envoit celle-ci
        cpu_temp = CPUTemperature().temperature
        publisher.publish(cpu_temp)

        time.sleep(3)
