import pandas as pd
import numpy as np


def calculate_projection(inputs):
    """
    Generate a 12-month financial projection based on user inputs.
    
    Args:
        inputs (dict): Dictionary containing all financial assumptions
        
    Returns:
        pd.DataFrame: Monthly projection with revenue, costs, profit, and cash
    """
    months = inputs.get('months', 12)
    
    # Initialize arrays for each metric
    month_numbers = list(range(1, months + 1))
    revenues = []
    cogs_values = []
    expenses_values = []
    net_profits = []
    cash_balances = []
    
    # Extract inputs
    starting_cash = inputs['starting_cash']
    avg_revenue = inputs['average_monthly_revenue']
    growth_rate = inputs['monthly_growth_rate']
    cogs_percent = inputs['cogs_percent']
    startup_costs = inputs['startup_costs']
    
    # Calculate fixed monthly operating expenses
    operating_expenses = (
        inputs['rent'] +
        inputs['payroll'] +
        inputs['utilities'] +
        inputs['software'] +
        inputs['miscellaneous'] +
        inputs['owner_draw'] +
        inputs['monthly_loan_payment']
    )
    
    # Month-by-month calculation
    for month in range(months):
        # Revenue calculation: Month 1 uses average, future months apply growth
        if month == 0:
            revenue = avg_revenue
        else:
            revenue = revenues[month - 1] * (1 + growth_rate)
        
        # COGS calculation
        cogs = revenue * (cogs_percent / 100)
        
        # Net profit calculation
        net_profit = revenue - cogs - operating_expenses
        
        # Cash flow calculation
        if month == 0:
            # Month 1: Start with initial cash, subtract startup costs, add net profit
            cash = starting_cash - startup_costs + net_profit
        else:
            # Future months: Prior cash + net profit
            cash = cash_balances[month - 1] + net_profit
        
        # Store results
        revenues.append(revenue)
        cogs_values.append(cogs)
        expenses_values.append(operating_expenses)
        net_profits.append(net_profit)
        cash_balances.append(cash)
    
    # Create DataFrame
    projection_df = pd.DataFrame({
        'Month': month_numbers,
        'Revenue': revenues,
        'COGS': cogs_values,
        'Expenses': expenses_values,
        'Net Profit': net_profits,
        'Ending Cash': cash_balances
    })
    
    return projection_df


def calculate_break_even(inputs):
    """
    Calculate the monthly revenue needed to break even.
    
    Formula:
        Break Even Revenue = Fixed Costs / Contribution Margin
        where Contribution Margin = 1 - (COGS % / 100)
    
    Args:
        inputs (dict): Dictionary containing financial assumptions
        
    Returns:
        float: Break-even monthly revenue
    """
    # Fixed costs = total operating expenses
    fixed_costs = (
        inputs['rent'] +
        inputs['payroll'] +
        inputs['utilities'] +
        inputs['software'] +
        inputs['miscellaneous'] +
        inputs['owner_draw'] +
        inputs['monthly_loan_payment']
    )
    
    # Contribution margin = 1 - COGS percentage
    contribution_margin = 1 - (inputs['cogs_percent'] / 100)
    
    # Avoid division by zero
    if contribution_margin <= 0:
        return float('inf')
    
    break_even_revenue = fixed_costs / contribution_margin
    
    return break_even_revenue


def calculate_summary_metrics(projection_df):
    """
    Calculate summary metrics from the projection DataFrame.
    
    Args:
        projection_df (pd.DataFrame): Monthly projection data
        
    Returns:
        dict: Summary metrics including totals and ending balances
    """
    summary = {
        'total_revenue': projection_df['Revenue'].sum(),
        'total_net_profit': projection_df['Net Profit'].sum(),
        'ending_cash': projection_df['Ending Cash'].iloc[-1]
    }
    
    return summary
