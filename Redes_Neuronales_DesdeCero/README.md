# ¿Por qué funciona Backpropagation?

Funciona porque permite resolver el problema de aprendizaje de la red neuronal.

Inicialmente, durante el *forward pass*, la red realiza predicciones que pueden ser prácticamente aleatorias debido a que sus pesos comienzan con valores iniciales. Como resultado, obtiene probabilidades para cada clase.

Luego, **Backpropagation** recorre la red desde la salida hacia la entrada, calculando cómo contribuye cada peso y sesgo al error de la predicción mediante el cálculo de gradientes.

Finalmente, estos gradientes permiten determinar en qué dirección deben ajustarse los pesos y sesgos para reducir el error respecto al resultado verdadero.

Este proceso, junto con un algoritmo de optimización como *Gradient Descent*, permite que la red ajuste progresivamente sus parámetros y mejore sus predicciones.
