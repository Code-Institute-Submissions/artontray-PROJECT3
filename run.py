# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
import time
from textwrap import wrap
from random import randint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('LeJustePrix')
WORKSHEETS = [
    'Level_Low',
    'Level_Medium',
    'Level_Hard',
    'Level_Champion'
]

def register_score(username,time,worksheet):
    """
    Return an custom print message
    """
    # Check if username already in data base 


    
    # result = update_database(name_user,worksheet,time)
    worksheet_to_edit = SHEET.worksheet(worksheet)
    cell = worksheet_to_edit.find(username)



    if worksheet_to_edit.find(username):
        # print(f"Cell: {cell.row}") # 6
        # print(f"Col : {cell.col}") # 1
        # We update the line with existing name only if Time score is better
        if int(worksheet_to_edit.cell(cell.row, 2).value) > int(time):
            worksheet_to_edit.update_cell(cell.row, 2, int(time))
            return "NewRecord" 
        else:
            return "NoNewRecord"    
    else:
        data = [username,int(time)]
        worksheet_to_edit.append_row(data)
        return "NewEntries"  
            

def my_print(message):
    """
    Return an custom print message
    """
    # How much letters per line
    SIZE = 30
    message_tab = wrap(message, SIZE)
    i = 1
    print("\n")
    print("." * 33)
    while i <= len(message_tab):
        str = message_tab[i-1]
        print('|' + str.center(31, " ") + '|')
        i += 1
    print(".....   .........................")
    print("      O     ^__^")
    print("        ˚   (oo) _______")
    print("            (__)         )--/ ")
    print("                ||----w|| \n")


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
    message = f"Welcome {data_username}! "
    message += "Choose your level ?"
    message += "Type 0 for Beginner, "
    message += "1 for Medium, "
    message += "2 for Hard, "
    message += "and 3 for Champion"
    my_print(message)
    while True:
        try:
            level_user = int(input("Enter your level : \n"))
            
            if level_user > 3:
                raise ValueError(
                    f"Wrong number!"
                )
            else:
                break    
        except ValueError as e:
            my_print(f"{e} - Only Number 0, 1, 2 or 3... Try Again!")
    return level_user        





def get_username():
    """
    Get username to register into Excel file
    """
    while True:
        my_print("Let\'s register your name!")
        data_username = input("Enter your name here : \n")
        data_username = data_username.replace(" ", "")

        if validate_data(data_username):
            return data_username




def validate_data(values):
    """
    Check the username input :
    Raises ValueError if strings more than 12 Caracters,
    or empty.
    """
    try:
        
        # data = worksheet_to_edit.get_all_values()
        if len(values) > 12:
            raise ValueError(
                f"12 caracters as a maximum!"
            )
        if len(values) == 0:
            raise ValueError(
                f"Empty name, provide a name please"
            )
    except ValueError as e:
        print(f"{e}, please try again.\n")
        return False

    return True

def get_time():
    """
    Return time : Used to calculate the time on-Game for scoring
    """
    return time.time()


def select_max_number(level):
    """
    According the level attribute it will return a number max for the range
    """
    if level == 0:
        nb_max = 100
    elif level == 1:
        nb_max = 500
    elif level == 2:
        nb_max = 1000
    elif level == 3:
        nb_max = 10000        
    else:
        nb_max = 100
    return nb_max    


def random_number(nb_max):
    """
    Return a number between 1 and nb_max
    """
    return randint(1, nb_max)



def check_input_user(nb_max):
    """
    Return the int value if user_input is integer and inside the range
    """
    while True:
        try:
            user_input = int(input(f"Enter a guess number from 0 to {nb_max} : \n"))
            if user_input <= nb_max:
                return user_input
        except ValueError:
            print("Error, try again!")
    
def check_result(user_guess_number,number_to_guess):
    """
    Return True if user guess correctly the number
    Return "More" if user guess a number smaller than correct number
    Return "Less" if user guess a number bigger than correct number
    """
    if user_guess_number == number_to_guess:
        return True
    if user_guess_number > number_to_guess:
        return "Less"
    if user_guess_number < number_to_guess:
        return "More"    




    

