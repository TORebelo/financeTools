"""
Reusable GUI components for financial statements application.
"""

import tkinter as tk
from tkinter import ttk

def create_button(parent, text, command, width=20, height=2, font=("Arial", 10)):
    """
    Create a styled button.
    
    Args:
        parent: Parent widget
        text: Button text
        command: Button command
        width: Button width
        height: Button height
        font: Button font
        
    Returns:
        Button widget
    """
    button = tk.Button(
        parent,
        text=text,
        command=command,
        width=width,
        height=height,
        font=font,
        bg="#f0f0f0",
        activebackground="#e0e0e0",
        relief=tk.RAISED,
        borderwidth=2
    )
    return button

def create_label_frame(parent, title, padding=10):
    """
    Create a styled label frame.
    
    Args:
        parent: Parent widget
        title: Frame title
        padding: Frame padding
        
    Returns:
        LabelFrame widget
    """
    frame = ttk.LabelFrame(parent, text=title, padding=padding)
    return frame

def create_section_header(parent, text, font=("Arial", 12, "bold")):
    """
    Create a section header.
    
    Args:
        parent: Parent widget
        text: Header text
        font: Header font
        
    Returns:
        Label widget
    """
    header = ttk.Label(parent, text=text, font=font)
    return header

def create_data_row(parent, label_text, value, row_index, bold=False):
    """
    Create a data row with label and value.
    
    Args:
        parent: Parent widget
        label_text: Label text
        value: Value to display
        row_index: Row index
        bold: Whether to use bold font
        
    Returns:
        Tuple of (label, value) widgets
    """
    font = ("Arial", 10, "bold") if bold else ("Arial", 10)
    
    label = ttk.Label(parent, text=label_text, font=font)
    label.grid(row=row_index, column=0, sticky="w", padx=5, pady=2)
    
    value_label = ttk.Label(parent, text=value, font=font)
    value_label.grid(row=row_index, column=1, sticky="e", padx=5, pady=2)
    
    return (label, value_label)