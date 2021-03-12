import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import numpy as np

# I state that somewhere in the middle of the production of this challenge/solution I started looking at the following link
# https://github.com/dillonwfletcher/freeCodeCampSolutions/blob/main/pythonProjects/pageViewTimeSeriesVisualizer/time_series_visualizer.py
# Some of the following code is not mine and some weirdly look like the same but I kinda understand that for the early level of these challenge it's okay
# Still using it for studying purposes and testing some of it on repl.it

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv').set_index('date')

# Clean data
df = df[(df.value >= df.value.quantile(0.025)) & (df.value <= df.value.quantile(0.975))]
df.index = pd.to_datetime(df.index)

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(11, 9))
    plt.plot(df.index, df['value'])
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.ylabel('Page Views')
    plt.xlabel('Date')
    plt.show
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['month'] = df_bar.index.month
    df_bar['year'] = df_bar.index.year
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    df_bar['month'] = df_bar['month'].apply(lambda data: months[data - 1])
    df_bar["month"] = pd.Categorical(df_bar["month"], categories=months)
    # Draw bar plot
    df_pivot = pd.pivot_table(df_bar,values="value",index="year",columns="month",aggfunc=np.mean)

    # Plot a bar chart using the DF
    ax = df_pivot.plot(kind="bar")
    # Get a Matplotlib figure from the axes object for formatting purposes
    fig = ax.get_figure()
    # Change the plot dimensions (width, height)
    fig.set_size_inches(7, 6)
    # Change the axes labels
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    
    # Draw box plots (using Seaborn)
    fig, axs = plt.subplots(1, 2)
    fig.set_size_inches(20, 10)
    sns.boxplot(x=df_box["year"], y=df_box["value"], ax=axs[0]).set(xlabel="Year", ylabel="Page Views")
    sns.boxplot(x=df_box["month"], y=df_box["value"], 
        order=['Jan', 'Feb', "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        ax = axs[1]).set(xlabel="Month",
        ylabel= "Page Views")
    axs[0].set_title('Year-wise Box Plot (Trend)')
    axs[1].set_title('Month-wise Box Plot (Seasonality)')
    
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig