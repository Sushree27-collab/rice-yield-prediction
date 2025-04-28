# =========================================
# Siya's Final Streamlit App (Polished)
# =========================================

import streamlit as st
import pandas as pd
import joblib

# Load the best trained model
model = joblib.load('Best_XGBoost_Model.pkl')  # <- Make sure this name matches your saved model!

# Streamlit app layout
st.set_page_config(page_title="Rice Yield Predictor 🌾", page_icon="🌾")

# Title
st.title('🌾 Rice Yield Prediction Under Hybrid CO₂ Conditions')
st.subheader('🚀 Powered by Machine Learning (XGBoost)')

st.markdown("""
This application predicts rice grain yield based on key phenological parameters  
and experimental CO₂ conditions.

**Required Columns in Upload CSV:**
- Panicle_Initiation
- Anthesis
- Physiological_Maturity
- Runs
- Condition_Encoded
    - 0 = Current CO₂
    - 1 = Projected CO₂
""")

# Upload CSV
uploaded_file = st.file_uploader("📄 Upload your input CSV file", type=["csv"])

if uploaded_file is not None:
    input_data = pd.read_csv(uploaded_file)
    st.success('✅ File uploaded successfully!')

    st.write('📈 Preview of Uploaded Data:')
    st.dataframe(input_data)

    # Predict
    st.subheader('🔮 Predicted Rice Grain Yield (kg/ha)')
    predictions = model.predict(input_data)
    input_data['Predicted_Grain_Yield_kg/ha'] = predictions
    st.dataframe(input_data)

    # Download button
    csv = input_data.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Prediction Results",
        data=csv,
        file_name='Predicted_Rice_Yield.csv',
        mime='text/csv'
    )

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by Siya 🚀")
