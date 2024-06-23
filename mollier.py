import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
from scipy.optimize import curve_fit




# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, y1, color='b',label='1 GeV')
plt.plot(x, y10, color='r',label='10 GeV')
plt.plot(x, y20, color='k',label='20 GeV')
plt.legend()
plt.scatter(x, y1, color='b', edgecolor='k')  # Optional: to show original data points
plt.scatter(x, y10, color='r', edgecolor='k')  # Optional: to show original data points
plt.scatter(x, y20, color='k', edgecolor='k')  # Optional: to show original data points

plt.xlabel('Radial Distance (mm)')
plt.ylabel('Fractional Energy Deposited (E/E$_0$)')
plt.title('Energy Deposition for electron beam of various energies w.r.t. radial distance with Spline Interpolation')
plt.grid(True)
# Set x-axis range
#plt.xlim(0, 25)
plt.savefig('Mollier.jpg', format='jpg')
plt.show()
# Original data points
x = [6.98,14.3,28.6,42.9,57.2,71.5,85.8]
y1 = np.array([2.334,2.971,3.130,3.173,3.188,3.208,3.210])
y1=y1/1000
x=pd.Series(x)
# Generate a spline of degree 3
spl = make_interp_spline(x, y, k=2)


y10=np.array([24.62,31.05,32.61,33.10,33.31,33.46,33.52])
y10=y10/10000
y20=np.array([48.79,61.06,64.12,64.98,65.33,65.49,65.58])
y20=y20/20000





x_new = np.linspace(x.min(), x.max(), 300)
y_new = spl(x_new)





# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, y1, color='b',label='1 GeV')
plt.plot(x, y10, color='r',label='10 GeV')
plt.plot(x, y20, color='k',label='20 GeV')
plt.legend()
plt.scatter(x, y1, color='b', edgecolor='k')  # Optional: to show original data points
plt.scatter(x, y10, color='r', edgecolor='k')  # Optional: to show original data points
plt.scatter(x, y20, color='k', edgecolor='k')  # Optional: to show original data points

plt.xlabel('Radial Distance (mm)')
plt.ylabel('Fractional Energy Deposited (E/E$_0$)')
plt.title('Energy Deposition for electron beam of various energies w.r.t. radial distance with Spline Interpolation')
plt.grid(True)
# Set x-axis range
#plt.xlim(0, 25)
plt.savefig('Mollier.jpg', format='jpg')
plt.show()
