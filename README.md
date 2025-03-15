# Simulador de Armado de PC

Simulador de compatibilidad de componentes de computadora desarrollado en Python con interfaz gráfica nativa usando Tkinter.

## Descripción

Este proyecto permite seleccionar diferentes componentes de hardware para simular el armado de una computadora y verificar si los componentes son compatibles entre sí.

El programa evalúa procesador, tarjeta madre, memoria RAM, tarjeta gráfica, almacenamiento, gabinete y fuente de poder.

## Tecnologías utilizadas

- Python
- Tkinter

## Características

* Permite seleccionar componentes principales de una computadora.
* Evalúa la compatibilidad entre procesador, tarjeta madre y memoria RAM.
* Verifica si el gabinete es compatible con el formato de la tarjeta madre.
* Revisa si la tarjeta madre cuenta con soporte para almacenamiento M.2 NVMe.
* Calcula el consumo aproximado del sistema.
* Comprueba si la fuente de poder tiene suficiente capacidad.
* Muestra un diagnóstico claro indicando si el armado es viable o incompatible.
* Funciona de manera local mediante una interfaz gráfica de escritorio.


## Reglas de compatibilidad

El simulador revisa:

1. Que el socket del procesador coincida con el socket de la tarjeta madre.
2. Que el tipo de memoria RAM sea compatible con la tarjeta madre.
3. Que el gabinete tenga espacio suficiente para el formato de la tarjeta madre.
4. Que la tarjeta madre tenga soporte para el tipo de almacenamiento seleccionado.
5. Que la fuente de poder tenga capacidad suficiente para el consumo total del sistema.

## Requisitos

- Python 3 instalado.

No es necesario instalar librerías adicionales porque Tkinter viene incluido en la mayoría de instalaciones de Python.

## Cómo ejecutar

Desde la terminal, ejecuta:

```bash
python simulador_pc.py
```


