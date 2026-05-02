# Unsupervised Machine Learning Application Project

## Project Overview

This project builds an interactive unsupervised machine learning application using Python and Streamlit. The goal of the app is to allow users to explore unsupervised learning methods through an intuitive interface that invites exploration and communicates results clearly.

Users can choose from built-in datasets or upload their own CSV file, select numeric features, handle missing values, adjust model settings, and observe how these changes affect clustering results, PCA visualizations, and evaluation scores.

The app focuses on finding patterns, groups, and structure in data without using a response variable.

݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.

## App Interface Preview

The screenshots below show the app’s sidebar controls, dataset selection options, and examples of PCA, KMeans clustering, and hierarchical clustering outputs.

### Dataset Selection and Controls

#### Sidebar Settings:
<img width="300" height="500" alt="Sidebar settings screenshot" src="https://github.com/user-attachments/assets/3c6e4f03-aacd-4b2e-bf83-328cc184b8ad" />

#### Uploading Your Own Dataset:
<img width="500" height="200" alt="Upload dataset screenshot" src="https://github.com/user-attachments/assets/28f25e72-bac2-4255-bf78-0e441e97988a" />


<img width="500" height="300" alt="Upload dataset screenshot: Example" src="https://github.com/user-attachments/assets/ba6c7ad6-dcd2-477f-b679-f910cc7e22d2" />


### Example Model Outputs

#### PCA Scatterplot:
<img width="728" height="617" alt="PCA scatterplot screenshot" src="https://github.com/user-attachments/assets/73bb2be0-ebe0-4f00-914e-b461469e5e3c" />

#### KMeans Elbow and Silhouette Plots:
<img width="719" height="300" alt="KMeans plots screenshot" src="https://github.com/user-attachments/assets/9dba0516-59e7-495f-9ce9-a5ffa20eb894" />

#### Hierarchical Clustering Dendrogram:
<!-- Add screenshot here -->
<img width="800" alt="Hierarchical dendrogram screenshot" src="PASTE_SCREENSHOT_LINK_HERE" />
<img width="715" height="274" alt="Hierarchical dendrogram screenshot" src="https://github.com/user-attachments/assets/488aa3a0-a474-482d-a342-7fb4a5475df0" />


݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.

## Machine Learning Concepts Used in This Project

This project is based on the following unsupervised learning ideas from class:

- Using unsupervised learning when there is no response variable
- Selecting numeric features for analysis
- Handling missing values before modeling
- Scaling data with `StandardScaler`
- Reducing dimensionality with PCA
- Finding groups with KMeans clustering
- Building cluster trees with hierarchical clustering
- Evaluating clusters with silhouette scores
- Comparing different values of `k`
- Using visualizations to interpret model results

The app allows users to experiment with these steps interactively and see how changes impact the results.

݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.

## Datasets Used in This Project

The app includes several built-in datasets:

- [🧬 Breast Cancer dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html)  
  Contains features computed from breast cancer cell nuclei.

- [🌸 Iris dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html)  
  Contains measurements of iris flowers.

- [🍷 Wine dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html)  
  Contains chemical properties of wines.

📂 Users can also upload their own CSV dataset.

Uploaded datasets need at least two numeric columns because PCA, KMeans, and hierarchical clustering all require numeric data.

݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.

## Missing Data Options

The app includes missing data options based on class notes:

- **Original DF**  
  Keeps the selected data unchanged.

- **Drop Rows**  
  Removes rows with missing values.

- **Drop Columns (>50% Missing)**  
  Removes columns where more than 50% of the values are missing.

- **Impute Mean**  
  Replaces missing values with the column mean.

- **Impute Median**  
  Replaces missing values with the column median.

- **Impute Zero**  
  Replaces missing values with zero.

The app also checks that enough rows and numeric columns remain after cleaning before running the models.

݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.

## Models and Methods Used in This Project

The app includes three unsupervised learning methods:

### Principal Component Analysis (PCA)

PCA reduces the data into fewer principal components while keeping as much variation as possible.

Users can adjust:

- **number of principal components**: controls how many PCA components are kept

The PCA section includes:

- explained variance ratio
- cumulative explained variance
- PCA scatterplot
- PCA loadings table
- PCA loadings chart
- scree plot
- variance explained bar plot

### KMeans Clustering

KMeans clustering partitions the data into a chosen number of clusters.

Users can adjust:

- **k**: controls the number of clusters

The KMeans section includes:

- cluster centroids
- first 10 cluster labels
- cluster results table
- cluster sizes
- silhouette score
- PCA scatterplot of KMeans clusters
- true-label comparison for built-in datasets
- WCSS values
- silhouette scores for different `k` values
- elbow plot
- silhouette score plot
- KMeans comparison table

### Hierarchical Clustering

Hierarchical clustering builds a tree of clusters. The dendrogram helps users decide how many clusters might make sense.

Users can adjust:

- **linkage method**: controls how distances between clusters are measured
- **number of clusters**: controls how many final clusters are created

The hierarchical clustering section includes:

- dendrogram
- cluster results table
- cluster sizes
- silhouette score
- PCA scatterplot of hierarchical clusters
- silhouette analysis for different cluster counts
- hierarchical clustering comparison table

݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.

## Evaluation and Visualizations

The app provides several forms of performance feedback and visualization.

### PCA visualizations:
- PCA scatterplot
- PCA loadings chart
- scree plot
- variance explained bar plot

### KMeans visualizations:
- PCA scatterplot of cluster assignments
- elbow plot using WCSS
- silhouette score plot
- KMeans comparison table

### Hierarchical clustering visualizations:
- dendrogram
- PCA scatterplot of cluster assignments
- silhouette analysis plot
- hierarchical clustering comparison table

These outputs help users understand how model settings affect the results instead of only seeing a final answer.

݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.

## Project Steps

The app follows these main steps:

1. Load and preview the dataset
2. Inspect the dataset shape and missing values
3. Select numeric features
4. Handle missing data
5. Scale the selected features using `StandardScaler`

#### Example from the app
```python
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features_df)
