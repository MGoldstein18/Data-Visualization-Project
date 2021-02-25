import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns

# load and "preview" all data
data = pd.read_csv('all_data.csv')
data.rename(columns={'Life expectancy at birth (years)': 'life_expectancy'}, inplace = True)
#print(data.head())

# function to explore number of countries and years covered in the data 
def explore_data(dataframe):
    countries = dataframe.Country.unique()
    years = dataframe.Year.unique()
    print('Print this dataframe contains data on the life expectancy and GDP of the following countries: {} over the following years: {}.'.format(countries, years))

# line plot of all countries life expectancy
def all_countries_life_expectancy(dataframe):
    sns.lineplot(data = dataframe, x = 'Year', y = 'life_expectancy', hue = 'Country')
    plt.title('All Countries - Life Expectancy')
    plt.show()

# line plot of all countries gdp
def all_countries_gdp(dataframe):
    sns.lineplot(data = dataframe, x = 'Year', y = 'GDP', hue = 'Country')
    plt.title('All Countries - GDP')
    plt.show()

#scatter plot of life expectancy vs gdp by country
def scatter_le_gdp(dataframe):
    sns.set_theme(style="whitegrid")
    sns.relplot(data = dataframe, x = 'life_expectancy', y = 'GDP', hue = 'Country')
    plt.title('All Countries - Life Expectancy vs GDP')
    plt.xlabel('Life Expectancy')
    plt.ylabel('GDP')
    plt.show()

#bar graph of mean of all countries life expectancy 
def bar_le(dataframe):
    plt.figure(figsize = (10,7))
    plt.title('Average Life Expectancy per Country')
    plt.ylabel('Life Expectancy')
    sns.set_palette('muted')
    sns.barplot(data = dataframe, x = 'Country', y = 'life_expectancy', ci = 'sd')
    plt.show()

# bar graph of mean of all countries GDP
def bar_gdp(dataframe):
    plt.figure(figsize = (12, 10))
    plt.title('Average GDP per Country')
    plt.ylabel('GDP')
    sns.set_palette('dark')
    sns.set_context('poster')
    sns.barplot(data = dataframe, x = 'Country', y = 'GDP', ci = 'sd')
    plt.show()
