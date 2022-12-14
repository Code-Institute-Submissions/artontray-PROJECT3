"""
 File used for custom print function and coloring strings
"""
import os
from textwrap import wrap

NB_LINES_MAX_OUTPUT = 24  # Number of lines maximum for the terminal output


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
    os.system('clear')  # Clear the screen before a new message
    message = message.splitlines()  # Split the message detecting "\n" caracter
    nb_lines = 0
    SIZE = 50  # max letters per line
    print("\n\n\n")
    print("." * (SIZE + 4))
    str_empty = " "
    for i in range(0, len(message)):
        # wrapping if message is bigger than SIZE
        message_tab = wrap(message[i], SIZE)
        j = 1
        while j <= len(message_tab):
            nb_lines += 1
            str = message_tab[j-1]
            j += 1
            if str.count(":") == 1:
                str = str.split(":")
                #  number of caracter around
                #  coloring message \033[32;1m{text}\033[0m
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
                print(f"| {str.center(SIZE, ' ')} |")
    nb_lines += 13  # 13 is the number of lines for the cowsay design below
    print("." * (SIZE + 4))
    for i in range(0, (NB_LINES_MAX_OUTPUT - nb_lines)):
        print("       .  ")
    print("        .   ^__^")
    print("          . (oo) _______")
    print("            (__)  Milka  )--/ ")
    print("                ||----w|| ")
    print("                ||     || ")
    print("                ||     || ")
    print(green_string(r"/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/"))


def welcome_print():
    """
    Method to print a welcome message for first visit
    """

    print(r" _    _ _____ _     _____ ________  ___ _____   _____ _____")
    print(r"| |  | |  ___| |   /  __ \  _  |  \/  ||  ___| |_   _|  _  |")
    print(r"| |  | | |__ | |   | /  \/ | | | .  . || |__     | | | | | |")
    print(r"| |/\| |  __|| |   | |   | | | | |\/| ||  __|    | | | | | |")
    print(r"\  /\  / |___| |___| \__/\ \_/ / |  | || |___    | | \ \_/ /")
    print(r" \/  \/\____/\_____/\____/\___/\_|  |_/\____/    \_/  \___/ ")

    print(r"   ___ _   _ _____ _____ _____  ____________ _______   __ ")
    print(r"  |_  | | | /  ___|_   _|  ___| | ___ \ ___ \_   _\ \ / /  ")
    print(r"    | | | | \ `--.  | | | |__   | |_/ / |_/ / | |  \ V /  ")
    print(r"    | | | | |`--. \ | | |  __|  |  __/|    /  | |  /   \ ")
    print(r"/\__/ / |_| /\__/ / | | | |___  | |   | |\ \ _| |_/ /^\ \  ")
    print(r"\____/ \___/\____/  \_/ \____/  \_|   \_| \_|\___/\/   \/  ")
    print("     O          ")
    print("      O     ^__^")
    print("        ??   (oo) _______")
    print("            (__)  Milka  )--/ ")
    print("                ||----w|| ")
    print("                ||     || ")
    print(green_string(r"/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/"))
    input("Press enter to Play...").center
