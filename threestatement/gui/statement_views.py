"""
Module for displaying financial statements.
"""

import tkinter as tk
from tkinter import ttk

def format_currency(value):
    """Format a value as currency."""
    return f"${value:,.0f}"

def show_income_statement(company_name, reporting_period, revenue, cogs, operating_expenses, interest_expense, tax_rate):
    """
    Display an income statement.
    
    Args:
        company_name: Name of the company
        reporting_period: Reporting period
        revenue: Revenue
        cogs: Cost of goods sold
        operating_expenses: Operating expenses
        interest_expense: Interest expense
        tax_rate: Tax rate
    """
    # Calculate derived values
    gross_profit = revenue - cogs
    operating_income = gross_profit - operating_expenses
    income_before_tax = operating_income - interest_expense
    income_tax = income_before_tax * tax_rate
    net_income = income_before_tax - income_tax
    
    # Create a new window
    window = tk.Toplevel()
    window.title(f"{company_name} - Income Statement")
    window.geometry("600x500")
    
    # Create a frame for the title
    title_frame = tk.Frame(window, pady=10)
    title_frame.pack(fill='x')
    
    # Add a title
    title_label = tk.Label(title_frame, text=f"{company_name}", font=("Arial", 16, "bold"))
    title_label.pack()
    
    subtitle_label = tk.Label(title_frame, text="Income Statement", font=("Arial", 14))
    subtitle_label.pack()
    
    period_label = tk.Label(title_frame, text=reporting_period, font=("Arial", 12))
    period_label.pack()
    
    # Create a frame for the income statement
    statement_frame = ttk.Frame(window, padding=20)
    statement_frame.pack(fill='both', expand=True)
    
    # Create the income statement
    row = 0
    
    # Revenue
    revenue_label = ttk.Label(statement_frame, text="Revenue", font=("Arial", 10, "bold"))
    revenue_label.grid(row=row, column=0, sticky="w", padx=5, pady=5)
    
    revenue_value = ttk.Label(statement_frame, text=format_currency(revenue), font=("Arial", 10, "bold"))
    revenue_value.grid(row=row, column=1, sticky="e", padx=5, pady=5)
    
    row += 1
    
    # Cost of Goods Sold
    cogs_label = ttk.Label(statement_frame, text="Cost of Goods Sold")
    cogs_label.grid(row=row, column=0, sticky="w", padx=5, pady=2)
    
    cogs_value = ttk.Label(statement_frame, text=format_currency(cogs))
    cogs_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
    
    row += 1
    
    # Gross Profit
    ttk.Separator(statement_frame, orient='horizontal').grid(row=row, column=0, columnspan=2, sticky="ew", pady=5)
    row += 1
    
    gross_profit_label = ttk.Label(statement_frame, text="Gross Profit", font=("Arial", 10, "bold"))
    gross_profit_label.grid(row=row, column=0, sticky="w", padx=5, pady=5)
    
    gross_profit_value = ttk.Label(statement_frame, text=format_currency(gross_profit), font=("Arial", 10, "bold"))
    gross_profit_value.grid(row=row, column=1, sticky="e", padx=5, pady=5)
    
    row += 1
    
    # Operating Expenses
    opex_label = ttk.Label(statement_frame, text="Operating Expenses")
    opex_label.grid(row=row, column=0, sticky="w", padx=5, pady=2)
    
    opex_value = ttk.Label(statement_frame, text=format_currency(operating_expenses))
    opex_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
    
    row += 1
    
    # Operating Income
    ttk.Separator(statement_frame, orient='horizontal').grid(row=row, column=0, columnspan=2, sticky="ew", pady=5)
    row += 1
    
    operating_income_label = ttk.Label(statement_frame, text="Operating Income", font=("Arial", 10, "bold"))
    operating_income_label.grid(row=row, column=0, sticky="w", padx=5, pady=5)
    
    operating_income_value = ttk.Label(statement_frame, text=format_currency(operating_income), font=("Arial", 10, "bold"))
    operating_income_value.grid(row=row, column=1, sticky="e", padx=5, pady=5)
    
    row += 1
    
    # Interest Expense
    interest_label = ttk.Label(statement_frame, text="Interest Expense")
    interest_label.grid(row=row, column=0, sticky="w", padx=5, pady=2)
    
    interest_value = ttk.Label(statement_frame, text=format_currency(interest_expense))
    interest_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
    
    row += 1
    
    # Income Before Tax
    ttk.Separator(statement_frame, orient='horizontal').grid(row=row, column=0, columnspan=2, sticky="ew", pady=5)
    row += 1
    
    ebt_label = ttk.Label(statement_frame, text="Income Before Tax", font=("Arial", 10, "bold"))
    ebt_label.grid(row=row, column=0, sticky="w", padx=5, pady=5)
    
    ebt_value = ttk.Label(statement_frame, text=format_currency(income_before_tax), font=("Arial", 10, "bold"))
    ebt_value.grid(row=row, column=1, sticky="e", padx=5, pady=5)
    
    row += 1
    
    # Income Tax
    tax_label = ttk.Label(statement_frame, text=f"Income Tax ({tax_rate:.0%})")
    tax_label.grid(row=row, column=0, sticky="w", padx=5, pady=2)
    
    tax_value = ttk.Label(statement_frame, text=format_currency(income_tax))
    tax_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
    
    row += 1
    
    # Net Income
    ttk.Separator(statement_frame, orient='horizontal').grid(row=row, column=0, columnspan=2, sticky="ew", pady=5)
    row += 1
    
    net_income_label = ttk.Label(statement_frame, text="Net Income", font=("Arial", 10, "bold"))
    net_income_label.grid(row=row, column=0, sticky="w", padx=5, pady=5)
    
    net_income_value = ttk.Label(statement_frame, text=format_currency(net_income), font=("Arial", 10, "bold"))
    net_income_value.grid(row=row, column=1, sticky="e", padx=5, pady=5)
    
    # Add a close button
    close_button = ttk.Button(window, text="Close", command=window.destroy)
    close_button.pack(pady=10)

