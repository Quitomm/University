import numpy as np
import matplotlib.pyplot as plt

# Зададим параметры системы
m = 1.0  # масса
k = 1.0  # коэффициент жесткости
omega = np.sqrt(k / m)  # частота колебаний
gamma = 0.2 * omega  # коэффициент затухания
u0 = 1.0  # начальное смещение
v0 = 0.0  # начальная скорость

t = np.linspace(0, 50, 500)
u = np.exp(-gamma / (2 * m) * t) * (u0 * np.cos(omega * np.sqrt(1 - (gamma / (2 * m * omega)) ** 2) * t) + (v0 + gamma / (2 * m) * u0) * np.sin(omega * np.sqrt(1 - (gamma / (2 * m * omega)) ** 2) * t))

for i in range(len(u)):
    if abs(u[i]) >= 0.5:
        t_eq = t[i]
        u_eq = u[i]
        break

plt.plot(t, u)
plt.plot([t_eq, t_eq], [-1, 1], 'r--')
plt.xlabel('Время, с')
plt.ylabel('Смещение, м')
plt.show()