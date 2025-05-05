"""
Enhanced data models for financial statements with market metrics.
"""

class FinancialData:
    """
    Enhanced class to store and manage financial data for a company.
    """

    def __init__(self, company_name, reporting_period, reporting_date):
        """
        Initialize financial data.
        
        Args:
            company_name (str): Name of the company
            reporting_period (str): Reporting period (e.g., "Year Ended December 31, 2023")
            reporting_date (str): Date of the balance sheet (e.g., "December 31, 2023")
        """
        self.company_name = company_name
        self.reporting_period = reporting_period
        self.reporting_date = reporting_date
        
        # Income Statement Data
        self.revenue = 0
        self.cogs = 0
        self.operating_expenses = 0
        self.interest_expense = 0
        self.tax_rate = 0.21
        self.net_income = 0
        self.depreciation_amortization = 0
        self.goodwill_impairment = 0
        self.ppe_write_down = 0
        self.debt_write_down = 0
        self.stock_based_compensation = 0
        
        # Balance Sheet Data
        # Assets
        self.cash = 0
        self.accounts_receivable = 0
        self.inventory = 0
        self.prepaid_expenses = 0
        self.property_plant_equipment = 0
        self.accumulated_depreciation = 0
        self.intangible_assets = 0
        self.goodwill = 0
        self.long_term_investments = 0
        
        # Liabilities
        self.accounts_payable = 0
        self.accrued_expenses = 0
        self.short_term_debt = 0
        self.long_term_debt = 0
        self.deferred_revenue = 0
        self.deferred_tax_liabilities = 0
        
        # Equity
        self.common_stock = 0
        self.additional_paid_in_capital = 0
        self.retained_earnings = 0
        self.treasury_stock = 0
        self.accumulated_other_comprehensive_income = 0
        
        # Share Data
        self.shares_outstanding = 1000000
        self.share_price = 10.0
        self.par_value = 1.0
        
        # Cash Flow Data
        self.depreciation_amortization = 0
        self.accounts_receivable_change = 0
        self.inventory_change = 0
        self.accounts_payable_change = 0
        self.accrued_expenses_change = 0
        self.deferred_revenue_change = 0
        self.other_operating_adjustments = 0
        
        self.capital_expenditures = 0
        self.acquisitions = 0
        self.investments_sold = 0
        self.other_investing = 0
        
        self.debt_issuance = 0
        self.debt_repayment = 0
        self.dividends_paid = 0
        self.dividends_declared = 0
        self.stock_issuance = 0
        self.stock_repurchase = 0
        self.equity_bailout = 0
        self.other_financing = 0
        
        self.beginning_cash_balance = 0
        self.ending_cash_balance = 0
        
        # Derived Metrics (calculated when needed)
        self._market_cap = None
        self._enterprise_value = None
        self._ebitda = None

    def load_sample_data(self):
        """
        Load sample financial data for demonstration purposes.
        """
        # Income Statement Data
        self.revenue = 1000000
        self.cogs = 400000
        self.operating_expenses = 300000
        self.interest_expense = 50000
        self.tax_rate = 0.21
        self.depreciation_amortization = 60000
        self.stock_based_compensation = 100000
        
        # Calculate net income
        gross_profit = self.revenue - self.cogs
        operating_income = gross_profit - self.operating_expenses
        ebt = operating_income - self.interest_expense
        income_tax = ebt * self.tax_rate
        self.net_income = ebt - income_tax
        
        # Balance Sheet Data
        # Assets
        self.cash = 250000
        self.accounts_receivable = 150000
        self.inventory = 200000
        self.prepaid_expenses = 25000
        self.property_plant_equipment = 500000
        self.accumulated_depreciation = 100000
        self.intangible_assets = 75000
        self.goodwill = 100000
        self.long_term_investments = 200000
        
        # Liabilities
        self.accounts_payable = 120000
        self.accrued_expenses = 80000
        self.short_term_debt = 50000
        self.long_term_debt = 300000
        self.deferred_revenue = 30000
        self.deferred_tax_liabilities = 70000
        
        # Equity
        self.common_stock = 100000
        self.additional_paid_in_capital = 100000
        self.retained_earnings = 400000
        self.treasury_stock = 0
        self.accumulated_other_comprehensive_income = 100000
        
        # Share Data
        self.shares_outstanding = 100000
        self.share_price = 10.0
        self.par_value = 1.0
        
        # Cash Flow Data
        self.depreciation_amortization = 60000
        self.accounts_receivable_change = 20000
        self.inventory_change = -15000
        self.accounts_payable_change = 10000
        self.accrued_expenses_change = 5000
        self.deferred_revenue_change = 8000
        self.other_operating_adjustments = 0
        
        self.capital_expenditures = 80000
        self.acquisitions = 0
        self.investments_sold = 15000
        self.other_investing = 0
        
        self.debt_issuance = 100000
        self.debt_repayment = 50000
        self.dividends_paid = 30000
        self.dividends_declared = 30000
        self.stock_issuance = 0
        self.stock_repurchase = 20000
        self.equity_bailout = 0
        self.other_financing = 0
        
        self.beginning_cash_balance = 200000
        
        # Calculate ending cash balance
        operating_cash_flow = self.net_income + self.depreciation_amortization - self.accounts_receivable_change - self.inventory_change + self.accounts_payable_change + self.accrued_expenses_change + self.deferred_revenue_change
        investing_cash_flow = -self.capital_expenditures - self.acquisitions + self.investments_sold + self.other_investing
        financing_cash_flow = self.debt_issuance - self.debt_repayment - self.dividends_paid + self.stock_issuance - self.stock_repurchase + self.other_financing
        
        self.ending_cash_balance = self.beginning_cash_balance + operating_cash_flow + investing_cash_flow + financing_cash_flow
    
    @property
    def market_cap(self):
        """Calculate market capitalization."""
        return self.shares_outstanding * self.share_price
    
    @property
    def enterprise_value(self):
        """Calculate enterprise value."""
        return self.market_cap + self.short_term_debt + self.long_term_debt - self.cash
    
    @property
    def ebitda(self):
        """Calculate EBITDA."""
        return self.net_income + self.interest_expense + (self.net_income * self.tax_rate / (1 - self.tax_rate)) + self.depreciation_amortization
    
    @property
    def earnings_per_share(self):
        """Calculate earnings per share."""
        return self.net_income / self.shares_outstanding if self.shares_outstanding > 0 else 0
    
    @property
    def book_value(self):
        """Calculate book value."""
        return self.common_stock + self.additional_paid_in_capital + self.retained_earnings - self.treasury_stock + self.accumulated_other_comprehensive_income
    
    @property
    def book_value_per_share(self):
        """Calculate book value per share."""
        return self.book_value / self.shares_outstanding if self.shares_outstanding > 0 else 0
    
    @property
    def total_assets(self):
        """Calculate total assets."""
        return (self.cash + self.accounts_receivable + self.inventory + self.prepaid_expenses + 
                self.property_plant_equipment - self.accumulated_depreciation + 
                self.intangible_assets + self.goodwill + self.long_term_investments)
    
    @property
    def total_liabilities(self):
        """Calculate total liabilities."""
        return (self.accounts_payable + self.accrued_expenses + self.short_term_debt + 
                self.long_term_debt + self.deferred_revenue + self.deferred_tax_liabilities)
    
    @property
    def total_equity(self):
        """Calculate total equity."""
        return self.book_value
    
    @property
    def operating_income(self):
        """Calculate operating income."""
        return self.revenue - self.cogs - self.operating_expenses
    
    @property
    def income_before_tax(self):
        """Calculate income before tax."""
        return self.operating_income - self.interest_expense