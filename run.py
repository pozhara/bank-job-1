# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import datetime  # to check age
import math  # to check decimal
import sys  # to exit the program
import time  # to add pauses
from os import system  # to clear terminal
import re  # to check for special characters in a string input
import random  # to approve or disapprove requests for time off
import gspread  # to use google sheets
from google.oauth2.service_account import Credentials

# Defines the scope
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

"""
Adds credentials to the account and authorises the client sheet.
Code taken from Love Sandwiches.
"""
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("bank-job")

# A greeting, instruction on what to do next
print("Hello, we are a recently opened bank,")
print("thank you for starting your career with us.")
print("Your next step is to add yourself as an employee to our system.\n")


def clear():
    """
    Clears the terminal
    https://stackoverflow.com/questions/2084508/clear-terminal-in-python
    """
    system('clear')


def wait():
    """
    Adds pause before going on.
    https://www.pythoncentral.io/pythons-time-sleep-pause-wait-sleep-stop-your-code/
    """
    time.sleep(2.5)


def update_worksheet(data, worksheet):
    """
    Updates worksheet.
    Code taken from Love Sandwiches.
    """
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)


def check_name(name):
    # Checks name for length and having numbers
    if len(name) < 1:
        return False
    if len(name) > 20:
        return False
    if name.isnumeric():
        return False
    if not name.isalpha():
        return False
    return name


def check_string(string):
    """
    Checks strings for length, having numbers
    or special characters.
    """
    regex = re.compile('[@_!#$%^&*()<>?/|}{~:]')
    if len(string) > 25:
        return False
    if len(string) < 1:
        return False
    if string.isnumeric():
        return False
    if not regex.search(string) is None:
        return False
    if not string.isalpha():
        return False
    return string


# Asks for first name, checks for length,
# the input not being a number or null.
# Raises ValueError if input isn't valid.
while True:
    try:
        first_name = input("\nPlease enter your"
                           " first name(maximum 20 characters):\n")
        cap_first_name = first_name.capitalize()
        check_first_name = check_name(first_name)
        if check_first_name is False:
            raise ValueError
        break
    except ValueError:
        print("Please try again, enter your "
              "first name, maximum 20 characters.")

# Asks for first name, checks for length,
# the input not being a number or null.
# Raises ValueError if input isn't valid.
while True:
    try:
        last_name = input("\nPlease enter your last "
                          "name(maximum 20 characters):\n")
        cap_last_name = last_name.capitalize()
        check_last_name = check_name(last_name)
        if check_last_name is False:
            raise ValueError
        break
    except ValueError:
        print("Please try again, enter your last name, maximum 20 characters.")

# Asks for birth day, checks for input being a number between 1 and 31.
# If it's lower, higher, null or a string, raises ValueError.
while True:
    try:
        age_day = int(input("\nPlease enter the day you were born:\n"))
        if age_day > 31 or age_day < 1:
            raise ValueError
        break
    except ValueError:
        print('Value must be a positive number and cannot be greater than 31.')

# Asks for birth month, checks for input being a number between 1 and 12.
# If input is lower, higher, null or a string, raises ValueError.
while True:
    try:
        age_month = int(input("\nPlease enter the month you were born:\n"))
        if age_month > 12 or age_month < 1:
            raise ValueError
        elif age_month == 2 and age_day > 29:
            raise ValueError
        break
    except ValueError:
        print('Value must be a positive number and must be between 1 and 12.')

# Asks for birth year, calculates age of an employee.
# Checks for it to be between 18 and 80.
# If it's not, raises ValueError.
# If it is, updates birthday worksheet.
while True:
    try:
        age_year = int(input("\nPlease enter the year you were born:\n"))
        date_of_birth = datetime.datetime(age_year, age_month, age_day)
        age = datetime.datetime.now() - date_of_birth
        days = int(age.days)
        converted_years = days/365
        employee_age = int(converted_years)
        if employee_age >= 18 and employee_age < 80:
            employee_birthday = (cap_first_name + "," + cap_last_name +
                                 "," + str(age_day) + "," + str(age_month))
            employee_birthday = employee_birthday.split(",")
            employee_birthday_for_ws = [i.strip() for i in employee_birthday]
            update_worksheet(employee_birthday_for_ws, "Birthdays")
        else:
            raise ValueError
        break
    except ValueError:
        print('Please try again, your age should be between 18 and 80.')

# Asks for a role. Checks for length
# and input being a number or null.
# If data is valid, it is added to employees worksheet.
# If it isn't, raises a ValueError.
while True:
    try:
        employee_role = input("\nPlease enter your job role"
                              "(maximum 25 characters):\n")
        cap_employee_role = employee_role.capitalize()
        check_role = check_string(employee_role)
        if check_role is False:
            raise ValueError
        elif len(employee_role) > 1:
            employee_data = (cap_first_name + "," + cap_last_name +
                             "," + cap_employee_role)
            employee_data = employee_data.split(",")
            employee_data_for_ws = [i.strip() for i in employee_data]
            update_worksheet(employee_data_for_ws, "Employees")
            print("\nThank you, the data provided is "
                  "valid and is now added to our database.\n")
        break
    except ValueError:
        print("Please try again, your job role "
              "should be 20 characters maximum.")


