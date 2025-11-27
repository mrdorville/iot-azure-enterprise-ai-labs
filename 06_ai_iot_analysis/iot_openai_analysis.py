from azure.storage.blob import BlobServiceClient
from fastavro import reader
import io
import requests
import json
from openai import AzureOpenAI

CONNECTION_STRING = "PEGA_AQUI_TU_CONNECTION_STRING"
CONTAINER_NAME = "telemetria-iot"

AZURE_OPENAI_ENDPOINT = "https://TU-RECURSO.openai.azure.com/"
AZURE_OPENAI_KEY = "TU_API_KEY"
AZURE_OPENAI_DEPLOYMENT = "gpt-iot-lab"

blob_service = BlobServiceClient.from_connection_string(CONNECTION_STRING)
container = blob_service.get_container_client(CONTAINER_NAME)

openai_client = AzureOpenAI(
    api_key=AZURE_OPENAI_KEY,
    api_version="2024-02-15-preview",
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
)

def obtener_temp_uruguay():
    url = "https://api.open-meteo.com/v1/forecast?latitude=-34.9&longitude=-56.2&current_weather=true"
    data = requests.get(url).json()
    return data["current_weather"]["temperature"]

temp_ext = obtener_temp_uruguay()
print("Temperatura externa:", temp_ext)

for blob in container.list_blobs():
    blob_client = container.get_blob_client(blob)
    content = blob_client.download_blob().readall()
    bytes_io = io.BytesIO(content)

    try:
        avro_reader = reader(bytes_io)
        for record in avro_reader:
            if "Body" not in record:
                continue

            body = json.loads(record["Body"].decode("utf-8", errors="ignore"))

            dispositivo = body["event"]["origin"]
            temperatura = body["event"]["payload"]["temperature"]
            alerta = body["event"]["payload"].get("alertLevel", "NORMAL")

            prompt = f"""
            Dispositivo: {dispositivo}
            Temperatura local: {temperatura}
            Temperatura externa: {temp_ext}
            Nivel de alerta: {alerta}
            Analiza riesgo operativo
            """

            response = openai_client.chat.completions.create(
                model=AZURE_OPENAI_DEPLOYMENT,
                messages=[
                    {"role": "system", "content": "Eres analista IoT"},
                    {"role": "user", "content": prompt}
                ]
            )

            print(response.choices[0].message.content)

    except Exception as e:
        print("Error:", str(e))
