import numpy as np
import matplotlib.pyplot as plt

x0, v0, omega, t = 1, 0, 2, np.linspace(0, 10, 100)
x = x0 * np.cos(omega * t) + v0 / omega * np.sin(omega * t)

plt.plot(t, x)
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.show()