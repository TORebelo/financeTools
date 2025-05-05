"""
Enhanced module for displaying financial statement comparisons.
"""

import tkinter as tk
from tkinter import ttk, scrolledtext
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def show_comparison_statement(parent, comparison, statement_type, base_year, forecast_year):
    """
    Show a comparison of financial statements.
    
    Args:
        parent: Parent widget
        comparison: FinancialComparison instance
        statement_type: Type of statement to compare ('income', 'balance', or 'cash_flow')
        base_year: Base year for comparison
        forecast_year: Forecast year for comparison
    """
    # Create a new window
    window = tk.Toplevel(parent)
    window.title(f"Financial Statement Comparison - {statement_type.replace('_', ' ').title()}")
    window.geometry("1200x800")
    
    # Create a frame for the title
    title_frame = tk.Frame(window, pady=10)
    title_frame.pack(fill='x')
    
    # Add a title
    title_label = tk.Label(
        title_frame, 
        text=f"{comparison.base_data.company_name} - {statement_type.replace('_', ' ').title()} Comparison", 
        font=("Arial", 16, "bold")
    )
    title_label.pack()
    
    subtitle_label = tk.Label(
        title_frame, 
        text=f"{base_year} vs. {forecast_year}", 
        font=("Arial", 12)
    )
    subtitle_label.pack()
    
    # Create a frame for the comparison
    comparison_frame = ttk.Frame(window, padding=10)
    comparison_frame.pack(fill='both', expand=True, padx=10, pady=10)
    
    # Create a notebook for the comparison views
    notebook = ttk.Notebook(comparison_frame)
    notebook.pack(fill='both', expand=True)
    
    # Create tabs for different views
    text_tab = ttk.Frame(notebook)
    chart_tab = ttk.Frame(notebook)
    notes_tab = ttk.Frame(notebook)
    
    notebook.add(text_tab, text="Text View")
    notebook.add(chart_tab, text="Chart View")
    notebook.add(notes_tab, text="Notes")
    
    # Create the text view
    text_frame = ttk.Frame(text_tab, padding=10)
    text_frame.pack(fill='both', expand=True)
    
    # Create a text area for the comparison
    comparison_text = scrolledtext.ScrolledText(text_frame, wrap=tk.WORD, width=120, height=30)
    comparison_text.pack(fill='both', expand=True)
    
    # Get the comparison data
    if statement_type == 'income':
        comparison_data = comparison.get_income_statement_comparison()
        text_content = _format_income_statement_comparison(comparison_data, base_year, forecast_year)
        chart_data = _get_income_statement_chart_data(comparison_data)
        notes = comparison.notes_generator.generate_income_statement_notes()
    elif statement_type == 'balance':
        comparison_data = comparison.get_balance_sheet_comparison()
        text_content = _format_balance_sheet_comparison(comparison_data, base_year, forecast_year)
        chart_data = _get_balance_sheet_chart_data(comparison_data)
        notes = comparison.notes_generator.generate_balance_sheet_notes()
    elif statement_type == 'cash_flow':
        comparison_data = comparison.get_cash_flow_comparison()
        text_content = _format_cash_flow_comparison(comparison_data, base_year, forecast_year)
        chart_data = _get_cash_flow_chart_data(comparison_data)
        notes = comparison.notes_generator.generate_cash_flow_notes()
    else:
        text_content = "Invalid statement type."
        chart_data = None
        notes = ""
    
    # Insert the text content
    comparison_text.insert(tk.END, text_content)
    comparison_text.config(state='disabled')
    
    # Create the chart view
    chart_frame = ttk.Frame(chart_tab, padding=10)
    chart_frame.pack(fill='both', expand=True)
    
    if chart_data:
        # Create a figure and axis
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Create the chart
        _create_comparison_chart(ax, chart_data, base_year, forecast_year)
        
        # Create a canvas to display the figure
        canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)
    
    # Create the notes view
    notes_frame = ttk.Frame(notes_tab, padding=10)
    notes_frame.pack(fill='both', expand=True)
    
    # Create a text area for the notes
    notes_text = scrolledtext.ScrolledText(notes_frame, wrap=tk.WORD, width=120, height=30)
    notes_text.pack(fill='both', expand=True)
    
    # Insert the notes
    notes_text.insert(tk.END, notes)
    notes_text.config(state='disabled')
    
    # Add a close button
    close_button = ttk.Button(window, text="Close", command=window.destroy)
    close_button.pack(pady=10)

