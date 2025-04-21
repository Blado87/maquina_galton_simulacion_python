# Simulación de la Maquina de Galton usando Python
Este proyecto es una simulación de la Máquina de Galton, un dispositivo que ilustra cómo una distribución normal puede emerger a partir de decisiones aleatorias.

## 🧪 Descripción

El programa simula la caída de esferas desde una posición central. Cada esfera recorre 10 niveles y en cada nivel puede desplazarse aleatoriamente a la izquierda o a la derecha. El resultado final es un histograma que muestra en qué posiciones aterrizaron las esferas.

> 📚 Inspirado en el artículo de Wikipedia sobre la [Máquina de Galton](https://es.wikipedia.org/wiki/M%C3%A1quina_de_Galton).

### 🧩 Ilustración de la Máquina de Galton

A continuación se muestra una ilustración de un tablero o máquina de Galton. En ella se destacan algunos aspectos clave que ayudan a comprender y analizar la solución implementada en Python.

![Ilustración de la Máquina de Galton](https://github.com/Blado87/maquina_galton_simulacion_python/blob/aba109bc30e93da5a60860b72eafe25ae830273e/img_guia_simulacion/tablero_simplificado.png)


### 🧮 Inicialización del Histograma de Caídas

Se inicializa un arreglo con 21 elementos, todos con valor cero. Este arreglo representa las posibles posiciones finales donde pueden caer las esferas, y servirá para almacenar el historial de caídas a medida que se realicen las simulaciones.

```python
histograma_caidas = [0] * 21
```

![Distribución de posiciones finales](https://github.com/Blado87/maquina_galton_simulacion_python/blob/ed5dac2e330c5c2690897525352c8baf95edb71b/img_guia_simulacion/histograma_caidas.png)
