import subprocess
import mysql.connector
import time

def bashclear():
    subprocess.run("clear")

def addbook():
    bashclear()
    book_name = input("Enter book name  : ")
    book_author = input("Enter book author : ")
    book_year = input("Enter book year   : ")

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="1101", database="asc_unsecure")
    cursor = mysqldb.cursor()
    
    cursor.execute(f"insert into books (bname, bauthor, year) values ('{book_name}', '{book_author}', '{book_year}');")
    mysqldb.commit()
    mysqldb.close()

    adminpage()    


def viewbookadmin():
    bashclear()
    print(" _________________________________________________")
    print("|                                                 |")
    print("| These are the books found in the system! Enjoy! |")
    print("|_________________________________________________|")
    
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="1101", database="asc_unsecure")
    cursor = mysqldb.cursor()
    
    cursor.execute(f"select * from books;")
    all_books = cursor.fetchall()

    for book in all_books:
        print (f"{book[1]}, by {book[2]} from the year {book[3]}")

    while True:
        choice = input("Back to main page? (y/n)")
        match choice:
            case "y":
                adminpage()
                break
            case "n":
                viewbookadmin()
                break
            case _:
                print("\nInvalid choice! Pick again:")

    adminpage()



def adminpage():
    bashclear()
    print(" _____________________________________________________")
    print("|                                                     |")
    print("| Welcome to the Book Managment System Administrator! |")
    print("|_____________________________________________________|")
    print("\n1. Add Book\n2. View Books\n3. Exit")

    while True:
        choice = input("\nChoice: ")
        match choice:
            case "1":
                addbook()
                break
            case "2":
                viewbookadmin()
                break
            case "3":
                exit()
            case _:
                print("Invalid choice! Pick again: ")

def viewbookuser():
    bashclear()
    print(" _________________________________________________")
    print("|                                                 |")
    print("| These are the books found in the system! Enjoy! |")
    print("|_________________________________________________|")
    
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="1101", database="asc_unsecure")
    cursor = mysqldb.cursor()
    
    cursor.execute(f"select * from books;")
    all_books = cursor.fetchall()

    for book in all_books:
        print (f"{book[1]}, by {book[2]} from the year {book[3]}")

    while True:
        choice = input("Back to main page? (y/n)")
        match choice:
            case "y":
                userpage()
            case "n":
                viewbookuser()
            case _:
                print("\nInvalid choice! Pick again:")

def adminpage():
    bashclear()
    print(" _____________________________________________________")
    print("|                                                     |")
    print("| Welcome to the Book Managment System Administrator! |")
    print("|_____________________________________________________|")
    print("\n1. Add Book\n2. View Books\n3. Exit")

    while True:
        choice = input("\nChoice: ")
        match choice:
            case "1":
                addbook()
                break
            case "2":
                viewbookadmin()
                break
            case "3":
                exit()
            case _:
                print("Invalid choice! Pick again: ")



def userpage():
    bashclear()
    print(" ____________________________________________")
    print("|                                            |")
    print("| Welcome to the Book Managment System User! |")
    print("|____________________________________________|")
    print("\n1. View Books\n2. Exit")

    while True:
        choice = input("\nChoice: ")
        match choice:
            case "1":
                viewbookuser()
            case "2":
                exit()
            case _:
                print("Invalid choice! Pick again: ")

def login():

    input_username = input("Username: ")
    input_password = input("Password: ")
    print("\n")

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="1101", database="asc_unsecure")
    cursor = mysqldb.cursor()

    cursor.execute(f"select username from cred where username='{input_username}';")
    db_out_un = cursor.fetchall()

    if len(db_out_un) == 0:
        print("Incorrect username or password!")
        mysqldb.close()
    else:
        db_username = db_out_un[0][0]

        cursor.execute(f"select password from cred where username='{db_username}';")
        db_out_pass = cursor.fetchall()

        if len(db_out_pass) == 0:
            print("Incorrect usernmae or password!")
            mysqldb.close()
        else:
            db_password = db_out_pass[0][0]

            if (input_username == db_username) and (input_password == db_password):
                if (input_username == "admin"):
                    adminpage()
                    mysqldb.close()
                else:
                    userpage()
                    mysqldb.close()
            else:
                print("Incorrect usernmae or password!")
                mysqldb.close()
        
def main():
    bashclear()
    print(" _________________________________________________________________")
    print("|                                                                 |")
    print("| Welcome to the Book Managment System! Please log in to proceed! |")
    print("|_________________________________________________________________|")
    
    login()

main()