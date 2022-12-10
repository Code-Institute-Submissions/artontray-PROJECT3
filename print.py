"""
 File used for custom print function and coloring strings
"""
import os
from textwrap import wrap

def blue_string(text):
    """
    Return a string in the colour blue
    """
    string = f"\033[36;1m{text}\033[0m"
    # print(len(text))
    # print(len(string))
    return string

def green_string(text):
    """
    Return a string in the colour green
    """
    string = f"\033[32;1m{text}\033[0m"
    return string


def red_string(text):
    """
    Return a string in the colour red
    """
    string = f"\033[31;1m{text}\033[0m"
    return string


def my_print(message):
    """
    Return an custom print message
    3 cases :
    - Normal strings : will display in the center of the custom box message
    - Strings with ":" which means its a score tab or
    listing tab (example -> Name : score)
    - Strings with ":" and a color, for example -> red:Error, wrong number!
    It will return a message in the associated color
    """
    os.system('clear') # Clear the screen before a new message
    message = message.splitlines()  # Split the message detecting "\n" caracter
    SIZE = 50  # max letters per line
    print("\n\n\n")
    print("." * (SIZE + 4))
    str_empty = " "
    for i in range(0, len(message)):
        # wrapping if message is bigger than SIZE
        message_tab = wrap(message[i], SIZE)
        j = 1
        while j <= len(message_tab):
            str = message_tab[j-1]
            j += 1
            if str.count(":") == 1:
                str = str.split(":")
                a = SIZE + 11 # 11 is the number of caracter around coloring message f"\033[32;1m{text}\033[0m"
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
                print(f"| {str.center(SIZE, ' ')} |")
    print("." * (SIZE + 4))
    print("      O     ^__^")
    print("        ˚   (oo) _______")
    print("            (__)  Milka  )--/ ")
    print("                ||----w|| ")
    print("                ||     || ")
    print(green_string("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ \n"))
    print("\n")


def welcome_print():
    """
    Method to print a welcome message for first visit
    """

    print(''' _    _ _____ _     _____ ________  ___ _____   _____ _____ 
| |  | |  ___| |   /  __ \  _  |  \/  ||  ___| |_   _|  _  |
| |  | | |__ | |   | /  \/ | | | .  . || |__     | | | | | |
| |/\| |  __|| |   | |   | | | | |\/| ||  __|    | | | | | |
\  /\  / |___| |___| \__/\ \_/ / |  | || |___    | | \ \_/ /
 \/  \/\____/\_____/\____/\___/\_|  |_/\____/    \_/  \___/  \n''')

    print('''   ___ _   _ _____ _____ _____  ____________ _______   __ 
  |_  | | | /  ___|_   _|  ___| | ___ \ ___ \_   _\ \ / /  
    | | | | \ `--.  | | | |__   | |_/ / |_/ / | |  \ V /  
    | | | | |`--. \ | | |  __|  |  __/|    /  | |  /   \ 
/\__/ / |_| /\__/ / | | | |___  | |   | |\ \ _| |_/ /^\ \  
\____/ \___/\____/  \_/ \____/  \_|   \_| \_|\___/\/   \/   \n''')
    print("     O          ")
    print("      O     ^__^")
    print("        ˚   (oo) _______")
    print("            (__)  Milka  )--/ ")
    print("                ||----w|| ")
    print("                ||     || ")
    print(green_string("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ \n"))
    input("Press enter to Play...").center