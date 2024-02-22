# END2END - KAFKA para la Gestión de Carteras de Criptomonedas con la API de Coinbase 

## Introducción
Este proyecto aborda la implementación de un sistema end-to-end utilizando Kafka para la monitorización en tiempo real del mercado de criptomonedas. Es especialmente útil para analistas financieros, traders y entusiastas de las criptomonedas que desean mantenerse informados sobre los cambios en sus carteras de criptoactivos.

## Proyecto
El caso de uso principal es la gestión y monitorización de carteras de criptomonedas, permitiendo a los usuarios obtener información actualizada sobre capitalización de mercado, volumen de operaciones y otros indicadores relevantes del mercado.

### Uso de Kafka:

- **Productor "Pricelist"**: Publicamos datos en tiempo real en un tópico de Kafka llamado "marketcap".
- **Consumidores para Procesamiento**: Leemos y procesamos datos desde "marketcap", aplicando filtros y cálculos necesarios.
- **KSQL para Filtrado Adicional**: Empleamos KSQL para realizar filtrado avanzado y análisis de datos en los tópicos mencionados.
- **Visualización de Datos**: Presentamos la información procesada en una interfaz de terminal utilizando Visual Studio Code y la UI de Confluent.

## Escenario: Identificación de Oportunidades de Compra
La aplicación está diseñada para identificar oportunidades de compra de criptomonedas al detectar variaciones significativas de precios que superan umbrales predefinidos, generando alertas oportunas para los usuarios.

### Arquitectura del Proyecto

La arquitectura del proyecto ha sido diseñada para optimizar la monitorización y análisis de los datos del mercado de criptomonedas en tiempo real. La implementación final consta de los siguientes componentes y flujos de datos:

API de Coinbase → Productor Kafka ("marketcap_filtro" o "marketcap") → Consumidor Kafka (Procesamiento y Filtrado)
→ Tópicos Kafka ("Alertas" y "Variaciones de Precios") → KSQL (Filtrado Avanzado) → Visualización (Terminal) 






