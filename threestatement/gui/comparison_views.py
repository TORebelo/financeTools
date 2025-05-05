"""
Module for displaying financial statement comparisons.
"""

import tkinter as tk
from tkinter import ttk, scrolledtext

def format_currency(value):
    """Format a value as currency."""
    return f"${value:,.0f}"

def format_percentage(value):
    """Format a value as percentage."""
    return f"{value:.1%}"

def format_change(value, percentage):
    """Format a change value with direction indicator."""
    if value > 0:
        return f"▲ {format_currency(value)} ({format_percentage(percentage)})"
    elif value < 0:
        return f"▼ {format_currency(abs(value))} ({format_percentage(abs(percentage))})"
    else:
        return f"— {format_currency(0)} (0.0%)"

def show_comparison_statement(parent, comparison, statement_type, base_year, forecast_year):
    """
    Display a comparison between base and forecast financial statements.
    
    Args:
        parent: Parent widget
        comparison: FinancialComparison instance
        statement_type: Type of statement ('income', 'balance', or 'cash_flow')
        base_year: Base year (e.g., "2023")
        forecast_year: Forecast year (e.g., "2024")
    """
    # Get the appropriate comparison data
    if statement_type == 'income':
        title = "Income Statement Comparison"
        data = comparison.get_income_statement_comparison()
        sections = [
            {
                'title': 'Revenue and Profitability',
                'items': [
                    ('Revenue', 'revenue'),
                    ('Cost of Goods Sold', 'cogs'),
                    ('Gross Profit', 'gross_profit'),
                    ('Operating Expenses', 'operating_expenses'),
                    ('Operating Income', 'operating_income'),
                    ('Interest Expense', 'interest_expense'),
                    ('Income Before Tax', 'income_before_tax'),
                    ('Income Tax', 'income_tax'),
                    ('Net Income', 'net_income')
                ]
            }
        ]
    elif statement_type == 'balance':
        title = "Balance Sheet Comparison"
        data = comparison.get_balance_sheet_comparison()
        sections = [
            {
                'title': 'Assets',
                'items': [
                    ('Cash and Cash Equivalents', 'cash'),
                    ('Accounts Receivable', 'accounts_receivable'),
                    ('Inventory', 'inventory'),
                    ('Prepaid Expenses', 'prepaid_expenses'),
                    ('Property, Plant & Equipment', 'property_plant_equipment'),
                    ('Accumulated Depreciation', 'accumulated_depreciation'),
                    ('Intangible Assets', 'intangible_assets'),
                    ('Total Assets', 'total_assets')
                ]
            },
            {
                'title': 'Liabilities',
                'items': [
                    ('Accounts Payable', 'accounts_payable'),
                    ('Accrued Expenses', 'accrued_expenses'),
                    ('Short-Term Debt', 'short_term_debt'),
                    ('Long-Term Debt', 'long_term_debt'),
                    ('Deferred Revenue', 'deferred_revenue'),
                    ('Total Liabilities', 'total_liabilities')
                ]
            },
            {
                'title': 'Equity',
                'items': [
                    ('Common Stock', 'common_stock'),
                    ('Retained Earnings', 'retained_earnings'),
                    ('Treasury Stock', 'treasury_stock'),
                    ('Total Equity', 'total_equity'),
                    ('Total Liabilities and Equity', 'total_liabilities_and_equity')
                ]
            }
        ]
    elif statement_type == 'cash_flow':
        title = "Cash Flow Statement Comparison"
        data = comparison.get_cash_flow_comparison()
        sections = [
            {
                'title': 'Operating Activities',
                'items': [
                    ('Net Income', 'net_income'),
                    ('Depreciation and Amortization', 'depreciation_amortization'),
                    ('Changes in Accounts Receivable', 'accounts_receivable_change'),
                    ('Changes in Inventory', 'inventory_change'),
                    ('Changes in Accounts Payable', 'accounts_payable_change'),
                    ('Net Cash from Operating Activities', 'operating_cash_flow')
                ]
            },
            {
                'title': 'Investing Activities',
                'items': [
                    ('Capital Expenditures', 'capital_expenditures'),
                    ('Acquisitions', 'acquisitions'),
                    ('Investments Sold', 'investments_sold'),
                    ('Net Cash from Investing Activities', 'investing_cash_flow')
                ]
            },
            {
                'title': 'Financing Activities',
                'items': [
                    ('Debt Issuance', 'debt_issuance'),
                    ('Debt Repayment', 'debt_repayment'),
                    ('Dividends Paid', 'dividends_paid'),
                    ('Stock Issuance', 'stock_issuance'),
                    ('Stock Repurchase', 'stock_repurchase'),
                    ('Net Cash from Financing Activities', 'financing_cash_flow')
                ]
            },
            {
                'title': 'Cash Balances',
                'items': [
                    ('Net Change in Cash', 'net_change_in_cash'),
                    ('Beginning Cash Balance', 'beginning_cash_balance'),
                    ('Ending Cash Balance', 'ending_cash_balance')
                ]
            }
        ]
    else:
        raise ValueError(f"Unknown statement type: {statement_type}")
    
    # Create a new window
    window = tk.Toplevel(parent)
    window.title(f"{title} - {base_year} vs. {forecast_year}")
    window.geometry("1000x700")
    
    # Create a frame for the title
    title_frame = tk.Frame(window, pady=10)
    title_frame.pack(fill='x')
    
    # Add a title
    title_label = tk.Label(
        title_frame, 
        text=f"{comparison.base_data.company_name} - {title}", 
        font=("Arial", 16, "bold")
    )
    title_label.pack()
    
    subtitle_label = tk.Label(
        title_frame, 
        text=f"{base_year} vs. {forecast_year}", 
        font=("Arial", 12)
    )
    subtitle_label.pack()
    
    # Create a frame for the comparison table
    table_frame = ttk.Frame(window, padding=10)
    table_frame.pack(fill='both', expand=True)
    
    # Create a canvas with scrollbar
    canvas = tk.Canvas(table_frame)
    scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    # Create the table header
    header_frame = ttk.Frame(scrollable_frame)
    header_frame.pack(fill='x', pady=5)
    
    # Column widths
    col_widths = [300, 150, 150, 200]
    
    # Header labels
    headers = ["Item", base_year, forecast_year, "Change"]
    
    for i, header in enumerate(headers):
        label = ttk.Label(
            header_frame, 
            text=header, 
            font=("Arial", 10, "bold"),
            width=col_widths[i] if i > 0 else col_widths[i]
        )
        label.grid(row=0, column=i, padx=5, pady=5, sticky='w')
    
    # Add a separator
    ttk.Separator(scrollable_frame, orient='horizontal').pack(fill='x', pady=5)
    
    # Add each section
    row_index = 1
    for section in sections:
        # Section title
        section_frame = ttk.Frame(scrollable_frame)
        section_frame.pack(fill='x', pady=5)
        
        section_label = ttk.Label(
            section_frame, 
            text=section['title'], 
            font=("Arial", 10, "bold")
        )
        section_label.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky='w')
        
        # Section items
        for item_name, item_key in section['items']:
            item_frame = ttk.Frame(scrollable_frame)
            item_frame.pack(fill='x')
            
            # Item name
            name_label = ttk.Label(
                item_frame, 
                text=item_name, 
                width=col_widths[0]
            )
            name_label.grid(row=0, column=0, padx=5, pady=2, sticky='w')
            
            # Base year value
            base_value = data[item_key]['base']
            base_label = ttk.Label(
                item_frame, 
                text=format_currency(base_value), 
                width=col_widths[1]
            )
            base_label.grid(row=0, column=1, padx=5, pady=2, sticky='w')
            
            # Forecast year value
            forecast_value = data[item_key]['forecast']
            forecast_label = ttk.Label(
                item_frame, 
                text=format_currency(forecast_value), 
                width=col_widths[2]
            )
            forecast_label.grid(row=0, column=2, padx=5, pady=2, sticky='w')
            
            # Change
            change_value = data[item_key]['change']
            change_percentage = data[item_key]['percentage']
            change_label = ttk.Label(
                item_frame, 
                text=format_change(change_value, change_percentage), 
                width=col_widths[3]
            )
            change_label.grid(row=0, column=3, padx=5, pady=2, sticky='w')
            
            row_index += 1
        
        # Add a separator after each section
        ttk.Separator(scrollable_frame, orient='horizontal').pack(fill='x', pady=5)
    
    # Add a notes section
    notes_frame = ttk.LabelFrame(window, text="Management Notes", padding=10)
    notes_frame.pack(fill='x', padx=10, pady=10, side='bottom')
    
    # Get notes for the specific statement type
    from analysis.notes_generator import NotesGenerator
    notes_gen = NotesGenerator(comparison)
    
    if statement_type == 'income':
        notes_text = notes_gen.generate_income_statement_notes()
    elif statement_type == 'balance':
        notes_text = notes_gen.generate_balance_sheet_notes()
    elif statement_type == 'cash_flow':
        notes_text = notes_gen.generate_cash_flow_notes()
    
    # Add a text area for notes
    notes_area = scrolledtext.ScrolledText(notes_frame, wrap=tk.WORD, height=10)
    notes_area.pack(fill='both', expand=True)
    notes_area.insert(tk.END, notes_text)
    notes_area.config(state='disabled')  # Make read-only
    
    # Add a close button
    close_button = ttk.Button(window, text="Close", command=window.destroy)
    close_button.pack(pady=10)

