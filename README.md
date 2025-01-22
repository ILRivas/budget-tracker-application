## Created by Israel L. Rivas II

## Description
The Budget Tracker is a simple Python program designed to help users manage their income and expenses. It allows you to record transactions, categorize them, and calculate totals to monitor your financial health. 

## Basic Features
- Add income and expenses xx
- Catagorize Transactions xx
- View a summary of income, expenses and savings xx
- Export transactions to a CSV file for book-keeping purposes.

## File Structure
main.py => 
    -Runs the program

menu_logic.py =>
    -Takes care of the logic behind the command prompt menu.

transactions.py =>
    -Added functionality to add transactions
    -Added functionality to view transactions
    -Added functionality to filter transactions via date, category and type.
    -Added functionality to provide a summary for the user providing total income, total expenses and finally their net balance.

utils.py => 
    -Houses utility functions such as date validation and auto-capitalization.

## The command prompt program has been completed and is stable. I will now attempt to implement a GUI using Tkinter.
    -pip install tk <- use this command in your command prompt to ensure the proper dependancies are downloaded and installed.

    -Developer Note: Initial plan did not go as well as I thought it would. Tkinter is maybe a bit too difficult for me at the moment. Will have to revisit. This section is now ON HOLD.

