# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
import time

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('LeJustePrix')

sales = SHEET.worksheet('Level_Low')

data = sales.get_all_values()

print(data)

def my_print(message):
    """
    Return an custom print message
    """
    print(f"  {message} ")
    print("______  __________")
    print("      \/         ")
    print("       \ ")
    print("        \   ^__^")
    print("         \  (oo)\_______")
    print("            (__)\       )\/")
    print("                ||----w |")
    print("                ||     ||")







def Calcul_time(time_start, time_end):
    """
    Return the time in second between time_start and time_end
    """
    time = time_end - time_start
    return int(time)

def get_username():
    """
    Get username to register into Excel file
    """
    while True:
        my_print("Let\'s register your name, Max 12 caracters, cannot be empty!")
        data_username = input("Enter your name here: \n")
        data_username = data_username.replace(" ", "")
        if validate_data(data_username):
            
            my_print("Data is valid!")
            break

    return data_username

def validate_data(values):
    """
    Check the username input :
    Raises ValueError if strings more than 12 Caracters,
    or empty.
    """
    try:
        if len(values) > 12:
            raise ValueError(
                f"12 caracters max, you provided {len(values)}"
            )
        if len(values) == 0 :
            raise ValueError(
                f"Empty name, provide a name please"
            )            
    except ValueError as e:
        my_print(f"Invalid data: {e}, please try again.\n")
        return False

    return True

start = time.time()
# time.sleep(1)
my_print(get_username())
end = time.time()
time = Calcul_time(start, end)
my_print(f"You finished the game in : {time} sec\n")