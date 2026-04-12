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