def show_balance_sheet(company_name, reporting_date, cash, accounts_receivable, inventory, prepaid_expenses, 
                      property_plant_equipment, accumulated_depreciation, intangible_assets,
                      accounts_payable, accrued_expenses, short_term_debt, long_term_debt, deferred_revenue,
                      common_stock, retained_earnings, treasury_stock=0):
    """
    Display a balance sheet.
    
    Args:
        company_name: Name of the company
        reporting_date: Date of the balance sheet
        cash: Cash and cash equivalents
        accounts_receivable: Accounts receivable
        inventory: Inventory
        prepaid_expenses: Prepaid expenses
        property_plant_equipment: Property, plant, and equipment
        accumulated_depreciation: Accumulated depreciation
        intangible_assets: Intangible assets
        accounts_payable: Accounts payable
        accrued_expenses: Accrued expenses
        short_term_debt: Short-term debt
        long_term_debt: Long-term debt
        deferred_revenue: Deferred revenue
        common_stock: Common stock
        retained_earnings: Retained earnings
        treasury_stock: Treasury stock
    """
    # Calculate derived values
    total_current_assets = cash + accounts_receivable + inventory + prepaid_expenses
    net_ppe = property_plant_equipment - accumulated_depreciation
    total_assets = total_current_assets + net_ppe + intangible_assets
    
    total_current_liabilities = accounts_payable + accrued_expenses + short_term_debt + deferred_revenue
    total_liabilities = total_current_liabilities + long_term_debt
    
    total_equity = common_stock + retained_earnings - treasury_stock
    total_liabilities_equity = total_liabilities + total_equity
    
    # Create a new window
    window = tk.Toplevel()
    window.title(f"{company_name} - Balance Sheet")
    window.geometry("600x700")
    
    # Create a frame for the title
    title_frame = tk.Frame(window, pady=10)
    title_frame.pack(fill='x')
    
    # Add a title
    title_label = tk.Label(title_frame, text=f"{company_name}", font=("Arial", 16, "bold"))
    title_label.pack()
    
    subtitle_label = tk.Label(title_frame, text="Balance Sheet", font=("Arial", 14))
    subtitle_label.pack()
    
    date_label = tk.Label(title_frame, text=f"As of {reporting_date}", font=("Arial", 12))
    date_label.pack()
    
    # Create a frame for the balance sheet
    statement_frame = ttk.Frame(window, padding=20)
    statement_frame.pack(fill='both', expand=True)
    
    # Create the balance sheet
    row = 0
    
    # Assets Header
    assets_label = ttk.Label(statement_frame, text="ASSETS", font=("Arial", 12, "bold"))
    assets_label.grid(row=row, column=0, sticky="w", padx=5, pady=10)
    row += 1
    
    # Current Assets Header
    current_assets_label = ttk.Label(statement_frame, text="Current Assets", font=("Arial", 10, "bold"))
    current_assets_label.grid(row=row, column=0, sticky="w", padx=5, pady=5)
    row += 1
    
    # Cash
    cash_label = ttk.Label(statement_frame, text="Cash and Cash Equivalents")
    cash_label.grid(row=row, column=0, sticky="w", padx=20, pady=2)
    
    cash_value = ttk.Label(statement_frame, text=format_currency(cash))
    cash_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
    row += 1
    
    # Accounts Receivable
    ar_label = ttk.Label(statement_frame, text="Accounts Receivable")
    ar_label.grid(row=row, column=0, sticky="w", padx=20, pady=2)
    
    ar_value = ttk.Label(statement_frame, text=format_currency(accounts_receivable))
    ar_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
    row += 1
    
    # Inventory
    inventory_label = ttk.Label(statement_frame, text="Inventory")
    inventory_label.grid(row=row, column=0, sticky="w", padx=20, pady=2)
    
    inventory_value = ttk.Label(statement_frame, text=format_currency(inventory))
    inventory_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
    row += 1
    
    # Prepaid Expenses
    prepaid_label = ttk.Label(statement_frame, text="Prepaid Expenses")
    prepaid_label.grid(row=row, column=0, sticky="w", padx=20, pady=2)
    
    prepaid_value = ttk.Label(statement_frame, text=format_currency(prepaid_expenses))
    prepaid_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
    row += 1
    
    # Total Current Assets
    ttk.Separator(statement_frame, orient='horizontal').grid(row=row, column=0, columnspan=2, sticky="ew", pady=5)
    row += 1
    
    total_ca_label = ttk.Label(statement_frame, text="Total Current Assets", font=("Arial", 10, "bold"))
    total_ca_label.grid(row=row, column=0, sticky="w", padx=5, pady=5)
    
    total_ca_value = ttk.Label(statement_frame, text=format_currency(total_current_assets), font=("Arial", 10, "bold"))
    total_ca_value.grid(row=row, column=1, sticky="e", padx=5, pady=5)
    row += 1
    
    # Non-Current Assets
    noncurrent_assets_label = ttk.Label(statement_frame, text="Non-Current Assets", font=("Arial", 10, "bold"))
    noncurrent_assets_label.grid(row=row, column=0, sticky="w", padx=5, pady=5)
    row += 1
    
    # Property, Plant, and Equipment
    ppe_label = ttk.Label(statement_frame, text="Property, Plant, and Equipment")
    ppe_label.grid(row=row, column=0, sticky="w", padx=20, pady=2)
    
    ppe_value = ttk.Label(statement_frame, text=format_currency(property_plant_equipment))
    ppe_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
    row += 1
    
    # Accumulated Depreciation
    accum_dep_label = ttk.Label(statement_frame, text="Accumulated Depreciation")
    accum_dep_label.grid(row=row, column=0, sticky="w", padx=20, pady=2)
    
    accum_dep_value = ttk.Label(statement_frame, text=f"({format_currency(accumulated_depreciation)})")
    accum_dep_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
    row += 1
    
    # Net PP&E
    net_ppe_label = ttk.Label(statement_frame, text="Net Property, Plant, and Equipment")
    net_ppe_label.grid(row=row, column=0, sticky="w", padx=20, pady=2)
    
    net_ppe_value = ttk.Label(statement_frame, text=format_currency(net_ppe))
    net_ppe_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
    row += 1
    
    # Intangible Assets
    intangible_label = ttk.Label(statement_frame, text="Intangible Assets")
    intangible_label.grid(row=row, column=0, sticky="w", padx=20, pady=2)
    
    intangible_value = ttk.Label(statement_frame, text=format_currency(intangible_assets))
    intangible_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
    row += 1
    
    # Total Assets
    ttk.Separator(statement_frame, orient='horizontal').grid(row=row, column=0, columnspan=2, sticky="ew", pady=5)
    row += 1
    
    total_assets_label = ttk.Label(statement_frame, text="TOTAL ASSETS", font=("Arial", 10, "bold"))
    total_assets_label.grid(row=row, column=0, sticky="w", padx=5, pady=5)
    
    total_assets_value = ttk.Label(statement_frame, text=format_currency(total_assets), font=("Arial", 10, "bold"))
    total_assets_value.grid(row=row, column=1, sticky="e", padx=5, pady=5)
    row += 1
    
    # Liabilities Header
    liabilities_label = ttk.Label(statement_frame, text="LIABILITIES", font=("Arial", 12, "bold"))
    liabilities_label.grid(row=row, column=0, sticky="w", padx=5, pady=10)
    row += 1
    
    # Current Liabilities Header
    current_liabilities_label = ttk.Label(statement_frame, text="Current Liabilities", font=("Arial", 10, "bold"))
    current_liabilities_label.grid(row=row, column=0, sticky="w", padx=5, pady=5)
    row += 1
    
    # Accounts Payable
    ap_label = ttk.Label(statement_frame, text="Accounts Payable")
    ap_label.grid(row=row, column=0, sticky="w", padx=20, pady=2)
    
    ap_value = ttk.Label(statement_frame, text=format_currency(accounts_payable))
    ap_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
    row += 1
    
    # Accrued Expenses
    accrued_label = ttk.Label(statement_frame, text="Accrued Expenses")
    accrued_label.grid(row=row, column=0, sticky="w", padx=20, pady=2)
    
    accrued_value = ttk.Label(statement_frame, text=format_currency(accrued_expenses))
    accrued_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
    row += 1
    
    # Short-term Debt
    std_label = ttk.Label(statement_frame, text="Short-term Debt")
    std_label.grid(row=row, column=0, sticky="w", padx=20, pady=2)
    
    std_value = ttk.Label(statement_frame, text=format_currency(short_term_debt))
    std_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
    row += 1
    
    # Deferred Revenue
    deferred_label = ttk.Label(statement_frame, text="Deferred Revenue")
    deferred_label.grid(row=row, column=0, sticky="w", padx=20, pady=2)
    
    deferred_value = ttk.Label(statement_frame, text=format_currency(deferred_revenue))
    deferred_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
    row += 1
    
    # Total Current Liabilities
    ttk.Separator(statement_frame, orient='horizontal').grid(row=row, column=0, columnspan=2, sticky="ew", pady=5)
    row += 1
    
    total_cl_label = ttk.Label(statement_frame, text="Total Current Liabilities", font=("Arial", 10, "bold"))
    total_cl_label.grid(row=row, column=0, sticky="w", padx=5, pady=5)
    
    total_cl_value = ttk.Label(statement_frame, text=format_currency(total_current_liabilities), font=("Arial", 10, "bold"))
    total_cl_value.grid(row=row, column=1, sticky="e", padx=5, pady=5)
    row += 1
    
    # Long-term Debt
    ltd_label = ttk.Label(statement_frame, text="Long-term Debt")
    ltd_label.grid(row=row, column=0, sticky="w", padx=20, pady=2)
    
    ltd_value = ttk.Label(statement_frame, text=format_currency(long_term_debt))
    ltd_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
    row += 1
    
    # Total Liabilities
    ttk.Separator(statement_frame, orient='horizontal').grid(row=row, column=0, columnspan=2, sticky="ew", pady=5)
    row += 1
    
    total_liabilities_label = ttk.Label(statement_frame, text="TOTAL LIABILITIES", font=("Arial", 10, "bold"))
    total_liabilities_label.grid(row=row, column=0, sticky="w", padx=5, pady=5)
    
    total_liabilities_value = ttk.Label(statement_frame, text=format_currency(total_liabilities), font=("Arial", 10, "bold"))
    total_liabilities_value.grid(row=row, column=1, sticky="e", padx=5, pady=5)
    row += 1
    
    # Equity Header
    equity_label = ttk.Label(statement_frame, text="EQUITY", font=("Arial", 12, "bold"))
    equity_label.grid(row=row, column=0, sticky="w", padx=5, pady=10)
    row += 1
    
    # Common Stock
    cs_label = ttk.Label(statement_frame, text="Common Stock")
    cs_label.grid(row=row, column=0, sticky="w", padx=20, pady=2)
    
    cs_value = ttk.Label(statement_frame, text=format_currency(common_stock))
    cs_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
    row += 1
    
    # Retained Earnings
    re_label = ttk.Label(statement_frame, text="Retained Earnings")
    re_label.grid(row=row, column=0, sticky="w", padx=20, pady=2)
    
    re_value = ttk.Label(statement_frame, text=format_currency(retained_earnings))
    re_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
    row += 1
    
    # Treasury Stock
    if treasury_stock > 0:
        ts_label = ttk.Label(statement_frame, text="Treasury Stock")
        ts_label.grid(row=row, column=0, sticky="w", padx=20, pady=2)
        
        ts_value = ttk.Label(statement_frame, text=f"({format_currency(treasury_stock)})")
        ts_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
        row += 1
    
    # Total Equity
    ttk.Separator(statement_frame, orient='horizontal').grid(row=row, column=0, columnspan=2, sticky="ew", pady=5)
    row += 1
    
    total_equity_label = ttk.Label(statement_frame, text="TOTAL EQUITY", font=("Arial", 10, "bold"))
    total_equity_label.grid(row=row, column=0, sticky="w", padx=5, pady=5)
    
    total_equity_value = ttk.Label(statement_frame, text=format_currency(total_equity), font=("Arial", 10, "bold"))
    total_equity_value.grid(row=row, column=1, sticky="e", padx=5, pady=5)
    row += 1
    
    # Total Liabilities and Equity
    ttk.Separator(statement_frame, orient='horizontal').grid(row=row, column=0, columnspan=2, sticky="ew", pady=5)
    row += 1
    
    total_le_label = ttk.Label(statement_frame, text="TOTAL LIABILITIES AND EQUITY", font=("Arial", 10, "bold"))
    total_le_label.grid(row=row, column=0, sticky="w", padx=5, pady=5)
    
    total_le_value = ttk.Label(statement_frame, text=format_currency(total_liabilities_equity), font=("Arial", 10, "bold"))
    total_le_value.grid(row=row, column=1, sticky="e", padx=5, pady=5)
    
    # Add a close button
    close_button = ttk.Button(window, text="Close", command=window.destroy)
    close_button.pack(pady=10)

