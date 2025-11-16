📊 Salary Prediction Web Application
A machine learning–powered web application built with Python, Streamlit, and Jupyter Notebook that predicts employee salary based on multiple factors such as job title, experience, education, and location.
This project uses ensemble algorithms like Random Forest, Gradient Boosting, and Voting Classifier to improve accuracy.

🚀 Features
🧹 Data Cleaning & Preprocessing (handle missing values, encoding, normalization)

📈 Exploratory Data Analysis (EDA)

🤖 Trained multiple ML models

🧠 Ensemble model for best accuracy

🖥 Interactive Streamlit Web App

📤 Upload CSV or enter values manually

🎯 Instant salary prediction
📚 Dataset Description
The dataset contains the following attributes (may vary based on your version):


Job Title
Experience (Years)
Departmemnt
Location
Age
Gender
Monthly Salary
Skills
Salary (Target Variable)

🧪 Model Training
The following models were trained and evaluated:

Linear Regression

Random Forest Regressor

Gradient Boosting Regressor

XGBoost (optional)

Voting Regressor (Final Model)

Metrics used:

MAE

RMSE

R² Score

The Voting Regressor with RF + GB gave the best performance and was saved as final_model.pkl.

🎨 Streamlit UI
The web UI provides:

🟢 Option 1: Manual Data Input
Users can enter:

1.years at company
2.Job Rate


▶ How to Run the App
1. Install dependencies
pip install -r requirements.txt

🖼 Screenshots⬇️
"C:\Users\tanis\Pictures\Screenshots\Screenshot (13).png"

🧩 Issues Faced
Missing values and inconsistent text formatting

Categorical variable encoding

Model overfitting

Streamlit UI rendering issues

Slow model loading for large datasets

✔ How Issues Were Solved
Used Label Encoding & OneHot Encoding

Applied StandardScaler for numeric columns

Tuned hyperparameters for ensemble models

Cached model using @st.cache_resource

Optimized UI layout and inputs

📌 Future Improvements
Deploy on Streamlit Cloud / Render / AWS

Add more user-friendly visualizations

Allow multiple models to be selected by the user

Add feature importance dashboard

Add deep learning model for comparison

👩‍💻 Author
Tanisha Das❤️
