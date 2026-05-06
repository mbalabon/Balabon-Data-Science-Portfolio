# Balabon-Data-Science-Portfolio
My Data Science Portfolio for Introduction to Data Science at the University of Notre Dame.

This repository contains my data science projects for the course.

₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁. ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ .  ⟡ ݁ . ⊹ ₊

## ⭐ About me: Macy Balabon

I am a Political Science major with a Data Science minor at the University of Notre Dame. I am interested in using data analysis and visualization to better understand real-world problems, particularly in policy, economics, and social systems.

This portfolio shows my experience with machine learning models, data cleaning, exploratory data analysis, and building interactive data applications using Python.

## What i'm learning! 

- Python
- Data Cleaning & Tidy Data Principles
- Exploratory Data Analysis (EDA)
- Data Visualization
- Interactive App Development
- Machine Learning

## Table of Contents: My Portfolio at a glance!

| Project | Repository | Description |
|---|---|---|
| [Unsupervised Machine Learning Explorer App](#-unsupervised-machine-learning-explorer-app-streamlit) | [View Project Repository](https://github.com/mbalabon/Balabon-Data-Science-Portfolio/tree/main/MLUnsupervisedApp) | Unsupervised ML app using PCA, KMeans, and hierarchical clustering |
| [Machine Learning Explorer App](#-machine-learning-explorer-app-streamlit) | [View Project Repository](https://github.com/mbalabon/Balabon-Data-Science-Portfolio/tree/main/MLStreamlitApp) | Supervised ML app using Linear Regression, Logistic Regression, Decision Trees, and KNN |
| [Tidy Data Project](#-tidy-data-project-federal-research--development-spending) | [View Project Repository](https://github.com/mbalabon/Balabon-Data-Science-Portfolio/tree/main/TidyData-Project) | Cleaning and reshaping federal R&D spending data |
| [Spotify Track Analysis App](#-spotify-track-analysis-app-streamlit) | [View Project Repository](https://github.com/mbalabon/Balabon-Data-Science-Portfolio/tree/main/basic_streamlit_app) | Interactive Streamlit app for exploring Spotify track data |

₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁. ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ .

## Projects
₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.

### ★ Unsupervised Machine Learning Explorer App (Streamlit)

🔗 [View Project Repository](https://github.com/mbalabon/Balabon-Data-Science-Portfolio/tree/main/MLUnsupervisedApp)

You can access the deployed app here:

🔗 [Streamlit App Link](https://mlunsupervisedapppy-gtrhzdntdsnsapphmthcqpd.streamlit.app/)

This project is an interactive unsupervised machine learning application built using Streamlit. The app allows users to explore patterns, groups, and structure in data without using a response variable.

#### Users can:
- choose from built-in datasets (Breast Cancer, Iris, Wine)
- upload their own CSV dataset
- select numeric features
- handle missing values
- scale the data with `StandardScaler`
- choose an unsupervised learning method
- adjust model settings and observe how the results change

#### Key Features
- Interactive sidebar controls for dataset selection, feature selection, cleaning method, and model choice
- Missing data options including drop rows, drop columns, impute mean, impute median, and impute zero
- PCA with explained variance, cumulative explained variance, scatterplots, loadings, scree plot, and variance explained bar plot
- KMeans clustering with adjustable `k`, cluster centroids, cluster labels, cluster sizes, silhouette score, elbow plot, silhouette plot, and comparison table
- Hierarchical clustering with adjustable linkage method and number of clusters, dendrogram, PCA cluster visualization, silhouette analysis, and comparison table

#### Example Code

The app scales the selected numeric features before running PCA, KMeans, or hierarchical clustering.

```python
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features_df)
```

For KMeans clustering, the app lets users choose the number of clusters and then fits the model to the scaled data.

```python
kmeans = KMeans(n_clusters=k, random_state=42)
clusters = kmeans.fit_predict(X_scaled)
```

The app also compares different values of `k` using WCSS and silhouette scores.

```python
ks = range(2, max_k + 1)

wcss = []
silhouette_scores = []

for temp_k in ks:
    km = KMeans(n_clusters=temp_k, random_state=42)
    km.fit(X_scaled)

    wcss.append(km.inertia_)

    labels = km.labels_
    silhouette_scores.append(silhouette_score(X_scaled, labels))
```

#### Visualizations:
- PCA scatterplot
- PCA loadings chart
- scree plot
- variance explained bar plot
- KMeans elbow plot
- KMeans silhouette score plot
- hierarchical clustering dendrogram
- PCA cluster scatterplots
- clustering comparison tables

<img width="719" height="300" alt="KMeans elbow and silhouette plot screenshot" src="https://github.com/user-attachments/assets/9dba0516-59e7-495f-9ce9-a5ffa20eb894" />

#### Why This Project Matters

This project demonstrates:
- understanding of unsupervised machine learning workflows
- ability to use PCA for dimensionality reduction and visualization
- ability to use KMeans and hierarchical clustering to find structure in data
- use of silhouette scores, elbow plots, dendrograms, and PCA visualizations to evaluate and explain results
- development of a fully interactive machine learning app that encourages experimentation

It complements my supervised machine learning app by showing a different side of machine learning. While the supervised app focuses on prediction with a target variable, this app focuses on discovering hidden patterns in data. Together, the two projects show my ability to build interactive machine learning tools for both prediction and exploration.

₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁. ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ .

### ★ Machine Learning Explorer App (Streamlit)

🔗 [View Project Repository](https://github.com/mbalabon/Balabon-Data-Science-Portfolio/tree/main/MLStreamlitApp)

You can access the deployed app here:

🔗 [Streamlit App Link](https://balabon-data-science-portfolio-zvzmhdruy93jxp92jm5edc.streamlit.app/)

This project is an interactive machine learning application built using Streamlit that allows users to explore supervised learning models in a hands-on way!

#### Users can:
- choose from built-in datasets (Breast Cancer, Diabetes, Iris, Wine)
- upload their own dataset
- select a model (Linear Regression, Logistic Regression, Decision Tree, KNN)
- adjust hyperparameters such as test size, max depth, min_samples_split, and number of neighbors
- view model performance through metrics and visualizations

#### Key Features
- Interactive sidebar controls for dataset and model selection
- Model training and prediction
- Multiple evaluation outputs:
-   confusion matrix
-   classification report
-   ROC curve and AUC
-   regression metrics (MSE, RMSE, R²)
- Visualizations:
-   confusion matrix heatmap
-   ROC curve
-   accuracy vs. k (KNN)
-   actual vs predicted scatter plot
-   decision tree visualization

<img width="924" height="741" alt="Screenshot 2026-04-12 at 4 09 27 PM" src="https://github.com/user-attachments/assets/477e5f1d-7136-441f-961a-07490bf3f40e" />


#### Why This Project Matters

This project demonstrates:
- understanding of core machine learning workflows (X and y, train/test split, model training, evaluation)
- ability to implement and compare multiple supervised learning models
- use of hyperparameter tuning to explore model performance
- development of a fully interactive, user-facing data application

It complements my portfolio by extending beyond data cleaning and basic interactivity into **model building and deployment**. While my tidy data project focuses on preparing data and my Spotify app focuses on exploration, this project shows how to **apply machine learning models and present results interactively to users.**

₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁. ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ .

### ★ Tidy Data Project: Federal Research & Development Spending

🔗 [View Project Repository](https://github.com/mbalabon/Balabon-Data-Science-Portfolio/tree/main/TidyData-Project)

This project focuses on cleaning and restructuring a federal R&D spending dataset using tidy data principles.

#### The original dataset was in a wide format, where:
- each department was one row
- each year was a separate column
- column names combined both year and GDP

#### I transformed the dataset into a tidy format where:
- each variable has its own column
- each observation is one row
- the dataset is easier to analyze and visualize

#### After cleaning the data, I conducted exploratory data analysis to examine:
- distribution of spending
- differences between departments
- trends in spending over time

#### Key Skills Demonstrated
- Data reshaping with pd.melt()
- String manipulation and column splitting
- Data type conversion
- Grouping and aggregation
- Data visualization (histogram, bar chart, line plot, pivot table)

#### Example Code
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
#### Example Visualization

Line plot of total spending over time to show trends across years
<img width="1126" height="898" alt="image" src="https://github.com/user-attachments/assets/73169612-3363-4f4c-835c-7fe47bd26a2d" />

#### Why This Project Matters

This project shows my ability to:

- take messy, real-world data and clean it
- apply structured data principles (tidy data)
- connect data cleaning directly to better analysis and visualization

It complements my portfolio by demonstrating strong data wrangling skills, which are essential before any meaningful analysis can happen.

₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁. ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ .

### ★ Spotify Track Analysis App (Streamlit)

🔗 [View Project Repository](https://github.com/mbalabon/Balabon-Data-Science-Portfolio/tree/main/basic_streamlit_app)

This project is an interactive data analysis app built using Streamlit that allows users to explore a [Spotify dataset](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset).

#### Users can filter tracks by:
- genre
- explicit vs non-explicit
- popularity
- danceability

The app updates in real time and displays filtered datasets, summary statistics, and visualizations.

#### Key Features
- Interactive filters using dropdowns and sliders
- Real-time dataset updates
- Multiple visualizations:
-   boxplot (popularity vs explicitness)
-   scatterplot (danceability vs energy)
-   bar chart (average popularity)

<img width="726" height="620" alt="Screenshot 2026-03-19 at 4 23 44 PM" src="https://github.com/user-attachments/assets/a89e60e1-6f09-46dd-a193-ee5ab5106542" /><img width="733" height="616" alt="Screenshot 2026-03-19 at 4 23 53 PM" src="https://github.com/user-attachments/assets/5c4b42b1-5262-44af-a33f-ddb591877378" /><img width="746" height="630" alt="Screenshot 2026-03-19 at 4 24 00 PM" src="https://github.com/user-attachments/assets/230b6646-3e6f-44ce-8a00-835266497072" />

#### Why This Project Matters

This project demonstrates:
- ability to build interactive data tools
- understanding of how users interact with data
- combining data filtering, analysis, and visualization in one application

It complements my portfolio by showing applied, user-facing data skills, while my tidy data project shows behind the scenes data preparation.
