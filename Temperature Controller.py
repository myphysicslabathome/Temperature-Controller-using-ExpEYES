# Program for water bath temperature controller using water heater
# 25/04/2024

# Establish Connection
import eyes17.eyes
p = eyes17.eyes.open()

# Import python libreary 
import time, math
import numpy as np

# Define the function to mesaure the temperature
def temperature():
    """Function to measure the instanteneous temperature"""
    R0 = 1000                    # PT1000 (RTD Name)
    Alpha = 3.85/1000            # Temperature coefficient 
    n = 1                        # NO of measurements for averaging
    Rsum = 0
    for x in range (0,n):        # Loop for averaging
        r = p.get_resistance()   # Measure the resistance in ohm
        Rsum = Rsum+r            # Sum of resistance
    R = Rsum/n                   # Average resistance
    T = (1/Alpha)*((R/R0)-1)     # Calculate Temperature from Resistance
    return T 


# ON & OFF the relay
ST  = float(input("Enter the set temperature (in degrees Celsius): "))
p.set_state(OD1=0)              # Set digital output to LOW 
t0 = time.time()                # Time initialization

 
while True:
    if temperature() < (ST):# If temp. less than Set temp.             
        p.set_state(OD1=1)  # Digital Out Put HIGH
        ts=time.time()
        t1=ts-t0
        print( temperature() )
        file = open ("Temperature70.dat", "a") # Appending file
        file.write("{0:4.2f} {1:4.1f}\n".format(t1,temperature()))
                                
    if temperature() >= (ST):# If temp. higher than Set temp.             
        p.set_state(OD1=0)    # Digital Out Put LOW
        ts=time.time()
        t2=ts-t0
        print( temperature() )
        file = open ("Temperature70.dat", "a") # Appending file
        file.write("{0:4.2f} {1:4.1f}\n".format(t2,temperature()))
    
    time.sleep(1)           # Waiting time in sec
