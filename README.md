# Shopping Trends Revenue Prediction App

This project is a Streamlit application that predicts cumulative revenue based on shopping trends data. It utilizes a linear regression model to forecast revenue based on customer gender, product category, and season.

## Overview

![image](https://github.com/user-attachments/assets/d2fd4a81-90d6-4b3c-bf7b-a709b39e3efc)


The application processes a dataset of shopping trends, performs exploratory data analysis (EDA), and builds a predictive model. The core functionality allows users to input specific criteria (gender, category, season) via a Streamlit interface and receive a predicted cumulative revenue.

## Features

* **Data Loading and Preprocessing:** Loads shopping trends data from a CSV file and calculates cumulative revenue.
* **Exploratory Data Analysis (EDA):** The Jupyter Notebook (`shopping_trend_analysis (1).pdf`) contains detailed EDA, including visualizations of age distribution, gender distribution, purchase amount by category, etc.
* **Linear Regression Modeling:**
    * Encodes categorical features ("Gender," "Category," "Season") using LabelEncoder.
    * Trains a linear regression model to predict cumulative revenue.
    * Evaluates model performance using Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared (R²) score.
* **Streamlit Interface:**
    * Provides a user-friendly interface to select gender, category, and season.
    * Predicts cumulative revenue based on user input.
    * Displays the predicted revenue in a clear, formatted output.

## Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-learn (sklearn)
    * `LinearRegression`
    * `LabelEncoder`

## Setup and Installation

1.  **Ensure you have Python installed.**

2.  **Install the required libraries:**

    ```bash
    pip install streamlit pandas numpy scikit-learn
    ```

3.  **Place the `shopping_trends.csv` file in the same directory as `app.py`.**

4.  **Run the Streamlit app:**

    ```bash
    streamlit run app.py
    ```

## Data

The application uses the `shopping_trends.csv` dataset, which contains information about customer demographics, purchase behavior, and product details. Key attributes include:

* Customer ID
* Age
* Gender
* Item Purchased
* Category
* Purchase Amount (USD)
* ... (and other features as detailed in the EDA)

The notebook provides more context on the dataset.

## How to Use

1.  Run the Streamlit application using the command above.
2.  Select the desired gender, category, and season from the dropdown menus in the app.
3.  The app will display the predicted cumulative revenue based on your selections.

## Model Evaluation (from Notebook)

The linear regression model was evaluated with the following metrics:

* Mean Absolute Error (MAE): 34010.81
* Mean Squared Error (MSE): 1672781360.03
* R-squared (R²) Score: 63.66%

## Limitations

* The model's performance is limited by the features used (Gender, Category, Season) and the inherent predictability of cumulative revenue.
* The linear regression model might not capture complex non-linear relationships in the data.
* Further improvements could involve feature engineering, using more sophisticated models, or incorporating other relevant data.

## Further Work

* Explore other machine learning models (e.g., Random Forest Regressor) for improved accuracy. [cite: 2]
* Incorporate more features from the dataset to potentially enhance predictive power.
* Implement more robust feature engineering techniques.
* Add functionality to visualize the impact of different input features on revenue.
