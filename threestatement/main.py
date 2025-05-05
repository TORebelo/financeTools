"""
Main application entry point for the financial statement application.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import os

from gui.components import create_button
from gui.statement_views import (
    show_income_statement,
    show_balance_sheet,
    show_cash_flow_statement,
    show_investing_analysis
)
from gui.comparison_views import (
    show_comparison_statement,
    show_management_discussion
)
from core.data_models import FinancialData
from analysis.forecasting import FinancialForecast
from analysis.comparison import FinancialComparison
from gui.editors import AssumptionsEditor
from gui.forecast_views import show_forecasted_statements

# Ensure directories exist
def ensure_directories():
    """Create necessary directories if they don't exist."""
    directories = [
        'core',
        'analysis',
        'gui',
    ]
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)

def main_financial_dashboard():
    """
    Main function to create a financial dashboard with buttons to show each statement
    """
    # Ensure directories exist
    ensure_directories()
    
    # Create the main window
    root = tk.Tk()
    root.title("Financial Statements Dashboard")
    root.geometry("900x700")
    
    # Company information
    company_name = "ABC Corporation"
    reporting_period = "Year Ended December 31, 2023"
    reporting_date = "December 31, 2023"
    
    # Create financial data model
    financial_data = FinancialData(company_name, reporting_period, reporting_date)
    financial_data.load_sample_data()
    
    # Create forecast model
    forecast_model = FinancialForecast(financial_data)
    
    # Create a frame for the title
    title_frame = tk.Frame(root, pady=20)
    title_frame.pack(fill='x')
    
    # Add a title
    title_label = tk.Label(title_frame, text=f"{company_name} Financial Statements", font=("Arial", 16, "bold"))
    title_label.pack()
    
    subtitle_label = tk.Label(title_frame, text=reporting_period, font=("Arial", 12))
    subtitle_label.pack()
    
    # Create notebook (tabbed interface)
    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True, padx=10, pady=10)
    
    # Create tabs
    current_tab = ttk.Frame(notebook)
    forecast_tab = ttk.Frame(notebook)
    comparison_tab = ttk.Frame(notebook)
    
    notebook.add(current_tab, text="Current Statements")
    notebook.add(forecast_tab, text="Forecast")
    notebook.add(comparison_tab, text="Comparison")
    
    # Current Statements Tab
    current_frame = ttk.LabelFrame(current_tab, text="Current Financial Statements")
    current_frame.pack(fill='both', expand=True, padx=10, pady=10)
    
    # Define button style
    button_width = 25
    button_height = 2
    button_font = ("Arial", 10)
    button_padx = 10
    button_pady = 10
    
    # Create a frame for the buttons in current tab
    current_button_frame = tk.Frame(current_frame, pady=20)
    current_button_frame.pack()
    
    # Income Statement Button
    income_button = create_button(
        current_button_frame, 
        "Income Statement", 
        lambda: show_income_statement(
            company_name, reporting_period,
            financial_data.revenue, 
            financial_data.cogs, 
            financial_data.operating_expenses, 
            financial_data.interest_expense, 
            financial_data.tax_rate
        ),
        button_width,
        button_height,
        button_font
    )
    income_button.grid(row=0, column=0, padx=button_padx, pady=button_pady)
    
    # Balance Sheet Button
    balance_button = create_button(
        current_button_frame, 
        "Balance Sheet", 
        lambda: show_balance_sheet(
            company_name, reporting_date,
            # Assets
            financial_data.cash, 
            financial_data.accounts_receivable, 
            financial_data.inventory, 
            financial_data.prepaid_expenses,
            financial_data.property_plant_equipment, 
            financial_data.accumulated_depreciation, 
            financial_data.intangible_assets,
            # Liabilities
            financial_data.accounts_payable, 
            financial_data.accrued_expenses, 
            financial_data.short_term_debt,
            financial_data.long_term_debt, 
            financial_data.deferred_revenue,
            # Equity
            financial_data.common_stock, 
            financial_data.retained_earnings,
            financial_data.treasury_stock
        ),
        button_width,
        button_height,
        button_font
    )
    balance_button.grid(row=0, column=1, padx=button_padx, pady=button_pady)
    
    # Cash Flow Statement Button
    cash_flow_button = create_button(
        current_button_frame, 
        "Cash Flow Statement", 
        lambda: show_cash_flow_statement(
            company_name, reporting_period,
            # Operating Activities
            financial_data.net_income,
            financial_data.depreciation_amortization,
            financial_data.accounts_receivable_change,
            financial_data.inventory_change,
            financial_data.accounts_payable_change,
            financial_data.accrued_expenses_change,
            financial_data.deferred_revenue_change,
            # Investing Activities
            financial_data.capital_expenditures,
            financial_data.acquisitions,
            financial_data.investments_sold,
            # Financing Activities
            financial_data.debt_issuance,
            financial_data.debt_repayment,
            financial_data.dividends_paid,
            financial_data.stock_issuance,
            financial_data.stock_repurchase,
            # Cash Balances
            financial_data.beginning_cash_balance
        ),
        button_width,
        button_height,
        button_font
    )
    cash_flow_button.grid(row=1, column=0, padx=button_padx, pady=button_pady)
    
    # Investing Analysis Button
    investing_button = create_button(
        current_button_frame, 
        "Investing Activities Analysis", 
        lambda: show_investing_analysis(
            financial_data.net_income + financial_data.depreciation_amortization,  # Operating cash flow
            financial_data.capital_expenditures,
            financial_data.cash + financial_data.accounts_receivable + 
            financial_data.inventory + financial_data.prepaid_expenses + 
            financial_data.property_plant_equipment - financial_data.accumulated_depreciation + 
            financial_data.intangible_assets,  # Total assets
            financial_data.revenue
        ),
        button_width,
        button_height,
        button_font
    )
    investing_button.grid(row=1, column=1, padx=button_padx, pady=button_pady)
    
    # Forecast Tab
    forecast_frame = ttk.LabelFrame(forecast_tab, text="Financial Forecasting")
    forecast_frame.pack(fill='both', expand=True, padx=10, pady=10)
    
    # Create a frame for the forecast controls
    forecast_control_frame = tk.Frame(forecast_frame, pady=20)
    forecast_control_frame.pack()
    
    # Function to handle forecast generation
    def generate_forecast():
        try:
            # Generate the forecast
            forecasted_data = forecast_model.generate_forecast()
            
            # Show the forecasted statements
            next_year = int(reporting_period[-4:]) + 1
            show_forecasted_statements(root, forecasted_data, str(next_year))
        except Exception as e:
            messagebox.showerror("Forecast Error", f"Error generating forecast: {str(e)}")
    
    # Function to open assumptions editor
    def open_assumptions_editor():
        AssumptionsEditor(root, forecast_model, on_apply_callback=None)
    
    # Edit Assumptions Button
    assumptions_button = create_button(
        forecast_control_frame, 
        "Edit Forecast Assumptions", 
        open_assumptions_editor,
        button_width,
        button_height,
        button_font
    )
    assumptions_button.grid(row=0, column=0, padx=button_padx, pady=button_pady)
    
    # Generate Forecast Button
    generate_button = create_button(
        forecast_control_frame, 
        "Generate Next Year Forecast", 
        generate_forecast,
        button_width,
        button_height,
        button_font
    )
    generate_button.grid(row=0, column=1, padx=button_padx, pady=button_pady)
    
    # Comparison Tab
    comparison_frame = ttk.LabelFrame(comparison_tab, text="Financial Statement Comparison")
    comparison_frame.pack(fill='both', expand=True, padx=10, pady=10)
    
    # Create a frame for the comparison controls
    comparison_control_frame = tk.Frame(comparison_frame, pady=20)
    comparison_control_frame.pack()
    
    # Function to generate comparison
    def generate_comparison():
        try:
            # Generate the forecast if not already done
            forecasted_data = forecast_model.generate_forecast()
            
            # Create comparison object
            comparison = FinancialComparison(financial_data, forecasted_data)
            
            # Get years
            base_year = reporting_period[-4:]
            next_year = str(int(base_year) + 1)
            
            # Show comparison window based on selected statement type
            statement_type = comparison_type_var.get()
            
            if statement_type == "income":
                show_comparison_statement(root, comparison, "income", base_year, next_year)
            elif statement_type == "balance":
                show_comparison_statement(root, comparison, "balance", base_year, next_year)
            elif statement_type == "cash_flow":
                show_comparison_statement(root, comparison, "cash_flow", base_year, next_year)
            elif statement_type == "md&a":
                show_management_discussion(root, comparison, base_year, next_year)
            else:
                messagebox.showerror("Error", "Please select a statement type for comparison.")
        except Exception as e:
            messagebox.showerror("Comparison Error", f"Error generating comparison: {str(e)}")
    
    # Create a frame for statement type selection
    selection_frame = ttk.LabelFrame(comparison_control_frame, text="Select Statement Type")
    selection_frame.grid(row=0, column=0, padx=button_padx, pady=button_pady)
    
    # Radio buttons for statement type
    comparison_type_var = tk.StringVar(value="income")
    
    ttk.Radiobutton(
        selection_frame, 
        text="Income Statement", 
        value="income", 
        variable=comparison_type_var
    ).pack(anchor="w", padx=5, pady=5)
    
    ttk.Radiobutton(
        selection_frame, 
        text="Balance Sheet", 
        value="balance", 
        variable=comparison_type_var
    ).pack(anchor="w", padx=5, pady=5)
    
    ttk.Radiobutton(
        selection_frame, 
        text="Cash Flow Statement", 
        value="cash_flow", 
        variable=comparison_type_var
    ).pack(anchor="w", padx=5, pady=5)
    
    ttk.Radiobutton(
        selection_frame, 
        text="Management Discussion & Analysis", 
        value="md&a", 
        variable=comparison_type_var
    ).pack(anchor="w", padx=5, pady=5)
    
    # Generate Comparison Button
    comparison_button = create_button(
        comparison_control_frame, 
        "Generate Comparison", 
        generate_comparison,
        button_width,
        button_height,
        button_font
    )
    comparison_button.grid(row=0, column=1, padx=button_padx, pady=button_pady)
    
    # Add a description of the comparison feature
    description_frame = ttk.Frame(comparison_frame, padding=10)
    description_frame.pack(fill='x', padx=10, pady=10)
    
    description_text = """
    The Comparison feature allows you to compare current financial statements with forecasted statements.
    
    1. First, set your forecast assumptions in the Forecast tab
    2. Select the type of statement you want to compare
    3. Click "Generate Comparison" to view a side-by-side comparison with explanatory notes
    
    The Management Discussion & Analysis option provides a comprehensive overview of all significant changes.
    """
    
    description_label = ttk.Label(description_frame, text=description_text, wraplength=600, justify="left")
    description_label.pack(fill='x')
    
    # Add a footer
    footer_frame = tk.Frame(root, pady=10)
    footer_frame.pack(side=tk.BOTTOM, fill='x')
    
    footer_text = tk.Label(footer_frame, text="© 2023 Financial Statement Generator", font=("Arial", 8))
    footer_text.pack()
    
    # Start the main loop
    root.mainloop()


if __name__ == "__main__":
    main_financial_dashboard()