def show_cash_flow_statement(company_name, reporting_period, net_income, depreciation_amortization,
                           accounts_receivable_change, inventory_change, accounts_payable_change,
                           accrued_expenses_change, deferred_revenue_change,
                           capital_expenditures, acquisitions, investments_sold,
                           debt_issuance, debt_repayment, dividends_paid, stock_issuance, stock_repurchase,
                           beginning_cash_balance):
    """
    Display a cash flow statement.
    
    Args:
        company_name: Name of the company
        reporting_period: Reporting period
        net_income: Net income
        depreciation_amortization: Depreciation and amortization
        accounts_receivable_change: Change in accounts receivable
        inventory_change: Change in inventory
        accounts_payable_change: Change in accounts payable
        accrued_expenses_change: Change in accrued expenses
        deferred_revenue_change: Change in deferred revenue
        capital_expenditures: Capital expenditures
        acquisitions: Acquisitions
        investments_sold: Investments sold
        debt_issuance: Debt issuance
        debt_repayment: Debt repayment
        dividends_paid: Dividends paid
        stock_issuance: Stock issuance
        stock_repurchase: Stock repurchase
        beginning_cash_balance: Beginning cash balance
    """
    # Calculate derived values
    operating_cash_flow = (net_income + depreciation_amortization - accounts_receivable_change - 
                          inventory_change + accounts_payable_change + accrued_expenses_change + 
                          deferred_revenue_change)
    
    investing_cash_flow = -capital_expenditures - acquisitions + investments_sold
    
    financing_cash_flow = debt_issuance - debt_repayment - dividends_paid + stock_issuance - stock_repurchase
    
    net_change_in_cash = operating_cash_flow + investing_cash_flow + financing_cash_flow
    
    ending_cash_balance = beginning_cash_balance + net_change_in_cash
    
    # Create a new window
    window = tk.Toplevel()
    window.title(f"{company_name} - Cash Flow Statement")
    window.geometry("600x700")
    
    # Create a frame for the title
    title_frame = tk.Frame(window, pady=10)
    title_frame.pack(fill='x')
    
    # Add a title
    title_label = tk.Label(title_frame, text=f"{company_name}", font=("Arial", 16, "bold"))
    title_label.pack()
    
    subtitle_label = tk.Label(title_frame, text="Cash Flow Statement", font=("Arial", 14))
    subtitle_label.pack()
    
    period_label = tk.Label(title_frame, text=reporting_period, font=("Arial", 12))
    period_label.pack()
    
    # Create a frame for the cash flow statement
    statement_frame = ttk.Frame(window, padding=20)
    statement_frame.pack(fill='both', expand=True)
    
    # Create the cash flow statement
    row = 0
    
    # Operating Activities Header
    operating_label = ttk.Label(statement_frame, text="OPERATING ACTIVITIES", font=("Arial", 12, "bold"))
    operating_label.grid(row=row, column=0, sticky="w", padx=5, pady=10)
    row += 1
    
    # Net Income
    ni_label = ttk.Label(statement_frame, text="Net Income")
    ni_label.grid(row=row, column=0, sticky="w", padx=20, pady=2)
    
    ni_value = ttk.Label(statement_frame, text=format_currency(net_income))
    ni_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
    row += 1
    
    # Adjustments to reconcile net income
    adj_label = ttk.Label(statement_frame, text="Adjustments to reconcile net income:", font=("Arial", 10, "italic"))
    adj_label.grid(row=row, column=0, sticky="w", padx=20, pady=5)
    row += 1
    
    # Depreciation and Amortization
    dep_label = ttk.Label(statement_frame, text="Depreciation and Amortization")
    dep_label.grid(row=row, column=0, sticky="w", padx=40, pady=2)
    
    dep_value = ttk.Label(statement_frame, text=format_currency(depreciation_amortization))
    dep_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
    row += 1
    
    # Changes in operating assets and liabilities
    changes_label = ttk.Label(statement_frame, text="Changes in operating assets and liabilities:", font=("Arial", 10, "italic"))
    changes_label.grid(row=row, column=0, sticky="w", padx=20, pady=5)
    row += 1
    
    # Accounts Receivable
    ar_label = ttk.Label(statement_frame, text="Accounts Receivable")
    ar_label.grid(row=row, column=0, sticky="w", padx=40, pady=2)
    
    ar_value = ttk.Label(statement_frame, text=format_currency(-accounts_receivable_change))
    ar_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
    row += 1
    
    # Inventory
    inv_label = ttk.Label(statement_frame, text="Inventory")
    inv_label.grid(row=row, column=0, sticky="w", padx=40, pady=2)
    
    inv_value = ttk.Label(statement_frame, text=format_currency(-inventory_change))
    inv_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
    row += 1
    
    # Accounts Payable
    ap_label = ttk.Label(statement_frame, text="Accounts Payable")
    ap_label.grid(row=row, column=0, sticky="w", padx=40, pady=2)
    
    ap_value = ttk.Label(statement_frame, text=format_currency(accounts_payable_change))
    ap_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
    row += 1
    
    # Accrued Expenses
    ae_label = ttk.Label(statement_frame, text="Accrued Expenses")
    ae_label.grid(row=row, column=0, sticky="w", padx=40, pady=2)
    
    ae_value = ttk.Label(statement_frame, text=format_currency(accrued_expenses_change))
    ae_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
    row += 1
    
    # Deferred Revenue
    dr_label = ttk.Label(statement_frame, text="Deferred Revenue")
    dr_label.grid(row=row, column=0, sticky="w", padx=40, pady=2)
    
    dr_value = ttk.Label(statement_frame, text=format_currency(deferred_revenue_change))
    dr_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
    row += 1
    
    # Net Cash from Operating Activities
    ttk.Separator(statement_frame, orient='horizontal').grid(row=row, column=0, columnspan=2, sticky="ew", pady=5)
    row += 1
    
    net_op_label = ttk.Label(statement_frame, text="Net Cash from Operating Activities", font=("Arial", 10, "bold"))
    net_op_label.grid(row=row, column=0, sticky="w", padx=5, pady=5)
    
    net_op_value = ttk.Label(statement_frame, text=format_currency(operating_cash_flow), font=("Arial", 10, "bold"))
    net_op_value.grid(row=row, column=1, sticky="e", padx=5, pady=5)
    row += 1
    
    # Investing Activities Header
    investing_label = ttk.Label(statement_frame, text="INVESTING ACTIVITIES", font=("Arial", 12, "bold"))
    investing_label.grid(row=row, column=0, sticky="w", padx=5, pady=10)
    row += 1
    
    # Capital Expenditures
    capex_label = ttk.Label(statement_frame, text="Capital Expenditures")
    capex_label.grid(row=row, column=0, sticky="w", padx=20, pady=2)
    
    capex_value = ttk.Label(statement_frame, text=f"({format_currency(capital_expenditures)})")
    capex_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
    row += 1
    
    # Acquisitions
    acq_label = ttk.Label(statement_frame, text="Acquisitions")
    acq_label.grid(row=row, column=0, sticky="w", padx=20, pady=2)
    
    acq_value = ttk.Label(statement_frame, text=f"({format_currency(acquisitions)})")
    acq_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
    row += 1
    
    # Investments Sold
    inv_sold_label = ttk.Label(statement_frame, text="Investments Sold")
    inv_sold_label.grid(row=row, column=0, sticky="w", padx=20, pady=2)
    
    inv_sold_value = ttk.Label(statement_frame, text=format_currency(investments_sold))
    inv_sold_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
    row += 1
    
    # Net Cash from Investing Activities
    ttk.Separator(statement_frame, orient='horizontal').grid(row=row, column=0, columnspan=2, sticky="ew", pady=5)
    row += 1
    
    net_inv_label = ttk.Label(statement_frame, text="Net Cash from Investing Activities", font=("Arial", 10, "bold"))
    net_inv_label.grid(row=row, column=0, sticky="w", padx=5, pady=5)
    
    net_inv_value = ttk.Label(statement_frame, text=format_currency(investing_cash_flow), font=("Arial", 10, "bold"))
    net_inv_value.grid(row=row, column=1, sticky="e", padx=5, pady=5)
    row += 1
    
    # Financing Activities Header
    financing_label = ttk.Label(statement_frame, text="FINANCING ACTIVITIES", font=("Arial", 12, "bold"))
    financing_label.grid(row=row, column=0, sticky="w", padx=5, pady=10)
    row += 1
    
    # Debt Issuance
    debt_iss_label = ttk.Label(statement_frame, text="Debt Issuance")
    debt_iss_label.grid(row=row, column=0, sticky="w", padx=20, pady=2)
    
    debt_iss_value = ttk.Label(statement_frame, text=format_currency(debt_issuance))
    debt_iss_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
    row += 1
    
    # Debt Repayment
    debt_rep_label = ttk.Label(statement_frame, text="Debt Repayment")
    debt_rep_label.grid(row=row, column=0, sticky="w", padx=20, pady=2)
    
    debt_rep_value = ttk.Label(statement_frame, text=f"({format_currency(debt_repayment)})")
    debt_rep_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
    row += 1
    
    # Dividends Paid
    div_label = ttk.Label(statement_frame, text="Dividends Paid")
    div_label.grid(row=row, column=0, sticky="w", padx=20, pady=2)
    
    div_value = ttk.Label(statement_frame, text=f"({format_currency(dividends_paid)})")
    div_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
    row += 1
    
    # Stock Issuance
    stock_iss_label = ttk.Label(statement_frame, text="Stock Issuance")
    stock_iss_label.grid(row=row, column=0, sticky="w", padx=20, pady=2)
    
    stock_iss_value = ttk.Label(statement_frame, text=format_currency(stock_issuance))
    stock_iss_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
    row += 1
    
    # Stock Repurchase
    stock_rep_label = ttk.Label(statement_frame, text="Stock Repurchase")
    stock_rep_label.grid(row=row, column=0, sticky="w", padx=20, pady=2)
    
    stock_rep_value = ttk.Label(statement_frame, text=f"({format_currency(stock_repurchase)})")
    stock_rep_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
    row += 1
    
    # Net Cash from Financing Activities
    ttk.Separator(statement_frame, orient='horizontal').grid(row=row, column=0, columnspan=2, sticky="ew", pady=5)
    row += 1
    
    net_fin_label = ttk.Label(statement_frame, text="Net Cash from Financing Activities", font=("Arial", 10, "bold"))
    net_fin_label.grid(row=row, column=0, sticky="w", padx=5, pady=5)
    
    net_fin_value = ttk.Label(statement_frame, text=format_currency(financing_cash_flow), font=("Arial", 10, "bold"))
    net_fin_value.grid(row=row, column=1, sticky="e", padx=5, pady=5)
    row += 1
    
    # Net Change in Cash
    ttk.Separator(statement_frame, orient='horizontal').grid(row=row, column=0, columnspan=2, sticky="ew", pady=5)
    row += 1
    
    net_change_label = ttk.Label(statement_frame, text="Net Change in Cash", font=("Arial", 10, "bold"))
    net_change_label.grid(row=row, column=0, sticky="w", padx=5, pady=5)
    
    net_change_value = ttk.Label(statement_frame, text=format_currency(net_change_in_cash), font=("Arial", 10, "bold"))
    net_change_value.grid(row=row, column=1, sticky="e", padx=5, pady=5)
    row += 1
    
    # Beginning Cash Balance
    beg_cash_label = ttk.Label(statement_frame, text="Beginning Cash Balance")
    beg_cash_label.grid(row=row, column=0, sticky="w", padx=5, pady=2)
    
    beg_cash_value = ttk.Label(statement_frame, text=format_currency(beginning_cash_balance))
    beg_cash_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
    row += 1
    
    # Ending Cash Balance
    ttk.Separator(statement_frame, orient='horizontal').grid(row=row, column=0, columnspan=2, sticky="ew", pady=5)
    row += 1
    
    end_cash_label = ttk.Label(statement_frame, text="Ending Cash Balance", font=("Arial", 10, "bold"))
    end_cash_label.grid(row=row, column=0, sticky="w", padx=5, pady=5)
    
    end_cash_value = ttk.Label(statement_frame, text=format_currency(ending_cash_balance), font=("Arial", 10, "bold"))
    end_cash_value.grid(row=row, column=1, sticky="e", padx=5, pady=5)
    
    # Add a close button
    close_button = ttk.Button(window, text="Close", command=window.destroy)
    close_button.pack(pady=10)

