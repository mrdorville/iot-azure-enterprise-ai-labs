from azure.storage.blob import BlobServiceClient
from fastavro import reader
import io
import json

CONNECTION_STRING = "PEGA_AQUI_TU_CONNECTION_STRING"
CONTAINER_NAME = "telemetria-iot"

blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
container_client = blob_service_client.get_container_client(CONTAINER_NAME)

blobs = container_client.list_blobs()

for blob in blobs:
    print("Blob:", blob.name)

    blob_client = container_client.get_blob_client(blob)
    content = blob_client.download_blob().readall()

    bytes_io = io.BytesIO(content)

    try:
        avro_reader = reader(bytes_io)
        for record in avro_reader:
            if "Body" in record:
                body = record["Body"].decode("utf-8", errors="ignore")
                data = json.loads(body)
                print(data)
    except Exception as e:
        print("Error:", str(e))
