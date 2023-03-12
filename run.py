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
