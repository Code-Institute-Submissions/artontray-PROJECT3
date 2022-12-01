# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
import time
from textwrap import wrap

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

#print(data)

def my_print(message):
    """
    Return an custom print message
    """
   
    SIZE = 22
   
    message_tab=wrap(message, SIZE)
    i = 1
    

    print("\n")
    print("˚" * 33)
    while i <= len(message_tab):
        str = message_tab[i-1]
        print('˚' + str.center(31, " ") + '˚')
        i += 1
    print("˚˚˚˚˚O˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚˚")
    print("      o     ^__^")
    print("        ˚   (oo)\_______")
    print("            (__)\       )\/")
    print("                ||----w||")







def Calcul_time(time_start, time_end):
    """
    Return the time in second between time_start and time_end
    """
    time = time_end - time_start
    return int(time)


def choose_level(data_username):
    """
    User can choose the level for the game
    can type 0, 1, 2 or 3
    """
    
    message = f"Welcome {data_username}, let's Play a Game!\n"
    message += "First, Choose your level ?\n"
    message += "0 for Beginner, \n"
    message += "1 for Medium, \n"
    message += "2 for Hard, \n"
    message += "and 3 for Champion\n"
    my_print(message)
    while True:
        try:
            level_user = int(input("Enter your level : \n"))
                

            if level_user > 3: 
                raise ValueError(
                    print(f"Type 0, 1, 2 or 3")
                )
            else:  
                break     
        except Exception:
            print("Error, Try Again!") 
        else:
            choose_level(data_username)    
    return level_user


            
def get_username():
    """
    Get username to register into Excel file
    """
    while True:
        my_print("Let\'s register your name, Max 12 caracters, cannot be empty!")
        data_username = input("Enter your name here : \n")
        data_username = data_username.replace(" ", "")
        if validate_data(data_username):
            return data_username
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
        print(f"{e}, please try again.\n")
        return False

    return True

start = time.time()
# time.sleep(1)
user_name = get_username()
user_level = choose_level(user_name)
my_print("your level is : " + str(user_level))
end = time.time()
time = Calcul_time(start, end)
my_print(f"You finished the game in : {time} sec\n")