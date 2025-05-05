"""
Module for financial forecasting.
"""

import copy

class FinancialForecast:
    """
    Class to handle financial forecasting.
    """
    
    def __init__(self, base_data):
        """
        Initialize with base financial data.
        
        Args:
            base_data: Current year's financial data
        """
        self.base_data = base_data
        
        # Initialize default assumptions
        self.assumptions = {
            # General assumptions
            'revenue_growth': 0.05,  # 5% revenue growth
            'cogs_percent': 0.40,    # COGS as % of revenue
            'opex_growth': 0.03,     # 3% operating expense growth
            'interest_rate': 0.05,   # 5% interest rate on debt
            'tax_rate': 0.21,        # 21% tax rate
            
            # Balance sheet assumptions
            'cash_percent': 0.25,    # Cash as % of revenue
            'ar_days': 55,           # Accounts receivable days
            'inventory_days': 73,    # Inventory days
            'ap_days': 45,           # Accounts payable days
            'capex_percent': 0.08,   # Capital expenditures as % of revenue
            'depreciation_rate': 0.10, # Depreciation rate for PP&E
            
            # Cash flow assumptions
            'dividend_payout': 0.15, # Dividend payout ratio
            'debt_repayment': 50000, # Annual debt repayment
            'new_borrowing': 0,      # New borrowing
        }
    
    def update_assumptions(self, new_assumptions):
        """
        Update forecast assumptions.
        
        Args:
            new_assumptions: Dictionary of new assumption values
        """
        self.assumptions.update(new_assumptions)
    
    def generate_forecast(self):
        """
        Generate forecasted financial statements based on assumptions.
        
        Returns:
            FinancialData: Forecasted financial data
        """
        # Create a new financial data object for the forecast
        forecast = copy.deepcopy(self.base_data)
        
        # Apply assumptions to generate forecast
        self._forecast_income_statement(forecast)
        self._forecast_balance_sheet(forecast)
        self._forecast_cash_flow(forecast)
        
        return forecast
    
    def _forecast_income_statement(self, forecast):
        """
        Forecast the income statement.
        
        Args:
            forecast: FinancialData object to update with forecasted values
        """
        # Revenue
        forecast.revenue = self.base_data.revenue * (1 + self.assumptions['revenue_growth'])
        
        # Cost of Goods Sold
        forecast.cogs = forecast.revenue * self.assumptions['cogs_percent']
        
        # Operating Expenses
        forecast.operating_expenses = self.base_data.operating_expenses * (1 + self.assumptions['opex_growth'])
        
        # Interest Expense
        total_debt = self.base_data.short_term_debt + self.base_data.long_term_debt
        forecast.interest_expense = total_debt * self.assumptions['interest_rate']
        
        # Tax Rate
        forecast.tax_rate = self.assumptions['tax_rate']
        
        # Calculate Net Income
        gross_profit = forecast.revenue - forecast.cogs
        operating_income = gross_profit - forecast.operating_expenses
        ebt = operating_income - forecast.interest_expense
        income_tax = ebt * forecast.tax_rate
        forecast.net_income = ebt - income_tax
    
    def _forecast_balance_sheet(self, forecast):
        """
        Forecast the balance sheet.
        
        Args:
            forecast: FinancialData object to update with forecasted values
        """
        # Assets
        # Cash
        forecast.cash = forecast.revenue * self.assumptions['cash_percent']
        
        # Accounts Receivable
        forecast.accounts_receivable = forecast.revenue * (self.assumptions['ar_days'] / 365)
        
        # Inventory
        forecast.inventory = forecast.cogs * (self.assumptions['inventory_days'] / 365)
        
        # Prepaid Expenses (assume same growth as revenue)
        forecast.prepaid_expenses = self.base_data.prepaid_expenses * (1 + self.assumptions['revenue_growth'])
        
        # Property, Plant & Equipment
        capex = forecast.revenue * self.assumptions['capex_percent']
        forecast.property_plant_equipment = self.base_data.property_plant_equipment + capex
        
        # Accumulated Depreciation
        new_depreciation = forecast.property_plant_equipment * self.assumptions['depreciation_rate']
        forecast.accumulated_depreciation = self.base_data.accumulated_depreciation + new_depreciation
        
        # Intangible Assets (assume no change unless specified)
        forecast.intangible_assets = self.base_data.intangible_assets
        
        # Liabilities
        # Accounts Payable
        forecast.accounts_payable = forecast.cogs * (self.assumptions['ap_days'] / 365)
        
        # Accrued Expenses (assume same growth as operating expenses)
        forecast.accrued_expenses = self.base_data.accrued_expenses * (1 + self.assumptions['opex_growth'])
        
        # Short-term Debt (assume same unless specified)
        forecast.short_term_debt = self.base_data.short_term_debt
        
        # Long-term Debt
        forecast.long_term_debt = self.base_data.long_term_debt - self.assumptions['debt_repayment'] + self.assumptions['new_borrowing']
        
        # Deferred Revenue (assume same growth as revenue)
        forecast.deferred_revenue = self.base_data.deferred_revenue * (1 + self.assumptions['revenue_growth'])
        
        # Equity
        # Common Stock (assume no change unless specified)
        forecast.common_stock = self.base_data.common_stock
        
        # Treasury Stock (assume no change unless specified)
        forecast.treasury_stock = self.base_data.treasury_stock
        
        # Retained Earnings
        dividends = forecast.net_income * self.assumptions['dividend_payout']
        forecast.retained_earnings = self.base_data.retained_earnings + forecast.net_income - dividends
    
    def _forecast_cash_flow(self, forecast):
        """
        Forecast the cash flow statement.
        
        Args:
            forecast: FinancialData object to update with forecasted values
        """
        # Operating Activities
        forecast.depreciation_amortization = forecast.property_plant_equipment * self.assumptions['depreciation_rate']
        
        # Changes in working capital
        forecast.accounts_receivable_change = forecast.accounts_receivable - self.base_data.accounts_receivable
        forecast.inventory_change = forecast.inventory - self.base_data.inventory
        forecast.accounts_payable_change = forecast.accounts_payable - self.base_data.accounts_payable
        forecast.accrued_expenses_change = forecast.accrued_expenses - self.base_data.accrued_expenses
        forecast.deferred_revenue_change = forecast.deferred_revenue - self.base_data.deferred_revenue
        
        # Investing Activities
        forecast.capital_expenditures = forecast.revenue * self.assumptions['capex_percent']
        forecast.acquisitions = 0  # Assume no acquisitions unless specified
        forecast.investments_sold = 0  # Assume no investments sold unless specified
        forecast.other_investing = 0  # Assume no other investing activities
        
        # Financing Activities
        forecast.debt_issuance = self.assumptions['new_borrowing']
        forecast.debt_repayment = self.assumptions['debt_repayment']
        forecast.dividends_paid = forecast.net_income * self.assumptions['dividend_payout']
        forecast.stock_issuance = 0  # Assume no stock issuance unless specified
        forecast.stock_repurchase = 0  # Assume no stock repurchase unless specified
        forecast.other_financing = 0  # Assume no other financing activities
        
        # Cash Balances
        forecast.beginning_cash_balance = self.base_data.ending_cash_balance
        
        # Calculate ending cash balance
        operating_cash_flow = forecast.net_income + forecast.depreciation_amortization - forecast.accounts_receivable_change - forecast.inventory_change + forecast.accounts_payable_change + forecast.accrued_expenses_change + forecast.deferred_revenue_change
        investing_cash_flow = -forecast.capital_expenditures - forecast.acquisitions + forecast.investments_sold + forecast.other_investing
        financing_cash_flow = forecast.debt_issuance - forecast.debt_repayment - forecast.dividends_paid + forecast.stock_issuance - forecast.stock_repurchase + forecast.other_financing
        
        forecast.ending_cash_balance = forecast.beginning_cash_balance + operating_cash_flow + investing_cash_flow + financing_cash_flow