# Machine Learning Application Project

## Project Overview

This project builds an interactive machine learning application using Python and Streamlit. The goal of the app is to allow users to explore supervised machine learning models through an intuitive interface that invites exploration and communicates results clearly.

Users can choose from four built-in datasets or upload their own dataset, select a model, adjust hyperparameters, and observe how these changes affect model performance.

The app follows the same workflow used in class, including defining features and targets, splitting the data, training models, and evaluating results using appropriate metrics and visualizations.

݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁. ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ 

## Machine Learning Concepts Used in This Project

This project is based on the following core ideas from class:

- Defining feature variables (X) and a target variable (y)
- Splitting data into training and testing sets
- Training supervised learning models
- Making predictions on test data
- Evaluating model performance using metrics and visualizations

The app allows users to experiment with these steps interactively and see how changes impact results.

݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁. ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ 

## Datasets Used in This Project

The app includes several built-in datasets:

- [🧬 Breast Cancer dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html) 
  Contains features computed from cell nuclei. The goal is to classify tumors as benign or malignant.

- [🩺 Diabetes dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html) 
  Contains medical measurements used to predict a continuous outcome.

- [🌸 Iris dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html)
  Contains measurements of iris flowers used to classify species.

- [🍷 Wine dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html)
  Contains chemical properties used to classify types of wine.

📂 Users can also upload their own CSV dataset and select a target variable.

݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁. ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ 

## Models Used in This Project

The app includes the following supervised learning models:

- **Linear Regression**  
  Used for predicting continuous outcomes.

- **Logistic Regression**  
  Used for classification problems.

- **Decision Tree**  
  A model that splits data into branches based on feature values.

- **K-Nearest Neighbors (KNN)**  
  Classifies data based on the closest neighboring observations.

Each model can be adjusted using parameters such as max depth, number of neighbors, or regularization strength.

݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁. ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ 

## Model Evaluation and Visualizations

The app evaluates models using the same metrics used in class.

### Classification metrics:
- Accuracy
- Confusion Matrix
- Classification Report (precision, recall, F1-score)
- ROC Curve and AUC (for binary classification)

### Regression metrics:
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² score

### Visualizations included:
- Confusion Matrix heatmap
- ROC Curve
- Accuracy vs. k for KNN
- Actual vs. Predicted scatter plot (for regression)
- Decision Tree visualization

These visualizations help interpret model performance and understand how predictions are made.

݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁. ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ 

## Project Steps

The app follows these main steps:

1. Load and preview the dataset  
2. Inspect structure, data types, and missing values  
3. Select the target variable  
4. Define feature variables (X) and target (y)  
5. Split the data into training and testing sets  
6. Train the selected model  
7. Generate predictions  
8. Evaluate model performance using metrics and visualizations  

݁₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁. ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ 

## How to Run This Project

### Requirements
This project uses Python and the following libraries:

- streamlit
- pandas
- numpy
- seaborn
- matplotlib
- scikit-learn
- graphviz

### Running the notebook
1. Download the repository
2. Open the MLStreamlitApp folder
3. Install the libraries
4. streamlit run the app in the terminal

### Example import statements
```
```

₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁. ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ ⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁.₊ 

## References

- [Scikit-learn info on the 🧬 Breast Cancer dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html) 

- [Scikit-learn info on the 🩺 Diabetes dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html) 

- [Scikit-learn info on the 🌸 Iris dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html)

- [Scikit-learn info on the 🍷 Wine dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html)

- [Streamlit Cheat Sheet](https://cheat-sheet.streamlit.app/)

- [Streamlit Cloud Instruction](https://docs.streamlit.io/get-started/installation/community-cloud)
