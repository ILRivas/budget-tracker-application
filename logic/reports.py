from logic.transactions import (filter_transactions_by_month, calculate_summary, calculate_spending_by_category)
from logic.utils import export_to_csv
##Generate monthly Budget Report
def generate_monthly_budget_report(transaction_list):
    """
    Generate a monthly budget report, displaying totals, transactions, 
    and spending by category for a specific month.

    Args:
        transaction_list (list): List of all transactions.
    """
    try:
        # Prompt for year and month
        year = int(input("Enter year (e.g., 2024): "))
        month = int(input("Enter month (1-12): "))
        if not (1 <= month <= 12):
            raise ValueError("Month must be between 1 and 12")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return  # Exit function if input is invalid

    # Filter transactions for the specified month
    filtered_transactions = filter_transactions_by_month(transaction_list, year, month)
    if not filtered_transactions:
        print(f"No transactions found for {month:02d}/{year}.\n")
        return

    # Calculate totals
    total_income, total_expenses, net_balance = calculate_summary(filtered_transactions)

    # Display report header
    print(f"\nMonthly Budget Report for {month:02d}/{year}")
    print("=" * 50)
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Net Balance: ${net_balance:.2f}\n")

    # Display transactions
    print("Transactions:")
    print(f"{'#':<5}{'Date':<12}{'Type':<10}{'Amount':<10}{'Category':<20}{'Description':<30}")
    print("-" * 90)
    for i, transaction in enumerate(filtered_transactions, start=1):
        print(f"{i:<5}{transaction['date']:<12}{transaction['type']:<10}${transaction['amount']:<10.2f}"
              f"{transaction['category']:<20}{transaction.get('transaction_description', 'None'):<20}")
    print()

    # Display spending by category
    print("Spending by Category:")
    category_spending = calculate_spending_by_category(filtered_transactions)
    for category, amount in category_spending.items():
        print(f"  {category}: ${amount:.2f}")
    print()
