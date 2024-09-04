""""
Description: A client program written to verify correctness of 
the activity classes.
Author: ACE Faculty
Edited by: {Student Name}
Date: {Date}
"""
#format 
from borrower_status.borrower_status import BorrowerStatus
from genre.genre import Genre
from library_item.library_item import LibraryItem
from library_user.library_user import LibraryUser

def main():
    """Test the functionality of the methods encapsulated 
    in this project.
    """ 
    # In the statements coded below, ensure that any statement that could result 
    # in an exception is handled.  When exceptions are 'caught', display the exception 
    # message to the console.

    # 1. Code a statement which creates an instance of the LibraryItem class with valid inputs.
    # Use your own unique valid values for the inputs to the class.
    try:
        library_item = LibraryItem(123,"Intermediate programming", "Mike",Genre.NON_FICTION,True)    
        library_user = LibraryUser(456,"Lily","lily08@gmail.com",BorrowerStatus.ACTIVE)
    # 2. Using the instance defined above, and the class Accessors, print 
    # each of the attributes of the LibraryItem instance.
        print(library_item.item_id)
        print(library_item.author)
        print(library_item.title)
        print(library_item.genre)
        print(library_item.is_borrowed)
        print(library_user.user_id)
        print(library_user.name)
        print(library_user.email)
        print(library_user.borrower_status)
    except ValueError as e:
        print(f"Error is:{e}")
    # 3. Code a statement which creates an instance of the LibraryItem class with one or more invalid inputs.
    # Use your own unique valid values for the inputs to the class.
    try:
        library_item = LibraryItem(" ", "Mike",Genre.NON_FICTION)
    except Exception as e:
        print(f"Error is:{e}")
    #Non-DELINQUENT user borrowing an item that is available.
    try:
        library_user = LibraryUser(456,"Lily","lily08@gmail.com",BorrowerStatus.ACTIVE)
        cosmetic_book = LibraryItem(124,"how to be beautiful", "Ross",Genre.NON_FICTION, False)
        result = library_user.borrow_item(cosmetic_book)
        print(result)
    except Exception as e:
        print(e)
    #DELINQUENT user borrowing an item that is available.
    try:
       delinquent_user = LibraryUser(458,"Moly","moly08@gmail.com",BorrowerStatus.DELINQUENT)
       cosmetic_book = LibraryItem(124,"how to be beautiful", "Ross",Genre.NON_FICTION, False)
       result = delinquent_user.borrow_item(cosmetic_book)
       print(result)
    except Exception as e:
        print(e)
    #Non-DELINQUENT user borrowing an item that is not available.
    try:
        library_user = LibraryUser(456,"Lily","lily08@gmail.com",BorrowerStatus.ACTIVE)
        science_book = LibraryItem(124,"science", "Ross",Genre.NON_FICTION, True)
        result = library_user.borrow_item(science_book)
        print(result)
    except Exception as e:
        print(e)
    # DELINQUENT user borrowing an item that is not available.
    try:
        delinquent_user = LibraryUser(458,"Moly","moly08@gmail.com",BorrowerStatus.DELINQUENT)
        science_book = LibraryItem(124,"science", "Ross",Genre.NON_FICTION, True)
        result = delinquent_user.borrow_item(science_book)
        print(result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()