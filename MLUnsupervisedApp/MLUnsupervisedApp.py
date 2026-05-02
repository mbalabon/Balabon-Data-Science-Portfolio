# Import all my libraries
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer, load_iris, load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

from scipy.cluster.hierarchy import linkage, dendrogram

#Setting up streamlit

# This is the title that appears at the top of my Streamlit app
st.title("Unsupervised Machine Learning Explorer")

# This explains what my app is for
st.write("""
This app explores unsupervised machine learning using KMeans clustering, hierarchical clustering, and PCA.

Unsupervised learning is different from supervised learning because there is no labeled data. Unsupervised models look for patterns, groups, or structure in the data.
""")

# This explains how to use the app
st.write("""
Use the controls to change model settings and observe how the plots, scores,
and results change.
""")

# This gives the user an overview of what the app does
# The expander makes the explanation collapsible because it was a fun function from the streamlit cheat sheet and clears up space on the page
with st.expander("What this app does"):  #streamlit cheat sheet
    st.write("""
    - Choose a sample dataset or upload a CSV file
    - Select numeric columns to use for unsupervised learning
    - Scale the data so large-number columns do not overpower the results
    - Explore KMeans clustering, hierarchical clustering, and PCA
    - Change settings like the number of clusters, linkage method, and number of PCA components
    - View plots like PCA scatterplots, elbow plots, silhouette plots, dendrograms, and loading charts
    """)


#Loading data and setting up the sidebar

#The Sidebar

# The sidebar keeps the user controls separate from the main results
# This makes the app easier to use because settings are on the left and outputs are on the main page

st.header("Step 1: Load the Data")

# The sidebar lets the user choose where the data comes from
st.sidebar.header("1. Choose Data")

# The user can either use a built-in sample dataset or upload their own CSV file
data_choice = st.sidebar.radio(    #streamlit cheat sheet
    "How do you want to load data?",
    ["Use a sample dataset", "Upload a CSV"]
)

# If the user chooses a sample dataset, this lets them pick one
if data_choice == "Use a sample dataset":

    sample_dataset = st.sidebar.selectbox(
        "Choose a sample dataset",
        ["Breast Cancer", "Iris", "Wine"]
    )

    # Load the Breast Cancer dataset
    if sample_dataset == "Breast Cancer":
        data = load_breast_cancer()
        df = pd.DataFrame(data.data, columns=data.feature_names)

    # Load the Iris dataset
    elif sample_dataset == "Iris":
        data = load_iris()
        df = pd.DataFrame(data.data, columns=data.feature_names)

    # Load the Wine dataset
    else:
        data = load_wine()
        df = pd.DataFrame(data.data, columns=data.feature_names)

# If the user wants to upload their own CSV, this lets them do that
else:
    uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

    # If a file is uploaded, read it into a pandas DataFrame
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

    # If no file is uploaded, stop the app
    else:
        st.info("Please upload a CSV file to begin, or choose a sample dataset from the sidebar.")
        st.stop()


# Show the first few rows of the dataset
st.subheader("Dataset Preview")
st.dataframe(df.head())

# Show the shape of the dataset
st.write("Dataset shape:", df.shape)

# Show missing values
st.subheader("Missing Values by Column")
st.dataframe(df.isnull().sum())


#setting things up and choosing features






#Select number features

st.header("Step 2: Select Numeric Features")

# These models need numeric columns because PCA and clustering use math and distance calculations
# Text columns are not included here because, i did not use text encoding for this unsupervised app
numeric_columns = df.select_dtypes(include="number").columns.tolist()

# If there are not at least two numeric columns, the app cannot run PCA or clustering
if len(numeric_columns) < 2:
    st.error("This app needs at least two numeric columns.")
    st.stop()


# Let the user choose numeric columns
st.sidebar.header("2. Choose Features")

selected_features = st.sidebar.multiselect(
    "Choose numeric columns",
    numeric_columns,
    default=numeric_columns[:min(6, len(numeric_columns))]
)

# Stop the app if the user chooses fewer than two columns
if len(selected_features) < 2:
    st.warning("Please choose at least two numeric columns.")
    st.stop()

# Create a dataframe with only the selected features
features_df = df[selected_features].copy()

