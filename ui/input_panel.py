import streamlit as st
import json
import os


def render_input_panel():
    """
    Render the sidebar input panel for financial assumptions.
    
    Returns:
        dict: Dictionary containing all user inputs
    """
    st.sidebar.header("Financial Assumptions")
    
    # Business Basics
    st.sidebar.subheader("Business Basics")
    business_name = st.sidebar.text_input(
        "Business Name",
        value="My Business"
    )
    starting_cash = st.sidebar.number_input(
        "Starting Cash ($)",
        min_value=0.0,
        value=20000.0,
        step=1000.0
    )
    
    # Revenue Assumptions
    st.sidebar.subheader("Revenue Assumptions")
    average_monthly_revenue = st.sidebar.number_input(
        "Average Monthly Revenue ($)",
        min_value=0.0,
        value=15000.0,
        step=500.0
    )
    monthly_growth_rate = st.sidebar.number_input(
        "Monthly Growth Rate (%)",
        min_value=-100.0,
        max_value=100.0,
        value=3.0,
        step=0.5
    ) / 100  # Convert to decimal
    
    # Cost Structure
    st.sidebar.subheader("Cost Structure")
    cogs_percent = st.sidebar.number_input(
        "COGS (% of Revenue)",
        min_value=0.0,
        max_value=100.0,
        value=35.0,
        step=1.0
    )
    
    # Expense Assumptions
    st.sidebar.subheader("Expense Assumptions")
    rent = st.sidebar.number_input(
        "Rent ($)",
        min_value=0.0,
        value=2000.0,
        step=100.0
    )
    payroll = st.sidebar.number_input(
        "Payroll ($)",
        min_value=0.0,
        value=5000.0,
        step=500.0
    )
    utilities = st.sidebar.number_input(
        "Utilities ($)",
        min_value=0.0,
        value=600.0,
        step=50.0
    )
    software = st.sidebar.number_input(
        "Software ($)",
        min_value=0.0,
        value=200.0,
        step=50.0
    )
    miscellaneous = st.sidebar.number_input(
        "Miscellaneous ($)",
        min_value=0.0,
        value=400.0,
        step=50.0
    )
    
    # Owner Compensation
    st.sidebar.subheader("Owner Compensation")
    owner_draw = st.sidebar.number_input(
        "Owner Draw ($)",
        min_value=0.0,
        value=3000.0,
        step=500.0
    )
    
    # Debt
    st.sidebar.subheader("Debt")
    monthly_loan_payment = st.sidebar.number_input(
        "Monthly Loan Payment ($)",
        min_value=0.0,
        value=800.0,
        step=100.0
    )
    
    # Startup Costs
    st.sidebar.subheader("Startup Costs")
    startup_costs = st.sidebar.number_input(
        "One-Time Startup Costs ($)",
        min_value=0.0,
        value=10000.0,
        step=1000.0
    )
    
    # Projection Settings
    st.sidebar.subheader("Projection Length")
    months = st.sidebar.number_input(
        "Number of Months",
        min_value=1,
        max_value=60,
        value=12,
        step=1
    )
    
    # Load Sample Data Button
    st.sidebar.markdown("---")
    if st.sidebar.button("Load Sample Data"):
        load_sample_data()
        st.rerun()
    
    # Compile all inputs into a dictionary
    inputs = {
        'business_name': business_name,
        'starting_cash': starting_cash,
        'average_monthly_revenue': average_monthly_revenue,
        'monthly_growth_rate': monthly_growth_rate,
        'cogs_percent': cogs_percent,
        'rent': rent,
        'payroll': payroll,
        'utilities': utilities,
        'software': software,
        'miscellaneous': miscellaneous,
        'owner_draw': owner_draw,
        'monthly_loan_payment': monthly_loan_payment,
        'startup_costs': startup_costs,
        'months': months
    }
    
    return inputs


def load_sample_data():
    """
    Load sample data from JSON file into session state.
    """
    sample_file = os.path.join('data', 'sample_inputs.json')
    
    if os.path.exists(sample_file):
        with open(sample_file, 'r') as f:
            sample_data = json.load(f)
        
        # Store in session state for persistence
        for key, value in sample_data.items():
            st.session_state[key] = value