def give_options():
    """
    Asks user what they want to do,
    checks user input to be a number between 1 and 4.
    If it is, clears terminal, waits a bit
    and does what the user chose.
    If it's not, raises ValueError.
    """
    print("\nWhat would you like to do?\n"
          "1. Request time off.\n"
          "2. See your colleagues' birthdays.\n"
          "3. See your colleagues' names and roles.\n"
          "4. Exit.")
    while True:
        try:
            global user_input
            user_input = int(input("Please enter a number:\n"))
            if user_input >= 1 and user_input <= 4:
                print("\nPlease wait, we are processing your request...\n")
                wait()
                clear()
                return user_input
            else:
                raise ValueError
            break
        except ValueError:
            print("\nPlease try again, enter a number between 1 and 4.\n")


# Function for checking date
def check_date(first_date, second_date):
    whole = math.floor(first_date)
    frac = first_date - whole
    needed_decimal = '0.23'
    whole_two = math.floor(second_date)
    frac_two = second_date - whole_two
    if first_date > 31.12 or second_date > 31.12:
        return False
    elif first_date < 01.01 or second_date < 01.01:
        return False
    elif first_date.is_integer() or second_date.is_integer():
        return False
    elif frac > 0.12:
        return False
    elif len(needed_decimal) > len(str(first_date)):
        return False
    elif frac_two > 0.12:
        return False
    elif len(needed_decimal) > len(str(second_date)):
        return False
    elif second_date < first_date:
        return False


def request_time_off(cap_first_name, cap_last_name):
    """
    Asks for starting and ending date
    and a reason for a day off.
    If the data is valid,
    request a day off worksheet is updated,
    waits a bit and asks what user wants to do next.
    """
    print("You are currently requesting time off. "
          "We will need you to provide starting "
          "and ending date, and a reason.\n")
    while True:
        user_name = ("Your name is " + cap_first_name +
                     " " + cap_last_name + ".")
        print(user_name)
        try:
            # https://stackoverflow.com/questions/3886402/how-to-get-numbers-after-decimal-point
            starting_date = float(input("\nPlease enter a starting date"
                                        " (For example: 01.02):\n"))
            ending_date = float(input("\nPlease enter an ending date"
                                      " (For example: 01.02):\n"))
            check_dates = check_date(starting_date, ending_date)
            if check_dates is False:
                raise ValueError
            break
        except ValueError:
            print("Please try again, provide both dates like this: 01.02\n")
    while True:
        try:
            # https://stackoverflow.com/questions/57062794/how-to-check-if-a-string-has-any-special-characters
            user_reason = input("\nPlease provide a reason"
                                " (maximum 25 characters):\n")
            check_reason = check_string(user_reason)
            if check_reason is False:
                raise ValueError
            else:
                request_data = (cap_first_name + "," + cap_last_name + "," +
                                str(starting_date) + "," + str(ending_date)
                                + "," + user_reason)
                request_data = request_data.split(",")
                request_data_for_sw = [i.strip() for i in request_data]
                update_worksheet(request_data_for_sw, "Time Off Requests")
                print("\nPlease wait, we are processing your request...\n")
            break
        except ValueError:
            print("Please provide a reason, maximum 25 characters. "
                  "You can write a number as long "
                  "as it's not at the beginning.")
    wait()
    wait()
    approve_request()


# Randomly approves or disapproves a request for time off.
def approve_request():
    random_number = random.randint(1, 10)
    if random_number % 2 == 0:
        print("Your request for time off was approved!")
        wait()
        return True
        give_options()
    else:
        print("Your request for time off was not approved. "
              "You can challenge disapproval if needed and "
              "we will give you a call to discuss it.\n")
        challenge_disapproval()


# Lets the user challenge disapproval of request for a time off.
def challenge_disapproval():
    while True:
        try:
            challenge_choice = input("Do you want to "
                                     "challenge disapproval? Y/N:\n")
            if challenge_choice.capitalize() == "Y":
                wait()
                print("Thank you. We will get in touch soon to discuss it!")
                wait()
                return True
                give_options()
            elif challenge_choice.capitalize() == "N":
                wait()
                print("Thank you.")
                wait()
                return True
                give_options()
            else:
                raise ValueError
        except ValueError:
            print("Please try again, enter Y or N.\n")


def see_birthdays():
    """
    Prints out employees' names and birthdays.
    Then waits and asks the user what they want to do.
    """
    birthdays = SHEET.worksheet("Birthdays").get_all_values()
    for row in birthdays:
        first_name_birthday = row[0]
        last_name_birthday = row[1]
        age_day_birthday = row[2]
        age_month_birthday = row[3]
        employees_birthday = (last_name_birthday + ", " + first_name_birthday +
                              ": " + age_day_birthday + "." +
                              age_month_birthday)
        print(employees_birthday)
    wait()
    return True
    give_options()


def see_roles():
    """
    Prints out employees and their roles.
    Then waits and asks the user what they want to do.
    """
    employees = SHEET.worksheet("Employees").get_all_values()
    for row in employees:
        employee_fname = row[0]
        employee_lname = row[1]
        role = row[2]
        data_to_print = employee_lname + ", " + employee_fname + " - " + role
        print(data_to_print)
    wait()
    return True
    give_options()


def main(cap_first_name, cap_last_name):
    """
    Main function which calls other functions
    based on user input.
    """
    while True:
        give_options()
        if user_input == 1:
            request_time_off(cap_first_name, cap_last_name)
        if user_input == 2:
            see_birthdays()
        if user_input == 3:
            see_roles()
        if user_input == 4:
            clear()
            sys.exit("You have exited the program. Thank you!")


# Calling the main function
main(cap_first_name, cap_last_name)
