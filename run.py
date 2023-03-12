import datetime  # to check age
import math  # to check decimal
import sys  # to exit the program
import time  # to add pauses
from os import system  # to clear terminal
import re  # to check for special characters in a string input
import random  # to approve or disapprove requests for time off
import gspread  # to use google sheets
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("bank-job")