def show_management_discussion(parent, comparison, base_year, forecast_year):
    """
    Show a management discussion and analysis of financial statement changes.
    
    Args:
        parent: Parent widget
        comparison: FinancialComparison instance
        base_year: Base year for comparison
        forecast_year: Forecast year for comparison
    """
    # Create a new window
    window = tk.Toplevel(parent)
    window.title("Management Discussion & Analysis")
    window.geometry("1200x800")
    
    # Create a frame for the title
    title_frame = tk.Frame(window, pady=10)
    title_frame.pack(fill='x')
    
    # Add a title
    title_label = tk.Label(
        title_frame, 
        text=f"{comparison.base_data.company_name} - Management Discussion & Analysis", 
        font=("Arial", 16, "bold")
    )
    title_label.pack()
    
    subtitle_label = tk.Label(
        title_frame, 
        text=f"{base_year} vs. {forecast_year}", 
        font=("Arial", 12)
    )
    subtitle_label.pack()
    
    # Create a frame for the MD&A
    mda_frame = ttk.Frame(window, padding=10)
    mda_frame.pack(fill='both', expand=True, padx=10, pady=10)
    
    # Create a notebook for the MD&A views
    notebook = ttk.Notebook(mda_frame)
    notebook.pack(fill='both', expand=True)
    
    # Create tabs for different views
    text_tab = ttk.Frame(notebook)
    chart_tab = ttk.Frame(notebook)
    
    notebook.add(text_tab, text="Text View")
    notebook.add(chart_tab, text="Chart View")
    
    # Create the text view
    text_frame = ttk.Frame(text_tab, padding=10)
    text_frame.pack(fill='both', expand=True)
    
    # Create a text area for the MD&A
    mda_text = scrolledtext.ScrolledText(text_frame, wrap=tk.WORD, width=120, height=30)
    mda_text.pack(fill='both', expand=True)
    
    # Generate the MD&A
    mda_content = comparison.notes_generator.generate_comprehensive_notes()
    
    # Insert the MD&A content
    mda_text.insert(tk.END, mda_content)
    mda_text.config(state='disabled')
    
    # Create the chart view
    chart_frame = ttk.Frame(chart_tab, padding=10)
    chart_frame.pack(fill='both', expand=True)
    
    # Create a figure and axis for the chart
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    
    # Get the comparison data
    income_data = comparison.get_income_statement_comparison()
    balance_data = comparison.get_balance_sheet_comparison()
    cash_flow_data = comparison.get_cash_flow_comparison()
    
    # Create the charts
    _create_comparison_chart(axes[0, 0], _get_income_statement_chart_data(income_data), base_year, forecast_year)
    axes[0, 0].set_title("Income Statement Comparison")
    
    _create_comparison_chart(axes[0, 1], _get_balance_sheet_chart_data(balance_data), base_year, forecast_year)
    axes[0, 1].set_title("Balance Sheet Comparison")
    
    _create_comparison_chart(axes[1, 0], _get_cash_flow_chart_data(cash_flow_data), base_year, forecast_year)
    axes[1, 0].set_title("Cash Flow Comparison")
    
    _create_ratio_chart(axes[1, 1], comparison, base_year, forecast_year)
    axes[1, 1].set_title("Key Ratios Comparison")
    
    # Adjust the layout
    plt.tight_layout()
    
    # Create a canvas to display the figure
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)
    
    # Add a close button
    close_button = ttk.Button(window, text="Close", command=window.destroy)
    close_button.pack(pady=10)