def show_management_discussion(parent, comparison, base_year, forecast_year):
    """
    Display a comprehensive management discussion and analysis.
    
    Args:
        parent: Parent widget
        comparison: FinancialComparison instance
        base_year: Base year (e.g., "2023")
        forecast_year: Forecast year (e.g., "2024")
    """
    # Create a new window
    window = tk.Toplevel(parent)
    window.title(f"Management Discussion and Analysis - {base_year} vs. {forecast_year}")
    window.geometry("800x600")
    
    # Create a frame for the title
    title_frame = tk.Frame(window, pady=10)
    title_frame.pack(fill='x')
    
    # Add a title
    title_label = tk.Label(
        title_frame, 
        text=f"{comparison.base_data.company_name} - Management Discussion and Analysis", 
        font=("Arial", 16, "bold")
    )
    title_label.pack()
    
    subtitle_label = tk.Label(
        title_frame, 
        text=f"{base_year} vs. {forecast_year}", 
        font=("Arial", 12)
    )
    subtitle_label.pack()
    
    # Create a frame for the MD&A content
    content_frame = ttk.Frame(window, padding=10)
    content_frame.pack(fill='both', expand=True)
    
    # Get comprehensive notes
    from analysis.notes_generator import NotesGenerator
    notes_gen = NotesGenerator(comparison)
    notes_text = notes_gen.generate_comprehensive_notes()
    
    # Add a text area for notes
    notes_area = scrolledtext.ScrolledText(content_frame, wrap=tk.WORD)
    notes_area.pack(fill='both', expand=True)
    notes_area.insert(tk.END, notes_text)
    notes_area.config(state='disabled')  # Make read-only
    
    # Add a close button
    close_button = ttk.Button(window, text="Close", command=window.destroy)
    close_button.pack(pady=10)