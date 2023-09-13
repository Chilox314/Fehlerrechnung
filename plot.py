#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(10,6.18))
ax.set_xlabel("$x$")
ax.set_ylabel("$h(x)$")
ax.scatter([20,40,60,80,100,120,140,160,180],[18.8, 18.15, 17.6, 16.85, 16.1, 15.45, 14.65, 14,13.2], color="red")
x_list = np.linspace(0, 200, 20)
y_list = -0.035 * x_list + 19.601
ax.plot(x_list,y_list)
fig.savefig("figure.pdf")