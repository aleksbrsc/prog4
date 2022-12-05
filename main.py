import json

class Book:
    def __init__(self, _name, _author, _yearPublished):
        self._name = _name
        self._author = _author
        self._yearPublished = _yearPublished

    def getName(self):
        return self._name

    def setName(self, x):
        self._name = x
    
    def getAuthor(self):
        return self._author
    
    def setAuthor(self, x):
        self._author = x
    
    def getYearPublished(self):
        return self._yearPublished
    
    def setYearPublished(self, x):
        self._yearPublished = x

def write_json(data, filename="resources.json"):
    with open (filename, "w") as f:
        json.dump(data, f, indent=4)

def check_value(data, value):
    return any(player['name'] == value for player in data['books'])

def contains_letters(string):
    return any(x.isalpha() for x in string)

def contains_numbers(string):
    return any(x.isdigit() for x in string)

def showMainMenu():
    print("\nPlease select an option.\n(Create / Read / Update / Delete / Exit)\n")
    while True:
        crud = input("\u001b[90m> \u001b[0m").lower()
        # CREATE
        if crud == "create" or crud == "c":
            print("\nVery well.\n")
            # input validation for name, author, year published
            while True:
                try:
                    bookName = input("\u001b[90mEnter the book's name: \u001b[0m").strip()
                except: pass
                with open ("resources.json", "r") as json_file:
                    data = json.load(json_file)
                    if check_value(data, bookName) == True:
                        print("\n\u001b[31mThis book already exists in the Bing Chilling Library.\u001b[0m")
                        showMainMenu()
                if contains_letters(bookName):
                    break
                else:
                    print("\nInvalid book name.\n")
            while True:
                try:
                    bookAuthor = input("\u001b[90mEnter the author's name: \u001b[0m").lower().strip()
                except: pass
                if contains_letters(bookAuthor) and (contains_numbers(bookAuthor) == False):
                    break
                else:
                    print("\nInvalid author name.\n")
            while True:
                bookYear = 2023
                try:
                    bookYear = int(input("\u001b[90mEnter the year of publication: \u001b[0m"))
                except: pass
                if bookYear < 2023:
                    break
                else:
                    print("\nInvalid year of publication\n")
            # appends to resources.json
            with open ("resources.json") as json_file:
                data = json.load(json_file)
                temp = data["books"]
                createdBook = {"name": bookName, "author": bookAuthor, "yearPublished": bookYear}
                temp.append(createdBook)
                
            write_json(data)
            print("\n\u001b[32mYour book has been successfully added.\u001b[0m\n")
            print("Please select an option.\n(Create / Read / Update / Delete / Exit)\n")

        # Read
        elif crud == "read" or crud == "r":
            print("\nVery well.\n")

            print("Please select an option.\n(Create / Read / Update / Delete / Exit)\n")
        # Update
        elif crud == "update" or crud == "u":
            print("\nVery well.\n")

            print("Please select an option.\n(Create / Read / Update / Delete / Exit)\n")
        # Delete
        elif crud == "delete" or crud == "del" or crud == "d":
            print("\nVery well.\n")

            print("Please select an option.\n(Create / Read / Update / Delete / Exit)\n")
        # Exit
        elif crud == "exit" or crud == "e":
            print("\nVery well.\n")
            quit()
        else:
            print("\nThat was not a valid option. Please try again\n(Create / Read / Update / Delete / Exit)\n")

def run():
    print("\n\u001b[90m~\u001b[0m MAIN MENU\n\nYou have arrived at Bing Chilling Library. Would you like to enter?\n(yes / no)\n")
    while True:
        cont = input("\u001b[90m> \u001b[0m").lower()
        if cont == "yes" or cont == "y":
            break
        elif cont == "no" or cont == "n":
            print("\nPlease add the following information.\n")
            quit()
        else:
            print("\nThat was not a valid option. Please try again\n(yes / no)\n")
    showMainMenu()

run()