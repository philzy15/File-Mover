#app that will help you move a file to whatever directory you want
import os , re

#main function to start the program
def main():
    choice = input(f"Hello what you like to do?\n1.Move File\n2.Rename File\n3.Delete file\nAny other key to exit\n")
    user_choice(choice)

#case structure to allow the user to choose what they want to do.
def user_choice(choice):
    match choice:
        case '1':
            print("You have chosen to move a file\n")
            move_file()
        case '2':
            print("You have chosen to rename a file\n")
            rename_file()
        case '3':
            print("You have chosen to delete a file\n")
            remove_file()
        case _:
            print("You have not selected a proper choice")
            exit


#Function to move the file
def move_file():
    file_path = input(f"Which file would you like to move? Please provide full file path\n")
    moved_to = input(f"Where would you like the file to go? Please provide full file path\n")
    os.replace(file_path, moved_to)
    directory_path = os.path.dirname(moved_to)
    contents = os.listdir(directory_path)
    print(contents)
    exit
 
#Function to rename the file
def rename_file():
    file_path = input(f"Which file would you like to rename? Please provide full file path\n")
    renamed = input(f"Where would you like the file to go? Please provide full file path\n")
    os.rename(file_path, renamed)
    directory_path = os.path.dirname(renamed)
    contents = os.listdir(directory_path)
    print(contents)
    exit

#Function to delete the file
def remove_file():
    file_path = input(f"Which file would you like to delete? Please provide full file path\n")
    print(file_path)
    os.remove(file_path)
    directory_path = os.path.dirname(file_path)
    contents = os.listdir(directory_path)
    print(contents)
    exit

#while loop to continue if the user wants to keep working 
work = 'Y'
while work == 'Y':
    main()
    print("\nDo you wish to continue? Y/N")
    work = input().upper()


#next we need to make a gui and be able to click and add the path instead of typing it in. Will probs end up using tkinter for this