from datetime import datetime
import os
import csv

def validate_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return None
    
def capitalize_first_letter(text):
    return text.strip().capitalize()


def export_to_csv(transactions, year, month, filename=None):
    """
    Exports the transactions of a selected month and year to a CSV file.

    Args:
        transactions (list): List of transactions to export.
        year (str): Year to filter by (e.g., "2025").
        month (str): Month to filter by e.g., "1" or "01".
        filename (str, optional): Optional custom filename for the CSV file.

        Returns:
            str: Message indicating success or failure.
    """
    
    try:
        month_formatted = f"{int(month):02d}"
        filtered_transactions = [
            
            t for t in transactions if t["date"].startswith(f"{year}-{month}")
        ]
        if not filtered_transactions:
            return "No transactions found for the selected month and year."
        if not filename:
            filename = f"transactions_{year}_{month_formatted}.csv"
        if os.path.exists(filename):
            user_input = input(f"{filename} already exists. Would you like to overwrite it? (yes/no): ").strip().lower()
            if user_input != "yes":
                return f"Export to CSV cancelled. File {filename} already exists and was not overwritten."
        #Write to CSV file
        with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Date', 'Type', 'Amount', 'Category', 'Description']
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

            #Write Header
            writer.writeheader()
            #Now write each transaction beneath the header
            for transaction in filtered_transactions:
                writer.writerow({
                    'Date': transaction.get('date'),
                    'Type': transaction.get('type'),
                    'Amount': transaction.get('amount'),
                    'Category': transaction.get('category'),
                    'Description': transaction.get('transaction_description'),
                })
            return f"Transactions for {year}-{month_formatted} exported to {filename} successfully"
    except Exception as e:
        return f"An error occured while exporting to CSV: {e}"