# Let the user choose how to handle missing values
st.sidebar.header("3. Clean Data")

missing_method = st.sidebar.radio(
    "How should missing values be handled?",
    ["Drop rows with missing values", "Fill missing values with column mean"]
)

# Drop rows with missing values
if missing_method == "Drop rows with missing values":
    features_df = features_df.dropna()

# fill missing values with the column mean
else:
    features_df = features_df.fillna(features_df.mean())

# Stop the app if there are too few rows left
if features_df.shape[0] < 5:
    st.error("There are not enough rows after cleaning.")
    st.stop()

# Show selected data
st.subheader("Selected Data")
st.dataframe(features_df.head())

st.write("Rows after cleaning:", features_df.shape[0])
st.write("Selected features:", selected_features)

#scaling the data

st.header("Step 3: Scale the Data")

# Scaling is important for PCA, KMeans, and hierarchical clustering
# If one column has very large numbers, it can overpower the model
# StandardScaler changes the columns so they have a mean of 0 and standard deviation of 1
st.write("""
The data is scaled using StandardScaler. This is important because PCA, KMeans,
and hierarchical clustering are affected by the scale of the variables.
""")

# Create the scaler
scaler = StandardScaler()

# Scale the selected features
X_scaled = scaler.fit_transform(features_df)

# Convert the scaled data back into a dataframe 
scaled_df = pd.DataFrame(X_scaled, columns=selected_features)

# Show scaled data in an expander
with st.expander("Show scaled data"): #streamlit cheat sheet
    st.dataframe(scaled_df.head())


#Choose an unsupervised learning model

st.header("Step 4: Choose and Run a Model")

st.write("""
Use the model controls below to experiment. After changing a setting, the plots and scores update automatically.
""")

st.sidebar.header("4. Choose Model")

# Let the user choose which unsupervised method to run
model_choice = st.sidebar.selectbox(
    "Choose a model",
    ["PCA", "KMeans Clustering", "Hierarchical Clustering"]
)

# This is used for cluster sliders and loops
max_k = min(10, features_df.shape[0] - 1)

# Method 1: PCA

if model_choice == "PCA":

    st.subheader("Principal Component Analysis")

    st.write("""
    PCA reduces the data into fewer components while keeping as much variation as possible.
    """)

    # Let the user choose how many components to keep
    max_components = min(len(selected_features), features_df.shape[0])

    n_components = st.slider(
        "Choose the number of principal components",
        2,
        max_components,
        min(2, max_components)
    )

    # Run PCA
    pca = PCA(n_components=n_components)
    X_pca = pca.fit_transform(X_scaled)

    # Explained variance
    explained_variance = pca.explained_variance_ratio_
    cumulative_variance = np.cumsum(explained_variance)

    st.subheader("Explained Variance")

    variance_df = pd.DataFrame({
        "Principal Component": [f"PC{i+1}" for i in range(n_components)],
        "Explained Variance": explained_variance,
        "Cumulative Explained Variance": cumulative_variance
    })

    st.dataframe(variance_df)

    # PCA scatterplot
    st.subheader("PCA Scatterplot")

    fig, ax = plt.subplots(figsize=(8, 6))

    ax.scatter(
        X_pca[:, 0],
        X_pca[:, 1],
        alpha=0.7,
        edgecolor="k",
        s=60
    )

    ax.set_xlabel("Principal Component 1")
    ax.set_ylabel("Principal Component 2")
    ax.set_title("PCA: 2D Projection of the Data")
    ax.grid(True)

    st.pyplot(fig)

    # Scree plot
    st.subheader("Scree Plot")

    fig, ax = plt.subplots(figsize=(8, 6))

    ax.plot(
        range(1, n_components + 1),
        cumulative_variance,
        marker="o"
    )

    ax.set_xlabel("Number of Components")
    ax.set_ylabel("Cumulative Explained Variance")
    ax.set_title("PCA Variance Explained")
    ax.set_xticks(range(1, n_components + 1))
    ax.grid(True)

    st.pyplot(fig)

    # PCA loadings for PC1 and PC2
    st.subheader("PCA Loadings")

    loadings_df = pd.DataFrame(
        pca.components_[:2],
        columns=selected_features,
        index=["PC1", "PC2"]
    )

    st.dataframe(loadings_df)

    st.write("""
The loadings show how much each original feature contributes to each principal component.
Larger positive or negative values mean that feature has a stronger influence.
""")

    # Loadings chart
    features = loadings_df.columns.tolist()
    y_pos = np.arange(len(features))
    bar_height = 0.3

    fig, ax = plt.subplots(figsize=(10, 8))

    ax.barh(
        y_pos + bar_height / 2,
        loadings_df.loc["PC1"],
        bar_height,
        label="PC1"
    )

    ax.barh(
        y_pos - bar_height / 2,
        loadings_df.loc["PC2"],
        bar_height,
        label="PC2"
    )

    ax.set_yticks(y_pos)
    ax.set_yticklabels(features)
    ax.set_xlabel("Loading Weight")
    ax.set_title("PCA Loadings")
    ax.axvline(0, color="grey", linewidth=0.8)
    ax.legend()
    ax.invert_yaxis()
    ax.grid(axis="x", alpha=0.3)

    plt.tight_layout()
    st.pyplot(fig)


