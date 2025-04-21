import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('shopping_trends.csv')

data['Cumulative Revenue (USD)'] = data['Purchase Amount (USD)'].cumsum()

df1 = data[['Gender', 'Category', 'Season', 'Cumulative Revenue (USD)']]
X = df1.drop(columns=['Cumulative Revenue (USD)'])
y = df1['Cumulative Revenue (USD)']

label_cols = X.select_dtypes(include='object').columns
lb_encoders = {}
for col in label_cols:
    lb_encoders[col] = LabelEncoder()
    X[col] = lb_encoders[col].fit_transform(X[col])

model = LinearRegression()
model.fit(X, y)

st.title("🛍️ Revenue Prediction App")
st.text("Created by Lutfor Rahman Sohan!")
st.write("Select the options below to predict the cumulative revenue:")

gender = st.selectbox("Select Gender", options=data['Gender'].unique())
category = st.selectbox("Select Category", options=data['Category'].unique())
season = st.selectbox("Select Season", options=data['Season'].unique())

gender_encoded = lb_encoders['Gender'].transform([gender])[0]
category_encoded = lb_encoders['Category'].transform([category])[0]
season_encoded = lb_encoders['Season'].transform([season])[0]

input_data = np.array([[gender_encoded, category_encoded, season_encoded]])
predicted_revenue = model.predict(input_data)[0]

st.success(f"### 💰 Predicted Cumulative Revenue: ${predicted_revenue:.2f}")
