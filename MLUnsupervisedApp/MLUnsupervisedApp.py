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

Unsupervised learning is different from supervised learning because there is no labeled data and no response variable. Unsupervised models look for patterns, groups, or structure in the data.
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
        y = data.target
        target_names = data.target_names

    # Load the Iris dataset
    elif sample_dataset == "Iris":
        data = load_iris()
        df = pd.DataFrame(data.data, columns=data.feature_names)
        y = data.target
        target_names = data.target_names

    # Load the Wine dataset
    else:
        data = load_wine()
        df = pd.DataFrame(data.data, columns=data.feature_names)
        y = data.target
        target_names = data.target_names

# If the user wants to upload their own CSV, this lets them do that
else:
    uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

    # If a file is uploaded, read it into a pandas DataFrame
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        y = None
        target_names = None

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

#select number features

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

# This follows the missing data options from my class notes
missing_method = st.sidebar.radio(
    "How should missing values be handled?",
    [
        "Original DF",
        "Drop Rows",
        "Drop Columns (>50% Missing)",
        "Impute Mean",
        "Impute Median",
        "Impute Zero"
    ]
)

# Apply the selected missing data handling method
if missing_method == "Original DF":
    pass

elif missing_method == "Drop Rows":
    features_df = features_df.dropna()

elif missing_method == "Drop Columns (>50% Missing)":
    features_df = features_df.drop(
        columns=features_df.columns[features_df.isnull().mean() > 0.5]
    )

elif missing_method == "Impute Mean":
    features_df = features_df.fillna(features_df.mean())

elif missing_method == "Impute Median":
    features_df = features_df.fillna(features_df.median())

elif missing_method == "Impute Zero":
    features_df = features_df.fillna(0)

# Stop the app if there are too few rows left
if features_df.shape[0] < 5:
    st.error("There are not enough rows after cleaning.")
    st.stop()

