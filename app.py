import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(page_title="Churn Intervention Dashboard", page_icon="🚨", layout="wide")

st.title("🚨 Live Customer Churn Forecasting")
st.markdown("This dashboard maps directly to the active 'Open Prospects' deployment engine. It translates real-time underlying metrics into actionable intervention targets for the commercial outreach teams.")

# Load Data
@st.cache_data
def load_data():
    try:
        return pd.read_csv('data/processed/open_prospects_churn_predictions.csv')
    except Exception as e:
        return None

df = load_data()

if df is None:
    st.error("No predictions found! Ensure you have executed `03_modeling/02_predict_open_prospects.ipynb` to generate the active CSV matrix.")
else:
    # Sidebar Filtering
    st.sidebar.header("Filter Interventions")
    
    st.sidebar.markdown('**Strategic Probability Threshold**')
    threshold = st.sidebar.slider("Minimum Predicted Churn Probability (%)", min_value=0, max_value=100, value=75, step=5)
    
    # Apply filters
    filtered_df = df[df['churn_probability'] >= threshold].sort_values(by='churn_probability', ascending=False)
    
    # Top metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Active Prospects Executed", f"{len(df):,}")
    col2.metric("Total Flagged (High Risk)", f"{len(df[df['predicted_class'] == 1]):,}")
    col3.metric(f"Severe Targets (>{threshold}%)", f"{len(filtered_df):,}")
    
    st.divider()
    
    st.subheader(f"Current Intervention Target List ({len(filtered_df)} Prospects)")
    st.markdown("These customers present the statistically mathematically highest danger. Route immediately to retention teams.")
    
    # Format display
    display_df = filtered_df[['co_ref', 'churn_probability', 'forecast']].copy()
    display_df['churn_probability'] = display_df['churn_probability'].apply(lambda x: f"{x:.1f}%")
    
    st.dataframe(display_df, use_container_width=True, hide_index=True)
    
    st.divider()
    
    # Basic Risk Chart
    st.subheader("Distribution Profile")
    risk_bins = pd.cut(df['churn_probability'], bins=[0, 20, 40, 60, 80, 100], labels=['0-20% (Safe)', '20-40%', '40-60%', '60-80%', '80-100% (Critical)'])
    st.bar_chart(risk_bins.value_counts().sort_index())
