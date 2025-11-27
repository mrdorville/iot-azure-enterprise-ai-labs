# Lab 04 - Critical Monitoring and Alerts

Este laboratorio simula un sistema empresarial de alertas basado en telemetría IoT.

## Objetivo

- Clasificar eventos en NORMAL, ALERTA o CRITICO
- Simular escenarios reales de sobrecalentamiento
- Generar reglas de negocio para monitoreo

## Reglas de negocio

| Temperatura | Nivel |
|------------|------|
| <= 25 °C   | NORMAL |
| 26 - 35 °C | ALERTA |
| > 35 °C    | CRITICO |

## Resultado esperado

- Los eventos CRITICO pueden ser ruteados a Blob Storage
- El sistema sirve como simulación de centros de monitoreo empresariales
