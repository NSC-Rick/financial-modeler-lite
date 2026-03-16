import streamlit as st
import pandas as pd


def render_results_panel(projection_df, summary_metrics, break_even_revenue, business_name):
    """
    Render the main results panel with projection table, charts, and metrics.
    
    Args:
        projection_df (pd.DataFrame): Monthly projection data
        summary_metrics (dict): Summary metrics
        break_even_revenue (float): Break-even monthly revenue
        business_name (str): Name of the business
    """
    st.title(f"📊 Financial Projection: {business_name}")
    
    # Summary Metrics at the top
    st.subheader("Summary Metrics")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Total Projected Revenue",
            f"${summary_metrics['total_revenue']:,.2f}"
        )
    
    with col2:
        st.metric(
            "Total Net Profit",
            f"${summary_metrics['total_net_profit']:,.2f}"
        )
    
    with col3:
        st.metric(
            "Ending Cash Balance",
            f"${summary_metrics['ending_cash']:,.2f}"
        )
    
    with col4:
        st.metric(
            "Break Even Revenue",
            f"${break_even_revenue:,.2f}/mo"
        )
    
    # Break-even analysis
    st.markdown("---")
    st.subheader("Break-Even Analysis")
    
    avg_revenue = projection_df['Revenue'].mean()
    
    if avg_revenue >= break_even_revenue:
        margin = avg_revenue - break_even_revenue
        st.success(
            f"✅ Your average monthly revenue (${avg_revenue:,.2f}) exceeds "
            f"break-even by ${margin:,.2f}"
        )
    else:
        gap = break_even_revenue - avg_revenue
        st.warning(
            f"⚠️ Your average monthly revenue (${avg_revenue:,.2f}) is "
            f"${gap:,.2f} below break-even"
        )
    
    # Projection Table
    st.markdown("---")
    st.subheader("Monthly Projection")
    
    # Format the DataFrame for display
    display_df = projection_df.copy()
    display_df['Revenue'] = display_df['Revenue'].apply(lambda x: f"${x:,.2f}")
    display_df['COGS'] = display_df['COGS'].apply(lambda x: f"${x:,.2f}")
    display_df['Expenses'] = display_df['Expenses'].apply(lambda x: f"${x:,.2f}")
    display_df['Net Profit'] = display_df['Net Profit'].apply(lambda x: f"${x:,.2f}")
    display_df['Ending Cash'] = display_df['Ending Cash'].apply(lambda x: f"${x:,.2f}")
    
    st.dataframe(display_df, width='stretch')
    
    # Download button for CSV
    csv = projection_df.to_csv(index=False)
    st.download_button(
        label="📥 Download Projection as CSV",
        data=csv,
        file_name=f"{business_name.replace(' ', '_')}_projection.csv",
        mime="text/csv"
    )