def _format_income_statement_comparison(data, base_year, forecast_year):
    """
    Format the income statement comparison as text.
    
    Args:
        data: Income statement comparison data
        base_year: Base year for comparison
        forecast_year: Forecast year for comparison
    
    Returns:
        Formatted text
    """
    # Calculate derived values
    gross_profit_base = data['revenue']['base'] - data['cogs']['base']
    gross_profit_forecast = data['revenue']['forecast'] - data['cogs']['forecast']
    
    operating_income_base = gross_profit_base - data['operating_expenses']['base']
    operating_income_forecast = gross_profit_forecast - data['operating_expenses']['forecast']
    
    income_before_tax_base = operating_income_base - data['interest_expense']['base']
    income_before_tax_forecast = operating_income_forecast - data['interest_expense']['forecast']
    
    # Format the comparison
    text = f"""
{'-' * 80}
INCOME STATEMENT COMPARISON
{'-' * 80}
                                    {base_year}         {forecast_year}        Change         % Change
{'-' * 80}

Revenue                         ${data['revenue']['base']:,.0f}    ${data['revenue']['forecast']:,.0f}    ${data['revenue']['change']:,.0f}    {data['revenue']['percentage']:.1%}

Cost of Goods Sold              ${data['cogs']['base']:,.0f}    ${data['cogs']['forecast']:,.0f}    ${data['cogs']['change']:,.0f}    {data['cogs']['percentage']:.1%}
{'-' * 80}
Gross Profit                    ${gross_profit_base:,.0f}    ${gross_profit_forecast:,.0f}    ${gross_profit_forecast - gross_profit_base:,.0f}    {(gross_profit_forecast - gross_profit_base) / gross_profit_base if gross_profit_base != 0 else 0:.1%}

Operating Expenses              ${data['operating_expenses']['base']:,.0f}    ${data['operating_expenses']['forecast']:,.0f}    ${data['operating_expenses']['change']:,.0f}    {data['operating_expenses']['percentage']:.1%}
{'-' * 80}
Operating Income                ${operating_income_base:,.0f}    ${operating_income_forecast:,.0f}    ${operating_income_forecast - operating_income_base:,.0f}    {(operating_income_forecast - operating_income_base) / operating_income_base if operating_income_base != 0 else 0:.1%}

Interest Expense                ${data['interest_expense']['base']:,.0f}    ${data['interest_expense']['forecast']:,.0f}    ${data['interest_expense']['change']:,.0f}    {data['interest_expense']['percentage']:.1%}
{'-' * 80}
Income Before Tax               ${income_before_tax_base:,.0f}    ${income_before_tax_forecast:,.0f}    ${income_before_tax_forecast - income_before_tax_base:,.0f}    {(income_before_tax_forecast - income_before_tax_base) / income_before_tax_base if income_before_tax_base != 0 else 0:.1%}

Income Tax                      ${data['income_tax']['base']:,.0f}    ${data['income_tax']['forecast']:,.0f}    ${data['income_tax']['change']:,.0f}    {data['income_tax']['percentage']:.1%}
{'-' * 80}
Net Income                      ${data['net_income']['base']:,.0f}    ${data['net_income']['forecast']:,.0f}    ${data['net_income']['change']:,.0f}    {data['net_income']['percentage']:.1%}

{'-' * 80}
KEY METRICS
{'-' * 80}
Gross Margin                    {gross_profit_base / data['revenue']['base'] if data['revenue']['base'] != 0 else 0:.1%}    {gross_profit_forecast / data['revenue']['forecast'] if data['revenue']['forecast'] != 0 else 0:.1%}    {(gross_profit_forecast / data['revenue']['forecast'] if data['revenue']['forecast'] != 0 else 0) - (gross_profit_base / data['revenue']['base'] if data['revenue']['base'] != 0 else 0):.1%}

Operating Margin                {operating_income_base / data['revenue']['base'] if data['revenue']['base'] != 0 else 0:.1%}    {operating_income_forecast / data['revenue']['forecast'] if data['revenue']['forecast'] != 0 else 0:.1%}    {(operating_income_forecast / data['revenue']['forecast'] if data['revenue']['forecast'] != 0 else 0) - (operating_income_base / data['revenue']['base'] if data['revenue']['base'] != 0 else 0):.1%}

Net Margin                      {data['net_income']['base'] / data['revenue']['base'] if data['revenue']['base'] != 0 else 0:.1%}    {data['net_income']['forecast'] / data['revenue']['forecast'] if data['revenue']['forecast'] != 0 else 0:.1%}    {(data['net_income']['forecast'] / data['revenue']['forecast'] if data['revenue']['forecast'] != 0 else 0) - (data['net_income']['base'] / data['revenue']['base'] if data['revenue']['base'] != 0 else 0):.1%}
{'-' * 80}
"""
    
    return text