def show_investing_analysis(operating_cash_flow, capital_expenditures, total_assets, revenue):
    """
    Display an investing activities analysis.
    
    Args:
        operating_cash_flow: Operating cash flow
        capital_expenditures: Capital expenditures
        total_assets: Total assets
        revenue: Revenue
    """
    # Calculate metrics
    capex_to_ocf = capital_expenditures / operating_cash_flow if operating_cash_flow != 0 else 0
    capex_to_revenue = capital_expenditures / revenue if revenue != 0 else 0
    capex_to_assets = capital_expenditures / total_assets if total_assets != 0 else 0
    
    # Create a new window
    window = tk.Toplevel()
    window.title("Investing Activities Analysis")
    window.geometry("500x400")
    
    # Create a frame for the title
    title_frame = tk.Frame(window, pady=10)
    title_frame.pack(fill='x')
    
    # Add a title
    title_label = tk.Label(title_frame, text="Investing Activities Analysis", font=("Arial", 16, "bold"))
    title_label.pack()
    
    # Create a frame for the analysis
    analysis_frame = ttk.Frame(window, padding=20)
    analysis_frame.pack(fill='both', expand=True)
    
    # Create the analysis
    row = 0
    
    # Key Metrics Header
    metrics_label = ttk.Label(analysis_frame, text="Key Metrics", font=("Arial", 12, "bold"))
    metrics_label.grid(row=row, column=0, columnspan=2, sticky="w", padx=5, pady=10)
    row += 1
    
    # Operating Cash Flow
    ocf_label = ttk.Label(analysis_frame, text="Operating Cash Flow")
    ocf_label.grid(row=row, column=0, sticky="w", padx=5, pady=2)
    
    ocf_value = ttk.Label(analysis_frame, text=format_currency(operating_cash_flow))
    ocf_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
    row += 1
    
    # Capital Expenditures
    capex_label = ttk.Label(analysis_frame, text="Capital Expenditures")
    capex_label.grid(row=row, column=0, sticky="w", padx=5, pady=2)
    
    capex_value = ttk.Label(analysis_frame, text=format_currency(capital_expenditures))
    capex_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
    row += 1
    
    # Total Assets
    assets_label = ttk.Label(analysis_frame, text="Total Assets")
    assets_label.grid(row=row, column=0, sticky="w", padx=5, pady=2)
    
    assets_value = ttk.Label(analysis_frame, text=format_currency(total_assets))
    assets_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
    row += 1
    
    # Revenue
    revenue_label = ttk.Label(analysis_frame, text="Revenue")
    revenue_label.grid(row=row, column=0, sticky="w", padx=5, pady=2)
    
    revenue_value = ttk.Label(analysis_frame, text=format_currency(revenue))
    revenue_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
    row += 1
    
    # Separator
    ttk.Separator(analysis_frame, orient='horizontal').grid(row=row, column=0, columnspan=2, sticky="ew", pady=10)
    row += 1
    
    # Ratios Header
    ratios_label = ttk.Label(analysis_frame, text="Investment Ratios", font=("Arial", 12, "bold"))
    ratios_label.grid(row=row, column=0, columnspan=2, sticky="w", padx=5, pady=10)
    row += 1
    
    # CapEx to Operating Cash Flow
    capex_ocf_label = ttk.Label(analysis_frame, text="CapEx to Operating Cash Flow")
    capex_ocf_label.grid(row=row, column=0, sticky="w", padx=5, pady=2)
    
    capex_ocf_value = ttk.Label(analysis_frame, text=f"{capex_to_ocf:.2f}")
    capex_ocf_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
    row += 1
    
    # CapEx to Revenue
    capex_rev_label = ttk.Label(analysis_frame, text="CapEx to Revenue")
    capex_rev_label.grid(row=row, column=0, sticky="w", padx=5, pady=2)
    
    capex_rev_value = ttk.Label(analysis_frame, text=f"{capex_to_revenue:.2f}")
    capex_rev_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
    row += 1
    
    # CapEx to Total Assets
    capex_assets_label = ttk.Label(analysis_frame, text="CapEx to Total Assets")
    capex_assets_label.grid(row=row, column=0, sticky="w", padx=5, pady=2)
    
    capex_assets_value = ttk.Label(analysis_frame, text=f"{capex_to_assets:.2f}")
    capex_assets_value.grid(row=row, column=1, sticky="e", padx=5, pady=2)
    row += 1
    
    # Analysis
    ttk.Separator(analysis_frame, orient='horizontal').grid(row=row, column=0, columnspan=2, sticky="ew", pady=10)
    row += 1
    
    analysis_header = ttk.Label(analysis_frame, text="Analysis", font=("Arial", 12, "bold"))
    analysis_header.grid(row=row, column=0, columnspan=2, sticky="w", padx=5, pady=5)
    row += 1
    
    # Generate analysis text
    if capex_to_ocf > 1.0:
        analysis_text = "The company is investing more than it generates from operations, which may indicate growth plans but could strain liquidity."
    elif capex_to_ocf > 0.7:
        analysis_text = "The company is investing a significant portion of its operating cash flow, suggesting a focus on growth and expansion."
    elif capex_to_ocf > 0.3:
        analysis_text = "The company is maintaining a balanced approach to investment, with moderate capital expenditures relative to operating cash flow."
    else:
        analysis_text = "The company is investing conservatively, with capital expenditures representing a small portion of operating cash flow."
    
    analysis_label = ttk.Label(analysis_frame, text=analysis_text, wraplength=400)
    analysis_label.grid(row=row, column=0, columnspan=2, sticky="w", padx=5, pady=5)
    
    # Add a close button
    close_button = ttk.Button(window, text="Close", command=window.destroy)
    close_button.pack(pady=10)