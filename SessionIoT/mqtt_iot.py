import os
import ssl
import time
import board

import socketpool
import wifi

import adafruit_minimqtt.adafruit_minimqtt as MQTT
from secrets import secrets

wifi.radio.connect(secrets["ssid"], secrets["password"])
print("Connected to wifi")


### Code ###
# Define callback methods which are called when events occur
def connected(client, userdata, flags, rc):
    # This function will be called when the client is connected
    # successfully to the broker.
    print(f"Connected to MQTT broker! Listening for topic ")
    # Subscribe to all changes on the default_topic feed.
    client.subscribe("makerspace/CMD/" + secrets["client_id"])


def disconnected(client, userdata, rc):
    # This method is called when the client is disconnected
    print("Disconnected from MQTT Broker!")


def message(client, topic, message):
    """Method callled when a client's subscribed feed has a new
    value.
    :param str topic: The topic of the feed with a new value.
    :param str message: The new value
    """
    print(f"New message on topic {topic}: {message}")


# Create a socket pool
pool = socketpool.SocketPool(wifi.radio)
ssl_context = ssl.create_default_context()

# If you need to use certificate/key pair authentication (e.g. X.509), you can load them in the
# ssl context by uncommenting the lines below and adding the following keys to your settings.toml:
# "device_cert_path" - Path to the Device Certificate
# "device_key_path" - Path to the RSA Private Key
# ssl_context.load_cert_chain(
#     certfile=os.getenv("device_cert_path"), keyfile=os.getenv("device_key_path")
# )

# Set up a MiniMQTT Client
mqtt_client = MQTT.MQTT(
    broker=secrets["broker"],
    port=1883,
    username=secrets["broker_user"],
    password=secrets["broker_pass"],
    socket_pool=pool,
    ssl_context=ssl_context,
    socket_timeout=0.3
)

# Setup the callback methods above
mqtt_client.on_connect = connected
mqtt_client.on_disconnect = disconnected
mqtt_client.on_message = message

# Connect the client to the MQTT broker.
print("Connecting to MQTT broker...")
mqtt_client.connect()

last = time.monotonic()

# Start a non blocking message loop...
# NOTE: Network reconnection is handled within this loop
while True:
    now = time.monotonic()
    if now - last > 5.0:
        message = "hello"
        mqtt_client.publish("makerspace/DATA/"+secrets["client_id"], message)
        last = now
    try:
        mqtt_client.loop(timeout=0.3)
    except (ValueError, RuntimeError) as e:
        print("Failed to get data, retrying\n", e)
        wifi.reset()
        mqtt_client.reconnect()
        continue