import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,100)
y1 = x
y2=2**x
y3=x**2
y4=np.log(x)
y5=x*np.log(x)
y6=1

plt.plot(x,y5, label='O(1)')
plt.plot(x,y1, label='O(n)')
plt.plot(x,y2, label='O(2^n)')
plt.plot(x,y3, label='O(n^2)')
plt.plot(x,y4, label='O(log(n))')
plt.plot(x,y5, label='O(nlog(n))')
plt.xlabel('Entradas')
plt.ylabel('Tiempo en ejecución')
plt.title('Notación BigO')
plt.ylim(0,8000)
plt.legend()
plt.show()