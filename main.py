import os
import pyfiglet
from rich import print
from datetime import datetime

def print_formatted_text(text):
    formatted_text = pyfiglet.figlet_format(text, font="small")
    print(f"[yellow]{formatted_text}[/yellow]")
    return formatted_text

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    sss = """
    
                                           ___________________________________________
                                          |    1 - ASCCI transfer  |    6 -           |              
                                          |    2 - uppercaser      |    5 -           |   
                                          |    3 - lowercaser      |    0 - AllAtOnce |             
                                          |________________________|__________________|
                                        
    """
    print(sss)
    print("Enter your text:")
    user_input = input()
    try:
        num = int(input("num:\n"))
    except ValueError:
        print("Invalid input. Please enter a number.")
        input("Press Enter to continue...")
        continue

    if num == 1:
        formatted_text = print_formatted_text(user_input)
    elif num == 2:
        result = user_input.upper()
        print(result)
    elif num == 3:
        result2 = user_input.lower()
        print(result2)
    elif num == 0:
        formatted_text = print_formatted_text(user_input)
        result = user_input.upper()
        print()
        print(result)
        result2 = user_input.lower()
        print()
        print(result2)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Invalid option. Please select a valid option.")
        input("Press Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
    
    append_to_file = input("Do you want to append the text to a file? (y/n)\n")
    if append_to_file.lower() == 'y':
        with open('output.txt', 'a') as file:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"\n\nTime: {current_time}\n")
            file.write(f"Original text: {user_input}\n")
            if num == 1:
                file.write(f"Formatted text:\n\n{formatted_text}\n")
            elif num == 2:
                file.write(f"Uppercased text:\n\n{result}\n")
            elif num == 3:
                file.write(f"Lowercased text:\n\n{result2}\n")
            elif num == 0:
                file.write(f"\nFormatted text:\n\n{formatted_text}\n")
                file.write(f"\nUppercased text:\n\n{result}\n")
                file.write(f"\nLowercased text:\n\n{result2}\n")
            print("\nTransfer succeeded.\n")
    
    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')
