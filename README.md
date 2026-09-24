# 💰 Salary Prediction using Linear Regression

## 🌐 Live Demo

🚀 **Try the application online:**

[Salary Prediction App](https://linearregrationpro-r9bgetrp3fddqymmycxhef.streamlit.app/)

---

## 📌 Project Overview

This project is a Machine Learning application that predicts an employee's salary based on their years of experience.

A Linear Regression model was trained using a salary dataset and deployed as an interactive web application using Streamlit.

The project demonstrates the complete Machine Learning workflow:

- Data loading
- Data cleaning
- Exploratory Data Analysis (EDA)
- Data visualization
- Feature and target selection
- Train/Test splitting
- Model training
- Model evaluation
- Model saving
- Web application development
- Model deployment

---

## 🎯 Project Objective

The main objective is to build a Machine Learning model that learns the relationship between:

- **Input:** Years of Experience
- **Target:** Salary

The trained model is then used to predict the expected salary for a given number of years of experience.

---

## 📊 Dataset

The dataset contains **30 records** and the following main variables:

| Feature | Description |
|---|---|
| YearsExperience | Number of years of professional experience |
| Salary | Employee salary |

The original dataset also contained an unnecessary `Unnamed: 0` index column, which was removed during preprocessing.

---

## 🧹 Data Preprocessing

The notebook performs the following steps:

1. Loads the dataset using Pandas.
2. Checks the dataset structure.
3. Checks for duplicated records.
4. Checks for missing values.
5. Removes the unnecessary `Unnamed: 0` column.
6. Selects `YearsExperience` as the input feature.
7. Selects `Salary` as the target.

```python
X = df[["YearsExperience"]]
y = df["Salary"]
```

---

## 🔍 Exploratory Data Analysis

The notebook includes a scatter plot and a correlation heatmap to explore the relationship between years of experience and salary.

### 📈 Years of Experience vs Salary

![Years of Experience vs Salary](scatter_plot.png)

The scatter plot shows a positive relationship between years of experience and salary.

### 🔥 Correlation Heatmap

![Correlation Heatmap](correlation_heatmap.png)

The correlation analysis shows a strong positive relationship between `YearsExperience` and `Salary`.

---

## 🤖 Machine Learning Model

### Linear Regression

The project uses **Linear Regression**, a supervised learning algorithm for predicting a continuous target.

The model represents the relationship as:

```text
Salary = m × YearsExperience + b
```

Where:

- `m` = coefficient
- `b` = intercept

---

## 📚 Train/Test Split

The dataset was divided into:

- **80% Training Data**
- **20% Testing Data**

```python
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

The `random_state=42` makes the split reproducible.

---

## 🏋️ Model Training

The Linear Regression model was trained using Scikit-learn:

```python
lr = LinearRegression()
lr.fit(x_train, y_train)
```

Predictions were generated using:

```python
predictions = lr.predict(x_test)
```

---

## 📏 Model Evaluation

The notebook evaluates the model using regression metrics including:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

### Evaluation Results

| Metric | Result |
|---|---:|
| MAE | 6286.45 |
| MSE | 49,830,096.86 |
| RMSE | 7059.04 |
| R² | 0.9024 |

An R² score of approximately **0.90** means the model explains about **90.24% of the variation in salary in the test set**.

The MAE is approximately **6286 salary units**, representing the average absolute difference between actual and predicted salary values on the test set.

---

## 📈 Actual vs Predicted

The notebook includes a visualization comparing the test-set salary values with the model's regression predictions.

![Actual vs Predicted Salary](actual_vs_predicted.png)

---

## 💾 Model Saving

The trained model was saved using Joblib:

```python
import joblib

joblib.dump(lr, "salary_model.pkl")
```

The saved model is:

```text
salary_model.pkl
```

This allows the trained model to be loaded later without retraining it.

---

## 🌐 Streamlit Web Application

The trained model was deployed as an interactive Streamlit application.

### 🏠 Home Page

The Home page provides an overview of the project, model, feature, target, and workflow.

### 💰 Salary Prediction Page

![Salary Prediction Streamlit App](prediction_page.png)

Users can:

1. Enter the number of years of experience.
2. Click **Predict Salary**.
3. Receive the predicted salary.

The application loads the saved model:

```python
model = joblib.load("salary_model.pkl")
```

and predicts using:

```python
prediction = model.predict([[years_experience]])
```

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit
- Git
- GitHub

---

## 📁 Project Structure

```text
linear_regration_pro/
│
├── app.py
├── ide.ipynb
├── Salary_dataset.csv
├── salary_model.pkl
├── requirements.txt
├── README.md
├── scatter_plot.png
├── correlation_heatmap.png
└── actual_vs_predicted.png
```

### File Description

| File | Description |
|---|---|
| `app.py` | Streamlit web application |
| `ide.ipynb` | Jupyter Notebook for data analysis and model development |
| `Salary_dataset.csv` | Salary dataset |
| `salary_model.pkl` | Trained Linear Regression model |
| `requirements.txt` | Required Python libraries |
| `README.md` | Project documentation |
| `scatter_plot.png` | EDA scatter plot |
| `correlation_heatmap.png` | Correlation heatmap |
| `actual_vs_predicted.png` | Model prediction visualization |
| `prediction_page.png` | Streamlit Salary Prediction page screenshot |

---

## 🚀 Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/Nusiba-rabea/linear_regration_pro.git
```

### 2. Open the project directory

```bash
cd linear_regration_pro
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

---

## ☁️ Deployment

The application is deployed using **Streamlit Community Cloud**.

### 🔗 Live Application

[Open Salary Prediction App](https://linearregrationpro-r9bgetrp3fddqymmycxhef.streamlit.app/)

---

## 📌 Machine Learning Workflow

```text
Dataset
   ↓
Data Loading
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Data Visualization
   ↓
Feature & Target Selection
   ↓
Train/Test Split
   ↓
Linear Regression
   ↓
Model Training
   ↓
Prediction
   ↓
Model Evaluation
   ↓
Save Model
   ↓
Streamlit Application
   ↓
Deployment
```

---

## 🎓 Learning Outcomes

Through this project, the following concepts were practiced:

- Python for Machine Learning
- Data manipulation using Pandas
- Exploratory Data Analysis
- Data visualization
- Correlation analysis
- Supervised Learning
- Linear Regression
- Train/Test Split
- Regression evaluation metrics
- Model serialization using Joblib
- Streamlit application development
- Git and GitHub
- Machine Learning model deployment

---

## 🔮 Future Improvements

Possible future improvements include:

- Using a larger and more diverse dataset.
- Adding more features such as education level, job position, industry, and location.
- Comparing Linear Regression with other regression algorithms.
- Adding more visualizations.
- Improving the Streamlit user interface.
- Comparing multiple Machine Learning models.
- Performing additional model optimization.

---

## 👩‍💻 Author

**Nusiba Rabee**

Electronics and Communications Engineering

---

## 📄 License

This project was created for educational and portfolio purposes.
