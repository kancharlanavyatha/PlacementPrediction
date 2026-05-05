# Campus Placement Prediction

A simple machine learning web app that predicts whether a student is likely to be placed based on academic profile, test score, and work experience.

This project includes:
- data exploration and model training in a notebook
- a saved trained model
- a lightweight Streamlit UI for quick predictions

## Project Structure

- `Campus Placement Prediction Using ML.ipynb` - notebook for EDA, preprocessing, training, and evaluation
- `Placement.csv` - dataset used for training
- `model_campus_placement` - saved trained model (Joblib)
- `app.py` - Streamlit app for prediction UI
- `requirements.txt` - Python dependencies

## Model Summary

Multiple classifiers were tested (Logistic Regression, SVC, KNN, Decision Tree, Random Forest, Gradient Boosting).

Best observed accuracy on the test split:
- **Logistic Regression: ~88.37%**

## Run Locally

1. Clone the repository:

```bash
git clone https://github.com/kancharlanavyatha/PlacementPrediction.git
cd PlacementPrediction
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start the app:

```bash
streamlit run app.py
```

4. Open in browser:

`http://localhost:8501`

## Deploy on Streamlit Community Cloud

1. Push this project to GitHub.
2. Go to [Streamlit Community Cloud](https://share.streamlit.io).
3. Click **New app**.
4. Select:
   - Repository: `kancharlanavyatha/PlacementPrediction`
   - Branch: `main`
   - Main file path: `app.py`
5. Click **Deploy**.

## Features in UI

- Clean form-based input
- Supports different 12th streams (`Arts`, `Commerce`, `Science`)
- Includes fallback option for specialisation (`Other / Not Sure`)
- Handles case where MBA is not completed
- Shows prediction with probability score

## Notes

- This is a student project for demonstration and learning.
- Predictions are based on the training dataset and may not generalize to all institutions.

## Author

**Kancharla Navyatha**
