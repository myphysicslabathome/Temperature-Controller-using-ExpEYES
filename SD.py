# Python Program to calculate the standard deviation, mean and Histogram plot

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Read the .dat file
data = np.loadtxt('Temperature.dat')

# select the column and data length
Temp = data[300:1200, 6]

# Calculate the standard deviation and mean
std_dev = np.std(Temp)
mean_value = np.mean(Temp)

# Print on screen
print("Mean Temperature:", "%0.1f"% mean_value)
print("Standard deviation is:", "%0.1f"% std_dev)

# Plottng 
# 1. Histogram plot of the data
plt.hist(Temp, bins=30, color = "skyblue", edgecolor='green')
plt.title('Histogram of Data')
plt.xlabel('Temperature (C)')
plt.ylabel('Frequency')
# 2. Distribution curve plot
xmin, xmax = plt.xlim()
ymin, ymax = plt.ylim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mean_value, std_dev)
plt.plot(x, p,  linewidth=2, label='Distribution Curve')

#Text position
Xp = xmax - (xmax-xmin)*(1/4)
Yp = ymax - (ymax-ymin)*(1/4)
plt.text(Xp,Yp, 'Mean Temperature = %0.1f \n Standard Deviation = %0.1f' % (mean_value, std_dev))

plt.grid(False)
plt.show()

