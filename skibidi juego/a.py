import numpy as np
import matplotlib.pyplot as plt

# Definir la función
def f(x):
    return 4 * np.sin(0.5 * (x + np.pi / 4)) + 1

# Crear un rango de valores x
x = np.linspace(-2 * np.pi, 6 * np.pi, 1000)
y = f(x)

# Crear el gráfico
plt.figure(figsize=(10, 5))
plt.plot(x, y, label=r"$y = 4\sin\left(\frac{1}{2}(x + \frac{\pi}{4})\right) + 1$", color='blue')
plt.axhline(5, color='green', linestyle='--', label='Máximo = 5')
plt.axhline(-3, color='red', linestyle='--', label='Mínimo = -3')
plt.axhline(1, color='gray', linestyle=':', label='Valor medio = 1')
plt.plot(3 * np.pi / 4, 5, 'ro', label='Punto máximo $(\dfrac{3\pi}{4}, 5)$')

# Estética del gráfico
plt.title("Gráfico de la función seno ajustada")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.axvline(0, color='black', linewidth=0.5)
plt.axhline(0, color='black', linewidth=0.5)
plt.ylim(-5, 7)
plt.show()