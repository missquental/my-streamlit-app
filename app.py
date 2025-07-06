import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="My Streamlit App",
    page_icon="🚀",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>🚀 My Streamlit Application</h1>
    <p>Created with GitHub Auto-Deploy</p>
</div>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page", ["Home", "Data Analysis", "Charts"])

if page == "Home":
    st.title("Welcome to Your App!")
    st.write("This app was automatically deployed from GitHub to Streamlit Cloud.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Users", "1,234", "↗️ 12%")
    
    with col2:
        st.metric("Revenue", "$45,678", "↗️ 8%")
    
    with col3:
        st.metric("Conversions", "89%", "↗️ 3%")

elif page == "Data Analysis":
    st.title("Data Analysis")
    
    # Generate sample data
    data = pd.DataFrame({
        'Date': pd.date_range('2024-01-01', periods=100),
        'Sales': np.random.randint(100, 1000, 100),
        'Customers': np.random.randint(10, 100, 100),
        'Region': np.random.choice(['North', 'South', 'East', 'West'], 100)
    })
    
    st.subheader("Sales Data")
    st.dataframe(data.head(10))
    
    st.subheader("Summary Statistics")
    st.write(data.describe())

elif page == "Charts":
    st.title("Interactive Charts")
    
    # Generate sample data
    data = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'Sales': [100, 120, 140, 110, 160, 180],
        'Expenses': [80, 90, 100, 85, 120, 140]
    })
    
    # Line chart
    fig = px.line(data, x='Month', y=['Sales', 'Expenses'], 
                  title='Monthly Sales vs Expenses')
    st.plotly_chart(fig, use_container_width=True)
    
    # Bar chart
    fig2 = px.bar(data, x='Month', y='Sales', 
                  title='Monthly Sales')
    st.plotly_chart(fig2, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")
