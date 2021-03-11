import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column

def isOverweight(row):
    metersHeight = row['height'] / 100
    bmi = (row['weight'] / metersHeight) / metersHeight
    if bmi > 25:
        return 1
    return 0
df['overweight'] = df.apply(lambda row: isOverweight(row),axis=1)
# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
def normalizeCholesterol(row):
    if row['cholesterol'] == 1:
        return 0
    return 1

def normalizeGluc(row):
    if row['gluc'] == 1:
        return 0
    return 1
df['cholesterol']   = df.apply(lambda row: normalizeCholesterol(row),axis=1)
df['gluc']          = df.apply(lambda row: normalizeGluc(row),axis=1)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = None

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
    df_cat = df.melt(id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active','overweight'])

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(x="variable", kind = "count", data=df_cat, hue = 'value', col= 'cardio').set_axis_labels('variable', 'total').fig


    # Do not modify the next two line
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = None

    # Calculate the correlation matrix
    corr = None

    # Generate a mask for the upper triangle
    mask = None


    # Set up the matplotlib figure
    # fig, ax = None

    # Draw the heatmap with 'sns.heatmap()'



    # Do not modify the next two lines
    # fig.savefig('heatmap.png')
    # return fig