def _format_balance_sheet_comparison(data, base_year, forecast_year):
    """
    Format the balance sheet comparison as text.
    
    Args:
        data: Balance sheet comparison data
        base_year: Base year for comparison
        forecast_year: Forecast year for comparison
    
    Returns:
        Formatted text
    """
    # Calculate derived values
    current_assets_base = data['cash']['base'] + data['accounts_receivable']['base'] + data['inventory']['base'] + data['prepaid_expenses']['base']
    current_assets_forecast = data['cash']['forecast'] + data['accounts_receivable']['forecast'] + data['inventory']['forecast'] + data['prepaid_expenses']['forecast']
    
    non_current_assets_base = data['property_plant_equipment']['base'] - data['accumulated_depreciation']['base'] + data['intangible_assets']['base']
    non_current_assets_forecast = data['property_plant_equipment']['forecast'] - data['accumulated_depreciation']['forecast'] + data['intangible_assets']['forecast']
    
    total_assets_base = current_assets_base + non_current_assets_base
    total_assets_forecast = current_assets_forecast + non_current_assets_forecast
    
    current_liabilities_base = data['accounts_payable']['base'] + data['accrued_expenses']['base'] + data['short_term_debt']['base'] + data['deferred_revenue']['base']
    current_liabilities_forecast = data['accounts_payable']['forecast'] + data['accrued_expenses']['forecast'] + data['short_term_debt']['forecast'] + data['deferred_revenue']['forecast']
    
    non_current_liabilities_base = data['long_term_debt']['base'] + data['deferred_tax_liabilities']['base']
    non_current_liabilities_forecast = data['long_term_debt']['forecast'] + data['deferred_tax_liabilities']['forecast']
    
    total_equity_base = data['common_stock']['base'] + data['retained_earnings']['base'] - data['treasury_stock']['base']
    total_equity_forecast = data['common_stock']['forecast'] + data['retained_earnings']['forecast'] - data['treasury_stock']['forecast']
    
    # Format the comparison
    text = f"""
{'-' * 80}
BALANCE SHEET COMPARISON
{'-' * 80}
                                    {base_year}         {forecast_year}        Change         % Change
{'-' * 80}
ASSETS
{'-' * 80}
Current Assets:
  Cash                          ${data['cash']['base']:,.0f}    ${data['cash']['forecast']:,.0f}    ${data['cash']['change']:,.0f}    {data['cash']['percentage']:.1%}
  Accounts Receivable           ${data['accounts_receivable']['base']:,.0f}    ${data['accounts_receivable']['forecast']:,.0f}    ${data['accounts_receivable']['change']:,.0f}    {data['accounts_receivable']['percentage']:.1%}
  Inventory                     ${data['inventory']['base']:,.0f}    ${data['inventory']['forecast']:,.0f}    ${data['inventory']['change']:,.0f}    {data['inventory']['percentage']:.1%}
  Prepaid Expenses              ${data['prepaid_expenses']['base']:,.0f}    ${data['prepaid_expenses']['forecast']:,.0f}    ${data['prepaid_expenses']['change']:,.0f}    {data['prepaid_expenses']['percentage']:.1%}
{'-' * 80}
  Total Current Assets          ${current_assets_base:,.0f}    ${current_assets_forecast:,.0f}    ${current_assets_forecast - current_assets_base:,.0f}    {(current_assets_forecast - current_assets_base) / current_assets_base if current_assets_base != 0 else 0:.1%}

Non-Current Assets:
  PP&E                          ${data['property_plant_equipment']['base']:,.0f}    ${data['property_plant_equipment']['forecast']:,.0f}    ${data['property_plant_equipment']['change']:,.0f}    {data['property_plant_equipment']['percentage']:.1%}
  Accumulated Depreciation      ${data['accumulated_depreciation']['base']:,.0f}    ${data['accumulated_depreciation']['forecast']:,.0f}    ${data['accumulated_depreciation']['change']:,.0f}    {data['accumulated_depreciation']['percentage']:.1%}
  Intangible Assets             ${data['intangible_assets']['base']:,.0f}    ${data['intangible_assets']['forecast']:,.0f}    ${data['intangible_assets']['change']:,.0f}    {data['intangible_assets']['percentage']:.1%}
{'-' * 80}
  Total Non-Current Assets      ${non_current_assets_base:,.0f}    ${non_current_assets_forecast:,.0f}    ${non_current_assets_forecast - non_current_assets_base:,.0f}    {(non_current_assets_forecast - non_current_assets_base) / non_current_assets_base if non_current_assets_base != 0 else 0:.1%}
{'-' * 80}
TOTAL ASSETS                    ${total_assets_base:,.0f}    ${total_assets_forecast:,.0f}    ${total_assets_forecast - total_assets_base:,.0f}    {(total_assets_forecast - total_assets_base) / total_assets_base if total_assets_base != 0 else 0:.1%}

{'-' * 80}
LIABILITIES AND EQUITY
{'-' * 80}
Current Liabilities:
  Accounts Payable              ${data['accounts_payable']['base']:,.0f}    ${data['accounts_payable']['forecast']:,.0f}    ${data['accounts_payable']['change']:,.0f}    {data['accounts_payable']['percentage']:.1%}
  Accrued Expenses              ${data['accrued_expenses']['base']:,.0f}    ${data['accrued_expenses']['forecast']:,.0f}    ${data['accrued_expenses']['change']:,.0f}    {data['accrued_expenses']['percentage']:.1%}
  Short-term Debt               ${data['short_term_debt']['base']:,.0f}    ${data['short_term_debt']['forecast']:,.0f}    ${data['short_term_debt']['change']:,.0f}    {data['short_term_debt']['percentage']:.1%}
  Deferred Revenue              ${data['deferred_revenue']['base']:,.0f}    ${data['deferred_revenue']['forecast']:,.0f}    ${data['deferred_revenue']['change']:,.0f}    {data['deferred_revenue']['percentage']:.1%}
{'-' * 80}
  Total Current Liabilities     ${current_liabilities_base:,.0f}    ${current_liabilities_forecast:,.0f}    ${current_liabilities_forecast - current_liabilities_base:,.0f}    {(current_liabilities_forecast - current_liabilities_base) / current_liabilities_base if current_liabilities_base != 0 else 0:.1%}

Non-Current Liabilities:
  Long-term Debt                ${data['long_term_debt']['base']:,.0f}    ${data['long_term_debt']['forecast']:,.0f}    ${data['long_term_debt']['change']:,.0f}    {data['long_term_debt']['percentage']:.1%}
  Deferred Tax Liabilities      ${data['deferred_tax_liabilities']['base']:,.0f}    ${data['deferred_tax_liabilities']['forecast']:,.0f}    ${data['deferred_tax_liabilities']['change']:,.0f}    {data['deferred_tax_liabilities']['percentage']:.1%}
{'-' * 80}
  Total Non-Current Liabilities ${non_current_liabilities_base:,.0f}    ${non_current_liabilities_forecast:,.0f}    ${non_current_liabilities_forecast - non_current_liabilities_base:,.0f}    {(non_current_liabilities_forecast - non_current_liabilities_base) / non_current_liabilities_base if non_current_liabilities_base != 0 else 0:.1%}
{'-' * 80}
TOTAL LIABILITIES               ${total_liabilities_base:,.0f}    ${total_liabilities_forecast:,.0f}    ${total_liabilities_forecast - total_liabilities_base:,.0f}    {(total_liabilities_forecast - total_liabilities_base) / total_liabilities_base if total_liabilities_base != 0 else 0:.1%}

Equity:
  Common Stock                  ${data['common_stock']['base']:,.0f}    ${data['common_stock']['forecast']:,.0f}    ${data['common_stock']['change']:,.0f}    {data['common_stock']['percentage']:.1%}
  Retained Earnings             ${data['retained_earnings']['base']:,.0f}    ${data['retained_earnings']['forecast']:,.0f}    ${data['retained_earnings']['change']:,.0f}    {data['retained_earnings']['percentage']:.1%}
  Treasury Stock                ${data['treasury_stock']['base']:,.0f}    ${data['treasury_stock']['forecast']:,.0f}    ${data['treasury_stock']['change']:,.0f}    {data['treasury_stock']['percentage']:.1%}
{'-' * 80}
TOTAL EQUITY                    ${total_equity_base:,.0f}    ${total_equity_forecast:,.0f}    ${total_equity_forecast - total_equity_base:,.0f}    {(total_equity_forecast - total_equity_base) / total_equity_base if total_equity_base != 0 else 0:.1%}
{'-' * 80}
TOTAL LIABILITIES AND EQUITY    ${total_liabilities_base + total_equity_base:,.0f}    ${total_liabilities_forecast + total_equity_forecast:,.0f}    ${(total_liabilities_forecast + total_equity_forecast) - (total_liabilities_base + total_equity_base):,.0f}    {((total_liabilities_forecast + total_equity_forecast) - (total_liabilities_base + total_equity_base)) / (total_liabilities_base + total_equity_base) if (total_liabilities_base + total_equity_base) != 0 else 0:.1%}
{'-' * 80}

KEY METRICS
{'-' * 80}
Current Ratio                   {current_assets_base / current_liabilities_base if current_liabilities_base != 0 else 0:.2f}    {current_assets_forecast / current_liabilities_forecast if current_liabilities_forecast != 0 else 0:.2f}    {(current_assets_forecast / current_liabilities_forecast if current_liabilities_forecast != 0 else 0) - (current_assets_base / current_liabilities_base if current_liabilities_base != 0 else 0):.2f}

Debt-to-Equity Ratio            {(data['short_term_debt']['base'] + data['long_term_debt']['base']) / total_equity_base if total_equity_base != 0 else 0:.2f}    {(data['short_term_debt']['forecast'] + data['long_term_debt']['forecast']) / total_equity_forecast if total_equity_forecast != 0 else 0:.2f}    {((data['short_term_debt']['forecast'] + data['long_term_debt']['forecast']) / total_equity_forecast if total_equity_forecast != 0 else 0) - ((data['short_term_debt']['base'] + data['long_term_debt']['base']) / total_equity_base if total_equity_base != 0 else 0):.2f}

Debt-to-Assets Ratio            {(data['short_term_debt']['base'] + data['long_term_debt']['base']) / total_assets_base if total_assets_base != 0 else 0:.2f}    {(data['short_term_debt']['forecast'] + data['long_term_debt']['forecast']) / total_assets_forecast if total_assets_forecast != 0 else 0:.2f}    {((data['short_term_debt']['forecast'] + data['long_term_debt']['forecast']) / total_assets_forecast if total_assets_forecast != 0 else 0) - ((data['short_term_debt']['base'] + data['long_term_debt']['base']) / total_assets_base if total_assets_base != 0 else 0):.2f}
{'-' * 80}
"""
    
    return text