def build_timeline(number_to_guess,max_nb):
    """
    Build up a timeline to show up the user where is
    situated his current guess in comparation to the
    number to guess
    """
    gap_btw_left_side = int(number_to_guess / 5)
    gap_btw_right_side = int((max_nb-number_to_guess)/5)
    timeline = []
    nb = 0
    timeline.append(nb)
    for i in range(0, 4):
        nb += gap_btw_left_side
        timeline.append(nb)
    nb =  number_to_guess   
    timeline.append(nb)    
    for i in range(0, 4):
        nb += gap_btw_right_side
        timeline.append(nb)
    timeline.append(max_nb)  
  
    return timeline 


def show_timeline(timeline,input_user):
    """
    timeline is an array with timeline numbers.
    input user is the current guess from user.
    We display the current guess number into 
    the timeline to show up where is situated
    the guess in comparation to the number to guess
    """
    i = 0
    timeline_string = f"You enter the Number : {input_user}                "
    timeline_string += "|"
    while i <= len(timeline):
        if i == 5: 
            timeline_string += "# "
            if input_user > timeline[i] and input_user < timeline[i+1]:
                timeline_string += "X " # input user is in between 2 values in the timeline
        elif i == len(timeline):
            timeline_string += "|" # we close the timeline
            break;
        elif input_user > timeline[i] and input_user < timeline[i+1]:
            timeline_string += "X " # input user is in between 2 values in the timeline
        elif input_user == timeline[i]:
            timeline_string += "X " # input user is exactly one of the value in timeline
        else:
            timeline_string += "- " # nothing to show, we draw a line
        i += 1
    return timeline_string

def run_game(level):
    """
    Main function of the Game
    select a Random number according level attribute
    prompt for user to guess the number
    """
    nb_max = select_max_number(level)
    number_to_guess = random_number(nb_max)
    print(number_to_guess)
    timeline = build_timeline(number_to_guess,nb_max)
    result = False
    # print(number_to_guess)
    while not result == True:
        user_guess_number = check_input_user(nb_max)
        time_line_string = show_timeline(timeline,user_guess_number)
        result = check_result(user_guess_number,number_to_guess)
        if result != True:
            my_print(f"{time_line_string}     It's {result}, try Again! ")

def which_worksheet(level):
    """
    Return the worksheet appropriate according the chosen level
    """
    if level == 0:
        worksheet = WORKSHEETS[level]
    elif level == 1:
        worksheet = WORKSHEETS[level]
    elif level == 2:
        worksheet = WORKSHEETS[level]
    elif level == 3:
        worksheet = WORKSHEETS[level]       
    else:
        worksheet = WORKSHEETS[0]
    return worksheet        


#worksheet_to_edit = SHEET.worksheet('Level_Low')

# take second element for sort
#def takeSecond(elem):
#    return elem[1]

# random list
#data = worksheet_to_edit.get_all_values()
# res = [eval(i) for i in data[i]]
# test_list = [int(i) for i in data[][i]]
# sort list with key
#data[0][1] = int(data[0][1])
#data.sort(key=takeSecond)
#print(data)


#def myFunc(e):
#  return e[1]


#data = worksheet_to_edit.get('B1')
#data.sort()
#print(data)
#number_lines = len(data)
#database = []
#for i in range(1, number_lines):
#    time = f"B{i+1}"
#    name = f"A{i+1}"
#    time = str(worksheet_to_edit.get(time))
#    name = str(worksheet_to_edit.get(name))
#    time = time.replace("[['", "")
#    time = time.replace("']]", "")
#    name = name.replace("[['", "")
#    name = name.replace("']]", "")
#    tab = []
#    # database[i-1]['name'] = name
#    # database[i-1]['time'] = time
#    tab.append((int(time),name))
#    # database.append(f'[{name},{time}]')
#    # print(f" Time {time} , Name : {name}")
#    database.append(tab)





#database.sort()

#print(database)







start = get_time()
# time.sleep(1)
user_name = get_username()
user_level = choose_level(user_name)
# my_print("your level is : " + str(user_level))
run_game(user_level)
end = get_time()
time_on_game = Calcul_time(start, end)
worksheet = which_worksheet(user_level)
result = register_score(user_name,time_on_game,worksheet)
message = f"Congrats! your time : {time_on_game} sec         "
if result == "NewEntries":
    message += "You are in score Tab"
elif result == "NoNewRecord":
    message += "No new record this Time!"
elif result == "NewRecord":
    message += "You made a New Record!"

my_print(message)
