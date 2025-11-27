import time
import random
from azure.iot.device import IoTHubDeviceClient, Message

CONNECTION_STRING = "PEGA_AQUI_TU_CONNECTION_STRING"

MSG_TXT = '{{"storeId":"Tienda_Centro","deviceId":"sensor-temp-01","temperature":{temp},"humidity":{hum}}}'

def main():
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

    for i in range(50):
        temp = round(random.uniform(22.0, 40.0), 2)
        hum = round(random.uniform(40.0, 70.0), 2)

        msg = MSG_TXT.format(temp=temp, hum=hum)
        message = Message(msg)

        if temp > 35:
            message.custom_properties["alert"] = "CRITICO"
        elif temp > 25:
            message.custom_properties["alert"] = "ALERTA"
        else:
            message.custom_properties["alert"] = "NORMAL"

        print("Enviando:", msg)
        client.send_message(message)
        time.sleep(2)

if __name__ == "__main__":
    main()
