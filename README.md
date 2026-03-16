# Financial Modeler Lite 💰

A lightweight Streamlit financial projection tool designed for small business advisors and entrepreneurs. The tool generates a simple 12-month financial projection using a minimal set of inputs and displays results including cash flow, net profit, charts, and break-even analysis.

## Features

- **Simple Input Interface**: Sidebar form for entering business assumptions
- **12-Month Projections**: Automatic calculation of revenue, costs, profit, and cash flow
- **Break-Even Analysis**: Instantly see if your business model is viable
- **Visual Charts**: Interactive Plotly charts for revenue, profit, and cash trends
- **Export Capability**: Download projections as CSV for further analysis
- **Sample Data**: Pre-loaded example to explore the tool quickly

## Financial Calculations

### Revenue Projection
- Month 1: Uses your average monthly revenue
- Future months: Applies growth rate to previous month

### Cost of Goods Sold (COGS)
- Calculated as a percentage of revenue

### Operating Expenses
- Rent + Payroll + Utilities + Software + Miscellaneous + Owner Draw + Loan Payment

### Net Profit
- Revenue - COGS - Operating Expenses

### Cash Flow
- Month 1: Starting Cash - Startup Costs + Net Profit
- Future months: Previous Cash + Net Profit

### Break-Even Revenue
- Fixed Costs ÷ Contribution Margin
- Where Contribution Margin = 1 - (COGS % ÷ 100)

## Installation & Local Setup

### Prerequisites
- Python 3.11.9 or higher
- pip package manager

### Steps

1. **Clone or download this repository**

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser**
   - The app will automatically open at `http://localhost:8501`

## Usage

1. **Enter Business Information**: Fill out the sidebar form with your business assumptions
2. **Adjust Projections**: Modify any values to see real-time updates
3. **Load Sample Data**: Click "Load Sample Data" to see an example (Sample Coffee Shop)
4. **Review Results**: Examine the projection table, charts, and break-even analysis
5. **Export Data**: Download the projection as CSV for external use

## Project Structure

```
financial_modeler_lite/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── runtime.txt                 # Python version specification
├── README.md                   # This file
├── model/
│   └── financial_engine.py     # Core financial calculation logic
├── ui/
│   ├── input_panel.py          # Sidebar input form
│   └── results_panel.py        # Main results display
├── utils/
│   └── charts.py               # Plotly chart generation
├── data/
│   └── sample_inputs.json      # Sample business data
└── docs/
    └── windsurf_reports/       # Documentation and reports
```

## Deployment to Render

This application is configured for deployment on Render Web Service.

### Render Configuration

**Build Command:**
```bash
pip install -r requirements.txt
```

**Start Command:**
```bash
streamlit run app.py --server.port $PORT
```

### Deployment Steps

1. Create a new Web Service on Render
2. Connect your repository
3. Set the build and start commands as shown above
4. Deploy!

## Future Enhancement Ideas

- **Scenario Comparison**: Compare conservative, expected, and aggressive projections side-by-side
- **Excel Export**: Export formatted Excel workbooks with charts
- **Funding Gap Detector**: Alert when cash balance goes negative and calculate funding needs
- **Multi-Year Projections**: Extend beyond 12 months
- **Industry Benchmarks**: Compare your metrics to industry standards
- **Sensitivity Analysis**: See how changes in key variables affect outcomes

## Code Quality Guidelines

This project follows these principles:
- Separation of financial logic from UI components
- Modular, reusable functions
- Clear comments on financial formulas
- Minimal complexity for maintainability
- Readability over cleverness

## License

This project is open source and available for use by entrepreneurs and advisors.

## Support

For questions or issues, please refer to the documentation in the `docs/` folder.

---

**Built with ❤️ for entrepreneurs and small business advisors**
