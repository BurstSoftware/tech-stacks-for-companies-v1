import streamlit as st  
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
import plotly.express as px  
from sklearn.model_selection import train_test_split  
from sklearn.ensemble import RandomForestClassifier  
from sklearn.metrics import accuracy_score  
from keras.models import Sequential  
from keras.layers import Dense  

# Title and Description  
st.title("Interactive Data Science Dashboard")  
st.markdown("This app allows you to explore data, visualize it, and apply Machine Learning models.")  

# File Upload Section  
uploaded_file = st.file_uploader("Upload your dataset (CSV format)", type=["csv"])  

if uploaded_file:  
    df = pd.read_csv(uploaded_file)  
    st.write("### Dataset Preview:")
    st.write(df.head())  

    # Dataset Summary  
    st.write("### Data Summary:")  
    st.write(df.describe())  

    # Column Selection for Visualization  
    selected_column = st.selectbox("Select a column for visualization", df.columns)  
    fig, ax = plt.subplots()  
    df[selected_column].hist(ax=ax, bins=20)  
    st.pyplot(fig)  

    # Machine Learning Model Training  
    st.write("### Train a Machine Learning Model")  
    target_column = st.selectbox("Select the target column", df.columns)  

    X = df.drop(columns=[target_column])  
    y = df[target_column]  

    # Splitting Data  
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  

    # Train Random Forest Model  
    model = RandomForestClassifier(n_estimators=100, random_state=42)  
    model.fit(X_train, y_train)  

    y_pred = model.predict(X_test)  
    accuracy = accuracy_score(y_test, y_pred)  

    st.write(f"**Random Forest Model Accuracy:** {accuracy:.2f}")  

    # Deep Learning Model  
    st.write("### Build a Neural Network Model")  

    nn_model = Sequential([  
        Dense(64, activation='relu', input_shape=(X_train.shape[1],)),  
        Dense(32, activation='relu'),  
        Dense(1, activation='sigmoid')  
    ])  

    nn_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])  

    st.write("Neural network model compiled successfully.")  

# Run with: streamlit run app.py  