def _format_cash_flow_comparison(data, base_year, forecast_year):
    """
    Format the cash flow comparison as text.
    
    Args:
        data: Cash flow comparison data
        base_year: Base year for comparison
        forecast_year: Forecast year for comparison
    
    Returns:
        Formatted text
    """
    # Format the comparison
    text = f"""
{'-' * 80}
CASH FLOW STATEMENT COMPARISON
{'-' * 80}
                                    {base_year}         {forecast_year}        Change         % Change
{'-' * 80}
Operating Activities:
  Net Income                    ${data['net_income']['base']:,.0f}    ${data['net_income']['forecast']:,.0f}    ${data['net_income']['change']:,.0f}    {data['net_income']['percentage']:.1%}
  Depreciation & Amortization   ${data['depreciation_amortization']['base']:,.0f}    ${data['depreciation_amortization']['forecast']:,.0f}    ${data['depreciation_amortization']['change']:,.0f}    {data['depreciation_amortization']['percentage']:.1%}
  Working Capital Changes       ${data['working_capital_changes']['base']:,.0f}    ${data['working_capital_changes']['forecast']:,.0f}    ${data['working_capital_changes']['change']:,.0f}    {data['working_capital_changes']['percentage']:.1%}
{'-' * 80}
  Net Cash from Operations      ${data['operating_cash_flow']['base']:,.0f}    ${data['operating_cash_flow']['forecast']:,.0f}    ${data['operating_cash_flow']['change']:,.0f}    {data['operating_cash_flow']['percentage']:.1%}

Investing Activities:
  Capital Expenditures          ${data['capital_expenditures']['base']:,.0f}    ${data['capital_expenditures']['forecast']:,.0f}    ${data['capital_expenditures']['change']:,.0f}    {data['capital_expenditures']['percentage']:.1%}
  Other Investing Activities    ${data['other_investing']['base']:,.0f}    ${data['other_investing']['forecast']:,.0f}    ${data['other_investing']['change']:,.0f}    {data['other_investing']['percentage']:.1%}
{'-' * 80}
  Net Cash from Investing       ${data['investing_cash_flow']['base']:,.0f}    ${data['investing_cash_flow']['forecast']:,.0f}    ${data['investing_cash_flow']['change']:,.0f}    {data['investing_cash_flow']['percentage']:.1%}

Financing Activities:
  Debt Issuance (Repayment)     ${data['debt_activities']['base']:,.0f}    ${data['debt_activities']['forecast']:,.0f}    ${data['debt_activities']['change']:,.0f}    {data['debt_activities']['percentage']:.1%}
  Dividends Paid                ${data['dividends_paid']['base']:,.0f}    ${data['dividends_paid']['forecast']:,.0f}    ${data['dividends_paid']['change']:,.0f}    {data['dividends_paid']['percentage']:.1%}
  Stock Activities              ${data['stock_activities']['base']:,.0f}    ${data['stock_activities']['forecast']:,.0f}    ${data['stock_activities']['change']:,.0f}    {data['stock_activities']['percentage']:.1%}
{'-' * 80}
  Net Cash from Financing       ${data['financing_cash_flow']['base']:,.0f}    ${data['financing_cash_flow']['forecast']:,.0f}    ${data['financing_cash_flow']['change']:,.0f}    {data['financing_cash_flow']['percentage']:.1%}
{'-' * 80}
Net Change in Cash              ${data['net_change_in_cash']['base']:,.0f}    ${data['net_change_in_cash']['forecast']:,.0f}    ${data['net_change_in_cash']['change']:,.0f}    {data['net_change_in_cash']['percentage']:.1%}

Beginning Cash Balance          ${data['beginning_cash_balance']['base']:,.0f}    ${data['beginning_cash_balance']['forecast']:,.0f}    ${data['beginning_cash_balance']['change']:,.0f}    {data['beginning_cash_balance']['percentage']:.1%}
{'-' * 80}
Ending Cash Balance             ${data['ending_cash_balance']['base']:,.0f}    ${data['ending_cash_balance']['forecast']:,.0f}    ${data['ending_cash_balance']['change']:,.0f}    {data['ending_cash_balance']['percentage']:.1%}
{'-' * 80}

KEY METRICS
{'-' * 80}
Free Cash Flow                  ${data['operating_cash_flow']['base'] - abs(data['capital_expenditures']['base']):,.0f}    ${data['operating_cash_flow']['forecast'] - abs(data['capital_expenditures']['forecast']):,.0f}    ${(data['operating_cash_flow']['forecast'] - abs(data['capital_expenditures']['forecast'])) - (data['operating_cash_flow']['base'] - abs(data['capital_expenditures']['base'])):,.0f}    {((data['operating_cash_flow']['forecast'] - abs(data['capital_expenditures']['forecast'])) - (data['operating_cash_flow']['base'] - abs(data['capital_expenditures']['base']))) / (data['operating_cash_flow']['base'] - abs(data['capital_expenditures']['base'])) if (data['operating_cash_flow']['base'] - abs(data['capital_expenditures']['base'])) != 0 else 0:.1%}

Cash Flow to Net Income         {data['operating_cash_flow']['base'] / data['net_income']['base'] if data['net_income']['base'] != 0 else 0:.2f}    {data['operating_cash_flow']['forecast'] / data['net_income']['forecast'] if data['net_income']['forecast'] != 0 else 0:.2f}    {(data['operating_cash_flow']['forecast'] / data['net_income']['forecast'] if data['net_income']['forecast'] != 0 else 0) - (data['operating_cash_flow']['base'] / data['net_income']['base'] if data['net_income']['base'] != 0 else 0):.2f}
{'-' * 80}
"""
    
    return text

