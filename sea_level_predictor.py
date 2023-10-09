##  Programmer:     labthe3rd
##  Date:           10/06/2023
##  Description:    Predicts teh sea level in a scatter plot and linegress
##  Note:           Project for freeCodeCamp python data analysis cert

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Convert DataFrame columns to numpy arrays
    years = df['Year'].values
    sea_levels = df['CSIRO Adjusted Sea Level'].values

    # Plotting the scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(years, sea_levels, c='DarkBlue', label='Data Points')
    
    # First line of best fit
    res = linregress(years, sea_levels)
    x = np.arange(years[0], 2051)  # This creates an array of years from the first year in the dataset to 2050
    y = res.intercept + res.slope * x
    plt.plot(x, y, 'r', label='Regression Line')
    
    # Second line of best fit (from year 2000)
    mask_2000 = years >= 2000
    years_2000 = years[mask_2000]
    sea_levels_2000 = sea_levels[mask_2000]

    res_2000 = linregress(years_2000, sea_levels_2000)
    x_2000 = np.linspace(2000, 2050, 51)  # Fixed the linspace arguments to generate 51 points from 2000 to 2050
    y_2000 = res_2000.intercept + res_2000.slope * x_2000
    plt.plot(x_2000, y_2000, 'g', label='Regression Line (2000 and beyond)')
    
    # Annotating the plot
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.legend()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()