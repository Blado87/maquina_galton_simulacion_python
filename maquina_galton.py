import random
import matplotlib.pyplot as plt

# Inicializa un arreglo con 21 posiciones (índices de 0 a 20) para representar
# el histograma de las posiciones finales de las esferas.
histograma_caidas = [0] * 21

def simular_caida_esfera(posicion_inicial):
    """
    Simula la caída de una esfera por una máquina de Galton.

    La esfera se mueve 10 niveles, eligiendo aleatoriamente entre moverse
    a la izquierda (-1) o a la derecha (+1) en cada nivel. La posición final
    está limitada entre 0 y 20 para evitar desbordamientos.

    Parámetros:
        posicion_inicial (int): La posición desde la cual inicia la esfera.

    Retorna:
        int: La posición final de la esfera después de caer.
    """
    posicion_final = posicion_inicial
    niveles_recorridos = 0

    while niveles_recorridos < 10:
        desplazamiento = random.choice([-1, 1])  # Movimiento aleatorio: izquierda o derecha
        posicion_final = max(0, min(20, posicion_final + desplazamiento))  # Limita dentro del rango [0, 20]
        niveles_recorridos += 1

    return posicion_final

# Simula la caída de 100 esferas desde la posición central (10)
# y actualiza el histograma con la posición final de cada esfera.
for _ in range(100):
    posicion_celda = simular_caida_esfera(10)
    histograma_caidas[posicion_celda] += 1

def filtrar_posiciones_pares(arreglo):
    """
    Filtra las posiciones pares de un arreglo, conservando solo los valores
    en los índices 0, 2, 4, ..., 20.

    Parámetros:
        arreglo (list): Lista de números (por ejemplo, el histograma original).

    Retorna:
        list: Lista con los valores en las posiciones pares del arreglo original.
    """
    return [valor for i, valor in enumerate(arreglo) if i % 2 == 0]

# Crea una nueva lista que contiene solo los valores del histograma en posiciones pares.
histograma_filtrado = filtrar_posiciones_pares(histograma_caidas)

def graficar_histograma(arreglo):
    """
    Genera una gráfica de barras que muestra la distribución de caídas de las esferas.

    Parámetros:
        arreglo (list): Lista con los datos del histograma a graficar.
    """
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(arreglo)), arreglo, color='skyblue', edgecolor='black')
    plt.title('Distribución de las Caídas de las Esferas en la Máquina de Galton')
    plt.xlabel('Posición de Caída')
    plt.ylabel('Número de Esferas')
    plt.xticks(range(len(arreglo)))
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Grafica el histograma.
graficar_histograma(histograma_filtrado)


