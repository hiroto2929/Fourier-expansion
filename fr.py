import numpy as np 
import matplotlib.pyplot as plt

while(1):
    n = int(input("フーリエ展開したい項数を指定してください: "))
    if n>0:
        break

y=0
xmin = -4.0*np.pi
xmax = 4.0*np.pi
fig = plt.figure(figsize=(7,5))
axes = fig.add_subplot(1,1,1)
x = np.arange(xmin, xmax, 0.1)
for k in range(1,n):
    y = y + np.sin((2*k-1)*x)/(2*k-1)
axes.plot(x, y)
plt.show()

