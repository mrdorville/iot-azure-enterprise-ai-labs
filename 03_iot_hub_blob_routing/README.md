# Lab 03 - IoT Hub to Blob Storage Routing

Este laboratorio implementa el ruteo de telemetría desde Azure IoT Hub hacia Azure Blob Storage.

## Objetivo

- Filtrar mensajes con temperatura superior a 25 °C
- Almacenar datos automáticamente en Azure Blob Storage
- Simular arquitectura empresarial tipo Data Lake

## Servicios Azure Requeridos

- Azure IoT Hub
- Azure Storage Account
- Blob Container: telemetria-iot

## Configuración de la ruta

En Azure Portal:

IoT Hub -> Message Routing -> Routes

Configurar la siguiente query:

$body.event.payload.temperature > 25

## Resultado esperado

- Los mensajes se almacenan en formato AVRO
- Se crean carpetas automáticas por fecha y partición
- Solo se almacenan mensajes críticos

Este paso construye la base de la arquitectura empresarial de datos IoT.