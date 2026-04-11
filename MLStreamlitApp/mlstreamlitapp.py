import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.metrics import roc_curve, roc_auc_score
from sklearn.metrics import mean_squared_error, r2_score

# from the Streamlit cheat sheet
st.set_page_config(page_title="Supervised ML Explorer", layout="wide")

st.title("Supervised Machine Learning Explorer")
st.markdown(
    """
    This app allows users to explore supervised machine learning models by selecting a sample dataset
    or uploading their own CSV file, choosing a model, adjusting hyperparameters, and viewing model
    performance metrics and visualizations.
    """
)

st.write("This app is designed to encourage experimentation with supervised learning models in a simple, interactive way.")

