import random
import time
import json
from azure.iot.device import IoTHubDeviceClient, Message

CONNECTION_STRING = "PEGA_AQUI_TU_CONNECTION_STRING"

client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

print("ESP32 Simulado iniciado")

try:
    while True:
        temperature = round(random.uniform(20, 45), 2)
        humidity = round(random.uniform(40, 70), 2)

        if temperature <= 25:
            alert = "NORMAL"
        elif temperature <= 35:
            alert = "ALERTA"
        else:
            alert = "CRITICO"

        data = {
            "event": {
                "origin": "sensor-temp-tienda01",
                "payload": {
                    "device": "esp32-simulado",
                    "temperature": temperature,
                    "humidity": humidity,
                    "alertLevel": alert
                }
            }
        }

        msg = Message(json.dumps(data))
        msg.content_type = "application/json"
        msg.content_encoding = "utf-8"

        client.send_message(msg)
        print("Mensaje enviado:", data)

        time.sleep(5)

except KeyboardInterrupt:
    print("Simulacion detenida")

finally:
    client.shutdown()
