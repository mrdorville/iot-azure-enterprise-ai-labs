# IoT Azure Enterprise AI Labs

Este repositorio contiene una serie de laboratorios empresariales de Internet of Things (IoT) utilizando Microsoft Azure, simulación de dispositivos, ruteo de datos empresariales y análisis con inteligencia artificial.

Los laboratorios replican escenarios reales utilizados en industrias como:
- Retail
- Data Centers
- Manufactura
- Seguridad empresarial

---

## Requisitos

- Suscripción activa de Microsoft Azure
- IoT Hub creado
- Dispositivo IoT registrado
- Azure Storage Account
- Azure Cloud Shell (Bash) o Windows con Python 3.x

Se recomienda usar Azure Cloud Shell como terminal principal.

---

## Arquitectura del laboratorio

1. Simulador de telemetría (Windows)  
2. Simulador ESP32 (Cloud Shell)  
3. Ruteo IoT Hub -> Blob Storage  
4. Sistema de alertas críticas  
5. Lectura de datos AVRO  
6. Análisis con Azure OpenAI  

---

## Servicios de Azure utilizados

- Azure IoT Hub  
- Azure Storage Account (Blob)  
- Azure AI Services  
- Azure OpenAI  

---

## Instalación de dependencias

~~~bash
pip install azure-iot-device azure-storage-blob fastavro openai requests
~~~

Cada carpeta contiene su script listo para ejecución y réplica empresarial completa.

---

## Laboratorios incluidos

1. Telemetry Simulator (Windows)
2. ESP32 Simulator (Cloud Shell)
3. IoT Hub to Blob Storage Routing
4. Critical Monitoring and Alerts
5. Blob Storage AVRO Reader
6. Azure AI / OpenAI IoT Analysis

---

## Diagrama de arquitectura

~~~text
[Simulador IoT / ESP32]
           |
           v
     Azure IoT Hub
           |
           v
Message Routing (reglas de negocio)
           |
           v
   Azure Blob Storage (AVRO)
           |
           v
Azure AI Services / Azure OpenAI
~~~

## Estructura del laboratorio IoT

Este repositorio contiene los laboratorios prácticos del curso de IoT, organizados por etapas progresivas, desde la simulación de telemetría hasta el análisis con Inteligencia Artificial.

Cada carpeta representa una fase del flujo IoT.

### 01. Telemetría simulada (Windows)

Simula un sensor de temperatura que genera datos como si fueran enviados desde una tienda física.

- Carpeta: `01_telemetry_simulator_windows/`  
- Script principal: [`sensor_temp_tienda01.py`](01_telemetry_simulator_windows/sensor_temp_tienda01.py)

Conceptos trabajados:

- Simulación de sensores IoT
- Generación de telemetría
- Estructura de mensajes

---

### 02. Simulador de ESP32 en Azure Cloud Shell

Simulación de un dispositivo tipo ESP32 enviando datos desde la nube.

- Carpeta: `02_esp32_simulator_cloudshell/`  
- Script principal: [`esp32_simulado.py`](02_esp32_simulator_cloudshell/esp32_simulado.py)

Conceptos trabajados:

- Simulación de dispositivos edge
- Formato de mensajes IoT
- Envío de telemetría

---

### 03. IoT Hub y enrutamiento hacia Blob Storage

Configuración lógica del envío de datos hacia almacenamiento.

- Carpeta: `03_iot_hub_blob_routing/`  
- Documentación: [`README.md`](03_iot_hub_blob_routing/README.md)

Conceptos trabajados:

- Rutas de mensajes
- Arquitectura IoT en Azure
- Flujo IoT Hub → Blob Storage

---

### 04. Generación de alertas críticas

Simulación de alertas con base en valores extremos de temperatura.

- Carpeta: `04_critical_alerts/`  
- Script principal: [`04_critical_alerts:esp32_simulado_alertas.py`](04_critical_alerts/04_critical_alerts:esp32_simulado_alertas.py)  
- Documentación: [`README.md`](04_critical_alerts/README.md)

Conceptos trabajados:

- Reglas de negocio para alertas
- Clasificación de criticidad
- Automatización de eventos

---

### 05. Lector de archivos Avro desde Blob Storage

Lectura de historiales IoT almacenados como archivos Avro.

- Carpeta: `05_blob_avro_reader/`  
- Script principal: [`read_blobs_avro.py`](05_blob_avro_reader/read_blobs_avro.py)

Conceptos trabajados:

- Formato Avro
- Acceso a Azure Blob Storage
- Análisis histórico de telemetría

---

### 06. Análisis IoT con Inteligencia Artificial

Análisis inteligente de datos IoT y clasificación de comportamientos térmicos.

- Carpeta: `06_ai_iot_analysis/`  
- Script principal: [`iot_openai_analysis.py`](06_ai_iot_analysis/iot_openai_analysis.py)

Conceptos trabajados:

- IA aplicada a datos IoT
- Análisis semántico de comportamientos
- Identificación de patrones de riesgo

---

## Lectura complementaria

Para profundizar en los conceptos utilizados en este laboratorio, se recomienda revisar los siguientes recursos.

### Documentación oficial

- [Azure IoT Hub Documentation](https://learn.microsoft.com/azure/iot-hub/)
- [Azure IoT Message Routing](https://learn.microsoft.com/azure/iot-hub/iot-hub-devguide-messages-d2c)
- [Azure Blob Storage Documentation](https://learn.microsoft.com/azure/storage/blobs/)
- [Apache Avro Specification](https://avro.apache.org/docs/)
- [Azure Cloud Shell](https://learn.microsoft.com/azure/cloud-shell/overview)

### IoT e Inteligencia Artificial

- [OpenAI API Documentation](https://platform.openai.com/docs/)
- [IoT y analítica avanzada en la nube (visión general)](https://learn.microsoft.com/azure/architecture/solution-ideas/articles/iot-remote-monitoring)

### Archivos clave dentro del repositorio

Para seguir el flujo completo del laboratorio:

- Simulación de sensor de tienda:  
  [`01_telemetry_simulator_windows/sensor_temp_tienda01.py`](01_telemetry_simulator_windows/sensor_temp_tienda01.py)

- Simulación ESP32 en Cloud Shell:  
  [`02_esp32_simulator_cloudshell/esp32_simulado.py`](02_esp32_simulator_cloudshell/esp32_simulado.py)

- Definición de alertas críticas:  
  [`04_critical_alerts/04_critical_alerts:esp32_simulado_alertas.py`](04_critical_alerts/04_critical_alerts:esp32_simulado_alertas.py)

- Lectura de datos históricos (Avro):  
  [`05_blob_avro_reader/read_blobs_avro.py`](05_blob_avro_reader/read_blobs_avro.py)

- Análisis de datos IoT con IA:  
  [`06_ai_iot_analysis/iot_openai_analysis.py`](06_ai_iot_analysis/iot_openai_analysis.py)

### Conceptos sugeridos para estudio adicional

- Arquitecturas basadas en eventos para IoT
- Diferencias entre IoT Hub y Event Hub
- Telemetría en tiempo real vs análisis batch
- Persistencia de datos históricos para IoT
- Casos de uso de IA aplicada a mantenimiento predictivo
