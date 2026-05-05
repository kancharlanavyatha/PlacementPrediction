import joblib
import pandas as pd
import streamlit as st


st.set_page_config(page_title="Campus Placement Predictor", page_icon="🎓")
st.title("🎓 Campus Placement Predictor")
st.caption("Simple UI for quick placement prediction (works for all academic streams)")

MODEL_PATH = "model_campus_placement"

try:
    model = joblib.load(MODEL_PATH)
except FileNotFoundError:
    st.error("Model file not found. Please keep 'model_campus_placement' in this folder.")
    st.stop()


def encode_inputs(
    gender: str,
    ssc_p: float,
    ssc_b: str,
    hsc_p: float,
    hsc_b: str,
    hsc_s: str,
    degree_p: float,
    degree_t: str,
    workex: str,
    etest_p: float,
    specialisation: str,
    mba_p: float,
) -> pd.DataFrame:
    encoded = {
        "gender": 1 if gender == "Male" else 0,
        "ssc_p": ssc_p,
        "ssc_b": 1 if ssc_b == "Central" else 0,
        "hsc_p": hsc_p,
        "hsc_b": 1 if hsc_b == "Central" else 0,
        "hsc_s": {"Arts": 0, "Commerce": 1, "Science": 2}[hsc_s],
        "degree_p": degree_p,
        "degree_t": {"Others": 0, "Comm&Mgmt": 1, "Sci&Tech": 2}[degree_t],
        "workex": 1 if workex == "Yes" else 0,
        "etest_p": etest_p,
        "specialisation": 1 if specialisation == "Mkt&HR" else 0,
        "mba_p": mba_p,
    }
    return pd.DataFrame([encoded])


col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Female", "Male"])
    ssc_p = st.number_input("10th Marks (%)", min_value=0.0, max_value=100.0, value=67.0, step=0.1)
    ssc_b = st.selectbox("10th Board Type", ["Others", "Central"])
    hsc_p = st.number_input("12th Marks (%)", min_value=0.0, max_value=100.0, value=70.0, step=0.1)
    hsc_b = st.selectbox("12th Board Type", ["Others", "Central"])
    hsc_s = st.selectbox("12th Stream", ["Arts", "Commerce", "Science"])

with col2:
    degree_p = st.number_input("Degree Marks (%)", min_value=0.0, max_value=100.0, value=65.0, step=0.1)
    degree_t = st.selectbox("Degree Category", ["Others", "Comm&Mgmt", "Sci&Tech"])
    workex = st.selectbox("Work Experience", ["No", "Yes"])
    etest_p = st.number_input("E-test Marks (%)", min_value=0.0, max_value=100.0, value=70.0, step=0.1)
    specialisation = st.selectbox(
        "Placement Specialisation",
        ["Mkt&Fin", "Mkt&HR", "Other / Not Sure"],
        help="If your specialisation is not listed, pick 'Other / Not Sure'.",
    )
    mba_not_applicable = st.checkbox("MBA not completed / not applicable", value=False)
    mba_p = st.number_input(
        "MBA Marks (%)",
        min_value=0.0,
        max_value=100.0,
        value=62.0,
        step=0.1,
        disabled=mba_not_applicable,
    )

if mba_not_applicable:
    # Model requires mba_p, so use a neutral default when unavailable.
    mba_p = 60.0

specialisation = "Mkt&Fin" if specialisation == "Other / Not Sure" else specialisation


if st.button("Predict", type="primary"):
    input_df = encode_inputs(
        gender,
        ssc_p,
        ssc_b,
        hsc_p,
        hsc_b,
        hsc_s,
        degree_p,
        degree_t,
        workex,
        etest_p,
        specialisation,
        mba_p,
    )

    pred = int(model.predict(input_df)[0])
    prob = float(model.predict_proba(input_df)[0][1])

    if pred == 1:
        st.success(f"Placed ✅ (probability: {prob:.2%})")
    else:
        st.error(f"Not Placed ❌ (probability of placement: {prob:.2%})")
