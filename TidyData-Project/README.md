# Tidy Data Project: Federal Research and Development Spending

## Project Overview

This project applies tidy data principles to a federal research and development spending dataset. The original dataset was in a wide format, where each department appeared in one row and each year was stored in a separate column, and the column names combined two variables, year and GDP, into a single label.

The goal of this project was to clean and reorganize the dataset into tidy format so it would be easier to analyze and visualize. According to tidy data principles, each variable should have its own column, each observation should have its own row, and each type of unit should form a table.

After tidying the data, I performed an exploratory data analysis (EDA) to examine the distribution of spending, compare departments, and analyze changes in spending over time.

This project shows how tidying data improves the clarity, structure, and usability of a dataset for analysis in pandas.

݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.

## Tidy Data Principles Used in This Project

This project is based on the following tidy data ideas:

- Each variable should have its own column
- Each observation should have its own row
- Column names should contain variable names, not data values

In the original dataset, the year and GDP were combined inside the column names, which made the data harder to work with. I cleaned the dataset by:

- reshaping the data from wide format to long format using pd.melt()
- splitting the combined Year_GDP column into separate Year and GDP columns
- removing the old combined column
- renaming columns to be more clear
- sorting the data for easier reading and analysis

These steps made the data easier to summarize, group, and visualize.
݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.

## Dataset Description

The dataset contains federal research and development spending by department across multiple years. It includes departments such as DOD, HHS, NIH, NASA, DOE, and more.

Source:
Federal R&D Budgets dataset 

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

After cleaning, each row represents one department-year observation.

݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.

## Project Steps

The notebook follows these main steps:

1. Load the dataset with pandas
2. Inspect the original wide-format data
3. Check summary statistics and missing values
4. Melt the dataset from wide to long format
6. Split the combined `Year_GDP` column into separate `Year` and `GDP` columns
7. Clean and rename columns
8. Convert variables to the correct data types
9. Sort the tidy dataset
10. Perform exploratory data analysis and create visualizations
11. Build a pivot table summary

݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.

## Exploratory Data Analysis

### Visualizations included
- **Histogram** of research and development spending to show the overall distribution
- **Bar chart** of average spending by department to compare agencies
- **Line plot** of total spending over time to show trends across years

These visualizations were much easier to create after tidying the data, because the key variables were separated into their own columns.

݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.

## Main Findings

Some of the main findings from the project include:

- Spending values are **right-skewed**, meaning that most observations are at lower spending levels while a smaller number are much higher
- Federal research and development spending is concentrated in a few departments
- **DOD** has the highest average spending by a large margin, followed by departments such as **HHS**, **NIH**, **NASA**, and **DOE**
- Total federal research and development spending generally shows an **overall upward trend over time**, although it is not perfectly steady

These findings show how the cleaned dataset tells a clearer story than the original version.

݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.

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

### References

Pandas Cheat Sheet: (insert link to Pandas Cheat Sheet)

Tidy Data Paper by Hadley Wickham: (insert link to Tidy Data paper)
