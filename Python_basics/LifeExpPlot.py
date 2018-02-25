
# coding: utf-8

# In[1]:


# This is LifeExpPlot.py

# importing packages

import pandas as pd
import matplotlib.pyplot as plt

# Reading file
my_file = pd.read_table("gapminder.txt")

#Subsetting Life Expectancy of Canada over a span of several years

Canada = my_file.loc[my_file['country'] == "Canada", :]

# Plotting
Canada.plot.line(x = "year", y = "lifeExp", label = "Life Expectancy", figsize = (8, 6))
plt.suptitle("Life Expectancy in Canada Over the Years", fontsize = 20)
plt.xlabel("Year", fontsize = 16)
plt.ylabel("Life Expectancy", fontsize = 16)
plt.savefig("PlotLifeExpectancy.png")