# Stop the app if there are too few columns left
if features_df.shape[1] < 2:
    st.error("There are not enough numeric columns after cleaning.")
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
    # In the notes, PCA is reduced to 2 components for visualization
    # Here, the user can choose the number of components
    pca = PCA(n_components=n_components)
    X_pca = pca.fit_transform(X_scaled)

    # Display the Explained Variance Ratio
    # This is the Streamlit version of the print statements from the notes
    explained_variance = pca.explained_variance_ratio_
    cumulative_variance = np.cumsum(explained_variance)

    st.subheader("Explained Variance")
    st.write("Explained Variance Ratio:", explained_variance)
    st.write("Cumulative Explained Variance:", cumulative_variance)

    # 3a. Scatter Plot of PCA Scores
    # This follows the plt.figure and plt.scatter style from the notes
    st.subheader("PCA Scatterplot")

    plt.figure(figsize=(8, 6))
    plt.scatter(
        X_pca[:, 0],
        X_pca[:, 1],
        alpha=0.7,
        edgecolor="k",
        s=60
    )
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.title("PCA: 2D Projection of the Data")
    plt.grid(True)
    st.pyplot(plt)

    # PCA Loadings
    # The notes build a DataFrame from pca.components_
    st.subheader("PCA Loadings")

    loadings_df = pd.DataFrame(
        pca.components_,
        columns=selected_features,
        index=[f"PC{i+1}" for i in range(pca.n_components_)]
    )

    st.dataframe(loadings_df)

    st.write("""
The loadings show how much each original feature contributes to each principal component.
A positive loading means higher values of that feature push a sample's score up along that component.
A negative loading means the opposite.
""")

    # PCA Loadings: Horizontal Grouped Bar Chart
    # This follows the grouped horizontal bar chart from the notes
    features = loadings_df.columns.tolist()
    y_pos = np.arange(len(features))
    bar_height = 0.3

    fig, ax = plt.subplots(figsize=(10, 10))

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
    ax.legend(loc="upper right")
    ax.invert_yaxis()
    ax.grid(axis="x", alpha=0.3)
    ax.set_frame_on(False)

    plt.tight_layout()
    st.pyplot(fig)

    # 3c. Scree Plot: Cumulative Explained Variance
    # This follows the notes by fitting a fuller PCA model
    st.subheader("Scree Plot: Cumulative Explained Variance")

    pca_full = PCA(n_components=max_components).fit(X_scaled)
    cumulative_variance_full = np.cumsum(pca_full.explained_variance_ratio_)

    plt.figure(figsize=(8, 6))
    plt.plot(
        range(1, len(cumulative_variance_full) + 1),
        cumulative_variance_full,
        marker="o"
    )
    plt.xlabel("Number of Components")
    plt.ylabel("Cumulative Explained Variance")
    plt.title("PCA Variance Explained")
    plt.xticks(range(1, len(cumulative_variance_full) + 1))
    plt.grid(True)
    st.pyplot(plt)

    # 3d. Bar Plot: Variance Explained by Each Component
    # This also comes from the PCA notes
    st.subheader("Variance Explained by Each Principal Component")

    plt.figure(figsize=(8, 6))
    components = range(1, len(pca_full.explained_variance_ratio_) + 1)
    plt.bar(
        components,
        pca_full.explained_variance_ratio_,
        alpha=0.7
    )
    plt.xlabel("Principal Component")
    plt.ylabel("Variance Explained")
    plt.title("Variance Explained by Each Principal Component")
    plt.xticks(components)
    plt.grid(True, axis="y")
    st.pyplot(plt)


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

    # Output the centroids and first few cluster assignments
    st.write("Centroids:")
    st.write(kmeans.cluster_centers_)
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

    # Reduce the data to 2 dimensions for visualization using PCA
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)

    # 3a. 2D Scatter Plot of Clustering Results Using PCA
    st.subheader("KMeans Clusters Shown with PCA")

    plt.figure(figsize=(8, 6))

    # Iterate over unique cluster labels
    for cluster_label in np.unique(clusters):

        # Get indices of data points belonging to the current cluster
        indices = np.where(clusters == cluster_label)

        # Scatter plot for the current cluster using the cluster label
        plt.scatter(
            X_pca[indices, 0],
            X_pca[indices, 1],
            alpha=0.7,
            edgecolor="k",
            s=60,
            label=f"Cluster {cluster_label}"
        )

    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.title("KMeans Clustering Results")
    plt.legend(loc="best")
    plt.grid(True)
    st.pyplot(plt)

    # 3b. Comparing Clusters with True Labels
    # This is only possible for the built-in sample datasets
    if y is not None:

        st.subheader("True Labels Shown with PCA")

        plt.figure(figsize=(8, 6))

        colors = ["navy", "darkorange", "green"]

        for i, target_name in enumerate(target_names):
            plt.scatter(
                X_pca[y == i, 0],
                X_pca[y == i, 1],
                color=colors[i],
                alpha=0.7,
                edgecolor="k",
                s=60,
                label=target_name
            )

        plt.xlabel("Principal Component 1")
        plt.ylabel("Principal Component 2")
        plt.title("True Labels: 2D PCA Projection")
        plt.legend(loc="best")
        plt.grid(True)
        st.pyplot(plt)

        # Accuracy score comparing KMeans clusters to true labels
        # This follows the KMeans notebook
        if len(np.unique(y)) == k:
            kmeans_accuracy = accuracy_score(y, clusters)

            st.subheader("Accuracy Score")
            st.write("Accuracy Score:", kmeans_accuracy)

        else:
            st.info("Accuracy is only shown when the number of clusters matches the number of true label groups.")

    else:
        st.info("True-label comparison is only available for the built-in sample datasets.")

    # Step 5: Evaluating the Best Number of Clusters
    st.subheader("Evaluating the Best Number of Clusters")

    st.write("""
The elbow plot shows how WCSS changes as k changes.
The silhouette plot shows how separated the clusters are for each k.
""")

    # Define the range of k values to try
    ks = range(2, max_k + 1)

    wcss = []               # Within-Cluster Sum of Squares for each k
    silhouette_scores = []  # Silhouette scores for each k

    # Loop over the range of k values
    for temp_k in ks:
        km = KMeans(n_clusters=temp_k, random_state=42)
        km.fit(X_scaled)

        # inertia: sum of squared distances within clusters
        wcss.append(km.inertia_)

        labels = km.labels_
        silhouette_scores.append(silhouette_score(X_scaled, labels))

    # Show the WCSS and silhouette score lists like the notebook prints them
    st.write("WCSS values:")
    st.write(wcss)

    st.write("Silhouette scores:")
    st.write(silhouette_scores)

    # Plot the Elbow Method and Silhouette Score results side by side
    plt.figure(figsize=(12, 5))

    # Plot the Elbow Method result
    plt.subplot(1, 2, 1)
    plt.plot(ks, wcss, marker="o")
    plt.xlabel("Number of clusters (k)")
    plt.ylabel("Within-Cluster Sum of Squares (WCSS)")
    plt.title("Elbow Method for Optimal k")
    plt.grid(True)

    # Plot the Silhouette Score result
    plt.subplot(1, 2, 2)
    plt.plot(ks, silhouette_scores, marker="o", color="green")
    plt.xlabel("Number of clusters (k)")
    plt.ylabel("Silhouette Score")
    plt.title("Silhouette Score for Optimal k")
    plt.grid(True)

    plt.tight_layout()
    st.pyplot(plt)

    best_k = list(ks)[np.argmax(silhouette_scores)]
    best_score = max(silhouette_scores)

    st.write(f"Best k by silhouette score: {best_k}")
    st.write("Best silhouette score:", best_score)

    # Create a table to show how k changes the results
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

    # Compute the linkage matrix
    Z = linkage(X_scaled, method=linkage_method)

    # Create dendrogram
    plt.figure(figsize=(20, 7))

    dendrogram(
        Z,
        no_labels=True
    )

    plt.title("Hierarchical Clustering Dendrogram")
    plt.xlabel("Observations")
    plt.ylabel("Distance")
    st.pyplot(plt)

    # Choose number of clusters
    k = st.slider("Choose the number of clusters", 2, max_k, 4)

    # Run agglomerative clustering
    agg = AgglomerativeClustering(n_clusters=k, linkage=linkage_method)
    cluster_labels = agg.fit_predict(X_scaled)

    # Create results dataframe
    results = features_df.copy()
    results["Cluster"] = cluster_labels

    # Show results like the notes print results.head()
    st.subheader("Cluster Results")
    st.dataframe(results.head())

    # Show cluster sizes like the notes print value_counts()
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

    # Low-Dimensional Insight with PCA
    # Note: PCA is only for display; it was not used to fit the clusters.
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)

    st.subheader("Hierarchical Clusters Shown with PCA")

    plt.figure(figsize=(10, 7))

    scatter = plt.scatter(
        X_pca[:, 0],
        X_pca[:, 1],
        c=cluster_labels,
        cmap="viridis",
        s=60,
        edgecolor="k",
        alpha=0.7
    )

    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.title("Agglomerative Clustering Results via PCA")
    plt.legend(*scatter.legend_elements(), title="Clusters")
    plt.grid(True)
    st.pyplot(plt)

    # Silhouette Score Optimization
    st.subheader("Silhouette Analysis for Different Cluster Counts")

    # Range of candidate cluster counts
    k_range = range(2, max_k + 1)
    sil_scores = []

    for temp_k in k_range:
        labels = AgglomerativeClustering(
            n_clusters=temp_k,
            linkage=linkage_method
        ).fit_predict(X_scaled)

        score = silhouette_score(X_scaled, labels)
        sil_scores.append(score)

    # Plot the curve
    plt.figure(figsize=(7, 4))
    plt.plot(list(k_range), sil_scores, marker="o")
    plt.xticks(list(k_range))
    plt.xlabel("Number of Clusters (k)")
    plt.ylabel("Average Silhouette Score")
    plt.title("Silhouette Analysis for Agglomerative Clustering")
    plt.grid(True, alpha=0.3)
    st.pyplot(plt)

    # Print best k
    best_k = list(k_range)[np.argmax(sil_scores)]

    st.write("Best k by silhouette:", best_k)
    st.write("Best silhouette score:", max(sil_scores))

    # Create a comparison table
    hierarchical_summary = pd.DataFrame({
        "Number of Clusters": list(k_range),
        "Silhouette Score": sil_scores
    })

    st.subheader("Hierarchical Clustering Comparison Table")
    st.dataframe(hierarchical_summary)

#End of my app

# The point of this app is experimentation
# The user can change the features, cleaning method, number of clusters, linkage method, or PCA components
# Then they can see how the plots, scores, and cluster results change
st.header("What to Try Next")

st.write("""
Try changing the selected features, cleaning method, number of clusters,
linkage method, or number of PCA components.

Then compare how the plots, scores, and cluster results change.
This helps show how different settings affect unsupervised machine learning results.
""")