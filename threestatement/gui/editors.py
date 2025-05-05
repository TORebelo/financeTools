"""
Module for editing financial statement assumptions.
"""

import tkinter as tk
from tkinter import ttk

class AssumptionsEditor:
    """
    Class to create an editor for forecast assumptions.
    """
    
    def __init__(self, parent, forecast_model, on_apply_callback=None):
        """
        Initialize the assumptions editor.
        
        Args:
            parent: Parent widget
            forecast_model: FinancialForecast instance
            on_apply_callback: Callback function to call when assumptions are applied
        """
        self.parent = parent
        self.forecast_model = forecast_model
        self.on_apply_callback = on_apply_callback
        
        # Create a new window
        self.window = tk.Toplevel(parent)
        self.window.title("Forecast Assumptions Editor")
        self.window.geometry("800x600")
        
        # Create a frame for the title
        title_frame = tk.Frame(self.window, pady=10)
        title_frame.pack(fill='x')
        
        # Add a title
        title_label = tk.Label(
            title_frame, 
            text="Edit Forecast Assumptions", 
            font=("Arial", 16, "bold")
        )
        title_label.pack()
        
        # Create a notebook (tabbed interface)
        self.notebook = ttk.Notebook(self.window)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Create tabs for different assumption categories
        self.general_tab = ttk.Frame(self.notebook)
        self.income_tab = ttk.Frame(self.notebook)
        self.balance_tab = ttk.Frame(self.notebook)
        self.cash_flow_tab = ttk.Frame(self.notebook)
        
        self.notebook.add(self.general_tab, text="General Assumptions")
        self.notebook.add(self.income_tab, text="Income Statement")
        self.notebook.add(self.balance_tab, text="Balance Sheet")
        self.notebook.add(self.cash_flow_tab, text="Cash Flow")
        
        # Create the assumption editors
        self._create_general_assumptions()
        self._create_income_assumptions()
        self._create_balance_assumptions()
        self._create_cash_flow_assumptions()
        
        # Create buttons frame
        buttons_frame = tk.Frame(self.window, pady=10)
        buttons_frame.pack(side=tk.BOTTOM, fill='x')
        
        # Add Apply and Cancel buttons
        apply_button = ttk.Button(
            buttons_frame, 
            text="Apply", 
            command=self._apply_assumptions
        )
        apply_button.pack(side=tk.RIGHT, padx=10)
        
        cancel_button = ttk.Button(
            buttons_frame, 
            text="Cancel", 
            command=self.window.destroy
        )
        cancel_button.pack(side=tk.RIGHT, padx=10)
        
        # Initialize the entry fields with current assumptions
        self._initialize_fields()
    
    def _create_general_assumptions(self):
        """Create the general assumptions tab."""
        frame = ttk.LabelFrame(self.general_tab, text="General Assumptions", padding=10)
        frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Revenue Growth
        ttk.Label(frame, text="Revenue Growth:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.revenue_growth = ttk.Entry(frame, width=10)
        self.revenue_growth.grid(row=0, column=1, sticky="w", padx=5, pady=5)
        ttk.Label(frame, text="% (e.g., 5 for 5%)").grid(row=0, column=2, sticky="w", padx=5, pady=5)
        
        # Tax Rate
        ttk.Label(frame, text="Tax Rate:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.tax_rate = ttk.Entry(frame, width=10)
        self.tax_rate.grid(row=1, column=1, sticky="w", padx=5, pady=5)
        ttk.Label(frame, text="% (e.g., 21 for 21%)").grid(row=1, column=2, sticky="w", padx=5, pady=5)
        
        # Interest Rate
        ttk.Label(frame, text="Interest Rate:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.interest_rate = ttk.Entry(frame, width=10)
        self.interest_rate.grid(row=2, column=1, sticky="w", padx=5, pady=5)
        ttk.Label(frame, text="% (e.g., 5 for 5%)").grid(row=2, column=2, sticky="w", padx=5, pady=5)
    
    def _create_income_assumptions(self):
        """Create the income statement assumptions tab."""
        frame = ttk.LabelFrame(self.income_tab, text="Income Statement Assumptions", padding=10)
        frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # COGS as % of Revenue
        ttk.Label(frame, text="COGS as % of Revenue:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.cogs_percent = ttk.Entry(frame, width=10)
        self.cogs_percent.grid(row=0, column=1, sticky="w", padx=5, pady=5)
        ttk.Label(frame, text="% (e.g., 40 for 40%)").grid(row=0, column=2, sticky="w", padx=5, pady=5)
        
        # Operating Expenses Growth
        ttk.Label(frame, text="Operating Expenses Growth:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.opex_growth = ttk.Entry(frame, width=10)
        self.opex_growth.grid(row=1, column=1, sticky="w", padx=5, pady=5)
        ttk.Label(frame, text="% (e.g., 3 for 3%)").grid(row=1, column=2, sticky="w", padx=5, pady=5)
    
    def _create_balance_assumptions(self):
        """Create the balance sheet assumptions tab."""
        frame = ttk.LabelFrame(self.balance_tab, text="Balance Sheet Assumptions", padding=10)
        frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Cash as % of Revenue
        ttk.Label(frame, text="Cash as % of Revenue:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.cash_percent = ttk.Entry(frame, width=10)
        self.cash_percent.grid(row=0, column=1, sticky="w", padx=5, pady=5)
        ttk.Label(frame, text="% (e.g., 25 for 25%)").grid(row=0, column=2, sticky="w", padx=5, pady=5)
        
        # Accounts Receivable Days
        ttk.Label(frame, text="Accounts Receivable Days:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.ar_days = ttk.Entry(frame, width=10)
        self.ar_days.grid(row=1, column=1, sticky="w", padx=5, pady=5)
        ttk.Label(frame, text="days").grid(row=1, column=2, sticky="w", padx=5, pady=5)
        
        # Inventory Days
        ttk.Label(frame, text="Inventory Days:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.inventory_days = ttk.Entry(frame, width=10)
        self.inventory_days.grid(row=2, column=1, sticky="w", padx=5, pady=5)
        ttk.Label(frame, text="days").grid(row=2, column=2, sticky="w", padx=5, pady=5)
        
        # Accounts Payable Days
        ttk.Label(frame, text="Accounts Payable Days:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.ap_days = ttk.Entry(frame, width=10)
        self.ap_days.grid(row=3, column=1, sticky="w", padx=5, pady=5)
        ttk.Label(frame, text="days").grid(row=3, column=2, sticky="w", padx=5, pady=5)
        
        # Capital Expenditures as % of Revenue
        ttk.Label(frame, text="Capital Expenditures as % of Revenue:").grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.capex_percent = ttk.Entry(frame, width=10)
        self.capex_percent.grid(row=4, column=1, sticky="w", padx=5, pady=5)
        ttk.Label(frame, text="% (e.g., 8 for 8%)").grid(row=4, column=2, sticky="w", padx=5, pady=5)
        
        # Depreciation Rate
        ttk.Label(frame, text="Depreciation Rate:").grid(row=5, column=0, sticky="w", padx=5, pady=5)
        self.depreciation_rate = ttk.Entry(frame, width=10)
        self.depreciation_rate.grid(row=5, column=1, sticky="w", padx=5, pady=5)
        ttk.Label(frame, text="% (e.g., 10 for 10%)").grid(row=5, column=2, sticky="w", padx=5, pady=5)
    
    def _create_cash_flow_assumptions(self):
        """Create the cash flow assumptions tab."""
        frame = ttk.LabelFrame(self.cash_flow_tab, text="Cash Flow Assumptions", padding=10)
        frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Dividend Payout Ratio
        ttk.Label(frame, text="Dividend Payout Ratio:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.dividend_payout = ttk.Entry(frame, width=10)
        self.dividend_payout.grid(row=0, column=1, sticky="w", padx=5, pady=5)
        ttk.Label(frame, text="% (e.g., 15 for 15%)").grid(row=0, column=2, sticky="w", padx=5, pady=5)
        
        # Debt Repayment
        ttk.Label(frame, text="Debt Repayment:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.debt_repayment = ttk.Entry(frame, width=10)
        self.debt_repayment.grid(row=1, column=1, sticky="w", padx=5, pady=5)
        ttk.Label(frame, text="$").grid(row=1, column=2, sticky="w", padx=5, pady=5)
        
        # New Borrowing
        ttk.Label(frame, text="New Borrowing:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.new_borrowing = ttk.Entry(frame, width=10)
        self.new_borrowing.grid(row=2, column=1, sticky="w", padx=5, pady=5)
        ttk.Label(frame, text="$").grid(row=2, column=2, sticky="w", padx=5, pady=5)
    
    def _initialize_fields(self):
        """Initialize the entry fields with current assumptions."""
        assumptions = self.forecast_model.assumptions
        
        # General assumptions
        self.revenue_growth.insert(0, str(assumptions['revenue_growth'] * 100))
        self.tax_rate.insert(0, str(assumptions['tax_rate'] * 100))
        self.interest_rate.insert(0, str(assumptions['interest_rate'] * 100))
        
        # Income statement assumptions
        self.cogs_percent.insert(0, str(assumptions['cogs_percent'] * 100))
        self.opex_growth.insert(0, str(assumptions['opex_growth'] * 100))
        
        # Balance sheet assumptions
        self.cash_percent.insert(0, str(assumptions['cash_percent'] * 100))
        self.ar_days.insert(0, str(assumptions['ar_days']))
        self.inventory_days.insert(0, str(assumptions['inventory_days']))
        self.ap_days.insert(0, str(assumptions['ap_days']))
        self.capex_percent.insert(0, str(assumptions['capex_percent'] * 100))
        self.depreciation_rate.insert(0, str(assumptions['depreciation_rate'] * 100))
        
        # Cash flow assumptions
        self.dividend_payout.insert(0, str(assumptions['dividend_payout'] * 100))
        self.debt_repayment.insert(0, str(assumptions['debt_repayment']))
        self.new_borrowing.insert(0, str(assumptions['new_borrowing']))
    
    def _apply_assumptions(self):
        """Apply the assumptions to the forecast model."""
        try:
            # Create a new assumptions dictionary
            new_assumptions = {
                # General assumptions
                'revenue_growth': float(self.revenue_growth.get()) / 100,
                'tax_rate': float(self.tax_rate.get()) / 100,
                'interest_rate': float(self.interest_rate.get()) / 100,
                
                # Income statement assumptions
                'cogs_percent': float(self.cogs_percent.get()) / 100,
                'opex_growth': float(self.opex_growth.get()) / 100,
                
                # Balance sheet assumptions
                'cash_percent': float(self.cash_percent.get()) / 100,
                'ar_days': float(self.ar_days.get()),
                'inventory_days': float(self.inventory_days.get()),
                'ap_days': float(self.ap_days.get()),
                'capex_percent': float(self.capex_percent.get()) / 100,
                'depreciation_rate': float(self.depreciation_rate.get()) / 100,
                
                # Cash flow assumptions
                'dividend_payout': float(self.dividend_payout.get()) / 100,
                'debt_repayment': float(self.debt_repayment.get()),
                'new_borrowing': float(self.new_borrowing.get())
            }
            
            # Update the forecast model
            self.forecast_model.update_assumptions(new_assumptions)
            
            # Call the callback if provided
            if self.on_apply_callback:
                self.on_apply_callback()
            
            # Close the window
            self.window.destroy()
        except ValueError as e:
            # Show an error message
            tk.messagebox.showerror(
                "Invalid Input", 
                f"Please enter valid numeric values for all fields.\n\nError: {str(e)}"
            )