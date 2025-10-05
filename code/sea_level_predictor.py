import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    
    # Create first line of best fit
    lineregress1 = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))
    predicted_sea_level = lineregress1.slope * years_extended + lineregress1.intercept
    r2 = lineregress1.rvalue ** 2 #We got a R2 value of 0.96 wich is a pretty good fit
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    ax.plot(years_extended, predicted_sea_level, color='red')


    # Create second line of best fit
    df = df[df['Year'] >= 2000]
    lineregress2 = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    years_extended2 = pd.Series(range(2000, 2051))
    predicted_sea_level_2000 = (lineregress2.slope * years_extended2 + lineregress2.intercept)
    r2 = lineregress2.rvalue ** 2 #We got a slightly lower r2 value here, with 0.95 wich is still pretty good
    ax.plot(years_extended2, predicted_sea_level_2000, color='orange')


    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
