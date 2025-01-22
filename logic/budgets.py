import json
import os
from collections import defaultdict
from logic.transactions import CATEGORIES

#Constants
BUDGET_FILE = "data/budgets.json"

def load_budgets(filename=BUDGET_FILE):
    """Load budgets from the JSON file.

    Args:
        filename (JSON, optional):. 
        Returns a dictionary with categories as keys and their respective budgets as values.
    """
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No saved budgets found. Starting Fresh!")
        return {}
    except json.JSONDecodeError:
        print("Error reading budgets. Starting fresh!")
        return {}

def save_budgets(budgets, filename=BUDGET_FILE):
    pass