#Method 2 KMeans Clustering

elif model_choice == "KMeans Clustering":

    st.subheader("KMeans Clustering")

    st.write("""
    KMeans clustering partitions the data into k clusters.
    """)

    # Let the user choose k
    k = st.slider("Choose the number of clusters (k)", 2, max_k, 2)

    # Run KMeans
    kmeans = KMeans(n_clusters=k, random_state=42)
    clusters = kmeans.fit_predict(X_scaled)

    # Show first cluster labels
    st.write("First 10 cluster labels:", clusters[:10])

    # Create results dataframe
    results = features_df.copy()
    results["Cluster"] = clusters

    st.subheader("Cluster Results")
    st.dataframe(results.head())

    st.subheader("Cluster Sizes")
    st.write(results["Cluster"].value_counts())

    # Silhouette score
    score = silhouette_score(X_scaled, clusters)

    st.subheader("Silhouette Score")
    st.write(score)

    st.write("""
The silhouette score helps show how separated the clusters are.
Higher values usually mean the clusters are more clearly separated.
""")

    # Use PCA for visualization
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)

    st.subheader("KMeans Clusters Shown with PCA")

    fig, ax = plt.subplots(figsize=(8, 6))

    for cluster_label in np.unique(clusters):
        indices = np.where(clusters == cluster_label)

        ax.scatter(
            X_pca[indices, 0],
            X_pca[indices, 1],
            alpha=0.7,
            edgecolor="k",
            s=60,
            label=f"Cluster {cluster_label}"
        )

    ax.set_xlabel("Principal Component 1")
    ax.set_ylabel("Principal Component 2")
    ax.set_title("KMeans Clustering Results")
    ax.legend(loc="best")
    ax.grid(True)

    st.pyplot(fig)

    # Evaluate different k values
    st.subheader("Evaluating the Best Number of Clusters")

    ks = range(2, max_k + 1)

    wcss = []
    silhouette_scores = []

    for temp_k in ks:
        km = KMeans(n_clusters=temp_k, random_state=42)
        km.fit(X_scaled)

        wcss.append(km.inertia_)

        labels = km.labels_
        silhouette_scores.append(silhouette_score(X_scaled, labels))

    # Plot elbow method
    fig, ax = plt.subplots(figsize=(8, 6))

    ax.plot(list(ks), wcss, marker="o")
    ax.set_xlabel("Number of clusters (k)")
    ax.set_ylabel("Within-Cluster Sum of Squares (WCSS)")
    ax.set_title("Elbow Method for Optimal k")
    ax.set_xticks(list(ks))
    ax.grid(True)

    st.pyplot(fig)

    # Plot silhouette scores
    fig, ax = plt.subplots(figsize=(8, 6))

    ax.plot(list(ks), silhouette_scores, marker="o")
    ax.set_xlabel("Number of clusters (k)")
    ax.set_ylabel("Silhouette Score")
    ax.set_title("Silhouette Score for Optimal k")
    ax.set_xticks(list(ks))
    ax.grid(True)

    st.pyplot(fig)

    best_k = list(ks)[np.argmax(silhouette_scores)]
    best_score = max(silhouette_scores)

    st.write(f"Best k by silhouette score: {best_k}")
    st.write("Best silhouette score:", best_score)

    #Create a table to show k changes the results
    kmeans_summary = pd.DataFrame({
        "k": list(ks),
        "WCSS": wcss,
        "Silhouette Score": silhouette_scores
    })

    st.subheader("KMeans k Comparison Table")
    st.dataframe(kmeans_summary)