def _get_income_statement_chart_data(data):
    """
    Get the income statement chart data.
    
    Args:
        data: Income statement comparison data
    
    Returns:
        Chart data
    """
    # Calculate derived values
    gross_profit_base = data['revenue']['base'] - data['cogs']['base']
    gross_profit_forecast = data['revenue']['forecast'] - data['cogs']['forecast']
    
    operating_income_base = gross_profit_base - data['operating_expenses']['base']
    operating_income_forecast = gross_profit_forecast - data['operating_expenses']['forecast']
    
    # Create the chart data
    chart_data = {
        'labels': ['Revenue', 'Gross Profit', 'Operating Income', 'Net Income'],
        'base_values': [data['revenue']['base'], gross_profit_base, operating_income_base, data['net_income']['base']],
        'forecast_values': [data['revenue']['forecast'], gross_profit_forecast, operating_income_forecast, data['net_income']['forecast']]
    }
    
    return chart_data

def _get_balance_sheet_chart_data(data):
    """
    Get the balance sheet chart data.
    
    Args:
        data: Balance sheet comparison data
    
    Returns:
        Chart data
    """
    # Calculate derived values
    current_assets_base = data['cash']['base'] + data['accounts_receivable']['base'] + data['inventory']['base'] + data['prepaid_expenses']['base']
    current_assets_forecast = data['cash']['forecast'] + data['accounts_receivable']['forecast'] + data['inventory']['forecast'] + data['prepaid_expenses']['forecast']
    
    non_current_assets_base = data['property_plant_equipment']['base'] - data['accumulated_depreciation']['base'] + data['intangible_assets']['base']
    non_current_assets_forecast = data['property_plant_equipment']['forecast'] - data['accumulated_depreciation']['forecast'] + data['intangible_assets']['forecast']
    
    current_liabilities_base = data['accounts_payable']['base'] + data['accrued_expenses']['base'] + data['short_term_debt']['base'] + data['deferred_revenue']['base']
    current_liabilities_forecast = data['accounts_payable']['forecast'] + data['accrued_expenses']['forecast'] + data['short_term_debt']['forecast'] + data['deferred_revenue']['forecast']
    
    non_current_liabilities_base = data['long_term_debt']['base'] + data['deferred_tax_liabilities']['base']
    non_current_liabilities_forecast = data['long_term_debt']['forecast'] + data['deferred_tax_liabilities']['forecast']
    
    total_equity_base = data['common_stock']['base'] + data['retained_earnings']['base'] - data['treasury_stock']['base']
    total_equity_forecast = data['common_stock']['forecast'] + data['retained_earnings']['forecast'] - data['treasury_stock']['forecast']
    
    # Create the chart data
    chart_data = {
        'labels': ['Current Assets', 'Non-Current Assets', 'Current Liabilities', 'Non-Current Liabilities', 'Equity'],
        'base_values': [current_assets_base, non_current_assets_base, current_liabilities_base, non_current_liabilities_base, total_equity_base],
        'forecast_values': [current_assets_forecast, non_current_assets_forecast, current_liabilities_forecast, non_current_liabilities_forecast, total_equity_forecast]
    }
    
    return chart_data

