# Unsupervised Machine Learning Application Project

## Project Overview

This project builds an interactive unsupervised machine learning application that allow users to explore unsupervised learning methods through an intuitive interface that invites exploration and communicates results clearly. Users can choose from built-in datasets or upload their own CSV file, select numeric features, handle missing values, choose an unsupervised learning method, adjust model settings, and observe how these changes affect plots, scores, and cluster results. Unlike supervised learning, unsupervised learning does not use a response variable. Instead, the app focuses on finding patterns, groups, and structure in the data.

݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.

## App Interface Preview

The screenshots below show the app’s sidebar controls, dataset upload option, and example outputs from PCA, KMeans clustering, and hierarchical clustering.

### Dataset Selection and Controls

#### Sidebar Settings:
<img width="300" height="500" alt="Sidebar settings screenshot" src="https://github.com/user-attachments/assets/3c6e4f03-aacd-4b2e-bf83-328cc184b8ad" />

#### Uploading Your Own Dataset:
<img width="500" height="200" alt="Upload dataset screenshot" src="https://github.com/user-attachments/assets/28f25e72-bac2-4255-bf78-0e441e97988a" />

#### Uploaded Dataset Example:
<img width="500" height="300" alt="Upload dataset screenshot example" src="https://github.com/user-attachments/assets/ba6c7ad6-dcd2-477f-b679-f910cc7e22d2" />

݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ 

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

The app allows users to experiment unsupervised machine learning through these steps and see how different settings affect the results.

݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.

## Datasets Used in This Project

The app includes several built-in datasets:

- [🧬 Breast Cancer dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html)  
  Contains features computed from breast cancer cell nuclei.

- [🌸 Iris dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html)  
  Contains measurements of iris flowers.

- [🍷 Wine dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html)  
  Contains chemical properties of wines.

📂 Users can also upload their own CSV dataset.

Uploaded datasets need at least two numeric columns because PCA, KMeans clustering, and hierarchical clustering all require numeric data.

݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.

## Missing Data Options

The app includes missing data options:

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

The app checks that enough rows and numeric columns remain after cleaning. It also stops the app if missing values remain, since PCA, KMeans, and hierarchical clustering cannot run with missing values.

݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.

## Models, Methods, and Settings Used in This Project

The app includes three unsupervised learning methods: PCA, KMeans clustering, and hierarchical clustering. Each method includes interactive settings so users can experiment and observe how the results change.

### Principal Component Analysis (PCA)

PCA reduces the data into fewer principal components while keeping as much variation as possible. It is useful for visualizing high-dimensional data and understanding which features contribute most to the new components.

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

Changing the number of components affects the explained variance, scree plot, variance explained bar plot, and PCA loadings.

### KMeans Clustering

KMeans clustering partitions the data into a chosen number of clusters. It assigns points to clusters based on distance and updates cluster centers until the clusters stabilize.

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

Changing `k` affects the cluster labels, cluster sizes, cluster centroids, PCA cluster scatterplot, silhouette score, elbow plot, and silhouette score plot.

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

Changing the linkage method or number of clusters affects the dendrogram, cluster labels, cluster sizes, PCA cluster scatterplot, and silhouette score.

݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.

## Evaluation and Visualizations

The app provides performance feedback and visualization for each method. These outputs help users understand how model settings affect the results instead of only seeing a final answer.

### PCA visualizations

PCA includes a scatterplot, loadings chart, scree plot, and variance explained bar plot. These visuals help show how the data is projected into principal components and how much variation is captured.

#### PCA Scatterplot
<img width="728" height="617" alt="PCA scatterplot screenshot" src="https://github.com/user-attachments/assets/73bb2be0-ebe0-4f00-914e-b461469e5e3c" />

### KMeans visualizations

KMeans includes a PCA scatterplot of cluster assignments, an elbow plot using WCSS, a silhouette score plot, and a comparison table. These visuals help show how changing `k` affects the clustering results.

#### KMeans Elbow and Silhouette Plots
<img width="719" height="300" alt="KMeans elbow and silhouette plot screenshot" src="https://github.com/user-attachments/assets/9dba0516-59e7-495f-9ce9-a5ffa20eb894" />

### Hierarchical clustering visualizations

Hierarchical clustering includes a dendrogram, a PCA scatterplot of cluster assignments, a silhouette analysis plot, and a comparison table. These visuals help show how the linkage method and number of clusters affect the results.

#### Hierarchical Clustering Dendrogram
<img width="715" height="274" alt="Hierarchical dendrogram screenshot" src="https://github.com/user-attachments/assets/488aa3a0-a474-482d-a342-7fb4a5475df0" />

݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.

## Project Steps

The app follows these main steps:

1. Load and preview the dataset  
2. Inspect the dataset shape and missing values  
3. Select numeric features  
4. Handle missing data  
5. Scale the selected features  
6. Choose an unsupervised learning method  
7. Adjust method-specific settings  
8. Run PCA, KMeans clustering, or hierarchical clustering  
9. Generate plots, scores, and comparison tables  
10. Compare how different settings affect the results  

