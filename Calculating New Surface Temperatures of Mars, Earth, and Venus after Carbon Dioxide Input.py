#!/usr/bin/env python
# coding: utf-8

# In[36]:


import math
import numpy as np
import matplotlib.pyplot as plt



print('==============================\n')
print('Surface Temperature Calculator\n')
print('==============================\n')



planet = input('Enter the planet name (Earth, Mars, Venus, or Mercury):\n')

delta = 0.0000000567
if planet == 'Earth':
    albedo = 0.33
    solar_irradiance = 1367
    initial_co2 = 413
    heat_capacity = 1.4 
    pressure = 1
    mm_atmos = 0.02896
    gravity = 9.8
    gas_constant = 8.3145
    surface_temp = (((((solar_irradiance)/4) * (1 - albedo)) / delta) ** (1/4)) - ((gravity / heat_capacity) * ((gas_constant * ((solar_irradiance * (1 - albedo) / (4 * 1 * (delta))) ** (1/4)) * math.log(pressure/2, 10)) / (gravity * mm_atmos * math.log(2.71828, 10)) / 1000))  
    
elif planet == 'Mars':
    surface_temp = 210
    initial_co2 = 953000
    
elif planet == 'Venus':
    surface_temp = 737
    initial_co2 = 965000
    
else:
    print('Invalid entry.')

    
    
change_co2 = float(input('What is the input of carbon dioxide (gigatons) per year?\n'))
years = float(input('For how many years is the carbon dioxide added?\n'))



current_gigaton_co2 = 3210
co2_proportion = initial_co2 / 1000000
ppm_change_co2 = ((co2_proportion / current_gigaton_co2) * change_co2) * 1000000



new_gigaton_co2 = current_gigaton_co2 + change_co2
new_co2 = (co2_proportion / current_gigaton_co2) * new_gigaton_co2
ppm_total_new_co2 = (new_co2) * 1000000



                                                             
def temp(x, y, z):
    return 5.35 * (x / 173.62) * math.log(y / z, 2.71828)

increase_temp = temp(surface_temp, ppm_total_new_co2, initial_co2)
new_temp = int(surface_temp + increase_temp * years)



print('After', years, 'years, the new carbon dioxide level is', int((ppm_change_co2 * years) + initial_co2), 'parts per million.\n')
print('The new temperature', years, 'years from now is', new_temp , 'degrees Kelvin if carbon dioxide is added at a constant rate.\n')

    
    
X = np.linspace(0, years, 5)
Y = initial_co2 + ppm_change_co2 * X

plt.plot(X, Y)
plt.title('Constant Input of Carbon Dioxide (ppm) Over Time (years)\n')
plt.xlabel('Time (years)')
plt.ylabel('Carbon Dioxide (ppm)')
plt.show()


X = np.linspace(0, years, 5)
Y = (surface_temp + increase_temp * X) 

plt.plot(X, Y)
plt.title('Increase in Temperature (K) Over Time (years) after CO2 Input\n')
plt.xlabel('Time (years)')
plt.ylabel('Temperature (K)')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




