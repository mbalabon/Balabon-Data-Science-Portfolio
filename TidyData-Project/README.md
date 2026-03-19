# Tidy Data Project: Federal Research and Development Spending

## Project Overview

This project applies tidy data principles to a federal research and development spending dataset. The original dataset was in a wide format, where each department appeared in one row and each year was stored in a separate column, and the column names combined two variables, year and GDP, into a single label.

The goal of this project was to clean and reorganize the dataset into tidy format so it would be easier to analyze and visualize. According to tidy data principles, each variable should have its own column, each observation should have its own row, and each type of unit should form a table.

After tidying the data, I performed an exploratory data analysis (EDA) to examine the distribution of spending, compare departments, and analyze changes in spending over time.

This project shows how tidying data improves the clarity, structure, and usability of a dataset for analysis in pandas.

݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁. ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ 

## Tidy Data Principles Used in This Project

This project is based on the following tidy data ideas:

- Each variable should have its own column
- Each observation should have its own row
- Column names should contain variable names, not data values

Original Dataset:<img width="1368" height="250" alt="Screenshot 2026-03-19 at 3 32 59 PM" src="https://github.com/user-attachments/assets/bbf5b40b-888c-4c52-810e-cfd56ad99f25" />
<img width="596" height="549" alt="Screenshot 2026-03-19 at 3 43 36 PM" src="https://github.com/user-attachments/assets/c4ebf60a-0d3b-4922-a552-768186a99a7d" />


In the original dataset, the year and GDP were combined inside the column names (as seen above), which made the data harder to work with. I cleaned the dataset by:

- reshaping the data from wide format to long format using pd.melt()
- splitting the combined Year_GDP column into separate Year and GDP columns
- removing the old combined column
- renaming columns to be more clear
- sorting the data for easier reading and analysis

These steps made the data easier to summarize, group, and visualize.

݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁. ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ 

## Dataset Description

The dataset contains federal research and development spending by department across multiple years. It includes departments such as DOD, HHS, NIH, NASA, DOE, and more.

Source:
[Federal R&D Budgets dataset](https://github.com/EliCash82/mutantmoneyball/tree/main)

### Original dataset characteristics
- One row per department
- One column per year
- Year and GDP combined in column names
- Missing values for some department-year combinations, especially DHS in earlier years

### Cleaned dataset variables
- `department`
- `Research_and_Development_Spending`
- `Year`
- `GDP`

<img width="533" height="250" alt="Screenshot 2026-03-19 at 3 36 54 PM" src="https://github.com/user-attachments/assets/8baeaf94-a03c-41ca-a1b2-1a697ab9bb3e" />


After cleaning, each row represents one department-year observation.

݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁. ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ 

## Project Steps

The notebook follows these main steps:

1. Load the dataset with pandas
2. Inspect the original wide-format data
3. Check summary statistics and missing values
4. Melt the dataset from wide to long format

```
df_melted = pd.melt(df,
    id_vars=['department'],
    value_vars = [
    '1976_gdp1790000000000.0',
    '1977_gdp2028000000000.0',
    '1978_gdp2278000000000.0',
    '1979_gdp2570000000000.0',
    '1980_gdp2797000000000.0',
    '1981_gdp3138000000000.0',
    '1982_gdp3314000000000.0',
    '1983_gdp3541000000000.0',
    '1984_gdp3953000000000.0',
    '1985_gdp4270000000000.0',
    '1986_gdp4536000000000.0',
    '1987_gdp4782000000000.0',
    '1988_gdp5155000000000.0',
    '1989_gdp5570000000000.0',
    '1990_gdp5915000000000.0',
    '1991_gdp6110000000000.0',
    '1992_gdp6435000000000.0',
    '1993_gdp6795000000000.0',
    '1994_gdp7198000000000.0',
    '1995_gdp7583000000000.0',
    '1996_gdp7978000000000.0',
    '1997_gdp8483000000000.0',
    '1998_gdp8955000000000.0',
    '1999_gdp9511000000000.0',
    '2000_gdp10148000000000.0',
    '2001_gdp10565000000000.0',
    '2002_gdp10877000000000.0',
    '2003_gdp11332000000000.0',
    '2004_gdp12089000000000.0',
    '2005_gdp12889000000000.0',
    '2006_gdp13685000000000.0',
    '2007_gdp14323000000000.0',
    '2008_gdp14752000000000.0',
    '2009_gdp14415000000000.0',
    '2010_gdp14799000000000.0',
    '2011_gdp15379000000000.0',
    '2012_gdp16027000000000.0',
    '2013_gdp16516000000000.0',
    '2014_gdp17244000000000.0',
    '2015_gdp17983000000000.0',
    '2016_gdp18470000000000.0',
    '2017_gdp19177000000000.0'],
    var_name='Year_GDP',
    value_name='R_D_Spending'
)

print("\nMelted DataFrame:")
print(df_melted)
```

6. Split the combined `Year_GDP` column into separate `Year` and `GDP` columns

```
df_melted[['Year', 'GDP']] = df_melted['Year_GDP'].str.split('_gdp', expand=True)

print("\nDataFrame after splitting Year_GDP:")
print(df_melted.head())
```

8. Clean and rename columns
9. Convert variables to the correct data types
10. Sort the tidy dataset
11. Perform exploratory data analysis and create visualizations
12. Build a pivot table summary

```pivot_department_mean = pd.pivot_table(
    df_tidy,
    values='Research_and_Development_Spending',
    index='department',
    aggfunc='mean'
)

pivot_department_mean = pivot_department_mean.sort_values(
    by='Research_and_Development_Spending',
    ascending=False
)

print(pivot_department_mean)
```

݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁. ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ 

## Exploratory Data Analysis

### Visualizations included
- **Histogram** of research and development spending to show the overall distribution
<img width="570" height="453" alt="Screenshot 2026-03-19 at 3 40 15 PM" src="https://github.com/user-attachments/assets/4a09d629-595f-4c2f-8da9-8c9349f952be" />

- **Bar chart** of average spending by department to compare agencies
<img width="553" height="482" alt="Screenshot 2026-03-19 at 3 41 21 PM" src="https://github.com/user-attachments/assets/eb38cf00-7298-41c4-86d3-723e145bc022" />

- **Line plot** of total spending over time to show trends across years
<img width="563" height="449" alt="Screenshot 2026-03-19 at 3 41 45 PM" src="https://github.com/user-attachments/assets/c4d73ac0-51ee-4256-a47c-b68b13604382" />

These visualizations were much easier to create after tidying the data, because the key variables were separated into their own columns.

݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁. ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ 

## Main Findings

Some of the main findings from the project include:

- Spending values are **right-skewed**, meaning that most observations are at lower spending levels while a smaller number are much higher
- Federal research and development spending is concentrated in a few departments
- **DOD** has the highest average spending by a large margin, followed by departments such as **HHS**, **NIH**, **NASA**, and **DOE**
- Total federal research and development spending generally shows an **overall upward trend over time**, although it is not perfectly steady

These findings show how the cleaned dataset tells a clearer story than the original version.

݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁. ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ 

## How to Run This Project

### Requirements
This project uses Python and the following libraries:

- pandas
- seaborn
- matplotlib

### Running the notebook
1. Download the repository
2. Make sure the dataset file is in the correct folder
3. Open the Jupyter Notebook
4. Run the cells in order from top to bottom

### Example import statements
```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
```

₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁. ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ 

## References

[Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)

[Tidy Data Paper by Hadley Wickham](https://vita.had.co.nz/papers/tidy-data.pdf)

[Pandas instructions on pandas.Series.str.split](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.split.html)