### Loading and Preparing the Data

Users can choose a built-in dataset or upload their own CSV file. Since PCA, KMeans, and hierarchical clustering rely on numeric values, the app selects numeric columns and lets users choose which features to include.

```python
numeric_columns = df.select_dtypes(include="number").columns.tolist()

selected_features = st.sidebar.multiselect(
    "Choose numeric columns",
    numeric_columns,
    default=numeric_columns[:min(6, len(numeric_columns))]
)
```

The app also includes missing data options from class notes, including dropping rows, dropping columns with more than 50% missing values, and imputing missing values with the mean, median, or zero. After cleaning, the app checks that there are enough rows and columns left before modeling.

### Scaling the Data

The app scales the selected features using `StandardScaler`. Scaling is important because PCA, KMeans, and hierarchical clustering are affected by the scale of the variables.

```python
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features_df)
```

### Choosing a Method

Users can choose between PCA, KMeans clustering, and hierarchical clustering.

```python
model_choice = st.sidebar.selectbox(
    "Choose a model",
    ["PCA", "KMeans Clustering", "Hierarchical Clustering"]
)
```

### Running PCA

For PCA, users choose the number of principal components. The app then shows explained variance, cumulative explained variance, a PCA scatterplot, PCA loadings, a scree plot, and a variance explained bar plot.

```python
pca = PCA(n_components=n_components)
X_pca = pca.fit_transform(X_scaled)

explained_variance = pca.explained_variance_ratio_
cumulative_variance = np.cumsum(explained_variance)
```

### Running KMeans Clustering

For KMeans clustering, users choose the number of clusters, `k`. The app displays cluster centroids, cluster labels, cluster sizes, a silhouette score, and PCA cluster visualizations.

```python
kmeans = KMeans(n_clusters=k, random_state=42)
clusters = kmeans.fit_predict(X_scaled)
```

The app also tests different values of `k` using WCSS and silhouette scores, then displays elbow and silhouette plots.

```python
for temp_k in ks:
    km = KMeans(n_clusters=temp_k, random_state=42)
    km.fit(X_scaled)
    wcss.append(km.inertia_)

    labels = km.labels_
    silhouette_scores.append(silhouette_score(X_scaled, labels))
```

### Running Hierarchical Clustering

For hierarchical clustering, users choose a linkage method and number of clusters. The app creates a dendrogram, assigns cluster labels, and uses PCA to show the clusters in two dimensions.

```python
Z = linkage(X_scaled, method=linkage_method)
dendrogram(Z, no_labels=True)

agg = AgglomerativeClustering(n_clusters=k, linkage=linkage_method)
cluster_labels = agg.fit_predict(X_scaled)
```

The app also tests different cluster counts using silhouette scores and displays a comparison table.

```python
for temp_k in k_range:
    labels = AgglomerativeClustering(
        n_clusters=temp_k,
        linkage=linkage_method
    ).fit_predict(X_scaled)

    score = silhouette_score(X_scaled, labels)
    sil_scores.append(score)
```

### Evaluating and Interpreting Results

The app evaluates and visualizes the results using explained variance, PCA scatterplots, PCA loadings, KMeans centroids, cluster sizes, elbow plots, silhouette scores, dendrograms, and comparison tables.

These outputs help users understand how different settings affect the results.

݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.

## How to Run This Project

### Live App

🔗 You can access the deployed app here:

[Streamlit App Link](https://mlunsupervisedapppy-gtrhzdntdsnsapphmthcqpd.streamlit.app/)

### Requirements

This project uses Python and the following libraries:

- streamlit
- pandas
- numpy
- matplotlib
- scikit-learn
- scipy

### Running the app locally

1. Download or clone the repository.
2. Open the project folder in VS Code.
3. Install the required libraries listed in [`requirements.txt`](https://github.com/mbalabon/Balabon-Data-Science-Portfolio/blob/main/MLUnsupervisedApp/requirements.txt)
4. Open the terminal and navigate to the `MLStreamlitApp` folder.
5. Run the app with:

```bash
streamlit run mlstreamlitapp.py
```

If running from the main repository folder, use:

```bash
streamlit run MLStreamlitApp/mlstreamlitapp.py
```

### Example import statements

```python
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer, load_iris, load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score, accuracy_score

from scipy.cluster.hierarchy import linkage, dendrogram
```

݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.

## 🔗 References

- [Scikit-learn info on the 🧬 Breast Cancer dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html)

- [Scikit-learn info on the 🌸 Iris dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html)

- [Scikit-learn info on the 🍷 Wine dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html)

- [Scikit-learn PCA documentation](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)

- [Streamlit Cheat Sheet](https://cheat-sheet.streamlit.app/)

- [Streamlit Cloud Instruction](https://docs.streamlit.io/get-started/installation/community-cloud)

- [Streamlit Managing dependencies when deploying your app](https://docs.streamlit.io/deploy/concepts/dependencies)
