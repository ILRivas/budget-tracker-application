from logic.transactions import (
    add_transaction, 
    del_transaction,
    display_transactions, 
    filter_by_date_range, 
    display_categories,
    filter_by_category, 
    filter_by_type,
    view_summary,
)
from logic.reports import generate_monthly_budget_report
from logic.utils import export_to_csv

def filter_menu(transaction_list):
    print("\nSelect a filter option: ")
    print("1. Filter by Date Range")
    print("2. Filter by Category")
    print("3. Filter by Type")
    filter_choice = input("Enter your filter choice: ")

    if filter_choice == "1":
        start_date = input("Enter the start date (YYYY-MM-DD): ")
        end_date = input("Enter the end date (YYYY-MM-DD): ")
        filter_by_date_range(transaction_list, start_date, end_date)
    elif filter_choice == "2":
        filter_by_category(transaction_list)
    elif filter_choice == "3":
        transaction_type = input("Enter the transaction type to filter by: ")
        filter_by_type(transaction_list, transaction_type)
    else:
        print("Invalid choice. Please enter 1, 2 or 3.")
          

def main_menu(transaction_list):
    while True:
        print("1. Add Transaction")
        print("2. Delete Transaction")
        print("3. View transactions")
        print("4. View Monthly Summary")
        print("5. Export Month report to CSV File")
        print("6. Exit")
        choice = input("Enter choice: ")
        ## Menu Logic
        if choice == "1":
            add_transaction(transaction_list)
        elif choice == "2":
            del_transaction(transaction_list)
        elif choice == "3":
            display_transactions(transaction_list)
        elif choice == "4":
            generate_monthly_budget_report(transaction_list)
        elif choice == "5":
            year = input("Enter the year to export: ")
            month = input("Enter the month to export: ")
            export_to_csv(transaction_list, year, month)
        elif choice == "6":
            print("Exiting program...")
            break
       
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
