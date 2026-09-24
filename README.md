# 💰 Salary Prediction using Linear Regression

## 📌 Project Overview

This project uses Machine Learning to predict an employee's salary based on their years of experience.

A Linear Regression model was trained using a salary dataset and deployed as an interactive web application using Streamlit.

---

## 🎯 Project Objective

The main objective is to build a simple Machine Learning model that learns the relationship between:

- **Input:** Years of Experience
- **Target:** Salary

The trained model can then predict the expected salary for a new number of years of experience.

---

## 📊 Dataset

The dataset contains information about employees' years of experience and salaries.

### Features

| Feature | Description |
|---|---|
| YearsExperience | Number of years of professional experience |
| Salary | Employee salary |

The dataset contains **30 records**.

---

## 🔍 Exploratory Data Analysis

The following steps were performed:

- Checked the dataset structure
- Checked for missing values
- Checked for duplicated records
- Removed the unnecessary index column
- Analyzed the relationship between Years of Experience and Salary
- Created a Scatter Plot
- Created a Correlation Heatmap

The analysis showed a strong positive relationship between years of experience and salary.

---

## 🤖 Machine Learning Model

### Linear Regression

The model learns a linear relationship between years of experience and salary:

```text
Salary = m × YearsExperience + b
Model Evaluation

The model was evaluated using:

Metric	Result
MAE	6286.45
MSE	49,830,096.86
RMSE	7059.04
R²	0.9024
Interpretation

The model achieved an R² score of approximately 0.90, meaning that the model explains about 90.24% of the variation in salary in the test set.

The MAE indicates an average absolute prediction error of approximately 6,286 salary units.