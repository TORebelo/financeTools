"""
Module for educational views and interactive learning features.
"""

import tkinter as tk
from tkinter import ttk, scrolledtext
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class FinancialLearningView:
    """
    Class to create educational views for financial statements.
    """
    
    def __init__(self, parent, financial_data, forecast_data=None):
        """
        Initialize the learning view.
        
        Args:
            parent: Parent widget
            financial_data: Current financial data
            forecast_data: Forecasted financial data (optional)
        """
        self.parent = parent
        self.current_data = financial_data
        self.forecast_data = forecast_data
        
        # Create a new window
        self.window = tk.Toplevel(parent)
        self.window.title("Financial Statement Learning Tool")
        self.window.geometry("1200x800")
        
        # Create a frame for the title
        title_frame = tk.Frame(self.window, pady=10)
        title_frame.pack(fill='x')
        
        # Add a title
        title_label = tk.Label(
            title_frame, 
            text=f"{financial_data.company_name} - Financial Learning Tool", 
            font=("Arial", 16, "bold")
        )
        title_label.pack()
        
        # Create a notebook (tabbed interface)
        self.notebook = ttk.Notebook(self.window)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Create tabs
        self.overview_tab = ttk.Frame(self.notebook)
        self.statement_impact_tab = ttk.Frame(self.notebook)
        self.ratio_analysis_tab = ttk.Frame(self.notebook)
        self.visualization_tab = ttk.Frame(self.notebook)
        
        self.notebook.add(self.overview_tab, text="Financial Overview")
        self.notebook.add(self.statement_impact_tab, text="Statement Impact Simulator")
        self.notebook.add(self.ratio_analysis_tab, text="Ratio Analysis")
        self.notebook.add(self.visualization_tab, text="Visualizations")
        
        # Create the content for each tab
        self._create_overview_tab()
        self._create_statement_impact_tab()
        self._create_ratio_analysis_tab()
        self._create_visualization_tab()
        
        # Add a close button
        close_button = ttk.Button(self.window, text="Close", command=self.window.destroy)
        close_button.pack(pady=10)
    
    def _create_overview_tab(self):
        """Create the financial overview tab."""
        # Create a frame for the overview
        overview_frame = ttk.Frame(self.overview_tab, padding=10)
        overview_frame.pack(fill='both', expand=True)
        
        # Create a scrollable text area for the overview
        overview_text = scrolledtext.ScrolledText(overview_frame, wrap=tk.WORD, height=30)
        overview_text.pack(fill='both', expand=True)
        
        # Add overview content
        overview_content = """
# Understanding Financial Statements

Financial statements are formal records of a company's financial activities and position. They provide a snapshot of a company's financial health and performance over a specific period. The three main financial statements are:

## 1. Income Statement

The income statement shows a company's revenues, expenses, and profits over a specific period. It answers the question: "Is the company profitable?"

Key components:
- Revenue: Money earned from selling products or services
- Cost of Goods Sold (COGS): Direct costs associated with producing goods or services
- Gross Profit: Revenue minus COGS
- Operating Expenses: Costs of running the business (salaries, rent, etc.)
- Operating Income: Gross profit minus operating expenses
- Interest Expense: Cost of borrowing money
- Income Tax: Taxes paid on profits
- Net Income: The "bottom line" profit after all expenses

## 2. Balance Sheet

The balance sheet shows a company's assets, liabilities, and equity at a specific point in time. It follows the accounting equation: Assets = Liabilities + Equity.

Key components:
- Assets: What the company owns (cash, inventory, property, etc.)
- Liabilities: What the company owes (debt, accounts payable, etc.)
- Equity: The owners' stake in the company (common stock, retained earnings, etc.)

## 3. Cash Flow Statement

The cash flow statement shows how cash moves in and out of a company over a specific period. It categorizes cash flows into three activities:

- Operating Activities: Cash generated from core business operations
- Investing Activities: Cash used for long-term assets and investments
- Financing Activities: Cash from debt and equity financing

## How Financial Statements Are Connected

Changes in one financial statement often affect the others:

1. Net income from the income statement increases retained earnings on the balance sheet.
2. Depreciation is an expense on the income statement but not a cash outflow; it's added back on the cash flow statement.
3. Capital expenditures don't appear on the income statement but reduce cash on the cash flow statement and increase assets on the balance sheet.
4. Debt issuance increases cash on the cash flow statement and increases liabilities on the balance sheet.

## Financial Ratios

Financial ratios help analyze a company's performance and financial health:

- Profitability Ratios: Measure a company's ability to generate profits (e.g., gross margin, net margin)
- Liquidity Ratios: Measure a company's ability to pay short-term obligations (e.g., current ratio)
- Solvency Ratios: Measure a company's ability to meet long-term obligations (e.g., debt-to-equity)
- Efficiency Ratios: Measure how efficiently a company uses its assets (e.g., inventory turnover)
- Valuation Ratios: Measure a company's stock price relative to its financials (e.g., P/E ratio, EV/EBITDA)

Use the other tabs in this tool to explore these concepts interactively!
"""
        
        overview_text.insert(tk.END, overview_content)
        overview_text.config(state='disabled')  # Make read-only
    
    def _create_statement_impact_tab(self):
        """Create the statement impact simulator tab."""
        # Create a frame for the simulator
        simulator_frame = ttk.Frame(self.statement_impact_tab, padding=10)
        simulator_frame.pack(fill='both', expand=True)
        
        # Create a frame for the input controls
        input_frame = ttk.LabelFrame(simulator_frame, text="Change Financial Parameters", padding=10)
        input_frame.pack(fill='x', padx=10, pady=10)
        
        # Create a grid for the input controls
        input_grid = ttk.Frame(input_frame)
        input_grid.pack(fill='x', padx=10, pady=10)
        
        # Create input fields for various financial parameters
        self.input_fields = {}
        
        # Income Statement Parameters
        ttk.Label(input_grid, text="Income Statement Parameters", font=("Arial", 10, "bold")).grid(row=0, column=0, columnspan=2, sticky="w", padx=5, pady=5)
        
        parameters = [
            ("Revenue Change ($)", "revenue_change"),
            ("COGS Change ($)", "cogs_change"),
            ("Operating Expenses Change ($)", "opex_change"),
            ("Interest Expense Change ($)", "interest_change")
        ]
        
        for i, (label_text, field_name) in enumerate(parameters):
            ttk.Label(input_grid, text=label_text).grid(row=i+1, column=0, sticky="w", padx=5, pady=2)
            entry = ttk.Entry(input_grid, width=15)
            entry.grid(row=i+1, column=1, padx=5, pady=2)
            entry.insert(0, "0")
            self.input_fields[field_name] = entry
        
        # Balance Sheet Parameters
        ttk.Label(input_grid, text="Balance Sheet Parameters", font=("Arial", 10, "bold")).grid(row=0, column=2, columnspan=2, sticky="w", padx=5, pady=5)
        
        parameters = [
            ("Cash Change ($)", "cash_change"),
            ("Accounts Receivable Change ($)", "ar_change"),
            ("Inventory Change ($)", "inventory_change"),
            ("PP&E Change ($)", "ppe_change"),
            ("Accounts Payable Change ($)", "ap_change"),
            ("Debt Change ($)", "debt_change")
        ]
        
        for i, (label_text, field_name) in enumerate(parameters):
            ttk.Label(input_grid, text=label_text).grid(row=i+1, column=2, sticky="w", padx=5, pady=2)
            entry = ttk.Entry(input_grid, width=15)
            entry.grid(row=i+1, column=3, padx=5, pady=2)
            entry.insert(0, "0")
            self.input_fields[field_name] = entry
        
        # Equity Parameters
        ttk.Label(input_grid, text="Equity Parameters", font=("Arial", 10, "bold")).grid(row=0, column=4, columnspan=2, sticky="w", padx=5, pady=5)
        
        parameters = [
            ("Issue New Shares ($)", "new_shares"),
            ("Repurchase Shares ($)", "repurchase_shares"),
            ("Declare Dividends ($)", "dividends"),
            ("Share Price Change ($)", "share_price_change")
        ]
        
        for i, (label_text, field_name) in enumerate(parameters):
            ttk.Label(input_grid, text=label_text).grid(row=i+1, column=4, sticky="w", padx=5, pady=2)
            entry = ttk.Entry(input_grid, width=15)
            entry.grid(row=i+1, column=5, padx=5, pady=2)
            entry.insert(0, "0")
            self.input_fields[field_name] = entry
        
        # Add a button to simulate the impact
        simulate_button = ttk.Button(
            input_frame, 
            text="Simulate Impact", 
            command=self._simulate_impact
        )
        simulate_button.pack(pady=10)
        
        # Create a frame for the output
        self.output_frame = ttk.LabelFrame(simulator_frame, text="Impact Analysis", padding=10)
        self.output_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Create a notebook for the output tabs
        self.output_notebook = ttk.Notebook(self.output_frame)
        self.output_notebook.pack(fill='both', expand=True)
        
        # Create tabs for each statement
        self.income_tab = ttk.Frame(self.output_notebook)
        self.balance_tab = ttk.Frame(self.output_notebook)
        self.cash_flow_tab = ttk.Frame(self.output_notebook)
        self.ratios_tab = ttk.Frame(self.output_notebook)
        
        self.output_notebook.add(self.income_tab, text="Income Statement")
        self.output_notebook.add(self.balance_tab, text="Balance Sheet")
        self.output_notebook.add(self.cash_flow_tab, text="Cash Flow")
        self.output_notebook.add(self.ratios_tab, text="Key Ratios")
        
        # Create text areas for each tab
        self.income_text = scrolledtext.ScrolledText(self.income_tab, wrap=tk.WORD, height=15)
        self.income_text.pack(fill='both', expand=True)
        
        self.balance_text = scrolledtext.ScrolledText(self.balance_tab, wrap=tk.WORD, height=15)
        self.balance_text.pack(fill='both', expand=True)
        
        self.cash_flow_text = scrolledtext.ScrolledText(self.cash_flow_tab, wrap=tk.WORD, height=15)
        self.cash_flow_text.pack(fill='both', expand=True)
        
        self.ratios_text = scrolledtext.ScrolledText(self.ratios_tab, wrap=tk.WORD, height=15)
        self.ratios_text.pack(fill='both', expand=True)
        
        # Create a frame for the explanation
        self.explanation_frame = ttk.LabelFrame(simulator_frame, text="Explanation of Impact", padding=10)
        self.explanation_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Create a text area for the explanation
        self.explanation_text = scrolledtext.ScrolledText(self.explanation_frame, wrap=tk.WORD, height=10)
        self.explanation_text.pack(fill='both', expand=True)
    
    def _simulate_impact(self):
        """Simulate the impact of changes on financial statements."""
        try:
            # Get the input values
            changes = {}
            for field_name, entry in self.input_fields.items():
                try:
                    changes[field_name] = float(entry.get())
                except ValueError:
                    changes[field_name] = 0
            
            # Create a copy of the current data
            from copy import deepcopy
            simulated_data = deepcopy(self.current_data)
            
            # Apply the changes to the simulated data
            # Income Statement Changes
            simulated_data.revenue += changes.get('revenue_change', 0)
            simulated_data.cogs += changes.get('cogs_change', 0)
            simulated_data.operating_expenses += changes.get('opex_change', 0)
            simulated_data.interest_expense += changes.get('interest_change', 0)
            
            # Recalculate net income
            gross_profit = simulated_data.revenue - simulated_data.cogs
            operating_income = gross_profit - simulated_data.operating_expenses
            ebt = operating_income - simulated_data.interest_expense
            income_tax = ebt * simulated_data.tax_rate
            simulated_data.net_income = ebt - income_tax
            
            # Balance Sheet Changes
            simulated_data.cash += changes.get('cash_change', 0)
            simulated_data.accounts_receivable += changes.get('ar_change', 0)
            simulated_data.inventory += changes.get('inventory_change', 0)
            simulated_data.property_plant_equipment += changes.get('ppe_change', 0)
            simulated_data.accounts_payable += changes.get('ap_change', 0)
            simulated_data.long_term_debt += changes.get('debt_change', 0)
            
            # Equity Changes
            new_shares = changes.get('new_shares', 0)
            repurchase_shares = changes.get('repurchase_shares', 0)
            dividends = changes.get('dividends', 0)
            
            if new_shares > 0:
                simulated_data.common_stock += new_shares
                simulated_data.cash += new_shares
            
            if repurchase_shares > 0:
                simulated_data.treasury_stock += repurchase_shares
                simulated_data.cash -= repurchase_shares
            
            if dividends > 0:
                simulated_data.retained_earnings -= dividends
                simulated_data.cash -= dividends
            
            # Share price change
            simulated_data.share_price += changes.get('share_price_change', 0)
            
            # Update the output text areas
            self._update_income_statement(simulated_data)
            self._update_balance_sheet(simulated_data)
            self._update_cash_flow(simulated_data)
            self._update_ratios(simulated_data)
            self._update_explanation(changes, simulated_data)
            
        except Exception as e:
            # Show error message
            self.explanation_text.delete(1.0, tk.END)
            self.explanation_text.insert(tk.END, f"Error: {str(e)}")
    
    def _update_income_statement(self, data):
        """Update the income statement text area."""
        self.income_text.config(state='normal')
        self.income_text.delete(1.0, tk.END)
        
        # Format the income statement
        income_statement = f"""
{data.company_name}
Income Statement
For the Year Ended {data.reporting_period}

Revenue                                 ${data.revenue:,.2f}
Cost of Goods Sold                      ${data.cogs:,.2f}
------------------------------------------------------------
Gross Profit                            ${data.revenue - data.cogs:,.2f}

Operating Expenses                      ${data.operating_expenses:,.2f}
------------------------------------------------------------
Operating Income                        ${data.revenue - data.cogs - data.operating_expenses:,.2f}

Interest Expense                        ${data.interest_expense:,.2f}
------------------------------------------------------------
Income Before Tax                       ${data.revenue - data.cogs - data.operating_expenses - data.interest_expense:,.2f}

Income Tax Expense                      ${(data.revenue - data.cogs - data.operating_expenses - data.interest_expense) * data.tax_rate:,.2f}
------------------------------------------------------------
Net Income                              ${data.net_income:,.2f}

Earnings Per Share                      ${data.earnings_per_share:,.2f}
"""
        
        self.income_text.insert(tk.END, income_statement)
        self.income_text.config(state='disabled')
    
    def _update_balance_sheet(self, data):
        """Update the balance sheet text area."""
        self.balance_text.config(state='normal')
        self.balance_text.delete(1.0, tk.END)
        
        # Calculate totals
        total_current_assets = data.cash + data.accounts_receivable + data.inventory + data.prepaid_expenses
        total_non_current_assets = data.property_plant_equipment - data.accumulated_depreciation + data.intangible_assets + data.goodwill + data.long_term_investments
        total_assets = total_current_assets + total_non_current_assets
        
        total_current_liabilities = data.accounts_payable + data.accrued_expenses + data.short_term_debt + data.deferred_revenue
        total_non_current_liabilities = data.long_term_debt + data.deferred_tax_liabilities
        total_liabilities = total_current_liabilities + total_non_current_liabilities
        
        total_equity = data.common_stock + data.additional_paid_in_capital + data.retained_earnings - data.treasury_stock + data.accumulated_other_comprehensive_income
        
        # Format the balance sheet
        balance_sheet = f"""
{data.company_name}
Balance Sheet
As of {data.reporting_date}

ASSETS
Current Assets:
  Cash and Cash Equivalents             ${data.cash:,.2f}
  Accounts Receivable                   ${data.accounts_receivable:,.2f}
  Inventory                             ${data.inventory:,.2f}
  Prepaid Expenses                      ${data.prepaid_expenses:,.2f}
------------------------------------------------------------
  Total Current Assets                  ${total_current_assets:,.2f}

Non-Current Assets:
  Property, Plant, and Equipment        ${data.property_plant_equipment:,.2f}
  Less: Accumulated Depreciation        ${data.accumulated_depreciation:,.2f}
  Intangible Assets                     ${data.intangible_assets:,.2f}
  Goodwill                              ${data.goodwill:,.2f}
  Long-term Investments                 ${data.long_term_investments:,.2f}
------------------------------------------------------------
  Total Non-Current Assets              ${total_non_current_assets:,.2f}
------------------------------------------------------------
TOTAL ASSETS                            ${total_assets:,.2f}

LIABILITIES AND EQUITY
Current Liabilities:
  Accounts Payable                      ${data.accounts_payable:,.2f}
  Accrued Expenses                      ${data.accrued_expenses:,.2f}
  Short-term Debt                       ${data.short_term_debt:,.2f}
  Deferred Revenue                      ${data.deferred_revenue:,.2f}
------------------------------------------------------------
  Total Current Liabilities             ${total_current_liabilities:,.2f}

Non-Current Liabilities:
  Long-term Debt                        ${data.long_term_debt:,.2f}
  Deferred Tax Liabilities              ${data.deferred_tax_liabilities:,.2f}
------------------------------------------------------------
  Total Non-Current Liabilities         ${total_non_current_liabilities:,.2f}
------------------------------------------------------------
TOTAL LIABILITIES                       ${total_liabilities:,.2f}

Equity:
  Common Stock                          ${data.common_stock:,.2f}
  Additional Paid-in Capital            ${data.additional_paid_in_capital:,.2f}
  Retained Earnings                     ${data.retained_earnings:,.2f}
  Treasury Stock                        ${data.treasury_stock:,.2f}
  Accumulated Other Comprehensive Income ${data.accumulated_other_comprehensive_income:,.2f}
------------------------------------------------------------
  Total Equity                          ${total_equity:,.2f}
------------------------------------------------------------
TOTAL LIABILITIES AND EQUITY            ${total_liabilities + total_equity:,.2f}

Market Capitalization                   ${data.market_cap:,.2f}
Enterprise Value                        ${data.enterprise_value:,.2f}
Book Value Per Share                    ${data.book_value_per_share:,.2f}
"""
        
        self.balance_text.insert(tk.END, balance_sheet)
        self.balance_text.config(state='disabled')
    
    def _update_cash_flow(self, data):
        """Update the cash flow text area."""
        self.cash_flow_text.config(state='normal')
        self.cash_flow_text.delete(1.0, tk.END)
        
        # Calculate cash flows
        operating_cash_flow = data.net_income + data.depreciation_amortization - data.accounts_receivable_change - data.inventory_change + data.accounts_payable_change + data.accrued_expenses_change + data.deferred_revenue_change
        
        investing_cash_flow = -data.capital_expenditures - data.acquisitions + data.investments_sold + data.other_investing
        
        financing_cash_flow = data.debt_issuance - data.debt_repayment - data.dividends_paid + data.stock_issuance - data.stock_repurchase + data.other_financing
        
        net_change_in_cash = operating_cash_flow + investing_cash_flow + financing_cash_flow
        
        ending_cash = data.beginning_cash_balance + net_change_in_cash
        
        # Format the cash flow statement
        cash_flow_statement = f"""
{data.company_name}
Statement of Cash Flows
For the Year Ended {data.reporting_period}

Cash Flows from Operating Activities:
  Net Income                            ${data.net_income:,.2f}
  Adjustments:
    Depreciation and Amortization       ${data.depreciation_amortization:,.2f}
  Changes in Working Capital:
    Accounts Receivable                 ${-data.accounts_receivable_change:,.2f}
    Inventory                           ${-data.inventory_change:,.2f}
    Accounts Payable                    ${data.accounts_payable_change:,.2f}
    Accrued Expenses                    ${data.accrued_expenses_change:,.2f}
    Deferred Revenue                    ${data.deferred_revenue_change:,.2f}
------------------------------------------------------------
  Net Cash from Operating Activities    ${operating_cash_flow:,.2f}

Cash Flows from Investing Activities:
  Capital Expenditures                  ${-data.capital_expenditures:,.2f}
  Acquisitions                          ${-data.acquisitions:,.2f}
  Sale of Investments                   ${data.investments_sold:,.2f}
  Other Investing Activities            ${data.other_investing:,.2f}
------------------------------------------------------------
  Net Cash from Investing Activities    ${investing_cash_flow:,.2f}

Cash Flows from Financing Activities:
  Debt Issuance                         ${data.debt_issuance:,.2f}
  Debt Repayment                        ${-data.debt_repayment:,.2f}
  Dividends Paid                        ${-data.dividends_paid:,.2f}
  Stock Issuance                        ${data.stock_issuance:,.2f}
  Stock Repurchase                      ${-data.stock_repurchase:,.2f}
  Other Financing Activities            ${data.other_financing:,.2f}
------------------------------------------------------------
  Net Cash from Financing Activities    ${financing_cash_flow:,.2f}
------------------------------------------------------------
Net Change in Cash                      ${net_change_in_cash:,.2f}

Cash at Beginning of Period             ${data.beginning_cash_balance:,.2f}
------------------------------------------------------------
Cash at End of Period                   ${ending_cash:,.2f}
"""
        
        self.cash_flow_text.insert(tk.END, cash_flow_statement)
        self.cash_flow_text.config(state='disabled')
    
    def _update_ratios(self, data):
        """Update the ratios text area."""
        self.ratios_text.config(state='normal')
        self.ratios_text.delete(1.0, tk.END)
        
        # Calculate ratios
        from analysis.ratios import FinancialRatios
        ratios = FinancialRatios(data).get_all_ratios()
        
        # Format the ratios
        ratios_text = f"""
{data.company_name}
Key Financial Ratios
As of {data.reporting_date}

Profitability Ratios:
  Gross Margin                          {ratios['profitability']['gross_margin']:.2%}
  Operating Margin                      {ratios['profitability']['operating_margin']:.2%}
  Net Margin                            {ratios['profitability']['net_margin']:.2%}
  Return on Assets                      {ratios['profitability']['return_on_assets']:.2%}
  Return on Equity                      {ratios['profitability']['return_on_equity']:.2%}

Liquidity Ratios:
  Current Ratio                         {ratios['liquidity']['current_ratio']:.2f}
  Quick Ratio                           {ratios['liquidity']['quick_ratio']:.2f}
  Cash Ratio                            {ratios['liquidity']['cash_ratio']:.2f}

Solvency Ratios:
  Debt to Assets                        {ratios['solvency']['debt_to_assets']:.2f}
  Debt to Equity                        {ratios['solvency']['debt_to_equity']:.2f}
  Interest Coverage                     {ratios['solvency']['interest_coverage']:.2f}
  Debt to EBITDA                        {ratios['solvency']['debt_to_ebitda']:.2f}

Efficiency Ratios:
  Asset Turnover                        {ratios['efficiency']['asset_turnover']:.2f}
  Receivables Turnover                  {ratios['efficiency']['receivables_turnover']:.2f}
  Inventory Turnover                    {ratios['efficiency']['inventory_turnover']:.2f}
  Days Sales Outstanding                {ratios['efficiency']['days_sales_outstanding']:.2f}
  Days Inventory Outstanding            {ratios['efficiency']['days_inventory_outstanding']:.2f}

Valuation Ratios:
  P/E Ratio                             {ratios['valuation']['pe_ratio']:.2f}
  Price to Book                         {ratios['valuation']['price_to_book']:.2f}
  Price to Sales                        {ratios['valuation']['price_to_sales']:.2f}
  EV/EBITDA                             {ratios['valuation']['ev_to_ebitda']:.2f}
  EV/Revenue                            {ratios['valuation']['ev_to_revenue']:.2f}
"""
        
        self.ratios_text.insert(tk.END, ratios_text)
        self.ratios_text.config(state='disabled')
    
    def _update_explanation(self, changes, data):
        """Update the explanation text area."""
        self.explanation_text.config(state='normal')
        self.explanation_text.delete(1.0, tk.END)
        
        # Generate explanation
        explanation = "# Impact Analysis\n\n"
        
        # Income Statement Impact
        if any(changes.get(field, 0) != 0 for field in ['revenue_change', 'cogs_change', 'opex_change', 'interest_change']):
            explanation += "## Income Statement Impact\n\n"
            
            if changes.get('revenue_change', 0) != 0:
                direction = "increased" if changes['revenue_change'] > 0 else "decreased"
                explanation += f"- Revenue {direction} by ${abs(changes['revenue_change']):,.2f}, which directly affects gross profit and net income.\n"
            
            if changes.get('cogs_change', 0) != 0:
                direction = "increased" if changes['cogs_change'] > 0 else "decreased"
                explanation += f"- Cost of Goods Sold {direction} by ${abs(changes['cogs_change']):,.2f}, which affects gross profit and net income.\n"
            
            if changes.get('opex_change', 0) != 0:
                direction = "increased" if changes['opex_change'] > 0 else "decreased"
                explanation += f"- Operating Expenses {direction} by ${abs(changes['opex_change']):,.2f}, which affects operating income and net income.\n"
            
            if changes.get('interest_change', 0) != 0:
                direction = "increased" if changes['interest_change'] > 0 else "decreased"
                explanation += f"- Interest Expense {direction} by ${abs(changes['interest_change']):,.2f}, which affects income before tax and net income.\n"
            
            explanation += "\n"
        
        # Balance Sheet Impact
        if any(changes.get(field, 0) != 0 for field in ['cash_change', 'ar_change', 'inventory_change', 'ppe_change', 'ap_change', 'debt_change']):
            explanation += "## Balance Sheet Impact\n\n"
            
            if changes.get('cash_change', 0) != 0:
                direction = "increased" if changes['cash_change'] > 0 else "decreased"
                explanation += f"- Cash {direction} by ${abs(changes['cash_change']):,.2f}, which affects liquidity ratios and enterprise value.\n"
            
            if changes.get('ar_change', 0) != 0:
                direction = "increased" if changes['ar_change'] > 0 else "decreased"
                explanation += f"- Accounts Receivable {direction} by ${abs(changes['ar_change']):,.2f}, which affects working capital and liquidity ratios.\n"
            
            if changes.get('inventory_change', 0) != 0:
                direction = "increased" if changes['inventory_change'] > 0 else "decreased"
                explanation += f"- Inventory {direction} by ${abs(changes['inventory_change']):,.2f}, which affects working capital and inventory turnover.\n"
            
            if changes.get('ppe_change', 0) != 0:
                direction = "increased" if changes['ppe_change'] > 0 else "decreased"
                explanation += f"- Property, Plant, and Equipment {direction} by ${abs(changes['ppe_change']):,.2f}, which affects total assets and return on assets.\n"
            
            if changes.get('ap_change', 0) != 0:
                direction = "increased" if changes['ap_change'] > 0 else "decreased"
                explanation += f"- Accounts Payable {direction} by ${abs(changes['ap_change']):,.2f}, which affects working capital and liquidity ratios.\n"
            
            if changes.get('debt_change', 0) != 0:
                direction = "increased" if changes['debt_change'] > 0 else "decreased"
                explanation += f"- Long-term Debt {direction} by ${abs(changes['debt_change']):,.2f}, which affects solvency ratios and enterprise value.\n"
            
            explanation += "\n"
        
        # Equity Impact
        if any(changes.get(field, 0) != 0 for field in ['new_shares', 'repurchase_shares', 'dividends', 'share_price_change']):
            explanation += "## Equity and Valuation Impact\n\n"
            
            if changes.get('new_shares', 0) != 0:
                explanation += f"- Issuing ${changes['new_shares']:,.2f} of new shares increases common stock and cash, diluting existing shareholders.\n"
            
            if changes.get('repurchase_shares', 0) != 0:
                explanation += f"- Repurchasing ${changes['repurchase_shares']:,.2f} of shares increases treasury stock and decreases cash, potentially increasing EPS.\n"
            
            if changes.get('dividends', 0) != 0:
                explanation += f"- Declaring ${changes['dividends']:,.2f} in dividends decreases retained earnings and cash, returning value to shareholders.\n"
            
            if changes.get('share_price_change', 0) != 0:
                direction = "increased" if changes['share_price_change'] > 0 else "decreased"
                explanation += f"- Share price {direction} by ${abs(changes['share_price_change']):,.2f}, affecting market capitalization and valuation ratios.\n"
            
            explanation += "\n"
        
        # Cross-Statement Impact
        explanation += "## Cross-Statement Impact\n\n"
        
        # Revenue to Net Income to Retained Earnings
        if changes.get('revenue_change', 0) != 0:
            net_income_impact = changes['revenue_change'] * (1 - data.tax_rate)
            explanation += f"- A ${changes['revenue_change']:,.2f} change in revenue flows through to approximately ${net_income_impact:,.2f} in net income (after tax).\n"
            explanation += f"- This net income change would increase retained earnings by the same amount if not distributed as dividends.\n"
        
        # Debt to Interest Expense
        if changes.get('debt_change', 0) != 0:
            # Assume 5% interest rate for simplicity
            interest_impact = changes['debt_change'] * 0.05
            explanation += f"- A ${changes['debt_change']:,.2f} change in debt would affect annual interest expense by approximately ${interest_impact:,.2f} (assuming 5% interest rate).\n"
            explanation += f"- This interest expense change would impact net income by approximately ${interest_impact * (1 - data.tax_rate):,.2f} after tax.\n"
        
        # Cash Flow Impact
        explanation += "\n## Cash Flow Impact\n\n"
        
        cash_impact = 0
        
        if changes.get('cash_change', 0) != 0:
            cash_impact += changes['cash_change']
        
        if changes.get('new_shares', 0) != 0:
            cash_impact += changes['new_shares']
            explanation += f"- Issuing shares increases cash flow from financing activities by ${changes['new_shares']:,.2f}.\n"
        
        if changes.get('repurchase_shares', 0) != 0:
            cash_impact -= changes['repurchase_shares']
            explanation += f"- Repurchasing shares decreases cash flow from financing activities by ${changes['repurchase_shares']:,.2f}.\n"
        
        if changes.get('dividends', 0) != 0:
            cash_impact -= changes['dividends']
            explanation += f"- Paying dividends decreases cash flow from financing activities by ${changes['dividends']:,.2f}.\n"
        
        if changes.get('debt_change', 0) != 0:
            cash_impact += changes['debt_change']
            explanation += f"- Changes in debt affect cash flow from financing activities by ${changes['debt_change']:,.2f}.\n"
        
        if changes.get('ppe_change', 0) != 0:
            cash_impact -= changes['ppe_change']
            explanation += f"- Capital expenditures decrease cash flow from investing activities by ${changes['ppe_change']:,.2f}.\n"
        
        explanation += f"\nTotal impact on cash: ${cash_impact:,.2f}\n"
        
        # Ratio Impact
        explanation += "\n## Key Ratio Impact\n\n"
        
        from analysis.ratios import FinancialRatios
        original_ratios = FinancialRatios(self.current_data).get_all_ratios()
        new_ratios = FinancialRatios(data).get_all_ratios()
        
        # Compare key ratios
        key_ratio_changes = [
            ("EV/EBITDA", original_ratios['valuation']['ev_to_ebitda'], new_ratios['valuation']['ev_to_ebitda']),
            ("P/E Ratio", original_ratios['valuation']['pe_ratio'], new_ratios['valuation']['pe_ratio']),
            ("Debt to Equity", original_ratios['solvency']['debt_to_equity'], new_ratios['solvency']['debt_to_equity']),
            ("Current Ratio", original_ratios['liquidity']['current_ratio'], new_ratios['liquidity']['current_ratio']),
            ("Net Margin", original_ratios['profitability']['net_margin'], new_ratios['profitability']['net_margin'])
        ]
        
        for ratio_name, original, new in key_ratio_changes:
            if original != new:
                direction = "increased" if new > original else "decreased"
                explanation += f"- {ratio_name} {direction} from {original:.2f} to {new:.2f}.\n"
        
        self.explanation_text.insert(tk.END, explanation)
        self.explanation_text.config(state='disabled')
    
    def _create_ratio_analysis_tab(self):
        """Create the ratio analysis tab."""
        # Create a frame for the ratio analysis
        ratio_frame = ttk.Frame(self.ratio_analysis_tab, padding=10)
        ratio_frame.pack(fill='both', expand=True)
        
        # Create a frame for the ratio categories
        categories_frame = ttk.LabelFrame(ratio_frame, text="Ratio Categories", padding=10)
        categories_frame.pack(fill='x', padx=10, pady=10)
        
        # Create buttons for each ratio category
        categories = [
            ("Profitability Ratios", self._show_profitability_ratios),
            ("Liquidity Ratios", self._show_liquidity_ratios),
            ("Solvency Ratios", self._show_solvency_ratios),
            ("Efficiency Ratios", self._show_efficiency_ratios),
            ("Valuation Ratios", self._show_valuation_ratios)
        ]
        
        # Create a grid for the category buttons
        button_frame = ttk.Frame(categories_frame)
        button_frame.pack(fill='x', padx=10, pady=10)
        
        for i, (category, command) in enumerate(categories):
            button = ttk.Button(button_frame, text=category, command=command)
            button.grid(row=0, column=i, padx=5, pady=5)
        
        # Create a frame for the ratio details
        self.ratio_details_frame = ttk.LabelFrame(ratio_frame, text="Ratio Details", padding=10)
        self.ratio_details_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Create a text area for the ratio details
        self.ratio_details_text = scrolledtext.ScrolledText(self.ratio_details_frame, wrap=tk.WORD, height=20)
        self.ratio_details_text.pack(fill='both', expand=True)
        
        # Show profitability ratios by default
        self._show_profitability_ratios()
    
    def _show_profitability_ratios(self):
        """Show profitability ratios details."""
        self.ratio_details_text.config(state='normal')
        self.ratio_details_text.delete(1.0, tk.END)
        
        details = """
# Profitability Ratios

Profitability ratios measure a company's ability to generate profits relative to its revenue, assets, equity, or other financial metrics.

## Gross Margin

**Formula:** Gross Profit / Revenue

**Interpretation:** Measures the percentage of revenue that exceeds the cost of goods sold. A higher gross margin indicates that a company can make a reasonable profit on sales, as long as it keeps overhead costs in control.

**Example:** If a company has revenue of $1,000,000 and COGS of $600,000, its gross profit is $400,000 and its gross margin is 40%.

## Operating Margin

**Formula:** Operating Income / Revenue

**Interpretation:** Measures the percentage of revenue that remains after paying for variable costs of production. It focuses on core business profitability before interest and taxes.

**Example:** If a company has operating income of $200,000 and revenue of $1,000,000, its operating margin is 20%.

## Net Margin

**Formula:** Net Income / Revenue

**Interpretation:** Measures the percentage of revenue that remains as profit after all expenses, including taxes and interest. It's the "bottom line" profitability metric.

**Example:** If a company has net income of $150,000 and revenue of $1,000,000, its net margin is 15%.

## Return on Assets (ROA)

**Formula:** Net Income / Total Assets

**Interpretation:** Measures how efficiently a company is using its assets to generate profits. A higher ROA indicates more efficient use of assets.

**Example:** If a company has net income of $150,000 and total assets of $1,500,000, its ROA is 10%.

## Return on Equity (ROE)

**Formula:** Net Income / Total Equity

**Interpretation:** Measures how efficiently a company is using its equity to generate profits. A higher ROE indicates more efficient use of shareholder capital.

**Example:** If a company has net income of $150,000 and total equity of $750,000, its ROE is 20%.

## Connections to Other Financial Statements:

- **Income Statement:** All profitability ratios use components from the income statement (revenue, gross profit, operating income, net income).
- **Balance Sheet:** ROA and ROE use total assets and total equity from the balance sheet.
- **Cash Flow Statement:** While not directly used in these ratios, strong profitability should generally correlate with strong operating cash flow.
"""
        
        self.ratio_details_text.insert(tk.END, details)
        self.ratio_details_text.config(state='disabled')
    
    def _show_liquidity_ratios(self):
        """Show liquidity ratios details."""
        self.ratio_details_text.config(state='normal')
        self.ratio_details_text.delete(1.0, tk.END)
        
        details = """
# Liquidity Ratios

Liquidity ratios measure a company's ability to pay off its short-term debts as they come due, using the company's current or quick assets.

## Current Ratio

**Formula:** Current Assets / Current Liabilities

**Interpretation:** Measures a company's ability to pay short-term obligations within one year. A ratio of 2:1 is considered ideal, meaning the company has twice as many current assets as current liabilities.

**Example:** If a company has current assets of $500,000 and current liabilities of $250,000, its current ratio is 2.0.

## Quick Ratio (Acid-Test Ratio)

**Formula:** (Current Assets - Inventory) / Current Liabilities

**Interpretation:** A more stringent measure of liquidity that excludes inventory, which may not be easily converted to cash. A ratio of 1:1 or higher is generally considered good.

**Example:** If a company has current assets of $500,000, inventory of $150,000, and current liabilities of $250,000, its quick ratio is 1.4.

## Cash Ratio

**Formula:** Cash and Cash Equivalents / Current Liabilities

**Interpretation:** The most conservative liquidity ratio, measuring a company's ability to cover its short-term liabilities with just its cash and cash equivalents.

**Example:** If a company has cash of $100,000 and current liabilities of $250,000, its cash ratio is 0.4.

## Working Capital

**Formula:** Current Assets - Current Liabilities

**Interpretation:** The amount of current assets that remain after paying all current liabilities. Positive working capital indicates that a company can pay its short-term liabilities and still fund its operations.

**Example:** If a company has current assets of $500,000 and current liabilities of $250,000, its working capital is $250,000.

## Connections to Other Financial Statements:

- **Balance Sheet:** All liquidity ratios use components from the balance sheet (current assets, inventory, cash, current liabilities).
- **Income Statement:** While not directly used in these ratios, profitability affects a company's ability to generate cash and maintain liquidity.
- **Cash Flow Statement:** Operating cash flow affects cash and cash equivalents, which are used in the cash ratio.
"""
        
        self.ratio_details_text.insert(tk.END, details)
        self.ratio_details_text.config(state='disabled')
    
    def _show_solvency_ratios(self):
        """Show solvency ratios details."""
        self.ratio_details_text.config(state='normal')
        self.ratio_details_text.delete(1.0, tk.END)
        
        details = """
# Solvency Ratios

Solvency ratios measure a company's ability to meet its long-term debt obligations and assess its financial stability.

## Debt to Assets

**Formula:** Total Debt / Total Assets

**Interpretation:** Measures the percentage of a company's assets that are financed by debt. A lower ratio indicates a more financially stable company with lower risk.

**Example:** If a company has total debt of $400,000 and total assets of $1,000,000, its debt to assets ratio is 0.4 or 40%.

## Debt to Equity

**Formula:** Total Debt / Total Equity

**Interpretation:** Measures the relative proportion of shareholder equity and debt used to finance a company's assets. A lower ratio indicates lower financial risk.

**Example:** If a company has total debt of $400,000 and total equity of $600,000, its debt to equity ratio is 0.67.

## Interest Coverage Ratio

**Formula:** EBIT / Interest Expense

**Interpretation:** Measures a company's ability to pay interest on its debt. A higher ratio indicates that the company can more easily meet its interest obligations.

**Example:** If a company has EBIT of $200,000 and interest expense of $50,000, its interest coverage ratio is 4.0.

## Debt to EBITDA

**Formula:** Total Debt / EBITDA

**Interpretation:** Measures a company's ability to pay off its debt using its earnings. A lower ratio indicates that a company can pay off its debt more quickly.

**Example:** If a company has total debt of $400,000 and EBITDA of $200,000, its debt to EBITDA ratio is 2.0.

## Connections to Other Financial Statements:

- **Balance Sheet:** Solvency ratios use total debt, total assets, and total equity from the balance sheet.
- **Income Statement:** Interest coverage ratio uses EBIT from the income statement, and debt to EBITDA uses EBITDA, which is derived from the income statement.
- **Cash Flow Statement:** While not directly used in these ratios, strong operating cash flow improves a company's ability to service its debt.
"""
        
        self.ratio_details_text.insert(tk.END, details)
        self.ratio_details_text.config(state='disabled')
    
    def _show_efficiency_ratios(self):
        """Show efficiency ratios details."""
        self.ratio_details_text.config(state='normal')
        self.ratio_details_text.delete(1.0, tk.END)
        
        details = """
# Efficiency Ratios

Efficiency ratios measure how effectively a company uses its assets and manages its liabilities to generate revenue and profits.

## Asset Turnover

**Formula:** Revenue / Total Assets

**Interpretation:** Measures how efficiently a company is using its assets to generate revenue. A higher ratio indicates more efficient use of assets.

**Example:** If a company has revenue of $1,000,000 and total assets of $500,000, its asset turnover ratio is 2.0.

## Inventory Turnover

**Formula:** Cost of Goods Sold / Average Inventory

**Interpretation:** Measures how many times a company's inventory is sold and replaced over a period. A higher ratio indicates more efficient inventory management.

**Example:** If a company has COGS of $600,000 and average inventory of $100,000, its inventory turnover ratio is 6.0.

## Receivables Turnover

**Formula:** Revenue / Average Accounts Receivable

**Interpretation:** Measures how efficiently a company collects revenue from its credit customers. A higher ratio indicates more efficient collection of accounts receivable.

**Example:** If a company has revenue of $1,000,000 and average accounts receivable of $200,000, its receivables turnover ratio is 5.0.

## Days Sales Outstanding (DSO)

**Formula:** 365 / Receivables Turnover

**Interpretation:** Measures the average number of days it takes a company to collect payment after a sale is made. A lower DSO indicates more efficient collection of accounts receivable.

**Example:** If a company's receivables turnover ratio is 5.0, its DSO is 73 days.

## Days Inventory Outstanding (DIO)

**Formula:** 365 / Inventory Turnover

**Interpretation:** Measures the average number of days it takes a company to sell its inventory. A lower DIO indicates more efficient inventory management.

**Example:** If a company's inventory turnover ratio is 6.0, its DIO is 60.8 days.

## Connections to Other Financial Statements:

- **Income Statement:** Efficiency ratios use revenue and COGS from the income statement.
- **Balance Sheet:** Efficiency ratios use total assets, inventory, and accounts receivable from the balance sheet.
- **Cash Flow Statement:** Efficient management of assets, inventory, and accounts receivable improves operating cash flow.
"""
        
        self.ratio_details_text.insert(tk.END, details)
        self.ratio_details_text.config(state='disabled')
    
    def _show_valuation_ratios(self):
        """Show valuation ratios details."""
        self.ratio_details_text.config(state='normal')
        self.ratio_details_text.delete(1.0, tk.END)
        
        details = """
# Valuation Ratios

Valuation ratios measure the relative value of a company's stock compared to its financial performance or assets.

## Price-to-Earnings (P/E) Ratio

**Formula:** Share Price / Earnings Per Share

**Interpretation:** Measures how much investors are willing to pay for each dollar of earnings. A higher P/E ratio may indicate that investors expect higher earnings growth in the future.

**Example:** If a company's share price is $50 and its EPS is $5, its P/E ratio is 10.

## Price-to-Book (P/B) Ratio

**Formula:** Share Price / Book Value Per Share

**Interpretation:** Compares a company's market value to its book value. A lower P/B ratio may indicate that the stock is undervalued.

**Example:** If a company's share price is $50 and its book value per share is $25, its P/B ratio is 2.0.

## Price-to-Sales (P/S) Ratio

**Formula:** Market Capitalization / Revenue

**Interpretation:** Compares a company's market value to its revenue. A lower P/S ratio may indicate that the stock is undervalued.

**Example:** If a company's market cap is $500 million and its revenue is $100 million, its P/S ratio is 5.0.

## Enterprise Value-to-EBITDA (EV/EBITDA)

**Formula:** Enterprise Value / EBITDA

**Interpretation:** Compares a company's enterprise value (market cap plus debt minus cash) to its earnings before interest, taxes, depreciation, and amortization. A lower ratio may indicate that the company is undervalued.

**Example:** If a company's EV is $600 million and its EBITDA is $100 million, its EV/EBITDA ratio is 6.0.

## Enterprise Value-to-Revenue (EV/Revenue)

**Formula:** Enterprise Value / Revenue

**Interpretation:** Compares a company's enterprise value to its revenue. A lower ratio may indicate that the company is undervalued.

**Example:** If a company's EV is $600 million and its revenue is $200 million, its EV/Revenue ratio is 3.0.

## Connections to Other Financial Statements:

- **Income Statement:** Valuation ratios use earnings, EBITDA, and revenue from the income statement.
- **Balance Sheet:** Valuation ratios use book value from the balance sheet, and enterprise value calculations use debt and cash from the balance sheet.
- **Market Data:** Valuation ratios also use market data like share price and market capitalization, which are not found in financial statements.
"""
        
        self.ratio_details_text.insert(tk.END, details)
        self.ratio_details_text.config(state='disabled')
    
    def _create_visualization_tab(self):
        """Create the visualization tab."""
        # Create a frame for the visualization
        visualization_frame = ttk.Frame(self.visualization_tab, padding=10)
        visualization_frame.pack(fill='both', expand=True)
        
        # Create a frame for the visualization controls
        controls_frame = ttk.LabelFrame(visualization_frame, text="Visualization Controls", padding=10)
        controls_frame.pack(fill='x', padx=10, pady=10)
        
        # Create a grid for the controls
        controls_grid = ttk.Frame(controls_frame)
        controls_grid.pack(fill='x', padx=10, pady=10)
        
        # Create radio buttons for visualization type
        ttk.Label(controls_grid, text="Visualization Type:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        
        self.viz_type_var = tk.StringVar(value="income_statement")
        
        viz_types = [
            ("Income Statement", "income_statement"),
            ("Balance Sheet", "balance_sheet"),
            ("Cash Flow", "cash_flow"),
            ("Key Ratios", "key_ratios")
        ]
        
        for i, (text, value) in enumerate(viz_types):
            ttk.Radiobutton(
                controls_grid, 
                text=text, 
                value=value, 
                variable=self.viz_type_var
            ).grid(row=0, column=i+1, padx=5, pady=5)
        
        # Create a button to generate the visualization
        generate_button = ttk.Button(
            controls_grid, 
            text="Generate Visualization", 
            command=self._generate_visualization
        )
        generate_button.grid(row=0, column=len(viz_types)+1, padx=5, pady=5)
        
        # Create a frame for the visualization
        self.viz_frame = ttk.LabelFrame(visualization_frame, text="Visualization", padding=10)
        self.viz_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Generate the default visualization
        self._generate_visualization()
    
    def _generate_visualization(self):
        """Generate a visualization based on the selected type."""
        # Clear the visualization frame
        for widget in self.viz_frame.winfo_children():
            widget.destroy()
        
        # Get the selected visualization type
        viz_type = self.viz_type_var.get()
        
        # Create a figure and axis
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Generate the visualization based on the selected type
        if viz_type == "income_statement":
            self._generate_income_statement_viz(ax)
        elif viz_type == "balance_sheet":
            self._generate_balance_sheet_viz(ax)
        elif viz_type == "cash_flow":
            self._generate_cash_flow_viz(ax)
        elif viz_type == "key_ratios":
            self._generate_key_ratios_viz(ax)
        
        # Create a canvas to display the figure
        canvas = FigureCanvasTkAgg(fig, master=self.viz_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)
    
    def _generate_income_statement_viz(self, ax):
        """Generate an income statement visualization."""
        # Get the data
        data = self.current_data
        
        # Create the data for the visualization
        labels = ['Revenue', 'COGS', 'Operating Expenses', 'Interest Expense', 'Income Tax', 'Net Income']
        values = [
            data.revenue,
            data.cogs,
            data.operating_expenses,
            data.interest_expense,
            data.income_before_tax * data.tax_rate,
            data.net_income
        ]
        
        # Create the bar chart
        bars = ax.bar(labels, values, color=['#4CAF50', '#F44336', '#F44336', '#F44336', '#F44336', '#2196F3'])
        
        # Add data labels
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 5000,
                    f'${height:,.0f}',
                    ha='center', va='bottom', rotation=0)
        
        # Set the title and labels
        ax.set_title('Income Statement Overview')
        ax.set_ylabel('Amount ($)')
        
        # Add a grid
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        
        # Add a waterfall chart explanation
        ax.text(0.5, -0.15, 
                'Note: Revenue (green) is the starting point. Expenses (red) reduce the total. Net Income (blue) is the final result.',
                ha='center', va='center', transform=ax.transAxes)
    
    def _generate_balance_sheet_viz(self, ax):
        """Generate a balance sheet visualization."""
        # Get the data
        data = self.current_data
        
        # Calculate totals
        total_current_assets = data.cash + data.accounts_receivable + data.inventory + data.prepaid_expenses
        total_non_current_assets = data.property_plant_equipment - data.accumulated_depreciation + data.intangible_assets + data.goodwill + data.long_term_investments
        total_assets = total_current_assets + total_non_current_assets
        
        total_current_liabilities = data.accounts_payable + data.accrued_expenses + data.short_term_debt + data.deferred_revenue
        total_non_current_liabilities = data.long_term_debt + data.deferred_tax_liabilities
        total_liabilities = total_current_liabilities + total_non_current_liabilities
        
        total_equity = data.common_stock + data.additional_paid_in_capital + data.retained_earnings - data.treasury_stock + data.accumulated_other_comprehensive_income
        
        # Create the data for the visualization
        labels = ['Current Assets', 'Non-Current Assets', 'Current Liabilities', 'Non-Current Liabilities', 'Equity']
        values = [total_current_assets, total_non_current_assets, total_current_liabilities, total_non_current_liabilities, total_equity]
        colors = ['#4CAF50', '#8BC34A', '#F44336', '#E57373', '#2196F3']
        
        # Create the bar chart
        bars = ax.bar(labels, values, color=colors)
        
        # Add data labels
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 5000,
                    f'${height:,.0f}',
                    ha='center', va='bottom', rotation=0)
        
        # Set the title and labels
        ax.set_title('Balance Sheet Overview')
        ax.set_ylabel('Amount ($)')
        
        # Add a grid
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        
        # Add a note about the accounting equation
        ax.text(0.5, -0.15, 
                f'Accounting Equation: Assets (${total_assets:,.0f}) = Liabilities (${total_liabilities:,.0f}) + Equity (${total_equity:,.0f})',
                ha='center', va='center', transform=ax.transAxes)
    
    def _generate_cash_flow_viz(self, ax):
        """Generate a cash flow visualization."""
        # Get the data
        data = self.current_data
        
        # Calculate cash flows
        operating_cash_flow = data.net_income + data.depreciation_amortization - data.accounts_receivable_change - data.inventory_change + data.accounts_payable_change + data.accrued_expenses_change + data.deferred_revenue_change
        
        investing_cash_flow = -data.capital_expenditures - data.acquisitions + data.investments_sold + data.other_investing
        
        financing_cash_flow = data.debt_issuance - data.debt_repayment - data.dividends_paid + data.stock_issuance - data.stock_repurchase + data.other_financing
        
        net_change_in_cash = operating_cash_flow + investing_cash_flow + financing_cash_flow
        
        ending_cash = data.beginning_cash_balance + net_change_in_cash
        
        # Create the data for the visualization
        labels = ['Beginning Cash', 'Operating CF', 'Investing CF', 'Financing CF', 'Ending Cash']
        values = [data.beginning_cash_balance, operating_cash_flow, investing_cash_flow, financing_cash_flow, ending_cash]
        colors = ['#9E9E9E', '#4CAF50', '#F44336' if investing_cash_flow < 0 else '#4CAF50', '#2196F3', '#9E9E9E']
        
        # Create the bar chart
        bars = ax.bar(labels, values, color=colors)
        
        # Add data labels
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 5000 if height >= 0 else height - 20000,
                    f'${height:,.0f}',
                    ha='center', va='bottom' if height >= 0 else 'top', rotation=0)
        
        # Set the title and labels
        ax.set_title('Cash Flow Overview')
        ax.set_ylabel('Amount ($)')
        
        # Add a grid
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        
        # Add a note about the cash flow
        ax.text(0.5, -0.15, 
                f'Net Change in Cash: ${net_change_in_cash:,.0f} = Operating CF (${operating_cash_flow:,.0f}) + Investing CF (${investing_cash_flow:,.0f}) + Financing CF (${financing_cash_flow:,.0f})',
                ha='center', va='center', transform=ax.transAxes)
    
    def _generate_key_ratios_viz(self, ax):
        """Generate a key ratios visualization."""
        # Get the data
        data = self.current_data
        
        # Calculate ratios
        from analysis.ratios import FinancialRatios
        ratios = FinancialRatios(data).get_all_ratios()
        
        # Create the data for the visualization
        labels = ['P/E Ratio', 'EV/EBITDA', 'Debt/Equity', 'Current Ratio', 'Net Margin']
        values = [
            ratios['valuation']['pe_ratio'],
            ratios['valuation']['ev_to_ebitda'],
            ratios['solvency']['debt_to_equity'],
            ratios['liquidity']['current_ratio'],
            ratios['profitability']['net_margin']
        ]
        
        # Create the bar chart
        bars = ax.bar(labels, values, color='#2196F3')
        
        # Add data labels
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                    f'{height:.2f}',
                    ha='center', va='bottom', rotation=0)
        
        # Set the title and labels
        ax.set_title('Key Financial Ratios')
        ax.set_ylabel('Ratio Value')
        
        # Add a grid
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        
        # Add a note about the ratios
        ax.text(0.5, -0.15, 
                'Note: These ratios help assess valuation (P/E, EV/EBITDA), solvency (Debt/Equity), liquidity (Current Ratio), and profitability (Net Margin).',
                ha='center', va='center', transform=ax.transAxes)