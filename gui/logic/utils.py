import os
import json
from datetime import datetime
from collections import defaultdict

## Constants
VALID_TRANSACTION_TYPES = ["Income", "Expense"]


############################ Loading and saving into transactions.json###########
def save_transactions(transaction_list, filename="data/transactions.json"):
    try:
        sorted_transactions = sorted(transaction_list, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%d"))
       ##print(f"Saving transactions: {transaction_list}")
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as file:
            json.dump(sorted_transactions, file, indent=4)
        print("Transactions saved successfully!\n")
    except Exception as e:
        print(f"An error occurred while saving transactions: {e}\n")


def load_transactions(filename="data/transactions.json"):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            ##print(f"Loaded transactions: {data}")
            return data
    except FileNotFoundError:
        print("No saved transactions found!\n")
        return []
    except json.JSONDecodeError:
        print("Error reading transactions. Starting Fresh.\n")
        return []

def sort_existing_json(filename="data/transactions.json"):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        sorted_transactions = sorted(data, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%d"))
        with open(filename, "w") as file:
            json.dump(sorted_transactions, file, indent=4)
        print("Transactions sorted successfully!\n")
    except FileNotFoundError:
        print("No saved transactions found!\n")
    except Exception as e:
        print(f"An error occurred while sorting transactions: {e}\n")


