"""
Module for calculating financial ratios and metrics.
"""

class FinancialRatios:
    """
    Class to calculate financial ratios from financial data.
    """
    
    def __init__(self, financial_data):
        """
        Initialize with financial data.
        
        Args:
            financial_data: FinancialData instance
        """
        self.data = financial_data
    
    def get_profitability_ratios(self):
        """
        Calculate profitability ratios.
        
        Returns:
            Dictionary of profitability ratios
        """
        revenue = self.data.revenue
        if revenue == 0:
            return {
                'gross_margin': 0,
                'operating_margin': 0,
                'net_margin': 0,
                'return_on_assets': 0,
                'return_on_equity': 0
            }
        
        gross_profit = revenue - self.data.cogs
        operating_income = self.data.operating_income
        net_income = self.data.net_income
        total_assets = self.data.total_assets
        total_equity = self.data.total_equity
        
        return {
            'gross_margin': gross_profit / revenue if revenue > 0 else 0,
            'operating_margin': operating_income / revenue if revenue > 0 else 0,
            'net_margin': net_income / revenue if revenue > 0 else 0,
            'return_on_assets': net_income / total_assets if total_assets > 0 else 0,
            'return_on_equity': net_income / total_equity if total_equity > 0 else 0
        }
    
    def get_liquidity_ratios(self):
        """
        Calculate liquidity ratios.
        
        Returns:
            Dictionary of liquidity ratios
        """
        current_assets = (self.data.cash + self.data.accounts_receivable + 
                         self.data.inventory + self.data.prepaid_expenses)
        
        current_liabilities = (self.data.accounts_payable + self.data.accrued_expenses + 
                              self.data.short_term_debt + self.data.deferred_revenue)
        
        quick_assets = current_assets - self.data.inventory
        
        return {
            'current_ratio': current_assets / current_liabilities if current_liabilities > 0 else float('inf'),
            'quick_ratio': quick_assets / current_liabilities if current_liabilities > 0 else float('inf'),
            'cash_ratio': self.data.cash / current_liabilities if current_liabilities > 0 else float('inf')
        }
    
    def get_solvency_ratios(self):
        """
        Calculate solvency ratios.
        
        Returns:
            Dictionary of solvency ratios
        """
        total_debt = self.data.short_term_debt + self.data.long_term_debt
        total_assets = self.data.total_assets
        total_equity = self.data.total_equity
        ebitda = self.data.ebitda
        interest_expense = self.data.interest_expense
        
        return {
            'debt_to_assets': total_debt / total_assets if total_assets > 0 else 0,
            'debt_to_equity': total_debt / total_equity if total_equity > 0 else float('inf'),
            'interest_coverage': ebitda / interest_expense if interest_expense > 0 else float('inf'),
            'debt_to_ebitda': total_debt / ebitda if ebitda > 0 else float('inf')
        }
    
    def get_efficiency_ratios(self):
        """
        Calculate efficiency ratios.
        
        Returns:
            Dictionary of efficiency ratios
        """
        revenue = self.data.revenue
        total_assets = self.data.total_assets
        accounts_receivable = self.data.accounts_receivable
        inventory = self.data.inventory
        accounts_payable = self.data.accounts_payable
        cogs = self.data.cogs
        
        return {
            'asset_turnover': revenue / total_assets if total_assets > 0 else 0,
            'receivables_turnover': revenue / accounts_receivable if accounts_receivable > 0 else float('inf'),
            'inventory_turnover': cogs / inventory if inventory > 0 else float('inf'),
            'payables_turnover': cogs / accounts_payable if accounts_payable > 0 else float('inf'),
            'days_sales_outstanding': 365 * accounts_receivable / revenue if revenue > 0 else 0,
            'days_inventory_outstanding': 365 * inventory / cogs if cogs > 0 else 0,
            'days_payable_outstanding': 365 * accounts_payable / cogs if cogs > 0 else 0
        }
    
    def get_valuation_ratios(self):
        """
        Calculate valuation ratios.
        
        Returns:
            Dictionary of valuation ratios
        """
        market_cap = self.data.market_cap
        enterprise_value = self.data.enterprise_value
        net_income = self.data.net_income
        revenue = self.data.revenue
        ebitda = self.data.ebitda
        book_value = self.data.book_value
        earnings_per_share = self.data.earnings_per_share
        share_price = self.data.share_price
        
        return {
            'pe_ratio': share_price / earnings_per_share if earnings_per_share > 0 else float('inf'),
            'price_to_book': market_cap / book_value if book_value > 0 else float('inf'),
            'price_to_sales': market_cap / revenue if revenue > 0 else float('inf'),
            'ev_to_ebitda': enterprise_value / ebitda if ebitda > 0 else float('inf'),
            'ev_to_revenue': enterprise_value / revenue if revenue > 0 else float('inf'),
            'dividend_yield': self.data.dividends_declared / market_cap if market_cap > 0 else 0
        }
    
    def get_all_ratios(self):
        """
        Get all financial ratios.
        
        Returns:
            Dictionary of all financial ratios
        """
        return {
            'profitability': self.get_profitability_ratios(),
            'liquidity': self.get_liquidity_ratios(),
            'solvency': self.get_solvency_ratios(),
            'efficiency': self.get_efficiency_ratios(),
            'valuation': self.get_valuation_ratios()
        }