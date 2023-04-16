import numpy as np
import matplotlib.pyplot as plt

omega, x0, v0, t = 2, 1, 0, np.linspace(0, 10, 100)
x = x0 * np.cos(omega * t) + v0 / omega * np.sin(omega * t)
y = np.random.normal(0, 1, len(t))
z = x + y

fig, axs = plt.subplots(2)
fig.suptitle('Harmonic oscillator with white noise')
axs[0].plot(t, x)
axs[0].set(ylabel='Displacement (m)')
axs[1].plot(t, y)
axs[1].set(xlabel='Time (s)', ylabel='Noise')
plt.show()