def _get_cash_flow_chart_data(data):
    """
    Get the cash flow chart data.
    
    Args:
        data: Cash flow comparison data
    
    Returns:
        Chart data
    """
    # Create the chart data
    chart_data = {
        'labels': ['Operating CF', 'Investing CF', 'Financing CF', 'Net Change in Cash'],
        'base_values': [data['operating_cash_flow']['base'], data['investing_cash_flow']['base'], data['financing_cash_flow']['base'], data['net_change_in_cash']['base']],
        'forecast_values': [data['operating_cash_flow']['forecast'], data['investing_cash_flow']['forecast'], data['financing_cash_flow']['forecast'], data['net_change_in_cash']['forecast']]
    }
    
    return chart_data

def _create_comparison_chart(ax, data, base_year, forecast_year):
    """
    Create a comparison chart.
    
    Args:
        ax: Matplotlib axis
        data: Chart data
        base_year: Base year for comparison
        forecast_year: Forecast year for comparison
    """
    # Set the width of the bars
    bar_width = 0.35
    
    # Set the positions of the bars on the x-axis
    r1 = range(len(data['labels']))
    r2 = [x + bar_width for x in r1]
    
    # Create the bars
    ax.bar(r1, data['base_values'], width=bar_width, label=base_year, color='#4CAF50')
    ax.bar(r2, data['forecast_values'], width=bar_width, label=forecast_year, color='#2196F3')
    
    # Add labels and title
    ax.set_xticks([r + bar_width/2 for r in range(len(data['labels']))])
    ax.set_xticklabels(data['labels'])
    ax.set_ylabel('Amount ($)')
    ax.legend()
    
    # Add data labels
    for i, v in enumerate(data['base_values']):
        ax.text(i - 0.1, v + 5000, f'${v:,.0f}', ha='center', va='bottom', rotation=90, fontsize=8)
    
    for i, v in enumerate(data['forecast_values']):
        ax.text(i + bar_width - 0.1, v + 5000, f'${v:,.0f}', ha='center', va='bottom', rotation=90, fontsize=8)
    
    # Add a grid
    ax.grid(axis='y', linestyle='--', alpha=0.7)

