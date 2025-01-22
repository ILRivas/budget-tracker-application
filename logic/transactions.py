import os
import json
from datetime import datetime
from collections import defaultdict

## Constants
VALID_TRANSACTION_TYPES = ["Income", "Expense"]
CATEGORIES = [
    "Paycheck",
    "Utilities",
    "Groceries",
    "Auto (Gas, Insurance, Repairs, Payment)",
    "Entertainment",
    "Dining Out",
    "Savings",
    "Debt Payment",
    "Health",
    "Subscriptions",
    "Phone Payment"
]
############################### TRANSACTION LOGIC ########################################
#Pure add_transaction function for GUI functionality.
def add_transaction(transaction_list, date, t_type, amount, category, description=None):
    """Add a new transaction to the transaction list.

    Args:
        transaction_list (list): List of all transactions
        t_type (str): Type of transaction (income / expense)
        category (str): Category of the transaction.
        amount (float): Amount of the transaction.
        date (str): Date of the transaction
        description (str, optional): Optional description of the transaction. Defaults to None.

    Returns:
        dict: The transaction added if successful.
    Raises:
        ValueError: If the transaction type, amount, or date is invalid.
    """
    if t_type.lower() not in ["income", "expense"]:
        raise ValueError("Invalid transaction type. Must be 'income' or 'expense'.")
    
    if amount <= 0:
        raise ValueError("Transaction amount must be greater than zero.")
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Expected YYYY-MM-DD.")
    
    transaction = {
        "type": t_type.capitalize(),
        "amount": amount,
        "category": category,
        "date": date,
        "transaction_description": description or None
    }
    transaction_list.append(transaction)
    return transaction

# def add_transaction(transaction_list):
#     """ Add a new transaction to the list.

#     Args:
#         transaction_list (list): List of containing all current transactions. Each transaction is
#         represented as a dictionary with keys such as 'date', 'type', 'amount', and 'category'.
#     """
#     while True:  # Outer loop for retrying the entire process if user makes a mistake
#         # Validate transaction type
#         while True:
#             transaction_type = input("Enter type (income/expense): ").strip().lower()
#             if transaction_type in VALID_TRANSACTION_TYPES:
#                 transaction_type = transaction_type.capitalize()  # Capitalize "Income" or "Expense"
#                 break
#             else:
#                 print("Invalid type. Please enter either 'income' or 'expense'.")

#         # Validate transaction amount
#         while True:
#             try:
#                 transaction_amount = float(input("Enter amount: "))
#                 if transaction_amount > 0:
#                     break
#                 else:
#                     print("Amount must be greater than 0.")
#             except ValueError:
#                 print("Invalid input. Please enter a valid number.")

#         #Validate set transaction categories
#         while True:
#             print("Select a category")
#             for i, category in enumerate(CATEGORIES, start = 1):
#                 print(f"{i}. {category}")
#             category_choice = input("Enter the number of the category: ")
#             try:
#                 category_choice = int(category_choice)
#                 if 1 <= category_choice <= len(CATEGORIES):
#                     transaction_category = CATEGORIES[category_choice - 1]
#                     break
#                 else:
#                     print("Invalid category number. Please select a valid number.")
#             except ValueError:
#                 print("Invalid input. Please enter a valid NUMBER.")

#         # Validate transaction date
#         while True:
#             transaction_date = input("Enter date (YYYY-MM-DD): ").strip()
#             try:
#                 transaction_date = datetime.strptime(transaction_date, "%Y-%m-%d")  # Validate format
#                 break
#             except ValueError:
#                 print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")

#         #Ask for an optional description
#         transaction_description = input("Enter a description of this transaction (optional): ")

#         # Display the transaction details for confirmation
#         print("\nHere is the transaction you entered:")
#         print(f"Type: {transaction_type}")
#         print(f"Amount: ${transaction_amount:.2f}")
#         print(f"Category: {transaction_category}")
#         print(f"Date: {transaction_date.strftime('%Y-%m-%d')}")
#         print(f"Description: {transaction_description or 'None'}")

#         # Ask for confirmation
#         confirm = input("Is this information correct? (yes/no): ").strip().lower()
#         if confirm == "yes":
#             # Create a transaction dictionary
#             transaction = {
#                 "type": transaction_type,
#                 "amount": transaction_amount,
#                 "category": transaction_category,
#                 "date": transaction_date.strftime("%Y-%m-%d"),
#                 "transaction_description": transaction_description or None,
                
#             }
#             # Append the transaction to the transactions list
#             transaction_list.append(transaction)
#             print("Transaction has been added successfully!\n")
#             break  # Exit the outer loop once the transaction is confirmed
#         else:
#             print("Let's try again.\n")  # Restart the process if user says "no"



