import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import graphviz
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.metrics import roc_curve, roc_auc_score
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import tree

# Set the title of the Streamlit app

# from the Streamlit cheat sheet
st.set_page_config(page_title="Machine Learning Explorer", layout="wide")

stars = "₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁. ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁₊ ⊹ . ݁ ⟡ ݁ "

st.title("☆ Machine Learning Models ☆")
st.markdown(stars)

st.write(
    "This app is designed to explore supervised machine learning models by choosing a sample dataset or uploading your own CSV file, "
    "selecting a model, adjusting hyperparameters, and viewing model performance."
)

#Choosing the dataset

# from the Streamlit cheat sheet
st.sidebar.header("1. Choose Dataset")

dataset = st.sidebar.selectbox(
    "Dataset",
    ["Breast Cancer", "Diabetes", "Iris", "Wine", "Upload Your Own"]
)

df = None

if dataset == "Breast Cancer":
    from sklearn.datasets import load_breast_cancer
    data = load_breast_cancer(as_frame=True)
    df = data.frame
    target = "target"
    st.info("🧬 This dataset contains features computed from breast cancer cell nuclei.")

elif dataset == "Diabetes":
    from sklearn.datasets import load_diabetes
    data = load_diabetes(as_frame=True)
    df = data.frame
    target = "target"
    st.info("🩺 This dataset contains medical features used to predict disease progression.")

elif dataset == "Iris":
    from sklearn.datasets import load_iris
    data = load_iris(as_frame=True)
    df = data.frame
    target = "target"
    st.info("🌸 This dataset contains measurements of iris flowers.")

elif dataset == "Wine":
    from sklearn.datasets import load_wine
    data = load_wine(as_frame=True)
    df = data.frame
    target = "target"
    st.info("🍷 This dataset contains chemical properties of wines.")

elif dataset == "Upload Your Own":
    uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.info("📂 Upload your own dataset and explore how different models perform.")

if df is None:
    st.info("Please choose a dataset or upload a CSV file.")
    st.stop()


# data preview

st.header("📊 Dataset Preview")

# from the Streamlit cheat sheet
col1, col2 = st.columns(2)

with col1:
    st.subheader("First Five Rows")
    st.dataframe(df.head())

with col2:
    st.subheader("Dataset Information")
    st.write("Shape:")
    st.write(df.shape)

    st.write("Data Types:")
    st.write(df.dtypes)

st.subheader("Summary Statistics")
st.write(df.describe())

st.subheader("Missing Values by Column")
st.write(df.isnull().sum())

# selecting the target variable
st.sidebar.header("2. Select Target Column")

if dataset == "Upload Your Own":
    target = st.sidebar.selectbox("Target Column", df.columns)

#preparing the data for modeling
if dataset == "Breast Cancer":
    features = df.columns.drop("target")
    X = df[features]
    y = df["target"]

elif dataset == "Diabetes":
    features = df.columns.drop("target")
    X = df[features]
    y = df["target"]

elif dataset == "Iris":
    features = df.columns.drop("target")
    X = df[features]
    y = df["target"]

elif dataset == "Wine":
    features = df.columns.drop("target")
    X = df[features]
    y = df["target"]

elif dataset == "Upload Your Own":
    features = [col for col in df.columns if col != target]
    X = df[features]
    y = df[target]

#choosing the model

st.sidebar.header("4. Choose Model")

if dataset == "Diabetes":
    model_name = st.sidebar.selectbox(
        "Model",
        ["Linear Regression"]
    )
else:
    model_name = st.sidebar.selectbox(
        "Model",
        ["Logistic Regression", "Decision Tree", "KNN"]
    )

st.header("🤖 Model Description")

if model_name == "Linear Regression":
    st.write(
        "Linear Regression predicts a continuous target. "
        "Linear Regression is evaluated using Mean Squared Error, Root Mean Squared Error, and R²."
    )

elif model_name == "Logistic Regression":
    st.write(
        "Logistic Regression is a classification model. "
        "Logistic Regression is evaluated with accuracy, a confusion matrix, a classification report, "
        "and predicted probabilities."
    )

elif model_name == "Decision Tree":
    st.write(
        "Decision Trees are intuitive and easy to interpret. "
        "They capture non-linear relationships without needing feature scaling. "
        "Tuning parameters like max_depth help improve performance and prevent overfitting."
    )

elif model_name == "KNN":
    st.write(
        "K-Nearest Neighbors classifies a new point based on the most common class among its nearest neighbors. "
        "KNN can be sensitive to feature scale, so StandardScaler can be used before fitting the model."
    )

#model settings
st.sidebar.header("4. Adjust Settings")

test_size = st.sidebar.slider("Test Size", 0.1, 0.4, 0.2)

if model_name == "Decision Tree":
    max_depth = st.sidebar.slider("Max Depth", 1, 10, 4)

if model_name == "KNN":
    k = st.sidebar.slider("Number of Neighbors (k)", 1, 19, 5, 2)

if model_name == "Logistic Regression":
    c_value = st.sidebar.slider("C", 0.1, 5.0, 1.0, 0.1)

#train and test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=test_size, random_state=42
)

# Keep copies for KNN accuracy-vs-k plot
X_train_knn = X_train.copy()
X_test_knn = X_test.copy()

#build the model

if model_name == "Linear Regression":
    model = LinearRegression()

elif model_name == "Logistic Regression":
    model = LogisticRegression(C=c_value, max_iter=1000)

elif model_name == "Decision Tree":
    model = DecisionTreeClassifier(max_depth=max_depth, random_state=42)

elif model_name == "KNN":
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    model = KNeighborsClassifier(n_neighbors=k)

