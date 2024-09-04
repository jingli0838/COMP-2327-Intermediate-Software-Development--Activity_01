"""
Description: Unit tests for the LibraryUser class.
Author: {Student Name}
Date: {Date}
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_library_user.py
"""

import unittest
from borrower_status.borrower_status import BorrowerStatus
from genre.genre import Genre
from library_item.library_item import LibraryItem
from library_user.library_user import LibraryUser

class TestLibraryUser(unittest.TestCase):
    # test init
    def test_init_valid(self):
        library_user = LibraryUser(456,"Lily","lily08@gmail.com",BorrowerStatus.ACTIVE)

        self.assertEqual(456,library_user._LibraryUser__user_id)
        self.assertEqual("Lily",library_user._LibraryUser__name)
        self.assertEqual("lily08@gmail.com",library_user._LibraryUser__email)
        self.assertEqual(BorrowerStatus.ACTIVE,library_user._LibraryUser__borrower_status)

    def test_init_invalid_user_id_raise_exception(self):
        with self.assertRaises(ValueError):
            library_user = LibraryUser(None,"Lily","lily08@gmail.com",BorrowerStatus.ACTIVE)

    def test_init_user_id_less_than_99_raise_exception(self):
        with self.assertRaises(ValueError):
            library_user = LibraryUser(45,"Lily","lily08@gmail.com",BorrowerStatus.ACTIVE)

    def test_init_invalid_name_raise_exception(self):
        with self.assertRaises(ValueError):
            library_user = LibraryUser(456," ","lily08@gmail.com",BorrowerStatus.ACTIVE)

    def test_init_invalid_email_raise_exception(self):
        with self.assertRaises(ValueError):
            library_user = LibraryUser(456,"Lily","  ",BorrowerStatus.ACTIVE)

    def test_init_invalid_borrower_status_raise_exception(self):
        with self.assertRaises(ValueError):
            library_user = LibraryUser(456,"Lily","lily08@gmail.com",None)
    # set up the information needed
    def setUp(self):
        self.library_user = LibraryUser(456,"Lily","lily08@gmail.com",BorrowerStatus.ACTIVE)
        self.delinquent_user = LibraryUser(458,"Moly","moly08@gmail.com",BorrowerStatus.DELINQUENT)
        self.minor_user = LibraryUser(457,"Monica","monica08@gmail.com",BorrowerStatus.MINOR)

        self.crim_book = LibraryItem(123,"Crime", "Mike",Genre.NON_FICTION, True)
        self.cosmetic_book = LibraryItem(124,"how to be beautiful", "Ross",Genre.NON_FICTION, False)
        self.science_book = LibraryItem(124,"science", "Ross",Genre.NON_FICTION, True)
        
    #test to get the attribute of user_id
    def test_user_id_accessor(self):
        self.assertEqual(456,self.library_user.user_id)
    #get the attribute of name
    def test_name_accessor(self):
        self.assertEqual("Lily",self.library_user.name)
    #test to get the attribute of email
    def test_email_accessor(self):
        self.assertEqual("lily08@gmail.com",self.library_user.email)
    #test to get the attribute of borrower_status
    def test_borrower_status_accessor(self):
        self.assertEqual(BorrowerStatus.ACTIVE,self.library_user.borrower_status)
    #test the __str__ method 
    def test_str(self):
        expected= "user_id:456,name:Lily,email address:lily08@gmail.com,the borrower status is:BorrowerStatus.ACTIVE"
        self.assertEqual(expected,str(self.library_user))
    #test borrow_item method when user is delinquent
    def test_borrow_item_user_delinquent(self):
        with self.assertRaises(Exception):
            self.delinquent_user.borrow_item(self.cosmetic_book)
    #test borrow_item method when user is minor(borrower_status.value == 3) and want to borrow a crime book(item.genre.value == 3)
    def test_borrow_item_user_minor_item_crime(self):
        with self.assertRaises(Exception):
            self.minor_user.borrow_item(self.crim_book)
    #test borrow_item method when the is_borrow equals to true
    def test_borrow_item_is_borrowed_true(self):
        with self.assertRaises(Exception):
            self.library_user.borrow_item(self.science_book)   
    #test borrow_item method when the is_borrow equals to false and borrow_status is not DELINQUENT or MINOR, and item.genre is not TURE_CRIME
    def test_borrow_item_available(self):
        expected = "Lily is eligible to borrow the item."
        self.assertEqual(expected,self.library_user.borrow_item(self.cosmetic_book))  
    #test return_item method  when user was DELINQUENT
    def test_return_item_users_delinquent(self):
       # self.delinquent_user.return_item(self.crim_book)
        result = self.delinquent_user.return_item(self.crim_book)
        self.assertEqual(BorrowerStatus.ACTIVE,self.delinquent_user.borrower_status)
        expected = "Item successfully returned. Moly has returned the item, status now changed to: ACTIVE."
        self.assertEqual(expected, result)
    #test return_item method to modify is_borrowed and return message as expected
    def test_return_item_is_borrowed_change_to_false(self):
        result= self.library_user.return_item(self.science_book)
        self.assertEqual(False,self.science_book.is_borrowed)
        expected = "Item successfully returned.Lily has returned the item, science can be borrowed now "
        self.assertEqual(expected,result)
    #test item is not borrowed
    def test_return_item_is_not_borrowed(self):
        expected = "Item was not borrowed."
        self.assertEqual(expected,self.library_user.return_item(self.cosmetic_book))
    