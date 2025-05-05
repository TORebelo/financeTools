"""
Formatting utilities for financial statements.
"""

def format_currency(value):
    """
    Format a value as currency.
    
    Args:
        value (float): The value to format
        
    Returns:
        str: Formatted currency string
    """
    return f"${value:,.0f}"

def format_percentage(value):
    """
    Format a value as percentage.
    
    Args:
        value (float): The value to format
        
    Returns:
        str: Formatted percentage string
    """
    return f"{value:.1%}"

def format_change(value, percentage):
    """
    Format a change value with direction indicator.
    
    Args:
        value (float): The change value
        percentage (float): The percentage change
        
    Returns:
        str: Formatted change string with direction indicator
    """
    if value > 0:
        return f"▲ {format_currency(value)} ({format_percentage(percentage)})"
    elif value < 0:
        return f"▼ {format_currency(abs(value))} ({format_percentage(abs(percentage))})"
    else:
        return f"— {format_currency(0)} (0.0%)"