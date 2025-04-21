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

### 🎯 Función `simular_caida_esfera()`

Esta función representa la trayectoria de una única esfera a través del tablero de la máquina de Galton. Simula su recorrido por los 10 niveles, donde en cada nivel la esfera puede desviarse aleatoriamente. Al finalizar, retorna la posición final donde cayó la esfera.

```python
def simular_caida_esfera(posicion_inicial):
    posicion_final = posicion_inicial
       # ...
```

#### 🔢 `posicion_inicial`

`posicion_inicial` representa la posición de salida de la esfera. Dado que los arreglos en Python comienzan en el índice `0`, el valor `10` corresponde al centro del tablero de 21 posiciones (de 0 a 20). Desde esta posición se simula el recorrido de cada esfera. La posición final se iguala con la de inicio, para que en el siclo `while` se modifique la trayectoria de la esfera  `posicion_final = posicion_inicial` 

La siguiente imagen ilustra la posición de partida:

![imagen índice de partida](https://github.com/Blado87/maquina_galton_simulacion_python/blob/02590fc4a5fef925b437e002668484897aff38e5/img_guia_simulacion/indice_partida.png)


#### 🎲 `random.choice([-1, 1])`

La función `random.choice()` nos permite seleccionar de forma aleatoria uno de los elementos de la lista `[-1, 1]`. Esto representa el movimiento que hará la esfera al chocar con un obstáculo: hacia la izquierda (`-1`) o hacia la derecha (`+1`). El valor se asigna a la variable `desplazamiento`.

#### 🔄 `posicion_final = max(0, min(20, posicion_final + desplazamiento))`

Esta línea actualiza la posición actual de la esfera sumando el desplazamiento. Para evitar que la esfera salga fuera del tablero, se utiliza una combinación de funciones:

- `posicion_final + desplazamiento`: calcula la nueva posición.
- `min(20, ...)`: asegura que la posición no sobrepase el índice máximo del tablero (20).
- `max(0, ...)`: asegura que la posición no sea menor que 0 (el inicio del tablero).

Esto garantiza que la esfera siempre se mantenga dentro de los límites válidos del arreglo.

#### 🔁 `niveles_recorridos += 1`

Cada vez que la esfera avanza un nivel (es decir, realiza un movimiento), se incrementa el contador `niveles_recorridos`. El bucle `while` continúa hasta que se hayan recorrido los 10 niveles del tablero.


```python
    while niveles_recorridos < 10:
        desplazamiento = random.choice([-1, 1]) 
        posicion_final = max(0, min(20, posicion_final + desplazamiento))
        niveles_recorridos += 1

	return posicion_final
```

Al final  `return posicion_final` nos regresa el índice en el que termino la esfera al final de recorrido.

![Desplazamiento de la esfera](https://github.com/Blado87/maquina_galton_simulacion_python/blob/02bc4e456f26243ad3a250eaa4842cd8c3c21ba0/img_guia_simulacion/desplazamiento.png)







