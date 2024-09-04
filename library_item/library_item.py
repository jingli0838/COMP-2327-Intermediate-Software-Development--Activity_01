""""
Description: A class to manage LibraryItem objects.
Author: {Jing Li}
Date: {9/1/2024}
"""

from genre.genre import Genre


class LibraryItem():
    def __init__(self, item_id:int, title:str, author:str, genre:Genre, is_borrowed:bool): 
        if isinstance(item_id,int):
            #An id number to uniquely identify the library item.
            self.__item_id = item_id
        else:
            raise ValueError("Item Id must be numeric.")
        
        if (len(title.strip())>0):
            self.__title = title
        else:
            raise ValueError("Title cannot be blank")
        
        if (len(author.strip())>0):
            self.__author = author
        else:
            raise ValueError("Author cannot be blank")
        
        if isinstance(genre,Genre):
            self.__genre = genre
        else:
            raise ValueError("Invalid Genre.")
        
        if isinstance(is_borrowed,bool):
            # Identifies whether the library item is borrowed (True) or available (False).
            self.__is_borrowed = is_borrowed 
        else:
            raise ValueError("Is Borrowed must be a boolean value.")
        
    @property
    def item_id(self) ->int:
        return self.__item_id
        
    @property
    def title(self) ->str:
        #return the title of the library item.
        return self.__title
    
    @property   
    def author(self) ->str:
        #return the author of the library item.
        return self.__author
    
    @property
    def genre(self) ->Genre:
        #return the Genre of the library item.
        return self.__genre
    
    @property
    def is_borrowed(self) ->bool:
        return self.__is_borrowed
    
    @is_borrowed.setter
    def is_borrowed(self,value:bool):
        if isinstance(value,bool):
            self.__is_borrowed = value  
        else:
            raise ValueError("Invalid is_borrowed value,must be boolean")  

    def __str__(self) -> str:
        return (f"Item ID: {self.__item_id}, Title: {self.__title}, "
                f"Author: {self.__author}, Genre: {self.__genre.value}, "
                f"Is Borrowed: {self.__is_borrowed}")  



