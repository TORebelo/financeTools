"""
Module for displaying forecasted financial statements.
"""

import tkinter as tk
from tkinter import ttk

from gui.statement_views import (
    show_income_statement,
    show_balance_sheet,
    show_cash_flow_statement
)

def show_forecasted_statements(parent, forecasted_data, forecast_year):
    """
    Display forecasted financial statements.
    
    Args:
        parent: Parent widget
        forecasted_data: Forecasted financial data
        forecast_year: Forecast year (e.g., "2024")
    """
    # Create a new window
    window = tk.Toplevel(parent)
    window.title(f"{forecasted_data.company_name} - Forecasted Statements for {forecast_year}")
    window.geometry("600x500")
    
    # Create a frame for the title
    title_frame = tk.Frame(window, pady=10)
    title_frame.pack(fill='x')
    
    # Add a title
    title_label = tk.Label(
        title_frame, 
        text=f"{forecasted_data.company_name} - Forecasted Financial Statements", 
        font=("Arial", 16, "bold")
    )
    title_label.pack()
    
    subtitle_label = tk.Label(
        title_frame, 
        text=f"Year Ending December 31, {forecast_year}", 
        font=("Arial", 12)
    )
    subtitle_label.pack()
    
    # Create a frame for the buttons
    button_frame = ttk.Frame(window, padding=20)
    button_frame.pack(fill='both', expand=True)
    
    # Define button style
    button_width = 25
    button_height = 2
    button_font = ("Arial", 10)
    button_padx = 10
    button_pady = 10
    
    # Income Statement Button
    income_button = tk.Button(
        button_frame,
        text="Forecasted Income Statement",
        command=lambda: show_income_statement(
            forecasted_data.company_name, f"Year Ending December 31, {forecast_year}",
            forecasted_data.revenue, 
            forecasted_data.cogs, 
            forecasted_data.operating_expenses, 
            forecasted_data.interest_expense, 
            forecasted_data.tax_rate
        ),
        width=button_width,
        height=button_height,
        font=button_font,
        bg="#f0f0f0",
        activebackground="#e0e0e0"
    )
    income_button.grid(row=0, column=0, padx=button_padx, pady=button_pady)
    
    # Balance Sheet Button
    balance_button = tk.Button(
        button_frame,
        text="Forecasted Balance Sheet",
        command=lambda: show_balance_sheet(
            forecasted_data.company_name, f"December 31, {forecast_year}",
            # Assets
            forecasted_data.cash, 
            forecasted_data.accounts_receivable, 
            forecasted_data.inventory, 
            forecasted_data.prepaid_expenses,
            forecasted_data.property_plant_equipment, 
            forecasted_data.accumulated_depreciation, 
            forecasted_data.intangible_assets,
            # Liabilities
            forecasted_data.accounts_payable, 
            forecasted_data.accrued_expenses, 
            forecasted_data.short_term_debt,
            forecasted_data.long_term_debt, 
            forecasted_data.deferred_revenue,
            # Equity
            forecasted_data.common_stock, 
            forecasted_data.retained_earnings,
            forecasted_data.treasury_stock
        ),
        width=button_width,
        height=button_height,
        font=button_font,
        bg="#f0f0f0",
        activebackground="#e0e0e0"
    )
    balance_button.grid(row=0, column=1, padx=button_padx, pady=button_pady)
    
    # Cash Flow Statement Button
    cash_flow_button = tk.Button(
        button_frame,
        text="Forecasted Cash Flow Statement",
        command=lambda: show_cash_flow_statement(
            forecasted_data.company_name, f"Year Ending December 31, {forecast_year}",
            # Operating Activities
            forecasted_data.net_income,
            forecasted_data.depreciation_amortization,
            forecasted_data.accounts_receivable_change,
            forecasted_data.inventory_change,
            forecasted_data.accounts_payable_change,
            forecasted_data.accrued_expenses_change,
            forecasted_data.deferred_revenue_change,
            # Investing Activities
            forecasted_data.capital_expenditures,
            forecasted_data.acquisitions,
            forecasted_data.investments_sold,
            # Financing Activities
            forecasted_data.debt_issuance,
            forecasted_data.debt_repayment,
            forecasted_data.dividends_paid,
            forecasted_data.stock_issuance,
            forecasted_data.stock_repurchase,
            # Cash Balances
            forecasted_data.beginning_cash_balance
        ),
        width=button_width,
        height=button_height,
        font=button_font,
        bg="#f0f0f0",
        activebackground="#e0e0e0"
    )
    cash_flow_button.grid(row=1, column=0, columnspan=2, padx=button_padx, pady=button_pady)
    
    # Add a description of the forecasted statements
    description_frame = ttk.Frame(window, padding=10)
    description_frame.pack(fill='x', padx=10, pady=10)
    
    description_text = """
    These forecasted financial statements represent management's expectations for the upcoming fiscal year.
    
    The forecasts are based on the assumptions set in the forecast editor and reflect anticipated changes in
    revenue, expenses, assets, and liabilities. These projections should be used for planning purposes and
    are subject to change based on actual business performance and market conditions.
    """
    
    description_label = ttk.Label(description_frame, text=description_text, wraplength=550, justify="left")
    description_label.pack(fill='x')
    
    # Add a close button
    close_button = ttk.Button(window, text="Close", command=window.destroy)
    close_button.pack(pady=10)