#Method 3: Hierarchical Clustering

else:

    st.subheader("Hierarchical Clustering")

    st.write("""
    Hierarchical clustering builds a tree of clusters. The dendrogram helps decide
    how many clusters might make sense.
    """)

    # Choose linkage method
    linkage_method = st.selectbox(
        "Choose linkage method",
        ["ward", "complete", "average", "single"]
    )

    # Create dendrogram
    Z = linkage(X_scaled, method=linkage_method)

    fig, ax = plt.subplots(figsize=(12, 6))

    dendrogram(
        Z,
        ax=ax,
        no_labels=True
    )

    ax.set_title("Hierarchical Clustering Dendrogram")
    ax.set_xlabel("Observations")
    ax.set_ylabel("Distance")

    st.pyplot(fig)

    # Choose number of clusters
    k = st.slider("Choose the number of clusters", 2, max_k, 4)

    # Run agglomerative clustering
    agg = AgglomerativeClustering(n_clusters=k, linkage=linkage_method)
    cluster_labels = agg.fit_predict(X_scaled)

    # Create results dataframe
    results = features_df.copy()
    results["Cluster"] = cluster_labels

    st.subheader("Cluster Results")
    st.dataframe(results.head())

    st.subheader("Cluster Sizes")
    st.write(results["Cluster"].value_counts())

    # Silhouette score
    score = silhouette_score(X_scaled, cluster_labels)

    st.subheader("Silhouette Score")
    st.write(score)

    st.write("""
The silhouette score helps show how separated the clusters are.
Higher values usually mean the clusters are more clearly separated.
""")
    
    # PCA for visualization
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)

    st.subheader("Hierarchical Clusters Shown with PCA")

    fig, ax = plt.subplots(figsize=(8, 6))

    scatter = ax.scatter(
        X_pca[:, 0],
        X_pca[:, 1],
        c=cluster_labels,
        cmap="viridis",
        s=60,
        edgecolor="k",
        alpha=0.7
    )

    ax.set_xlabel("Principal Component 1")
    ax.set_ylabel("Principal Component 2")
    ax.set_title("Agglomerative Clustering Results")
    ax.legend(*scatter.legend_elements(), title="Clusters")
    ax.grid(True)

    st.pyplot(fig)

    # Silhouette score optimization
    st.subheader("Silhouette Analysis for Different Cluster Counts")

    k_range = range(2, max_k + 1)
    sil_scores = []

    for temp_k in k_range:
        labels = AgglomerativeClustering(
            n_clusters=temp_k,
            linkage=linkage_method
        ).fit_predict(X_scaled)

        score = silhouette_score(X_scaled, labels)
        sil_scores.append(score)

    fig, ax = plt.subplots(figsize=(8, 6))

    ax.plot(list(k_range), sil_scores, marker="o")
    ax.set_xlabel("Number of Clusters (k)")
    ax.set_ylabel("Average Silhouette Score")
    ax.set_title("Silhouette Analysis for Agglomerative Clustering")
    ax.set_xticks(list(k_range))
    ax.grid(True)

    st.pyplot(fig)

    best_k = list(k_range)[np.argmax(sil_scores)]
    best_score = max(sil_scores)

    st.write(f"Best k by silhouette score: {best_k}")
    st.write("Best silhouette score:", best_score)

    hierarchical_summary = pd.DataFrame({
        "Number of Clusters": list(k_range),
        "Silhouette Score": sil_scores
    })

    st.subheader("Hierarchical Clustering Comparison Table")
    st.dataframe(hierarchical_summary)

#End of my app

# The point of this app is experimentation
# The user can change the features, number of clusters, linkage method, or PCA components
# Then they can see how the plots and scores change
st.header("What to Try Next")

st.write("""
Try changing the selected features, the number of clusters, the linkage method,
or the number of PCA components.

Then look at how the plots and scores change. That's the point of this app:
to make unsupervised machine learning interactive and easier to understand!
""")