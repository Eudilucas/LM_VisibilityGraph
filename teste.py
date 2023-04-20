import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 20, 50, 80, 130])

logx = np.log(x)
logy = np.log(y)

plt.scatter(logx, logy)
plt.xlabel('log(x)')
plt.ylabel('log(y)')

coefs = np.polyfit(logx, logy, 1)
a = coefs[0]
logk = coefs[1]
k = np.exp(logk)

x_line = np.linspace(min(logx), max(logx), 100)
y_line = k * x_line**a
plt.plot(x_line, y_line, color='red')

plt.show()

