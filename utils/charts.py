import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


def create_revenue_chart(projection_df):
    """
    Create a line chart showing revenue projection over time.
    
    Args:
        projection_df (pd.DataFrame): Monthly projection data
        
    Returns:
        plotly.graph_objects.Figure: Revenue chart
    """
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=projection_df['Month'],
        y=projection_df['Revenue'],
        mode='lines+markers',
        name='Revenue',
        line=dict(color='#2E86AB', width=3),
        marker=dict(size=8)
    ))
    
    fig.update_layout(
        title='Revenue Projection',
        xaxis_title='Month',
        yaxis_title='Revenue ($)',
        hovermode='x unified',
        template='plotly_white',
        height=400,
        margin=dict(l=20, r=20, t=40, b=20)
    )
    
    fig.update_yaxes(tickformat='$,.0f')
    
    return fig


def create_profit_chart(projection_df):
    """
    Create a bar chart showing net profit by month.
    
    Args:
        projection_df (pd.DataFrame): Monthly projection data
        
    Returns:
        plotly.graph_objects.Figure: Net profit chart
    """
    # Color bars based on positive/negative profit
    colors = ['#06A77D' if x >= 0 else '#D62828' for x in projection_df['Net Profit']]
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=projection_df['Month'],
        y=projection_df['Net Profit'],
        name='Net Profit',
        marker_color=colors
    ))
    
    # Add a zero line
    fig.add_hline(y=0, line_dash="dash", line_color="gray", opacity=0.5)
    
    fig.update_layout(
        title='Net Profit by Month',
        xaxis_title='Month',
        yaxis_title='Net Profit ($)',
        hovermode='x unified',
        template='plotly_white',
        height=400,
        margin=dict(l=20, r=20, t=40, b=20)
    )
    
    fig.update_yaxes(tickformat='$,.0f')
    
    return fig


def create_cash_chart(projection_df):
    """
    Create an area chart showing cash balance over time.
    
    Args:
        projection_df (pd.DataFrame): Monthly projection data
        
    Returns:
        plotly.graph_objects.Figure: Cash balance chart
    """
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=projection_df['Month'],
        y=projection_df['Ending Cash'],
        mode='lines',
        name='Cash Balance',
        fill='tozeroy',
        line=dict(color='#F77F00', width=2),
        fillcolor='rgba(247, 127, 0, 0.2)'
    ))
    
    # Add a zero line
    fig.add_hline(y=0, line_dash="dash", line_color="red", opacity=0.5)
    
    fig.update_layout(
        title='Cash Balance Over Time',
        xaxis_title='Month',
        yaxis_title='Cash Balance ($)',
        hovermode='x unified',
        template='plotly_white',
        height=400,
        margin=dict(l=20, r=20, t=40, b=20)
    )
    
    fig.update_yaxes(tickformat='$,.0f')
    
    return fig


def create_combined_chart(projection_df):
    """
    Create a combined chart showing revenue, expenses, and profit.
    
    Args:
        projection_df (pd.DataFrame): Monthly projection data
        
    Returns:
        plotly.graph_objects.Figure: Combined financial chart
    """
    fig = go.Figure()
    
    # Calculate total costs
    projection_df['Total Costs'] = projection_df['COGS'] + projection_df['Expenses']
    
    fig.add_trace(go.Scatter(
        x=projection_df['Month'],
        y=projection_df['Revenue'],
        mode='lines+markers',
        name='Revenue',
        line=dict(color='#2E86AB', width=2)
    ))
    
    fig.add_trace(go.Scatter(
        x=projection_df['Month'],
        y=projection_df['Total Costs'],
        mode='lines+markers',
        name='Total Costs',
        line=dict(color='#D62828', width=2)
    ))
    
    fig.add_trace(go.Scatter(
        x=projection_df['Month'],
        y=projection_df['Net Profit'],
        mode='lines+markers',
        name='Net Profit',
        line=dict(color='#06A77D', width=2)
    ))
    
    fig.update_layout(
        title='Revenue, Costs, and Profit',
        xaxis_title='Month',
        yaxis_title='Amount ($)',
        hovermode='x unified',
        template='plotly_white',
        height=500,
        margin=dict(l=20, r=20, t=40, b=20),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    fig.update_yaxes(tickformat='$,.0f')
    
    return fig
