# IoT Azure Enterprise AI Labs

Este repositorio contiene una serie de laboratorios empresariales de Internet of Things (IoT) utilizando Microsoft Azure, simulacion de dispositivos, ruteo de datos empresariales y analisis con inteligencia artificial.

Los laboratorios replican escenarios reales utilizados en industrias como:
- Retail
- Data Centers
- Manufactura
- Seguridad empresarial

---

## Requisitos

- Suscripcion activa de Microsoft Azure
- IoT Hub creado
- Dispositivo IoT registrado
- Azure Storage Account
- Azure Cloud Shell (Bash) o Windows con Python 3.x

Se recomienda usar Azure Cloud Shell como terminal principal

---

## Arquitectura del laboratorio

1. Simulador de telemetria (Windows)
2. Simulador ESP32 (Cloud Shell)
3. Ruteo IoT Hub -> Blob Storage
4. Sistema de alertas criticas
5. Lectura de datos AVRO
6. Analisis con Azure OpenAI

---

## Servicios de Azure utilizados

- Azure IoT Hub
- Azure Storage Account (Blob)
- Azure AI Services
- Azure OpenAI

---

## Instalacion de dependencias

```bash
pip install azure-iot-device azure-storage-blob fastavro openai requests

Cada carpeta contiene su script listo para ejecucion y replica empresarial completa.

---

## Laboratorios incluidos

1. Telemetry Simulator (Windows)
2. ESP32 Simulator (Cloud Shell)
3. IoT Hub to Blob Storage Routing
4. Critical Monitoring and Alerts
5. Blob Storage AVRO Reader
6. Azure AI / OpenAI IoT Analysis

