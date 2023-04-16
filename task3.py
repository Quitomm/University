import numpy as np
import matplotlib.pyplot as plt

# Зададим параметры системы
m = 1.0  # масса
k = 1.0  # коэффициент жесткости
omega = np.sqrt(k / m)  # частота колебаний
gamma = 0.2 * omega  # коэффициент затухания
u0 = 1.0  # начальное смещение
v0 = 0.0  # начальная скорость
destroy = 5 # момент нарушения равновесия

t = np.linspace(destroy, 50, 500)
u = np.exp(-gamma / (2 * m) * t) * (u0 * np.cos(omega * np.sqrt(1 - (gamma / (2 * m * omega)) ** 2) * t) + (v0 + gamma / (2 * m) * u0) * np.sin(omega * np.sqrt(1 - (gamma / (2 * m * omega)) ** 2) * t))
t_destroy = np.insert(t, 0, np.linspace(1, destroy, destroy//1))
u_destroy = np.insert(u, 0, [0] * destroy)

plt.plot(t_destroy, u_destroy)
plt.plot([destroy, destroy], [-1, 1], 'r--')
plt.xlabel('Время, с')
plt.ylabel('Смещение, м')
plt.show()
