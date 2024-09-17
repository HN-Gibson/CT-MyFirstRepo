#Create a function for adding an entry to Journal.txt
def add_journal_entry (date):
    entry = input("What would you like to log?\n")
    with open('Journal.txt', 'a') as file:
        file.write(f"{date} - {entry}")
        return print("Log Added!")
#Create a function for adding a new Weekly summary
def add_weekly_log (week):
    while True:
        user_option = input ("Would you like to add a line?\n(Yes or No)\n").lower
        if user_option() == "no":
            return print("Thank you for your summary!")
        else:
            entry = input("What would you like to log?\n")
            with open(f'weekly_logs\\Week {week} @ CT.txt', 'a') as file:
                file.write(f"{entry}\n")
#Write a program to manage adding new Journal entries and Weekly Summaries
    #Have Journal Entries automate the date and look for 1 line of text
    #Have Weekly Entries loop to ask for more lines if necessary

while True:
    user_selection = input("Type 'weekly' to add a weekly log or 'daily' to add a daily log.\nEnter 'quit' to exit:\n").lower
    if user_selection() == "quit":
        break
    if user_selection() == "weekly":
        log_week=input("Enter the number value for the weeks you would like to log:\n")
        add_weekly_log(log_week)
    if user_selection() == "daily":
        log_day=input("Please enter the date for your entry\n(month/day/year):\n")
        add_journal_entry(log_day)
    else:
        print("\nInvalid Entry: Please type 'weekly', 'daily', or 'quit'\n")
    