""""
Description: A class to manage User objects.
Author: {Jing Li}
Date: {9/1/2024}
"""
from borrower_status.borrower_status import BorrowerStatus
from email_validator import validate_email, EmailNotValidError

from library_item.library_item import LibraryItem


class LibraryUser:
    def __init__(self, user_id:int, name:str, email:str, borrower_status: BorrowerStatus):
        if not isinstance(user_id,int):
            raise ValueError("User Id must be numeric")
        if (user_id<99):
            raise ValueError("Invalid User Id.")
        self.__user_id = user_id
        
        if(len(name.strip())>0):
            self.__name = name
        else:
            raise ValueError("Name cannot be blank.")
        
        try:
            user_email = validate_email(email)
            self.__email = user_email.email
        except EmailNotValidError:
            raise ValueError("Invalid email address.")
        
        if isinstance(borrower_status,BorrowerStatus):
            self.__borrower_status = borrower_status
        else:
            raise ValueError("Invalid Borrower Status.")
        
    @property
    def user_id(self) ->int :
        return self.__user_id
    
    @property
    def name(self) ->str:
        return self.__name
    
    @property
    def email(self) ->str:
        return self.__email
    
    @property
    def borrower_status(self) ->BorrowerStatus:
        return self.__borrower_status
    
    #set borrower_status
    @borrower_status.setter
    def borrower_status(self,status: BorrowerStatus):
        if not isinstance(status,BorrowerStatus):
            raise ValueError("Invalid Borrower Status.")
        self.__borrower_status = status
  
    def borrow_item(self,item:LibraryItem) ->str:
        '''
        when users want to borrow a book, they are not allowed to borrow if users' borrower_status are DELINQUENT or if item is borrowed by others 
        and raise exception.
        when users want to borrow a book, they are not allowed to borrow if users' borrower_status are MINOR or if item'genre is TRUE_CRIME, 
        and raise exception.
        if the bove are all not true, then they can borrow books, and modify the item.is_borrowed (borrowed by this user) into TRUE, and retrun a message indicating user is allowed to borrow.
        '''
        if self.borrower_status == BorrowerStatus.DELINQUENT:
            raise Exception (f"{self.name} cannot borrow an item due to their {self.borrower_status.name} status")
        elif item.is_borrowed:
            raise Exception (f"{item.title} has already been borrowed")
        elif item.genre.value == 3 and self.borrower_status.value == 3:
            raise Exception(f"{self.name} is not allowed to borrow this book{item.title} due to the {self.borrower_status}")
        else:
            item.is_borrowed = True
            return f"{self.name} is eligible to borrow the item."
        
    def return_item(self, item:LibraryItem) ->str:
        '''
        when DELINQUENT users returned the book, modify their borrower_status into ACtive and return a message to explain.
        when users are not DELINQUENT and returned a book, modify is_borrowed attribute of the item in to false, indicating the book now is available
        or if the bove are all not true, then retrun a message indicating the book is not borrowed.
        '''
        if self.borrower_status == BorrowerStatus.DELINQUENT:
            self.borrower_status = BorrowerStatus.ACTIVE
            return f"Item successfully returned. {self.name} has returned the item, status now changed to: {self.borrower_status.name}."
        if item.is_borrowed:
            item.is_borrowed = False
            return f"Item successfully returned.{self.name} has returned the item, {item.title} can be borrowed now "
        else:
            return "Item was not borrowed."
    
    def __str__(self) -> str:
        return f"user_id:{self.__user_id},name:{self.__name},email address:{self.__email},the borrower status is:{self.__borrower_status}"


  

        
        

