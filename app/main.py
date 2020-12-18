from fastapi import FastAPI
from fastapi_mqtt import FastMQTT, MQQTConfig

app = FastAPI()

mqtt_config = MQQTConfig()

mqtt = FastMQTT(config=mqtt_config)


@app.on_event("startup")
async def startapp():
    await mqtt.connection()


@app.on_event("shutdown")
async def shutdown():
    await mqtt.client.disconnect()


@mqtt.on_connect()
def connect(client, flags, rc, properties):
    mqtt.client.subscribe("testtopic/#")


@mqtt.on_message()
async def message(client, topic, payload, qos, properties):
    print("Received Message", topic, payload.decode('utf8'), qos, properties)


@mqtt.on_disconnect()
def disconnect(client, packet, exc=None):
    print("Disconnected")


@mqtt.on_subscribe()
def subscribe(client, mid, qos, properties):
    print("Subscribed", client, mid, qos, properties)


# API Testing
@app.get("/")
async def root():
    return {"data": "Device Provisioning Service"}
