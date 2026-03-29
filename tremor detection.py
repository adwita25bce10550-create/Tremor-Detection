import math
import random
import time
import matplotlib.pyplot as plt
import numpy as np
import webbrowser
#websites
webbrowser.open("https://www.ninds.nih.gov/health-information/disorders/tremor")
webbrowser.open("https://pmc.ncbi.nlm.nih.gov/articles/PMC5296883")

 
time_data=[]
magnitude=[]
delta=[]

last_magnitude=0
Threshold=2.0
#50 sensor readings
for i in range(50):
    timing=i*0.1
    #simulated sensor numbers
    x=random.uniform(-2,2)
    y=random.uniform(8,10)
    z=random.uniform(-2,2)

    if random.random()<0.2:
        x+=random.uniform(3,5)
        #calculate magnitude
    magnitudes=math.sqrt(x*x+y*y+z*z)
    #calculate change
    d=abs(magnitudes- last_magnitude)
    time_data.append(timing)
    magnitude.append(magnitudes)
    #simple output
    delta.append(d)
    if d>Threshold:
        print("Tremor is being Detected at time",timing)
    else:
        print("tremor is stable")
#plot the graph of tremor
plt.figure()
plt.plot(time_data,magnitude,label="magnitude")
plt.plot(time_data,delta,linestyle='dashed',label="delta")
plt.xlabel("time")
plt.ylabel("number")
plt.title("tremor detection")
plt.legend()
plt.show()




