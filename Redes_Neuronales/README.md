Challenge de **Cyberdyne Systems**: entrenar una red neuronal desde cero para reconocer dígitos escritos a mano (**MNIST**) y, después, prendas de ropa (**Fashion MNIST**), entendiendo *por qué* funciona: activaciones (ReLU vs Sigmoid) y optimizadores (SGD vs Adam).

## 📂 Contenido

| Archivo | Qué hace |
|---|---|
| `01_mnist.ipynb` | Parte 1: dígitos. Exploración, preprocesamiento, arquitectura, 4 experimentos, evaluación y conclusiones. |
| `02_fashion_mnist.ipynb` | Parte 2: prendas. Misma estructura, usando la arquitectura ganadora de la Parte 1. |

**Framework:** TensorFlow / Keras. Se arma la red en pocas líneas con `Sequential`, `fit()` devuelve el historial de loss/accuracy para graficar, y ambos datasets vienen incluidos.

## 🧠 Qué arquitectura ganó

```
Entrada 28×28 → Flatten (784) → Dense(128, ReLU) → Dense(10, softmax)
```

Una sola capa oculta (Cyberdyne permite 1 o 2), 101.770 parámetros, entrenada con **Adam**, 10 épocas y batch de 32.

### Experimento: activación × optimizador (accuracy de validación, época 10)

| | MNIST · ReLU | MNIST · Sigmoid | Fashion · ReLU | Fashion · Sigmoid |
|---|---|---|---|---|
| **SGD** | 95.0% | 90.9% | 86.2% | 82.3% |
| **Adam** | 97.1% | 97.4% | 88.5% | 88.3% |

- **Adam le gana a SGD** en los dos datasets: en MNIST, en 1 época iguala lo que SGD logra en 10.
- **ReLU vs Sigmoid:** con SGD, ReLU gana claramente. Con Adam quedan empatadas (diferencias de ~0.2 a 0.5 puntos, que son ruido de una sola corrida). Elegí ReLU + Adam porque aprende más rápido y es más robusta.

### Resultado final en test

| Dataset | Accuracy en test | Errores (de 10.000) | Confusión más frecuente |
|---|---|---|---|
| MNIST | **97.1%** | 291 | 9 → 7 |
| Fashion MNIST | **87.6%** | 1.244 | T-shirt → Shirt |

> Los números corresponden a una ejecución con semilla fija (`42`); en otra máquina pueden variar unas décimas.

## 🚀 Qué optimizador usaría en producción

**Adam.** Converge mucho más rápido que SGD con los valores por defecto, casi no requiere ajustar la tasa de aprendizaje y dio el mejor resultado en ambos datasets. Lo usaría junto con **Early Stopping**, porque en las curvas se ve que la red empieza a memorizar (overfitting) alrededor de la época 5.

## 😬 ¿Miedo o respeto?

**Respeto (con un poco de miedo).** Respeto, porque con solo 101.770 parámetros llega a 97% en dígitos. Miedo, porque es **sobreconfiada**: clasificó un 9 como 4 con ~100% de seguridad y una sandalia como bolso con ~100%.


## ▶️ Cómo correrlo

```bash
pip install tensorflow numpy matplotlib scikit-learn
```

Abrir `01_mnist.ipynb` y `02_fashion_mnist.ipynb` y usar *Run All*. Los datasets se descargan solos la primera vez.

## 🛠️ Herramientas

TensorFlow/Keras · NumPy · Matplotlib · scikit-learn (matriz de confusión) · Jupyter Notebook