#train the model
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

#show the results
st.header("📈 Model Results")
# from the Streamlit cheat sheet
col1, col2 = st.columns(2)

#for regression, show MSE, RMSE, R², and a scatter plot of actual vs predicted values
if model_name == "Linear Regression":
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    with col1:
        st.subheader("Performance Metrics")
        # from the Streamlit cheat sheet
        st.metric("📉 MSE", round(mse, 2))
        # from the Streamlit cheat sheet
        st.metric("📏 RMSE", round(rmse, 2))
        # from the Streamlit cheat sheet
        st.metric("📊 R²", round(r2, 2))

        st.subheader("Interpretation")
        st.write("Mean Squared Error measures the average squared difference between actual and predicted values.")
        st.write("Root Mean Squared Error gives an error measure in the same units as the target.")
        st.write("Lower RMSE values indicate better predictive performance.")
        st.write("R² indicates the proportion of the variance in the target variable explained by the model.")
        st.write("An R² close to 1 suggests a very good fit, while an R² near 0 indicates the model fails to capture much variance.")

    with col2:
        st.subheader("Actual vs Predicted")
        fig, ax = plt.subplots()
        ax.scatter(y_test, y_pred)
        ax.set_xlabel("Actual")
        ax.set_ylabel("Predicted")
        ax.set_title("Actual vs Predicted")
        st.pyplot(fig)

    st.subheader("Model Coefficients")
    coef_df = pd.DataFrame({
        "Feature": X.columns,
        "Coefficient": model.coef_
    })
    st.dataframe(coef_df)

#for classification, show accuracy, confusion matrix, classification report, and ROC curve if binary classification

else:
    accuracy = accuracy_score(y_test, y_pred)

    with col1:
        st.subheader("Performance Metrics")
        # from the Streamlit cheat sheet
        st.metric("🎯 Accuracy", round(accuracy, 2))

        st.subheader("Classification Report")
        st.text(classification_report(y_test, y_pred))

        st.subheader("Interpretation")
        st.write("Accuracy is the proportion of correct predictions.")
        st.write("The confusion matrix shows the number of correct and incorrect predictions.")
        st.write("The classification report gives precision, recall, and F1-score.")
        st.write("Precision shows how many predicted positives were actually positive.")
        st.write("Recall shows how many actual positives were correctly identified.")
        st.write("F1-score balances precision and recall.")

    with col2:
        st.subheader("Confusion Matrix")
        st.write("This confusion matrix shows how many predictions were correct versus incorrect.")
        cm = confusion_matrix(y_test, y_pred)
        fig, ax = plt.subplots()
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax)
        ax.set_xlabel("Predicted")
        ax.set_ylabel("Actual")
        ax.set_title("Confusion Matrix")
        st.pyplot(fig)
    
    if model_name == "Decision Tree":
        st.subheader("🌳 Decision Tree Visualization")

    try:
        import graphviz
        from sklearn import tree

        dot_data = tree.export_graphviz(
            model,
            feature_names=X.columns,
            class_names=[str(c) for c in np.unique(y)],
            filled=True
        )

        graph = graphviz.Source(dot_data)

        st.graphviz_chart(graph)

    except:
        st.warning("Decision tree visualization not available for this model.")

    if len(np.unique(y)) == 2 and hasattr(model, "predict_proba"):
        st.subheader("ROC Curve and AUC")
        st.write("The ROC curve shows how well the model separates the two classes.")

        y_prob = model.predict_proba(X_test)[:, 1]
        fpr, tpr, thresholds = roc_curve(y_test, y_prob)
        auc = roc_auc_score(y_test, y_prob)

        # from the Streamlit cheat sheet
        st.metric("📊 AUC", round(auc, 2))

        fig2, ax2 = plt.subplots()
        ax2.plot(fpr, tpr, label=f"AUC = {auc:.2f}")
        ax2.plot([0, 1], [0, 1], linestyle="--")
        ax2.set_xlabel("False Positive Rate")
        ax2.set_ylabel("True Positive Rate")
        ax2.set_title("ROC Curve")
        ax2.legend()
        st.pyplot(fig2)

        st.subheader("ROC Interpretation")
        st.write("The ROC curve helps evaluate model performance across different classification thresholds.")
        st.write("AUC summarizes the overall ability of the model to discriminate between classes.")
        st.write("AUC closer to 1 indicates better ability to separate the two classes.")

    if model_name == "KNN":
        st.subheader("Accuracy vs. Number of Neighbors (k)")
        st.write("This plot shows how accuracy changes as we vary the number of neighbors (k).")

        scaler_knn = StandardScaler()
        X_train_knn_scaled = scaler_knn.fit_transform(X_train_knn)
        X_test_knn_scaled = scaler_knn.transform(X_test_knn)

        k_values = range(1, 20, 2)
        accuracies = []

        for k_temp in k_values:
            knn_temp = KNeighborsClassifier(n_neighbors=k_temp)
            knn_temp.fit(X_train_knn_scaled, y_train)
            y_temp_pred = knn_temp.predict(X_test_knn_scaled)
            accuracies.append(accuracy_score(y_test, y_temp_pred))

        fig3, ax3 = plt.subplots()
        ax3.plot(k_values, accuracies, marker="o")
        ax3.set_title("Accuracy vs. Number of Neighbors (k)")
        ax3.set_xlabel("Number of Neighbors (k)")
        ax3.set_ylabel("Accuracy")
        ax3.set_xticks(list(k_values))
        st.pyplot(fig3)

st.markdown(stars)
# from the Streamlit cheat sheet
st.success("Done! Try different datasets, models, and settings. ☆")
st.markdown(stars)