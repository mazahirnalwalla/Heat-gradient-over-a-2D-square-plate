import numpy as np
import matplotlib.pyplot as plt

xdim = int(input("Enter the no.of divisions on each axis of the square plate: "))
ydim = xdim

T1 = float(input("Enter the temperature of the top left corner in celcius: "))
T2 = float(input("Enter the temperature of the bottom left corner in celcius: "))
T3 = float(input("Enter the temperature of the bottom right corner in celcius: "))
T4 = float(input("Enter the temperature of the top right corner in celcius: "))

T_guess = 35
T = np.zeros((xdim,ydim))
T.fill(T_guess)

T[0:xdim,0] = T2
T[0,1:ydim] = T1
T[0:xdim,ydim-1] = T4
T[xdim-1,1:ydim] = T3

n_iterations = int(input("How many iterations would you like to run? "))

for n in range(0,n_iterations):
    for i in range(1,xdim-1,1):
        for j in range(1,ydim-1,1):
            T[i][j] = (T[i-1][j]+T[i+1][j]+T[i][j-1]+T[i][j+1])/4

plt.figure(figsize=(10,10))
plt.contourf(T,1000,cmap="hot")
plt.title("Temperature Gradient")
plt.colorbar()
plt.grid()
plt.show()