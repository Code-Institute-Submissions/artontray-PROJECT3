# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
import time
import os
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
    'Beginner',
    'Medium',
    'Hard',
    'Champion'
]
# Max Number for selected level of difficulty
MAX_NB_LEVEL0 = 100
MAX_NB_LEVEL1 = 500
MAX_NB_LEVEL2 = 1000
MAX_NB_LEVEL3 = 10000



def check_database(worksheet):
    """
    Check database, if worksheet does not exist we create it
    return True if worksheet exist or created successfully
    """
    try:
        worksheet_to_edit = SHEET.worksheet(worksheet)
        
    except gspread.exceptions.WorksheetNotFound:
        message = f"red:Error: Worksheet could not open.\n"
        message += f"blue:Creating worksheet..."
        my_print(message)
        input("Press Enter to continue...")
        worksheet = SHEET.add_worksheet(title=worksheet, rows="500", cols="2")
        data = ['name', 'time']
        worksheet.append_row(data)
    return True
        

def register_score(username, time, worksheet):
    """
    Register / Update username and time into selected worksheet
    - New line in the File if User is not already in the file
    - Update the File with new data if score is better
    """
    message = f"green:Congrats! Your time is {time} sec\n"
    message += "blue:Updating database, please wait......\n"
    my_print(message)
    # Check if username already in data base
    worksheet_to_edit = SHEET.worksheet(worksheet)
    cell = worksheet_to_edit.find(username)
    if worksheet_to_edit.find(username):
        # Username already exist
        if (int(time) < int(worksheet_to_edit.cell(cell.row, 2).value)):
            # We update the Time on excel File only if Time score is better
            worksheet_to_edit.update_cell(cell.row, 2, int(time))
            return "green:New Personal Record!\n"
        else:
            return "blue:No new Personal record this Time!\n"
    else:
        # First Time for this user, we register into Excel File
        data = [username, int(time)]
        worksheet_to_edit.append_row(data)
        return "blue:Your Score is registered!\n"



        
def Calcul_time(time_start, time_end):
    """
    Return the time in second between time_start and time_end
    """
    time = time_end - time_start
    return int(time)


def my_print(message):
    """
    Return an custom print message
    2 cases :
    - Normal strings : will display in the center of the custom box message
    - Strings with ":" which means its a score tab or
    listing tab (example -> Name : score)
    """
    os.system('clear')
    message = message.splitlines()  # Split the message detecting "\n" caracter
    SIZE = 50  # max letters per line
    print("\n\n\n")
    print("." * (SIZE + 4))
    str_empty = " "
    for i in range(0, len(message)):
        # For each line of message, we wrap into new
        # tab if message is bigger than SIZE
        message_tab = wrap(message[i], SIZE)
        j = 1
        while j <= len(message_tab):
            # For each line of message_tab
            str = message_tab[j-1]
            j += 1
            # We detect if existing ":" caracter
            # If so We split the message in 2 to display it in a nice way
            if str.count(":") == 1:
                str = str.split(":")
                a = SIZE + 11
                if str[0] == 'blue':
                    print(f"| {blue_string(str[1]).center(a,' ')} |")
                elif str[0] == 'red':
                    print(f"| {red_string(str[1]).center(a,' ')} |")
                elif str[0] == 'green':
                    print(f"| {green_string(str[1]).center(a,' ')} |")
                else:
                    a = SIZE - len(str[0]) - len(str[1]) - 3
                    # We place an empty string in the center after
                    # each line so "|" will end up always same place
                    
                    print(f"| {str[0]} : {str[1]}{str_empty.center(a, ' ')} |")
               
            else:
                # Normal string displayed middle of the box
                print(f"| {str.center(SIZE, ' ')} |")
    print("." * (SIZE + 4))
    print("      O     ^__^")
    print("        ˚   (oo) _______")
    print("            (__)  Milka  )--/ ")
    print("                ||----w|| ")
    print("                ||     || \n")
    print("\n")




def choose_level():
    """
    User can choose the level for the game
    can type 0, 1, 2 or 3
    """
    message = "green:Choose your level ?\n"
    message += "0:Beginner\n"
    message += "1:Medium\n"
    message += "2:Hard\n"
    message += "3:Champion\n"
    message_original = message
    while True:
        my_print(message)
        message = message_original
        try:
            level_user = int(input("Enter your level(Type 0, 1, 2 or 3) : \n"))
            if (level_user > 3) or (level_user < 0):
                message += "red:Wrong number!\n"
            else:
                break
        except ValueError:
            message += "red:Unauthorized Caracter!\n"
    return level_user

def clean_username(username):
    """
    Return a clean username without specific caracters
    """    
    
    char_to_remov = [":", "\\n", "\"", "\\t", "\\b", "\\a", "\\", " "]
    for char in char_to_remov:
        # Deleting some specific caracter
        username = username.replace(char, "")
    return username