def _create_ratio_chart(ax, comparison, base_year, forecast_year):
    """
    Create a ratio chart.
    
    Args:
        ax: Matplotlib axis
        comparison: FinancialComparison instance
        base_year: Base year for comparison
        forecast_year: Forecast year for comparison
    """
    # Calculate ratios
    from analysis.ratios import FinancialRatios
    
    base_ratios = FinancialRatios(comparison.base_data).get_all_ratios()
    forecast_ratios = FinancialRatios(comparison.forecast_data).get_all_ratios()
    
    # Create the chart data
    labels = ['P/E Ratio', 'EV/EBITDA', 'Debt/Equity', 'Current Ratio', 'Net Margin']
    
    base_values = [
        base_ratios['valuation']['pe_ratio'] if base_ratios['valuation']['pe_ratio'] != float('inf') else 0,
        base_ratios['valuation']['ev_to_ebitda'] if base_ratios['valuation']['ev_to_ebitda'] != float('inf') else 0,
        base_ratios['solvency']['debt_to_equity'] if base_ratios['solvency']['debt_to_equity'] != float('inf') else 0,
        base_ratios['liquidity']['current_ratio'] if base_ratios['liquidity']['current_ratio'] != float('inf') else 0,
        base_ratios['profitability']['net_margin']
    ]
    
    forecast_values = [
        forecast_ratios['valuation']['pe_ratio'] if forecast_ratios['valuation']['pe_ratio'] != float('inf') else 0,
        forecast_ratios['valuation']['ev_to_ebitda'] if forecast_ratios['valuation']['ev_to_ebitda'] != float('inf') else 0,
        forecast_ratios['solvency']['debt_to_equity'] if forecast_ratios['solvency']['debt_to_equity'] != float('inf') else 0,
        forecast_ratios['liquidity']['current_ratio'] if forecast_ratios['liquidity']['current_ratio'] != float('inf') else 0,
        forecast_ratios['profitability']['net_margin']
    ]
    
    # Set the width of the bars
    bar_width = 0.35
    
    # Set the positions of the bars on the x-axis
    r1 = range(len(labels))
    r2 = [x + bar_width for x in r1]
    
    # Create the bars
    ax.bar(r1, base_values, width=bar_width, label=base_year, color='#4CAF50')
    ax.bar(r2, forecast_values, width=bar_width, label=forecast_year, color='#2196F3')
    
    # Add labels and title
    ax.set_xticks([r + bar_width/2 for r in range(len(labels))])
    ax.set_xticklabels(labels)
    ax.set_ylabel('Ratio Value')
    ax.legend()
    
    # Add data labels
    for i, v in enumerate(base_values):
        ax.text(i - 0.1, v + 0.5, f'{v:.2f}', ha='center', va='bottom', rotation=90, fontsize=8)
    
    for i, v in enumerate(forecast_values):
        ax.text(i + bar_width - 0.1, v + 0.5, f'{v:.2f}', ha='center', va='bottom', rotation=90, fontsize=8)

