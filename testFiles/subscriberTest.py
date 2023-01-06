from Libraries.MqttClasses.MqttSubscriber import MqttSubscriber

subscriber = MqttSubscriber("polytech/mqtt", "2", "broker.hivemq.com", 1883)
subscriber.connect_mqtt()

listen = True
while listen:
    subscriber.subscribe()