## Create a function that will display all logged transactions
def display_transactions(transaction_list):
    if not transaction_list:
        print("No transactions to display.\n")
        return

    # Print the header
    print(f"\n{'#':<5}{'Date':<12}{'Type':<10}{'Amount':<10}{'Category':<15}{ 'Description':<20}")
    print("-" * 50)

    # Iterate directly over the sorted list
    for i, transaction in enumerate(
        sorted(transaction_list, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%d")),
        start=1
    ):
        print(f"{i:<5}{transaction['date']:<12}{transaction['type']:<10}${transaction['amount']:<10.2f}{transaction['category']:<15}{transaction['transaction_description'] or 'None'}")
    print()


def del_transaction(transaction_list):
    if not transaction_list:
        print("No transactions to delete.\n")
        return

    # Display transactions with index numbers starting at 1
    print("Here are your transactions:")
    display_transactions(transaction_list)

    while True:
        try:
            # Ask user for the transaction number to delete
            user_index = int(input("Enter the number of the transaction you want to delete: "))
            
            # Validate 1-based input
            if 1 <= user_index <= len(transaction_list):
                actual_index = user_index - 1  # Convert to 0-based index
                ##print(f"DEBUG: User entered {user_index}, which maps to actual index {actual_index}")  # Debugging
                
                # Get the selected transaction
                transaction_to_delete = transaction_list[actual_index]

                # Confirm before deleting
                confirmation = input(
                    f"Are you sure you want to delete this transaction:\n"
                    f"Type: {transaction_to_delete['type']}, Amount: ${transaction_to_delete['amount']:.2f}, "
                    f"Category: {transaction_to_delete['category']}, Date: {transaction_to_delete['date']}? (yes/no): "
                ).strip().lower()

                if confirmation == "yes":
                    deleted_transaction = transaction_list.pop(actual_index)
                    print(f"Deleted transaction: {deleted_transaction['type']} of ${deleted_transaction['amount']:.2f} ({deleted_transaction['category']} on {deleted_transaction['date']})")
                    break
                else:
                    print("Transaction not deleted.\n")
                    break
            else:
                print(f"Invalid transaction number. Please select a number between 1 and {len(transaction_list)}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")



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


######################### TRANSACTION FILTERS ##########################################
def display_categories():
    print("\nAvailable Categories:")
    for index, category in enumerate(CATEGORIES, start=1):
        print(f"{index}. {category}")
    while True:
        try:
            category_choice = int(input("Enter the number of the category: "))
            if 1 <= category_choice <= len(CATEGORIES):
                return CATEGORIES[category_choice - 1]
            else:
                print("Invalid category number. Please select a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def filter_by_category(transaction_list):
    selected_category = display_categories
    filtered_transactions = [
        transaction for transaction in transaction_list
        if transaction["type"] == "Expense" and transaction["category"] == selected_category
    ]
    if not filtered_transactions:
        print(f"No transactions found for the category '{selected_category}'.\n")
        return
    #display the filtered transactions
    print(f"\nTransactions for the category '{selected_category}':")
    print(f"{'#':<5}{'Date':<12}{'Amount':<10}{'Category':<15}")
    print("-" * 40)
    for i, transaction in enumerate(filtered_transactions, start=1):
        print(f"{i:<5}{transaction['date']:<12}${transaction['amount']:<10.2f}")
    print()
    total_spending = sum(t["amount"] for t in filtered_transactions)
    print(f"Total spending for the category '{selected_category}': ${total_spending:.2f}\n")

def filter_by_type(transaction_list, transaction_type):
    filtered_transactions = [t for t in transaction_list if t["type"].lower() == transaction_type.lower()]
    if filtered_transactions:
        display_transactions(filtered_transactions)
    else:
        print(f"No transactions found for the type '{transaction_type}'.\n")
        
def filter_by_date_range(transaction_list, start_date, end_date):
    try:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")

        filtered_transactions = [
            t for t in transaction_list
            if start_date <= datetime.strptime(t["date"], "%Y-%m-%d") <= end_date
        ]
        if filtered_transactions:
            display_transactions(filtered_transactions)
        else:
            print("No transactions found within the specified date range.\n")
    except ValueError:
        print("Invalid date format. Please enter the date in the format YYYY-MM-DD.\n")

############################ MATHEMATICAL LOGIC FOR TRANSACTIONS #############################
def calculate_summary(transaction_list):
    ## Calculate total income ##
    total_income = sum(t["amount"] for t in transaction_list if t["type"] == "Income")
    ## calculate total expenses ##
    total_expenses = sum(t["amount"] for t in transaction_list if t["type"] == "Expense")
    ## Calculate net income ##
    net_balance = total_income - total_expenses
    return total_income, total_expenses, net_balance


def view_summary(transaction_list):
    total_income, total_expenses, net_balance = calculate_summary(transaction_list)
    print(f"\nSummary Statistics:")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Net Balance: ${net_balance:.2f}\n")

##Calculate monthly summary
def filter_transactions_by_month(transaction_list, year, month):
    filtered = [
        transaction
        for transaction in transaction_list
        if transaction["date"].startswith(f"{year}-{month:02d}")
    ]
    return filtered

##Generate Spending Report by Category
def calculate_spending_by_category(transaction_list):
    spending_by_category = defaultdict(float)
    for transaction in transaction_list:
        if transaction["type"] == "Expense":
            spending_by_category[transaction["category"]] += transaction["amount"]
    return dict(spending_by_category)


