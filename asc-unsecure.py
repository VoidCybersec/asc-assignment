import subprocess

def bashclear():
    subprocess.run("clear")

def login():

    username = input("\nUsername: ")
    password = input("\nPassword: ")
    print("\n")

    #set up db

def main():
    bashclear()
    print(" _________________________________________________________________|")
    print("|                                                                 |")
    print("| Welcome to the Book Managment System! Please log in to proceed! |")
    print("|_________________________________________________________________|")
    
    login()