def get_username():
    """
    Get username to register into Excel file
    """
    my_print("blue:Let\'s register your name!\n")
    while True:
        data_username = input("Enter your name here (7 caracters max): \n")
        data_username = clean_username(data_username)
        if validate_data(data_username):
            my_print(f"blue:Welcome {data_username} !")
            break
    return data_username



def validate_data(values):
    """
    Check the username input :
    Raises ValueError if strings more than 7 Caracters,
    or empty.
    """
   
    try:
        if len(values) > 7:
            raise ValueError(
                f"red:7 caracters as a maximum!"
            )
        if len(values) == 0:
            raise ValueError(
                f"red:Empty name, provide a name "
            )
    except ValueError as e:
        my_print(f"{e}, please try again.")
        return False

    return True


def get_time():
    """
    Return time : Used to calculate the time on-Game for scoring
    """
    return time.time()


def select_max_number(level):
    """
    Depending the value of "level", it will return a number max for the range
    """
    if level == 0:
        nb_max = MAX_NB_LEVEL0
    elif level == 1:
        nb_max = MAX_NB_LEVEL1
    elif level == 2:
        nb_max = MAX_NB_LEVEL2
    elif level == 3:
        nb_max = MAX_NB_LEVEL3
    else:
        nb_max = MAX_NB_LEVEL0
    return nb_max


def random_number(nb_max):
    """
    Return a number between 1 and nb_max
    """
    message = f"Computer have chosen a number between 1 and {nb_max}!\n"
    message += "green:GOOD LUCK!"
    my_print(message)
    return randint(1, nb_max)


def check_input_user(nb_max):
    """
    Return the int value if user_input is integer and inside the range
    """
    while True:
        try:
            user_input = int(input(f"Enter a number from 1 to {nb_max} : \n"))
            if user_input <= nb_max and user_input >= 0:
                return user_input
            else:
                raise ValueError(
                    print(red_string("Enter a number into the range!"))
                )
        except ValueError:
            print(red_string("Error, try again!"))


def check_result(user_guess_number, number_to_guess):
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


def build_timeline(number_to_guess, max_nb):
    """
    Build up a timeline :
    Array of 11 numbers from 0 to max_nb with calculated gaps in between
    example : [0, 31, 62, 93, 124, 155, 224, 293, 362, 431, 500]
    the number to guess will be always in the middle : 155 in this example
    """
    gap_btw_left_side = int(number_to_guess / 5)
    gap_btw_right_side = int((max_nb-number_to_guess)/5)
    if gap_btw_right_side == 0:
        gap_btw_right_side += 1

    timeline = []
    nb = 0
    # We add the number 0 in first position of the array
    timeline.append(nb)
    for i in range(0, 4):
        nb += gap_btw_left_side
        timeline.append(nb)
        # We add the number to guess in the middle of the array
    timeline.append(number_to_guess)
    nb = number_to_guess
    for i in range(0, 4):
        nb += gap_btw_right_side
        timeline.append(nb)
    # We add the number max_nb at the end of the array
    timeline.append(max_nb)
    return timeline


def show_timeline(timeline, input_user):
    """
    timeline is an array with timeline numbers.
    input user is the current guess from user.
    We display the current guess number into
    the timeline to show up where is situated
    the guess in comparation to the number to guess
    """
    i = 0
    timeline_string = f"blue:You enter the Number {input_user}\n"
    timeline_string += "-"*24 + "\n"
    timeline_string += "|"
    while i < (len(timeline)-1):
        if (input_user > timeline[i] and input_user <= timeline[i+1]):
            timeline_string += "X "
        else:
            if input_user == 0 and i == 0:
                timeline_string += "X "
            else:
                timeline_string += "- "
        if i == 4:
            timeline_string += "# "

        i += 1
    timeline_string += "|\n"
    timeline_string += "-"*24 + "\n"
    return timeline_string


def run_game(level):
    """
    Main function of the Game
    select a Random number according level attribute
    prompt for user to guess the number
    """
    nb_max = select_max_number(level)
    number_to_guess = random_number(nb_max)
    timeline = build_timeline(number_to_guess, nb_max)
    result = False
    while True:
        user_guess_number = check_input_user(nb_max)
        time_line_string = show_timeline(timeline, user_guess_number)
        result = check_result(user_guess_number, number_to_guess)
        if result is not True:
            message = f"{time_line_string}\n"
            message += f"blue:It's {result}, try Again!"
            my_print(message)
        else:
            break


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


def sort_result(worksheet):
    """
    Return a sorted tab by "Time" from a selected worksheet
    This tab will help to build up a scoring tab to show to user
    example :
    - from worksheet_to_sort.get() function we have a following result :
    [['damien']] [['22']]
    [['deuz']] [['12']]
    [['trois']] [['7']]
    [['quatre']] [['17']]
    [['fred']] [['11']]
    [['dsadsa']] [['6']]
    - This function will return a sorted list as the following result
    [(6, 'dsadsa'), (7, 'trois'), (11, 'fred'), (12, 'deuz'),
    (17, 'quatre'), (22, 'damien')]
    """
    worksheet_to_sort = SHEET.worksheet(worksheet)
    data = worksheet_to_sort.get_all_values()
    number_lines = len(data)
    tab = []
    for i in range(1, number_lines):
        time = f"B{i+1}"
        name = f"A{i+1}"
        time = str(worksheet_to_sort.get(time))
        name = str(worksheet_to_sort.get(name))
        time = time.replace("[['", "")
        time = time.replace("']]", "")
        name = name.replace("[['", "")
        name = name.replace("']]", "")
        tab.append((int(time), name))
    tab.sort()
    return tab


