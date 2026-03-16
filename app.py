import streamlit as st
from model.financial_engine import calculate_projection, calculate_break_even, calculate_summary_metrics
from ui.input_panel import render_input_panel
from ui.results_panel import render_results_panel
from utils.charts import create_revenue_chart, create_profit_chart, create_cash_chart, create_combined_chart


def main():
    """
    Main application entry point for Financial Modeler Lite.
    """
    st.set_page_config(
        page_title="Financial Modeler Lite",
        page_icon="💰",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Render input panel and get user inputs
    inputs = render_input_panel()
    
    # Calculate financial projection
    projection_df = calculate_projection(inputs)
    
    # Calculate break-even revenue
    break_even_revenue = calculate_break_even(inputs)
    
    # Calculate summary metrics
    summary_metrics = calculate_summary_metrics(projection_df)
    
    # Render results panel
    render_results_panel(
        projection_df=projection_df,
        summary_metrics=summary_metrics,
        break_even_revenue=break_even_revenue,
        business_name=inputs['business_name']
    )
    
    # Charts Section
    st.markdown("---")
    st.subheader("📈 Visual Analysis")
    
    # Create tabs for different chart views
    tab1, tab2, tab3, tab4 = st.tabs([
        "Combined View",
        "Revenue",
        "Net Profit",
        "Cash Balance"
    ])
    
    with tab1:
        st.plotly_chart(
            create_combined_chart(projection_df),
            width='stretch'
        )
    
    with tab2:
        st.plotly_chart(
            create_revenue_chart(projection_df),
            width='stretch'
        )
    
    with tab3:
        st.plotly_chart(
            create_profit_chart(projection_df),
            width='stretch'
        )
    
    with tab4:
        st.plotly_chart(
            create_cash_chart(projection_df),
            width='stretch'
        )
    
    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: #666; padding: 20px;'>
            <p><strong>Financial Modeler Lite</strong> | A simple financial projection tool for entrepreneurs and advisors</p>
            <p style='font-size: 0.9em;'>Use this tool to quickly evaluate business feasibility and cash flow projections</p>
        </div>
        """,
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
