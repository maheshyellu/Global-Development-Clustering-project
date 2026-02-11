# Global-Development-Clustering-project

## Project Overview

This project analyzes global socio-economic indicators to identify patterns among countries and classify them into development categories.

The system combines unsupervised learning (KMeans clustering) and supervised learning (SVM classification) to build an end-to-end predictive solution.

The final output is a Streamlit-based web application that allows users to input country-level indicators and receive a predicted development category.

 ## Objective

The main objective of this project is:

To group countries into meaningful development segments based on measurable socio-economic features.

To build a predictive system capable of classifying new data into those segments.

 ## Dataset & Features

The dataset contains 16 socio-economic indicators, including:

- GDP-related metrics

- Birth rate

- Business tax rate

- Days to start a business

- Health and economic indicators

These features represent economic strength, development infrastructure, and demographic factors.

 ## Methodology
### 1️.Data Preprocessing

- Cleaned and structured the dataset

- Selected relevant features

- Applied RobustScaler for feature scaling

### Why scaling was necessary:
KMeans uses Euclidean distance. Since features like GDP and birth rate are on different scales, scaling ensures fair contribution from all variables. RobustScaler was used to reduce sensitivity to extreme outliers.

### 2️.Country Segmentation (Unsupervised Learning)

- Applied KMeans clustering (k = 3)

- Identified natural groupings of countries

- Analyzed cluster-wise feature averages to interpret results

- The three segments were interpreted as:

### Emerging & Developing

### Least Developed

### Developed Superpowers

## Cluster Distribution:

- Emerging & Developing → 2045 countries

- Least Developed → 97 countries

- Developed Superpowers → 21 countries

The imbalance reflects real-world global economic distribution.

### 3.Development Category Prediction (Supervised Learning)

### To enable real-time prediction:

Cluster labels were used as target variables.

A Support Vector Machine (SVM) classifier was trained on the segmented data.

### Why SVM?

SVM was chosen because:

It performs well in high-dimensional feature spaces.

It creates strong decision boundaries between classes.

It is effective for structured classification problems after clustering.

The trained model and scaler were saved using pickle for deployment.

### 4️.Deployment using Streamlit

An interactive Streamlit web application was built to:

Accept 16 socio-economic inputs

Scale inputs using the saved RobustScaler

Predict the development category using the trained SVM model

Display classification results in real-time

This makes the system practical and user-friendly.

## Technologies Used

Python

NumPy

Pandas

Scikit-learn

Matplotlib

Seaborn

Streamlit

SciPy
