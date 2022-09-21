import pandas as pd
import csv

import matplotlib.pyplot as plt


df = pd.read_csv('Projects/total_stars.csv')
df
df.columns
df.drop(['Unnamed: 0','Unnamed: 6', 'Star_name.1', 'Distance.1', 'Mass.1', 'Radius.1','Luminosity'],axis=1,inplace=True)
final_data = df.dropna()
final_data
final_data.reset_index(drop=True,inplace = True)
final_data
final_data.to_csv('final_data.csv')
final_data.info()
final_data.describe()
final_data.head(5)
final_data.dtypes
df.head()
mass = df["Mass"].to_list()
radius = df["Radius"].to_list()
dist = df["Distance"].to_list()
gravity = df["Gravity"].to_list()

def gravity_calculation(radius,mass):
    G=6.674e-11
    for index in range(0,len(mass)):
        g=(mass[index]*G)/((radius[index])**2)
        gravity.append(g)
gravity_calculation(radius,mass)
df["Gravity"]=gravity
df
mass.sort()
radius.sort()
gravity.sort()
plt.plot(radius,mass)


plt.title("Radius & Mass of the Star")
plt.xlabel("Radius")
plt.ylabel("Mass")
plt.show()

plt.plot(mass,gravity)

plt.title("Mass vs Gravity")
plt.xlabel("Mass")
plt.ylabel("Gravity")
plt.show()


plt.scatter(radius,mass)
plt.xlabel("Radius")
plt.ylabel("Mass")
plt.show()