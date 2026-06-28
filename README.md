# Campus Placement Prediction using Machine Learning

A machine learning web application that predicts whether a student is likely to be placed based on their academic performance, test scores, work experience, and educational background.

This project demonstrates the complete machine learning workflow, including data preprocessing, exploratory data analysis (EDA), model training, evaluation, and deployment using Streamlit.

## Live Demo

**Deployed Application:**  
https://placementpredictioncit.streamlit.app/

---

## Overview

The application allows users to enter academic and professional details and predicts whether they are likely to be placed. Along with the prediction, it displays the model's confidence score.

---

## Features

- Predicts campus placement status
- Interactive Streamlit web interface
- Displays prediction probability
- Supports multiple higher secondary streams:
  - Science
  - Commerce
  - Arts
- Includes work experience as an input feature
- Handles cases where MBA specialization is unavailable
- Lightweight and easy to use

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
- Streamlit

---

## Project Structure

```text
PlacementPrediction/
│
├── Campus Placement Prediction Using ML.ipynb
├── Placement.csv
├── model_campus_placement
├── app.py
├── requirements.txt
└── README.md
```

### Files

| File | Description |
|------|-------------|
| `Campus Placement Prediction Using ML.ipynb` | Data preprocessing, exploratory data analysis, model training, and evaluation |
| `Placement.csv` | Dataset used for training |
| `model_campus_placement` | Serialized trained model using Joblib |
| `app.py` | Streamlit application |
| `requirements.txt` | Project dependencies |

---

## Dataset

The dataset contains information about students' academic backgrounds and professional experience.

### Input Features

- Gender
- Secondary Education Percentage (10th)
- Higher Secondary Percentage (12th)
- Higher Secondary Stream
- Degree Percentage
- Degree Type
- Work Experience
- Employability Test Score
- MBA Percentage
- MBA Specialization

### Target Variable

- Placement Status
  - Placed
  - Not Placed

---

## Machine Learning Models Evaluated

The following classification algorithms were trained and compared:

- Logistic Regression
- Support Vector Classifier (SVC)
- K-Nearest Neighbors (KNN)
- Decision Tree Classifier
- Random Forest Classifier
- Gradient Boosting Classifier

### Best Performing Model

| Model | Test Accuracy |
|--------|--------------:|
| Logistic Regression | **88.37%** |

The Logistic Regression model achieved the highest accuracy and was selected for deployment.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/kancharlanavyatha/PlacementPrediction.git
```

Navigate to the project directory:

```bash
cd PlacementPrediction
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will be available at:

```
http://localhost:8501
```

---

## Application Workflow

1. Enter the required student details.
2. Submit the form.
3. The trained machine learning model processes the input.
4. The application predicts whether the student is likely to be placed.
5. The prediction confidence score is displayed.

---

## Future Improvements

- Hyperparameter optimization
- Cross-validation
- Feature importance visualization
- Explainable AI using SHAP
- Docker support
- Cloud deployment enhancements
- Prediction history and analytics

---

## Author

**Kancharla Navyatha**

GitHub: https://github.com/kancharlanavyatha

---

## License

This project is intended for educational and learning purposes.
