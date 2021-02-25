# Data Visualization Project
This is a data visualization project which uses pandas, matplotlib and seaborn to load, manipulate and visualize data to understand the relationship between life expectancy and GDP in several countries. 

### There are the following functions in script.py:
1. explore_data - This function takes the dataframe as an argument and print a sentence with information about the number of countries and years covered in the data.
2. all_countries_life_expectancy and all_countries_gdp - These functions create Seaborn to show the how the life expectancy and gdp of each country have changed over time
3. scatter_le_gdp - This function creates Seaborn scatter plot to show the Life Expectancy vs GDP for each country. 
4. bar_le and bar_gdp - These function show the means of each country's life expectancy and GDP in Seaborn bar graphs. 

### Key Insights from Analysis:
- It seems clear that a GDP and life expectancy are somewhat correlated - countries with higher average GDPs tend to have higher average life expectancies. 
- It is also clear that there are not perfectly correlated and that the two can increase independently - see Zimbabwe as a good example. 