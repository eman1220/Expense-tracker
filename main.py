import calendar
import datetime
from expense_class import Expense

def main():
  print("Welcome to the Expense Tracker")
  expense_file_path = "expenses.csv"
  budget = float(input("Enter your budget for the month ($): "))
  
  # Get user input for an expense
  expense = get_user_expense()
  
  # Save expense to a file
  save_expense_to_file(expense, expense_file_path)
  
  # Read and summarise expenses from the file
  summarise_expenses(expense_file_path, budget)
  


def get_user_expense():
  print("Getting user expense...")
  # Get name and cost of the expense
  expense_name = input("Enter expense name: ")
  expense_amount = float(input("Enter expense amount ($): "))
  
  # Display expense categories
  expense_categories = ["🍔 Food", "🏠 Home", "💼 Work", "🚗 Transport", "🎉 Fun", "✨ Misc"]
  category_amount = len(expense_categories)
  for i, category in enumerate(expense_categories):
    print(f" {i+1}. {category}")
    
  # Get user to select a category
  while True:
    try: 
      expense_category = int(input(f"Select an expense category (1-{category_amount}): " ))
      if expense_category in range(1,category_amount+1):
        selected_category = expense_categories[expense_category-1]

        # Return a new Expense object with the user input
        new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
        return new_expense
      else:
        print(f"Invalid input. Please enter a number between 1 and {category_amount}.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")
  


def save_expense_to_file(expense,expense_file_path):
  print(f"Saving user expense: {expense} to {expense_file_path}")
  with open(expense_file_path, "a") as f:
    f.write(f"{expense.name},{expense.category},{expense.amount}\n")
  
  


def summarise_expenses(expense_file_path, budget):
  print("Summarising user expenses...")
  # Read expenses from the file and add to a list
  expenses: list[Expense] = []
  with open(expense_file_path, "r") as f:
    lines = f.readlines()
    for line in lines:
      new_line = line.strip().split(",")
      expense_line = Expense(name=new_line[0], category=new_line[1], amount=float(new_line[2]))
      expenses.append(expense_line)
      print(expense_line)

  # Summarise expense amount by category and print the result
  category_amount_option = input("Would you like to see the amount spent by category? (y/n): ")
  if category_amount_option.lower() != "y":
    pass
  amount_per_category = {}
  for expense in expenses:
    key = expense.category
    if key in amount_per_category:
      amount_per_category[key] += expense.amount
    else:
      amount_per_category[key] = expense.amount
      
  print("Expenses by category:")
  for key, amount in amount_per_category.items():
    print(f" {key}: ${amount:.2f}")

  # Print total spent and remaining budget
  total_spent = sum(amount_per_category.values()) 
  print(f"Total spent: ${total_spent:.2f}")
  remaining_budget = budget - total_spent
  print(f"Remaining budget: ${remaining_budget:.2f}")

  # Find and print the average spending per day to stay within monthly budget
  daily_budget_option = input("Would you like to see your daily budget? (y/n): ")
  if daily_budget_option.lower() != "y":
    pass
  else:
    today = datetime.date.today()
    days_in_month = calendar.monthrange(today.year, today.month)[1]
    remaining_days = days_in_month - today.day
    daily_budget = remaining_budget / remaining_days
    print(f"Remaining days for this month: {remaining_days}")
    print(f"Daily budget: ${daily_budget:.2f}")
  
  
if __name__ == "__main__":
  main()