def show_scoring(score_tab, worksheet, user):
    """
    Return a string with the 5 first all-time record
    if user is not in the list (5 first best players) we 
    add his position in the scoring tab with 
    his position in the list.
    """
    
    message = f"Level {worksheet.upper()}\n"

    for i in range(0, len(score_tab)):
        if i < 5:
            if score_tab[i][1] == user:
                message += f"{i+1}:{score_tab[i][1]} - {score_tab[i][0]} sec          <-You\n"
            else:
                message += f"{i+1}:{score_tab[i][1]} - {score_tab[i][0]} sec\n"
        else:
            if score_tab[i][1] == user:
                message += f"{i+1}:{score_tab[i][1]} - {score_tab[i][0]} sec          <-You\n"
    return message


def instructions():
    """
    Return a instruction message to explain the rules of this game
    """
    get_instruction = True

    while get_instruction:
        instruction_command = input(
            "Do you want to see instruction(s) for this game? y/n : "
            )
        if instruction_command.lower() == "y":
            message = "The aim of this game is to guess "
            message += "a number between a selected range.\n"
            message += "4 differents levels of difficulty \n"
            message += "Beginner:1-100\n"
            message += "Medium:1-500\n"
            message += "Hard:1-1000\n"
            message += "Champion:1-10000\n"
            my_print(message)
            input("Press Enter to continue.... ")
            message = "When you have selected your level of difficulty, "
            message += "blue:Computer choose a number.\n"
            message += "You can try to guess this number as many time "
            message += "as you want, but time is running!!\n"
            message += "blue:Try to be fast to get good scoring!\n"
            my_print(message)
            input("Press Enter to continue.... ")
            message = "blue: Let\'s make an example!\n"
            message += "The number to guess is 153.\n"
            timeline = build_timeline(153, 1000)
            message += show_timeline(timeline, 40)
            message += "red:It\'s More\n"
            message += "blue:Computer will display a Timeline as above!\n"
            message += "On the middle the symbol # is the number to guess\n"
            message += "The X is showing how far you are from it !\n"
            my_print(message)
            input("Press Enter to continue.... ")
            message = "Let\'s try again!\n"
            timeline = build_timeline(153, 1000)
            message += show_timeline(timeline, 160)
            message += "red:It\'s Less\n"
            message += "You are very close to discover the number, try again"
            message += "... and so on...\n"
            my_print(message)
            input("Press Enter to continue.... ")
            message = "When you discovered my number, I will register "
            message += "your score by calculating your time! \n"
            message += "Challenge yourself and be the faster Player on "
            message += "the score tab!\n"
            my_print(message)
        elif instruction_command.lower() == "n":
            get_instruction = False
        else:
            my_print("red:That is not a valid option. Please try again!")


def main(user_name):
    """
    Main function of the Game
    1/Get instructions of the game : instructions()
    2/choose the level of the game : choose_level()
    3/Time is starting to get registered : start = get_time()
    4/Run the Game : run_game(user_level)
    5/user found the good number, we stop the Time : end = get_time()
    6/Calculate the time on-game : Calcul_time(start, end)
    7/According the selected level, we select a right
    worksheet : which_worksheet(user_level)
    8/We register the data into excel file : register_score(user_name,
    time_on_game,worksheet)
    9/We sort the files by Time value, smaller time is
    first : sort_result(worksheet)
    10/We show the scoring tab : show_scoring(score_tab,worksheet,user_name)
    """
    playing_game = True
    while playing_game:
        instructions()
        user_level = choose_level()
        start = get_time()
        run_game(user_level)
        end = get_time()
        time_on_game = Calcul_time(start, end)
        worksheet = which_worksheet(user_level)
        check_database(worksheet)
        result = register_score(user_name, time_on_game, worksheet)
        message = result
        score_tab = sort_result(worksheet)
        result = show_scoring(score_tab, worksheet, user_name)
        message += result
        my_print(message)
        instruction_command = input("Enter any key to play again or 'q' to quit : \n")
        if instruction_command.lower() == "q":
            playing_game = False
            my_print("Thank you for playing! Bye")

def blue_string(text):
    """ Print a string in the colour blue """
    string = f"\033[36;1m{text}\033[0m"
    # print(len(text))
    # print(len(string))
    return string

def green_string(text):
    """ Print a string in the colour green """
    string = f"\033[32;1m{text}\033[0m"
    return string


def red_string(text):
    """ Print a string in the colour red """
    string = f"\033[31;1m{text}\033[0m"
    return string

# my_print('green:Please enter your name please !\n')
user_name = get_username()
main(user_name)
