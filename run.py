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

while True:
    try:
        """
        Asks for first name, checks for length,
        the input not being a number or null.
        Raises ValueError if input isn't valid.
        """
        first_name = input("\nPlease enter your"
                           " first name(maximum 20 characters):\n")
        cap_first_name = first_name.capitalize()
        if len(first_name) < 1 or len(first_name) > 20 or first_name.isnumeric() or not first_name.isalpha():
            raise ValueError
        break
    except ValueError:
        print("Please try again, enter your "
              "first name, maximum 20 characters.")

while True:
    try:
        """
        Asks for first name, checks for length,
        the input not being a number or null.
        Raises ValueError if input isn't valid.
        """
        last_name = input("\nPlease enter your last "
                          "name(maximum 20 characters):\n")
        cap_last_name = last_name.capitalize()
        if len(last_name) < 1 or len(last_name) > 20 or last_name.isnumeric() or not last_name.isalpha():
            raise ValueError
        break
    except ValueError:
        print("Please try again, enter your last name, maximum 20 characters.")

while True:
    try:
        """
        Asks for birth day, checks for input being a number between 1 and 31.
        If it's lower, higher, null or a string, raises ValueError.
        """
        age_day = int(input("\nPlease enter the day you were born:\n"))
        if age_day > 31 or age_day < 1:
            raise ValueError
        break
    except ValueError:
        print('Value must be a positive number and cannot be greater than 31.')

while True:
    try:
        """
        Asks for birth month, checks for input being a number between 1 and 12.
        If input is lower, higher, null or a string, raises ValueError.
        """
        age_month = int(input("\nPlease enter the month you were born:\n"))
        if age_month > 12 or age_month < 1:
            raise ValueError
        elif age_month == 2 and age_day > 29:
            raise ValueError
        break
    except ValueError:
        print('Value must be a positive number and must be between 1 and 12.')

while True:
    try:
        """
        Asks for birth year, calculates age of an employee.
        Checks for it to be between 18 and 80.
        If it's not, raises ValueError.
        If it is, updates birthday worksheet.
        """
        age_year = int(input("\nPlease enter the year you were born:\n"))
        date_of_birth = datetime.datetime(age_year, age_month, age_day)
        age = (datetime.datetime.now() - date_of_birth)
        days = int(age.days)
        converted_years = days/365
        employee_age = int(converted_years)
        if employee_age >= 18 and employee_age < 80:
            employee_birthday = cap_first_name + "," + cap_last_name + "," + str(age_day) + "," + str(age_month)
            employee_birthday = employee_birthday.split(",")
            employee_birthday_for_ws = [i.strip() for i in employee_birthday]
            update_worksheet(employee_birthday_for_ws, "Birthday")
        else:
            raise ValueError
        break
    except ValueError:
        print('Please try again, your age should be between 18 and 80.')

while True:
    try:
        """
        Asks for a role. Checks for length
        and input being a number or null.
        If data is valid, it is added to employees worksheet.
        If it isn't, raises a ValueError.
        """
        employee_role = input("\nPlease enter your job role"
                              "(maximum 20 characters):\n")
        cap_employee_role = employee_role.capitalize()
        if len(employee_role) < 1 or len(employee_role) > 20 or employee_role.isnumeric() or not employee_role.isalpha():
            raise ValueError
        elif len(employee_role) > 1:
            employee_data = cap_first_name + "," + cap_last_name + "," + cap_employee_role
            employee_data = employee_data.split(",")
            employee_data_for_ws = [i.strip() for i in employee_data]
            update_worksheet(employee_data_for_ws, "Employees")
            print("\nThank you, the data provided is "
                  "valid and is now added to our database.\n")
        break
    except ValueError:
        print("Please try again, your job role "
              "should be 20 characters maximum.")
