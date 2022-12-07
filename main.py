import json
from pprint import pprint

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

# checks if a string contains alphabet characters
def contains_letters(string):
    return any(x.isalpha() for x in string)

# checks if a string contains numeric characters
def contains_numbers(string):
    return any(x.isdigit() for x in string)

# function for writing to the file resources.json
def write_json(data, filename="resources.json"):
    with open (filename, "w") as f:
        json.dump(data, f, indent=4)

# checks if a book with the same name (value) already exists inside of the json file
def check_identical_value(data, value):
    return any(book['name'] == value for book in data)

def view():
    with open ("resources.json", "r") as f:
        temp = json.load(f)
        i = 1
        for book in temp:
            name = book["name"]
            author = book["author"]
            yearPublished = book["yearPublished"]
            print(f"~ Book #{i}:")
            print(f"Name: {name}\nAuthor: {author}\nYear published: {yearPublished}\n")
            i += 1

# searches for a book in the json file given its name and then prettyprints it
def search(data, name):
    for book in data:
        if book['name'] == name:
            print(book)

# prompts user to add a book to the json file
def create():
# input validation for name, author, year published
    while True:
        bookName = input("\u001b[90mEnter the book's name: \u001b[0m").strip()
        with open ("resources.json", "r") as json_file:
            data = json.load(json_file)
            if check_identical_value(data, bookName):
                print("\n\u001b[31mThis book name already exists in the Bing Chilling Library.\u001b[0m")
                showMainMenu()
        if contains_letters(bookName):
            break
        else: print("\nInvalid book name.\n")
    while True:
        bookAuthor = input("\u001b[90mEnter the author's name: \u001b[0m").lower().strip()
        if contains_letters(bookAuthor) and (contains_numbers(bookAuthor) == False):
            break
        else: print("\nInvalid author name.\n")
    while True:
        bookYear = 2023
        try:
            bookYear = int(input("\u001b[90mEnter the year of publication: \u001b[0m"))
        except: pass
        if bookYear < 2023:
            break
        else: print("\nInvalid year of publication\n")
    # appends to resources.json
    with open ("resources.json") as json_file:
        data = json.load(json_file)
        createdBook = {"name": bookName, "author": bookAuthor, "yearPublished": bookYear}
        data.append(createdBook)
    write_json(data)
    print("\n\u001b[32mYour book has been successfully added.\u001b[0m")

def update():
    with open ("resources.json", "r") as json_file:
        data = json.load(json_file)
    bookName = input("\u001b[90mEnter the book's name: \u001b[0m").strip()
    if check_identical_value(data, bookName) == True:
        print("\n\u001b[32mWe found the following book:\u001b[0m")
        search(data, bookName) #prints the book info
        while True:
            try:
                updateKind = input("\nEnter a valid kind of update.\n(name / author / year published)\n\n\u001b[90m> \u001b[0m").lower()
            except: pass
            #update name
            if updateKind == "name" or updateKind == "n":
                while True:
                    bookNewName = input("\n\u001b[90mEnter the new book name: \u001b[0m").strip()
                    if check_identical_value(data, bookNewName) == True:
                        print("\n\u001b[31mThis book name already exists in the Bing Chilling Library.\u001b[0m")
                        showMainMenu()
                    if contains_letters(bookNewName):
                        break
                    else: print("\n\u001b[31mInvalid book name. Please try again\u001b[0m")
                for i, book in enumerate(data):
                    if book['name'] == bookName:
                        data[i]['name'] = bookNewName
                        with open ("resources.json", "w") as f:
                            json.dump(data, f, indent=4)
                        print("\n\u001b[32mYour book has been successfully edited.\u001b[0m")
                        showMainMenu()
            #update author
            elif updateKind == "author" or updateKind == "a":
                while True:
                    bookAuthor = input("\n\u001b[90mEnter the new author name: \u001b[0m").lower().strip()
                    if contains_letters(bookAuthor) and (contains_numbers(bookAuthor) == False):
                        break
                    else: print("\n\u001b[31mInvalid author name. Please try again\u001b[0m")
                for i, book in enumerate(data):
                    if book['name'] == bookName:
                        data[i]['author'] = bookAuthor
                        with open ("resources.json", "w") as f:
                            json.dump(data, f, indent=4)
                        print("\n\u001b[32mYour book has been successfully edited.\u001b[0m")
                        showMainMenu()
            #update year published
            elif updateKind == "year published" or updateKind == "year" or updateKind == "y":
                updateSelected = 3
                while True:
                    bookYear = 2023
                    try:
                        bookYear = int(input("\n\u001b[90mEnter the new year of publication: \u001b[0m"))
                    except: pass
                    if bookYear < 2023:
                        break
                    else: print("\n\u001b[31mInvalid year of publication. Please try again\u001b[0m")
                for i, book in enumerate(data):
                    if book['name'] == bookName:
                        data[i]["yearPublished"] = bookYear
                        with open ("resources.json", "w") as f:
                            json.dump(data, f, indent=4)
                        print("\n\u001b[32mYour book has been successfully edited.\u001b[0m")
                        showMainMenu()
            else: 
                print("\n\u001b[31mThat was not a valid option. Please try again\u001b[0m")
    else:
        print("\n\u001b[31mSuch a book does not exist in the Bing Chilling Library\n\u001b[90m(double-check spelling, capitalization or other errors)\u001b[0m")
        showMainMenu()

