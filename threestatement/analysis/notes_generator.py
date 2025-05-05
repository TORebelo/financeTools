"""
Enhanced module for generating explanatory notes about financial statement changes.
"""

class NotesGenerator:
    """
    Enhanced class to generate explanatory notes about financial statement changes.
    """
    
    def __init__(self, comparison):
        """
        Initialize with a financial comparison.
        
        Args:
            comparison: FinancialComparison instance
        """
        self.comparison = comparison
    
    def generate_income_statement_notes(self):
        """
        Generate notes explaining changes in the income statement.
        
        Returns:
            String with explanatory notes
        """
        notes = []
        income_data = self.comparison.get_income_statement_comparison()
        
        # Revenue notes
        if abs(income_data['revenue']['percentage']) >= 0.01:
            direction = "increased" if income_data['revenue']['change'] > 0 else "decreased"
            notes.append(f"Revenue {direction} by {abs(income_data['revenue']['percentage']):.1%} " +
                        f"(${abs(income_data['revenue']['change']):,.0f}), primarily due to " +
                        self._get_revenue_change_reason(income_data['revenue']['percentage']))
            
            # Show correlations
            notes.append("  - Impact: This change in revenue directly affects gross profit, operating income, and net income.")
            notes.append("  - Balance Sheet Effect: May increase accounts receivable if sales are on credit.")
            notes.append("  - Cash Flow Effect: Will increase operating cash flow as receivables are collected.")
        
        # Gross profit notes
        if abs(income_data['gross_profit']['percentage']) >= 0.01:
            direction = "increased" if income_data['gross_profit']['change'] > 0 else "decreased"
            notes.append(f"Gross profit {direction} by {abs(income_data['gross_profit']['percentage']):.1%} " +
                        f"(${abs(income_data['gross_profit']['change']):,.0f}), resulting in a " +
                        f"gross margin of {income_data['gross_profit']['forecast'] / income_data['revenue']['forecast']:.1%} " +
                        f"compared to {income_data['gross_profit']['base'] / income_data['revenue']['base']:.1%} in the prior year.")
            
            # Show correlations
            notes.append("  - Impact: Changes in gross profit directly affect operating income and net income.")
            notes.append("  - Valuation Effect: Improved gross margins often lead to higher valuation multiples.")
        
        # Operating expenses notes
        if abs(income_data['operating_expenses']['percentage']) >= 0.01:
            direction = "increased" if income_data['operating_expenses']['change'] > 0 else "decreased"
            notes.append(f"Operating expenses {direction} by {abs(income_data['operating_expenses']['percentage']):.1%} " +
                        f"(${abs(income_data['operating_expenses']['change']):,.0f}), primarily due to " +
                        self._get_opex_change_reason(income_data['operating_expenses']['percentage']))
            
            # Show correlations
            notes.append("  - Impact: Changes in operating expenses directly affect operating income and net income.")
            notes.append("  - Cash Flow Effect: Most operating expenses reduce operating cash flow.")
            notes.append("  - Balance Sheet Effect: May increase accrued expenses if not paid immediately.")
        
        # Operating income notes
        if abs(income_data['operating_income']['percentage']) >= 0.01:
            direction = "increased" if income_data['operating_income']['change'] > 0 else "decreased"
            notes.append(f"Operating income {direction} by {abs(income_data['operating_income']['percentage']):.1%} " +
                        f"(${abs(income_data['operating_income']['change']):,.0f}), resulting in an " +
                        f"operating margin of {income_data['operating_income']['forecast'] / income_data['revenue']['forecast']:.1%} " +
                        f"compared to {income_data['operating_income']['base'] / income_data['revenue']['base']:.1%} in the prior year.")
            
            # Show correlations
            notes.append("  - Impact: Operating income is a key metric for evaluating operational efficiency.")
            notes.append("  - Valuation Effect: Higher operating margins often lead to higher EV/EBITDA multiples.")
        
        # Interest expense notes
        if abs(income_data['interest_expense']['percentage']) >= 0.01:
            direction = "increased" if income_data['interest_expense']['change'] > 0 else "decreased"
            notes.append(f"Interest expense {direction} by {abs(income_data['interest_expense']['percentage']):.1%} " +
                        f"(${abs(income_data['interest_expense']['change']):,.0f}), primarily due to " +
                        self._get_interest_change_reason(income_data['interest_expense']['percentage']))
            
            # Show correlations
            notes.append("  - Impact: Changes in interest expense directly affect income before tax and net income.")
            notes.append("  - Cash Flow Effect: Interest payments reduce operating cash flow.")
            notes.append("  - Balance Sheet Effect: Related to changes in debt levels.")
        
        # Net income notes
        if abs(income_data['net_income']['percentage']) >= 0.01:
            direction = "increased" if income_data['net_income']['change'] > 0 else "decreased"
            notes.append(f"Net income {direction} by {abs(income_data['net_income']['percentage']):.1%} " +
                        f"(${abs(income_data['net_income']['change']):,.0f}), resulting in a " +
                        f"net margin of {income_data['net_income']['forecast'] / income_data['revenue']['forecast']:.1%} " +
                        f"compared to {income_data['net_income']['base'] / income_data['revenue']['base']:.1%} in the prior year.")
            
            # Show correlations
            notes.append("  - Impact: Net income increases retained earnings on the balance sheet.")
            notes.append("  - Shareholder Effect: Affects earnings per share and potential dividend payments.")
            notes.append("  - Valuation Effect: Directly impacts P/E ratio and other earnings-based valuation metrics.")
        
        # If no significant changes
        if not notes:
            notes.append("No significant changes in the income statement compared to the prior year.")
        
        return "\n\n".join(notes)
    
    def generate_balance_sheet_notes(self):
        """
        Generate notes explaining changes in the balance sheet.
        
        Returns:
            String with explanatory notes
        """
        notes = []
        balance_data = self.comparison.get_balance_sheet_comparison()
        
        # Assets notes
        asset_notes = []
        
        # Cash notes
        if abs(balance_data['cash']['percentage']) >= 0.01:
            direction = "increased" if balance_data['cash']['change'] > 0 else "decreased"
            asset_notes.append(f"Cash and cash equivalents {direction} by {abs(balance_data['cash']['percentage']):.1%} " +
                             f"(${abs(balance_data['cash']['change']):,.0f}), primarily due to " +
                             self._get_cash_change_reason(balance_data['cash']['percentage']))
            
            # Show correlations
            asset_notes.append("  - Impact: Changes in cash affect liquidity ratios like current ratio and cash ratio.")
            asset_notes.append("  - Enterprise Value Effect: Higher cash reduces enterprise value (EV = Market Cap + Debt - Cash).")
        
        # Accounts receivable notes
        if abs(balance_data['accounts_receivable']['percentage']) >= 0.01:
            direction = "increased" if balance_data['accounts_receivable']['change'] > 0 else "decreased"
            asset_notes.append(f"Accounts receivable {direction} by {abs(balance_data['accounts_receivable']['percentage']):.1%} " +
                             f"(${abs(balance_data['accounts_receivable']['change']):,.0f}), reflecting " +
                             self._get_ar_change_reason(balance_data['accounts_receivable']['percentage']))
            
            # Show correlations
            asset_notes.append("  - Impact: Changes in accounts receivable affect working capital and cash conversion cycle.")
            asset_notes.append("  - Cash Flow Effect: Increases in accounts receivable reduce operating cash flow.")
        
        # Inventory notes
        if abs(balance_data['inventory']['percentage']) >= 0.01:
            direction = "increased" if balance_data['inventory']['change'] > 0 else "decreased"
            asset_notes.append(f"Inventory {direction} by {abs(balance_data['inventory']['percentage']):.1%} " +
                             f"(${abs(balance_data['inventory']['change']):,.0f}), primarily due to " +
                             self._get_inventory_change_reason(balance_data['inventory']['percentage']))
            
            # Show correlations
            asset_notes.append("  - Impact: Changes in inventory affect working capital and inventory turnover ratio.")
            asset_notes.append("  - Cash Flow Effect: Increases in inventory reduce operating cash flow.")
        
        # PP&E notes
        if abs(balance_data['property_plant_equipment']['percentage']) >= 0.01:
            direction = "increased" if balance_data['property_plant_equipment']['change'] > 0 else "decreased"
            asset_notes.append(f"Property, plant, and equipment {direction} by {abs(balance_data['property_plant_equipment']['percentage']):.1%} " +
                             f"(${abs(balance_data['property_plant_equipment']['change']):,.0f}), primarily due to " +
                             self._get_ppe_change_reason(balance_data['property_plant_equipment']['percentage']))
            
            # Show correlations
            asset_notes.append("  - Impact: Changes in PP&E affect asset turnover ratio and return on assets.")
            asset_notes.append("  - Cash Flow Effect: Capital expenditures reduce investing cash flow.")
            asset_notes.append("  - Income Statement Effect: Will increase depreciation expense in future periods.")
        
        # Total assets notes
        if abs(balance_data['total_assets']['percentage']) >= 0.01:
            direction = "increased" if balance_data['total_assets']['change'] > 0 else "decreased"
            asset_notes.append(f"Total assets {direction} by {abs(balance_data['total_assets']['percentage']):.1%} " +
                             f"(${abs(balance_data['total_assets']['change']):,.0f}).")
            
            # Show correlations
            asset_notes.append("  - Impact: Changes in total assets affect return on assets and asset turnover ratios.")
        
        if asset_notes:
            notes.append("Assets:\n" + "\n".join(asset_notes))
        
        # Liabilities notes
        liability_notes = []
        
        # Accounts payable notes
        if abs(balance_data['accounts_payable']['percentage']) >= 0.01:
            direction = "increased" if balance_data['accounts_payable']['change'] > 0 else "decreased"
            liability_notes.append(f"Accounts payable {direction} by {abs(balance_data['accounts_payable']['percentage']):.1%} " +
                                 f"(${abs(balance_data['accounts_payable']['change']):,.0f}), primarily due to " +
                                 self._get_ap_change_reason(balance_data['accounts_payable']['percentage']))
            
            # Show correlations
            liability_notes.append("  - Impact: Changes in accounts payable affect working capital and cash conversion cycle.")
            liability_notes.append("  - Cash Flow Effect: Increases in accounts payable increase operating cash flow.")
        
        # Long-term debt notes
        if abs(balance_data['long_term_debt']['percentage']) >= 0.01:
            direction = "increased" if balance_data['long_term_debt']['change'] > 0 else "decreased"
            liability_notes.append(f"Long-term debt {direction} by {abs(balance_data['long_term_debt']['percentage']):.1%} " +
                                 f"(${abs(balance_data['long_term_debt']['change']):,.0f}), primarily due to " +
                                 self._get_debt_change_reason(balance_data['long_term_debt']['percentage']))
            
            # Show correlations
            liability_notes.append("  - Impact: Changes in debt affect debt-to-equity ratio and interest coverage ratio.")
            liability_notes.append("  - Cash Flow Effect: New debt increases financing cash flow; repayments decrease it.")
            liability_notes.append("  - Income Statement Effect: Will affect interest expense in future periods.")
            liability_notes.append("  - Enterprise Value Effect: Higher debt increases enterprise value.")
        
        # Total liabilities notes
        if abs(balance_data['total_liabilities']['percentage']) >= 0.01:
            direction = "increased" if balance_data['total_liabilities']['change'] > 0 else "decreased"
            liability_notes.append(f"Total liabilities {direction} by {abs(balance_data['total_liabilities']['percentage']):.1%} " +
                                 f"(${abs(balance_data['total_liabilities']['change']):,.0f}).")
            
            # Show correlations
            liability_notes.append("  - Impact: Changes in total liabilities affect debt-to-assets ratio.")
        
        if liability_notes:
            notes.append("Liabilities:\n" + "\n".join(liability_notes))
        
        # Equity notes
        equity_notes = []
        
        # Retained earnings notes
        if abs(balance_data['retained_earnings']['percentage']) >= 0.01:
            direction = "increased" if balance_data['retained_earnings']['change'] > 0 else "decreased"
            equity_notes.append(f"Retained earnings {direction} by {abs(balance_data['retained_earnings']['percentage']):.1%} " +
                              f"(${abs(balance_data['retained_earnings']['change']):,.0f}), primarily due to " +
                              self._get_retained_earnings_change_reason(balance_data['retained_earnings']['percentage']))
            
            # Show correlations
            equity_notes.append("  - Impact: Retained earnings increase from net income and decrease from dividends.")
            equity_notes.append("  - Shareholder Effect: Represents accumulated profits not distributed to shareholders.")
        
        # Total equity notes
        if abs(balance_data['total_equity']['percentage']) >= 0.01:
            direction = "increased" if balance_data['total_equity']['change'] > 0 else "decreased"
            equity_notes.append(f"Total equity {direction} by {abs(balance_data['total_equity']['percentage']):.1%} " +
                              f"(${abs(balance_data['total_equity']['change']):,.0f}).")
            
            # Show correlations
            equity_notes.append("  - Impact: Changes in equity affect return on equity and debt-to-equity ratios.")
            equity_notes.append("  - Book Value Effect: Directly impacts book value per share.")
        
        if equity_notes:
            notes.append("Equity:\n" + "\n".join(equity_notes))
        
        # If no significant changes
        if not notes:
            notes.append("No significant changes in the balance sheet compared to the prior year.")
        
        return "\n\n".join(notes)
    
    def generate_cash_flow_notes(self):
        """
        Generate notes explaining changes in the cash flow statement.
        
        Returns:
            String with explanatory notes
        """
        notes = []
        cash_flow_data = self.comparison.get_cash_flow_comparison()
        
        # Operating cash flow notes
        if abs(cash_flow_data['operating_cash_flow']['percentage']) >= 0.01:
            direction = "increased" if cash_flow_data['operating_cash_flow']['change'] > 0 else "decreased"
            notes.append(f"Cash flow from operating activities {direction} by {abs(cash_flow_data['operating_cash_flow']['percentage']):.1%} " +
                        f"(${abs(cash_flow_data['operating_cash_flow']['change']):,.0f}), primarily due to " +
                        self._get_operating_cf_change_reason(cash_flow_data['operating_cash_flow']['percentage']))
            
            # Show correlations
            notes.append("  - Impact: Operating cash flow is critical for sustainable business operations.")
            notes.append("  - Balance Sheet Effect: Directly increases cash and cash equivalents.")
            notes.append("  - Financial Health: Strong operating cash flow indicates healthy core business operations.")
        
        # Investing cash flow notes
        if abs(cash_flow_data['investing_cash_flow']['percentage']) >= 0.01:
            direction = "increased" if cash_flow_data['investing_cash_flow']['change'] > 0 else "decreased"
            notes.append(f"Cash flow from investing activities {direction} by {abs(cash_flow_data['investing_cash_flow']['percentage']):.1%} " +
                        f"(${abs(cash_flow_data['investing_cash_flow']['change']):,.0f}), primarily due to " +
                        self._get_investing_cf_change_reason(cash_flow_data['investing_cash_flow']['percentage']))
            
            # Show correlations
            notes.append("  - Impact: Investing cash flow reflects capital expenditures and investment activities.")
            notes.append("  - Balance Sheet Effect: Capital expenditures increase PP&E assets.")
            notes.append("  - Growth Indicator: High capital expenditures may indicate investment in future growth.")
        
        # Financing cash flow notes
        if abs(cash_flow_data['financing_cash_flow']['percentage']) >= 0.01:
            direction = "increased" if cash_flow_data['financing_cash_flow']['change'] > 0 else "decreased"
            notes.append(f"Cash flow from financing activities {direction} by {abs(cash_flow_data['financing_cash_flow']['percentage']):.1%} " +
                        f"(${abs(cash_flow_data['financing_cash_flow']['change']):,.0f}), primarily due to " +
                        self._get_financing_cf_change_reason(cash_flow_data['financing_cash_flow']['percentage']))
            
            # Show correlations
            notes.append("  - Impact: Financing cash flow reflects debt and equity financing activities.")
            notes.append("  - Balance Sheet Effect: Affects debt levels and equity accounts.")
            notes.append("  - Capital Structure: Changes in financing activities impact the company's capital structure.")
        
        # Net change in cash notes
        if abs(cash_flow_data['net_change_in_cash']['percentage']) >= 0.01:
            direction = "increased" if cash_flow_data['net_change_in_cash']['change'] > 0 else "decreased"
            notes.append(f"Net change in cash {direction} by {abs(cash_flow_data['net_change_in_cash']['percentage']):.1%} " +
                        f"(${abs(cash_flow_data['net_change_in_cash']['change']):,.0f}).")
            
            # Show correlations
            notes.append("  - Impact: Net change in cash directly affects the cash balance on the balance sheet.")
            notes.append("  - Liquidity Effect: Changes in cash impact liquidity ratios and financial flexibility.")
        
        # If no significant changes
        if not notes:
            notes.append("No significant changes in the cash flow statement compared to the prior year.")
        
        return "\n\n".join(notes)
    
    def generate_comprehensive_notes(self):
        """
        Generate comprehensive notes explaining changes across all financial statements.
        
        Returns:
            String with comprehensive explanatory notes
        """
        income_notes = self.generate_income_statement_notes()
        balance_notes = self.generate_balance_sheet_notes()
        cash_flow_notes = self.generate_cash_flow_notes()
        
        # Generate correlation notes between statements
        correlation_notes = self._generate_cross_statement_correlations()
        
        return f"""
# Management Discussion and Analysis

## Income Statement
{income_notes}

## Balance Sheet
{balance_notes}

## Cash Flow Statement
{cash_flow_notes}

## Cross-Statement Correlations
{correlation_notes}

## Summary
The financial projections reflect management's expectations for the upcoming fiscal year based on current market conditions, historical performance, and strategic initiatives. The assumptions used in these projections are subject to various risks and uncertainties that could cause actual results to differ materially from those projected.
"""
    
    def _generate_cross_statement_correlations(self):
        """
        Generate notes explaining correlations between different financial statements.
        
        Returns:
            String with correlation notes
        """
        notes = []
        
        # Revenue to accounts receivable correlation
        revenue_change = self.comparison.changes.get('revenue', 0)
        ar_change = self.comparison.changes.get('accounts_receivable', 0)
        
        if abs(revenue_change) > 0 and abs(ar_change) > 0:
            if (revenue_change > 0 and ar_change > 0) or (revenue_change < 0 and ar_change < 0):
                notes.append("Revenue and accounts receivable are moving in the same direction, which is consistent with business growth or contraction.")
            else:
                notes.append("Revenue and accounts receivable are moving in opposite directions, which may indicate changes in collection efficiency or credit policies.")
        
        # Net income to retained earnings correlation
        net_income_change = self.comparison.changes.get('net_income', 0)
        retained_earnings_change = self.comparison.changes.get('retained_earnings', 0)
        dividends_paid = self.comparison.forecast_data.dividends_paid
        
        if abs(net_income_change) > 0 and abs(retained_earnings_change) > 0:
            notes.append(f"Net income of ${self.comparison.forecast_data.net_income:,.0f} contributes to the change in retained earnings, adjusted for dividends paid of ${dividends_paid:,.0f}.")
        
        # Capital expenditures to PP&E correlation
        capex = self.comparison.forecast_data.capital_expenditures
        ppe_change = self.comparison.changes.get('property_plant_equipment', 0)
        
        if capex > 0 and ppe_change > 0:
            notes.append(f"Capital expenditures of ${capex:,.0f} are reflected in the increase in property, plant, and equipment, before accounting for depreciation.")
        
        # Debt changes to interest expense correlation
        debt_change = self.comparison.changes.get('long_term_debt', 0) + self.comparison.changes.get('short_term_debt', 0)
        interest_change = self.comparison.changes.get('interest_expense', 0)
        
        if abs(debt_change) > 0 and abs(interest_change) > 0:
            if (debt_change > 0 and interest_change > 0) or (debt_change < 0 and interest_change < 0):
                notes.append("Changes in debt levels are reflected in corresponding changes to interest expense.")
            else:
                notes.append("Changes in debt levels and interest expense are moving in opposite directions, which may indicate refinancing at different interest rates.")
        
        # Cash flow to cash balance correlation
        ocf = self.comparison.forecast_data.net_income + self.comparison.forecast_data.depreciation_amortization
        icf = -self.comparison.forecast_data.capital_expenditures
        fcf = self.comparison.forecast_data.debt_issuance - self.comparison.forecast_data.debt_repayment
        cash_change = self.comparison.changes.get('cash', 0)
        
        notes.append(f"The net change in cash of ${cash_change:,.0f} is the result of operating cash flow (${ocf:,.0f}), investing cash flow (${icf:,.0f}), and financing cash flow (${fcf:,.0f}).")
        
        # Share issuance/repurchase to equity correlation
        share_issuance = self.comparison.forecast_data.stock_issuance
        share_repurchase = self.comparison.forecast_data.stock_repurchase
        equity_change = self.comparison.changes.get('total_equity', 0)
        
        if (share_issuance > 0 or share_repurchase > 0) and abs(equity_change) > 0:
            if share_issuance > 0:
                notes.append(f"Stock issuance of ${share_issuance:,.0f} contributes to the change in total equity.")
            if share_repurchase > 0:
                notes.append(f"Stock repurchase of ${share_repurchase:,.0f} reduces total equity.")
        
        # If no significant correlations
        if not notes:
            notes.append("No significant cross-statement correlations to highlight.")
        
        return "\n".join(notes)
    
    def _get_revenue_change_reason(self, percentage):
        """Generate reason for revenue change based on percentage."""
        if percentage > 0.15:
            return "significant market expansion and new product launches."
        elif percentage > 0.05:
            return "moderate growth in existing markets and increased customer demand."
        elif percentage < -0.15:
            return "challenging market conditions and decreased customer demand."
        elif percentage < -0.05:
            return "slight contraction in certain market segments."
        else:
            return "relatively stable market conditions."
    
    def _get_opex_change_reason(self, percentage):
        """Generate reason for operating expenses change based on percentage."""
        if percentage > 0.15:
            return "significant investments in research and development and marketing initiatives."
        elif percentage > 0.05:
            return "increased personnel costs and moderate expansion of operations."
        elif percentage < -0.15:
            return "major cost-cutting initiatives and operational restructuring."
        elif percentage < -0.05:
            return "improved operational efficiencies and targeted cost reductions."
        else:
            return "relatively stable operational costs."
    
    def _get_interest_change_reason(self, percentage):
        """Generate reason for interest expense change based on percentage."""
        if percentage > 0.15:
            return "increased debt levels and higher interest rates."
        elif percentage > 0.05:
            return "moderate increases in borrowing."
        elif percentage < -0.15:
            return "significant debt repayment and refinancing at lower interest rates."
        elif percentage < -0.05:
            return "partial debt repayment and favorable interest rate environment."
        else:
            return "relatively stable debt levels and interest rates."
    
    def _get_cash_change_reason(self, percentage):
        """Generate reason for cash change based on percentage."""
        if percentage > 0.15:
            return "strong operating cash flow and strategic cash management."
        elif percentage > 0.05:
            return "improved cash collection and moderate operating performance."
        elif percentage < -0.15:
            return "significant investments, debt repayment, and dividend payments."
        elif percentage < -0.05:
            return "moderate capital expenditures and shareholder returns."
        else:
            return "balanced cash inflows and outflows."
    
    def _get_ar_change_reason(self, percentage):
        """Generate reason for accounts receivable change based on percentage."""
        if percentage > 0.15:
            return "significant sales growth and extended payment terms for key customers."
        elif percentage > 0.05:
            return "moderate sales growth and typical payment patterns."
        elif percentage < -0.15:
            return "improved collection efforts and potential reduction in credit sales."
        elif percentage < -0.05:
            return "slightly improved collection efficiency."
        else:
            return "consistent credit policies and collection practices."
    
    def _get_inventory_change_reason(self, percentage):
        """Generate reason for inventory change based on percentage."""
        if percentage > 0.15:
            return "strategic inventory build-up in anticipation of increased demand."
        elif percentage > 0.05:
            return "moderate inventory increases aligned with sales growth expectations."
        elif percentage < -0.15:
            return "significant inventory reduction initiatives and improved inventory management."
        elif percentage < -0.05:
            return "slight improvements in inventory turnover and supply chain efficiency."
        else:
            return "stable inventory management practices."
    
    def _get_ppe_change_reason(self, percentage):
        """Generate reason for PP&E change based on percentage."""
        if percentage > 0.15:
            return "significant capital expenditures for expansion and modernization."
        elif percentage > 0.05:
            return "moderate investments in production capacity and infrastructure."
        elif percentage < -0.15:
            return "asset disposals and limited capital investment below depreciation levels."
        elif percentage < -0.05:
            return "selective asset rationalization and focused capital spending."
        else:
            return "maintenance capital expenditures approximately equal to depreciation."
    
    def _get_ap_change_reason(self, percentage):
        """Generate reason for accounts payable change based on percentage."""
        if percentage > 0.15:
            return "increased purchasing activity and negotiated extended payment terms."
        elif percentage > 0.05:
            return "moderate increases in procurement aligned with business growth."
        elif percentage < -0.15:
            return "accelerated supplier payments and potential early payment discounts."
        elif percentage < -0.05:
            return "slight reduction in purchasing activity or payment term adjustments."
        else:
            return "consistent supplier payment practices."
    
    def _get_debt_change_reason(self, percentage):
        """Generate reason for debt change based on percentage."""
        if percentage > 0.15:
            return "new debt issuance to fund strategic initiatives and capital investments."
        elif percentage > 0.05:
            return "moderate additional borrowing to support operations and growth."
        elif percentage < -0.15:
            return "significant debt repayment as part of deleveraging strategy."
        elif percentage < -0.05:
            return "scheduled debt repayments and modest deleveraging efforts."
        else:
            return "relatively stable debt levels with refinancing of maturing obligations."
    
    def _get_retained_earnings_change_reason(self, percentage):
        """Generate reason for retained earnings change based on percentage."""
        if percentage > 0.15:
            return "strong profitability and limited dividend distributions."
        elif percentage > 0.05:
            return "solid net income and balanced shareholder returns."
        elif percentage < -0.15:
            return "net losses or significant dividend payments exceeding current earnings."
        elif percentage < -0.05:
            return "modest profitability offset by dividend distributions."
        else:
            return "balanced earnings and shareholder returns."
    
    def _get_operating_cf_change_reason(self, percentage):
        """Generate reason for operating cash flow change based on percentage."""
        if percentage > 0.15:
            return "improved profitability and working capital management."
        elif percentage > 0.05:
            return "moderate earnings growth and stable working capital."
        elif percentage < -0.15:
            return "decreased profitability and increased working capital requirements."
        elif percentage < -0.05:
            return "slight earnings pressure and modest working capital increases."
        else:
            return "relatively stable earnings and working capital levels."
    
    def _get_investing_cf_change_reason(self, percentage):
        """Generate reason for investing cash flow change based on percentage."""
        if percentage > 0.15:
            return "reduced capital expenditures and potential asset sales."
        elif percentage > 0.05:
            return "moderately lower investment activity compared to prior year."
        elif percentage < -0.15:
            return "significant increases in capital expenditures and strategic investments."
        elif percentage < -0.05:
            return "modest increases in capital spending and investment activity."
        else:
            return "investment activity consistent with prior year levels."
    
    def _get_financing_cf_change_reason(self, percentage):
        """Generate reason for financing cash flow change based on percentage."""
        if percentage > 0.15:
            return "increased debt issuance or equity financing activities."
        elif percentage > 0.05:
            return "moderate increases in external financing."
        elif percentage < -0.15:
            return "significant debt repayment, share repurchases, or dividend increases."
        elif percentage < -0.05:
            return "modest increases in shareholder returns or debt service."
        else:
            return "financing activities consistent with prior year levels."