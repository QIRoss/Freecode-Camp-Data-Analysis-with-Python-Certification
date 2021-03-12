import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

#solution 4 and 5 special thanks to dillonwfletcher
#repo https://github.com/dillonwfletcher/freeCodeCampSolutions/blob/main/pythonProjects/seaLevelPredictor/sea_level_predictor.py

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv", float_precision='legacy') #study more about precision of floating points for pandas and benchmarking it for my gpu maybe

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = np.array([i for i in df['Year']] + [i for i in range(2014, 2050)]) #search other ways around
    plt.plot(x, res.intercept + res.slope*x, 'r') #optional param label but good practice

    # Create second line of best fit
    x = np.array([i for i in range(2000, 2050)]) #search other ways around
    yr2000 = df[df['Year'] >= 2000]
    res2000 = linregress(yr2000['Year'], yr2000['CSIRO Adjusted Sea Level'])
    plt.plot(x, res2000.intercept + res2000.slope*x, 'r') #optional param label but good practice

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    # plt.legend -> if you used label param on plot
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()