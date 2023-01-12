import subprocess
import mysql.connector

mysqldb = mysql.connector.connect(host="localhost", user="root", password="1101")

cursor = mysqldb.cursor()

cursor.execute("") #sql statement

def bashclear():
    subprocess.run("clear")

def login():

    username = input("\nUsername: ")
    password = input("\nPassword: ")
    print("\n")

    #set up db so that login can be checked

def main():
    bashclear()
    print(" _________________________________________________________________|")
    print("|                                                                 |")
    print("| Welcome to the Book Managment System! Please log in to proceed! |")
    print("|_________________________________________________________________|")
    
    login()