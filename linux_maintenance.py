import os
import time

"""
Author: Rafał Zaręba

Python script that do all nessesary udates and upgrades in linux system
"""


def print_menu():
    """
    Function prints out the menu
    """
    os.system('clear')
    print("--------------LINUX SYSTEM MAINTENANCE MANAGER---------\n\n"
          "Choose what would you like to do: \n"
          "1. System cleaning\n"
          "2. Upgrade of all applications\n"
          "3. Upgrade system paths\n"
          "4. Full maintenance + reboot the computer\n"
          "5. Full maintenance + shutdown the computer\n"
          "6. Exit")


def countdown(process, seconds):
    """
    Function prints out the countdown
    :param process: name of process, that will start in seconds
    :param seconds: number of seconds
    :return:
    """
    for i in range(seconds, 0, -1):
        os.system('clear')
        print('{} process starts in {} seconds...'
              'To cancel press Ctrl+Z '.format(process, i))
        time.sleep(1)


print_menu()
choice = int(input('Choice : '))

while choice != 6:

    if choice == 1:
        os.system('clear')
        countdown(process='System cleaning', seconds=5)
        os.system('sudo apt-get autoremove')
        os.system('sudo apt-get autoclean')
        input('Press ENTER to continue...')

    elif choice == 2:
        os.system('clear')
        countdown(process='Application upgrade', seconds=5)
        os.system('sudo apt-get update')
        os.system('sudo apt-get upgrade -y')
        input('Press ENTER to continue...')

    elif choice == 3:
        os.system('clear')
        countdown(process='System paths upgrade', seconds=5)
        os.system('sudo apt-get dist-upgrade -y')
        input('Press ENTER to continue...')

    elif choice == 4:
        os.system('clear')
        countdown(process='Full maintenance + reboot', seconds=5)

        os.system('sudo apt-get update')
        os.system('sudo apt-get upgrade -y')
        os.system('sudo apt-get dist-upgrade -y')
        os.system('sudo updatedb')
        os.system('sudo apt-get autoremove')
        os.system('sudo apt-get autoclean')

        countdown(process='Reboot', seconds=10)
        os.system('sudo reboot')

    elif choice == 5:
        os.system('clear')
        countdown(process='Full maintenance + shutdown', seconds=5)

        os.system('sudo apt-get update')
      
        os.system('sudo apt-get upgrade -y')
        os.system('sudo apt-get dist-upgrade -y')
        os.system('sudo updatedb')
        os.system('sudo apt-get autoremove')
        os.system('sudo apt-get autoclean')

        countdown(process='Shutdown', seconds=10)
        os.system('sudo shutdown -h now')

    elif choice == 6:
        os.system('clear')
        os.system('exit')

    else:
        print('Wrong option passed, try: 1-6')

    print_menu()
    choice = int(input('Choice : '))