# prompts user to enter a book to be deleted from the json file
def delete():
    new_data = []
    with open ("resources.json", "r") as json_file:
        data = json.load(json_file)
        try:
            bookName = input("\u001b[90mEnter the book's name: \u001b[0m").strip()
        except: pass
        if check_identical_value(data, bookName) == True:
            print("\nWe have found the book following book:")
            search(data, bookName) #prints the book info
            for i, book in enumerate(data):
                if book['name'] == bookName:
                    print("\u001b[32mThe book has been successfully deleted.\u001b[0m")
                    data.pop(i)
                    with open ("resources.json", "w") as f:
                        json.dump(data, f, indent=4)
        else:
            print("\n\u001b[31mSuch a book does not exist in the Bing Chilling Library\n\u001b[90m(double-check spelling, capitalization or other errors)\u001b[0m")
            showMainMenu()

# shows user the main menu options
def showMainMenu():
    while True:
        crud = input("\nPlease select a valid option.\n(Create / List / Search / Update / Delete / Exit)\n\n\u001b[90m> \u001b[0m").lower()
        # CreateE
        if crud == "create" or crud == "c":
            print("\nVery well.\n")
            create()
        # List
        elif crud == "List" or crud == "l":
            print("\nHere is a list of all books in the Bing Chilling Library:\n")
            view()
        # Search
        elif crud == "search" or crud == "s" or crud == "serach":
            print("\nVery well.\n")
            with open ("resources.json", "r") as json_file:
                data = json.load(json_file)
                try:
                    bookName = input("\u001b[90mEnter the book's name: \u001b[0m").strip()
                except: pass
                if check_identical_value(data, bookName) == True:
                    # figure out search
                    print("\n\u001b[32mWe found the following book:\u001b[0m")
                    search(data, bookName)
                else:
                    print("\n\u001b[31mSuch a book does not exist in the Bing Chilling Library\n\u001b[90m(double-check spelling, capitalization or other errors)\u001b[0m")
                    showMainMenu()
        # Update
        elif crud == "update" or crud == "u":
            print("\nVery well. Enter the book you want to update.\n")
            update()
        # Delete
        elif crud == "delete" or crud == "del" or crud == "d":
            print("\nVery well.\n")
            delete()
        # Exit
        elif crud == "exit" or crud == "e":
            print("\nVery well.\n")
            quit()

# starts program and asks user if they want to continue
def run():
    print("\n\u001b[90m~\u001b[0m MAIN MENU\n\nYou have arrived at Bing Chilling Library. Would you like to enter?\n(yes / no)\n")
    while True:
        cont = input("\u001b[90m> \u001b[0m").lower()
        if cont == "yes" or cont == "y":
            break
        elif cont == "no" or cont == "n":
            print("\nHave a nice day.\n")
            quit()
        else:
            print("\n\u001b[31mThat was not a valid option. Please try again\u001b[0m")
            print("\nWould you like to enter the library?\n(yes / no)\n")
    showMainMenu()

run()