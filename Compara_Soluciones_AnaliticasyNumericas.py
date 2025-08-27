import numpy as np
import matplotlib.pyplot as plt

# Definimos la ecuación diferencial: dy/dt = y
def f(t, y):
    return y

# Condiciones iniciales
t0 = 0
y0 = 1
h = 0.2
t_final = 1

# Método de Euler
t_values = np.arange(t0, t_final + h, h)
y_euler = np.zeros(len(t_values))
y_euler[0] = y0

for i in range(1, len(t_values)):
    y_euler[i] = y_euler[i-1] + h * f(t_values[i-1], y_euler[i-1])

# Solución exacta: y = e^t
y_exact = np.exp(t_values)

# Mostrar los resultados
print("t\tEuler\tExacta")
for t, ye, ye_exact in zip(t_values, y_euler, y_exact):
    print(f"{t:.1f}\t{ye:.5f}\t{ye_exact:.5f}")

# Graficar las soluciones
plt.figure(figsize=(8,5))
plt.plot(t_values, y_exact, 'g-', label="Solución exacta", linewidth=2)
plt.plot(t_values, y_euler, 'ro--', label="Aproximación de Euler")
plt.title("Comparación entre la solución exacta y el método de Euler")
plt.xlabel("t")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()