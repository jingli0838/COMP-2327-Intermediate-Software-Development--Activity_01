"""
Description: Unit tests for the Book class.
Author: {Jing Li}
Date: {9/1/2024}
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_book.py
"""

import unittest
from genre.genre import Genre
from library_item.library_item import LibraryItem

class TestLiabraryItem(unittest.TestCase):
    #test init input
    def test_init_valid(self):
        library_item = LibraryItem(123,"Intermediate programming", "Mike",Genre.NON_FICTION, True)

        self.assertEqual(123,library_item._LibraryItem__item_id)
        self.assertEqual("Intermediate programming",library_item._LibraryItem__title)
        self.assertEqual("Mike",library_item._LibraryItem__author)
        self.assertEqual(Genre.NON_FICTION,library_item._LibraryItem__genre)
        self.assertEqual(True,library_item._LibraryItem__is_borrowed)
    #test when set item id None
    def test_init_invalid_item_id_raise_exception(self):
        with self.assertRaises(ValueError):
            library_item = LibraryItem(None, "Intermediate programming", "Mike",Genre.NON_FICTION, True)
    #test when set item title null
    def test_init_invalid_title_raise_exception(self):
        with self.assertRaises(ValueError):
            library_item = LibraryItem(123,"","Mike",Genre.NON_FICTION,True)
    #test when set item author null
    def test_init_invalid_author_raise_exception(self):
        with self.assertRaises(ValueError):
            library_item = LibraryItem(123,"Intermediate programming","",Genre.NON_FICTION,True)
    #test when set item genre None  
    def test_init_invalid_Genre_raise_exception(self):
        with self.assertRaises(ValueError):
            library_item = LibraryItem(123,"Intermediate programming", "Mike",None,True)
    #test when set item is_borrowed equals to None
    def test_init_invalid_is_borrowed(self):
        with self.assertRaises(ValueError):
            library_item = LibraryItem(123,"Intermediate programming", "Mike",Genre.NON_FICTION, None)

    def setUp(self):
        self.library_item = LibraryItem(123,"Intermediate programming", "Mike",Genre.NON_FICTION,True)

    #test all attribute accessor
    def test_item_id_accessor(self):
        self.assertEqual(123,self.library_item.item_id)    

    def test_title_accessor(self):
        self.assertEqual("Intermediate programming",self.library_item.title)

    def test_author_accessor(self):
        self.assertEqual("Mike",self.library_item.author)

    def test_genre_accessor(self):
        self.assertEqual(Genre.NON_FICTION,self.library_item.genre)

    def test_is_borrowed_accessor(self):
        self.assertEqual(True,self.library_item.is_borrowed)
    #test is_borrowed setter
    def test_is_borrowed_setter_valid(self):
        self.library_item.is_borrowed = False
        self.assertEqual(False, self.library_item.is_borrowed)

    def test_is_borrowed_setter_invalid(self):
        with self.assertRaises(ValueError):
            self.library_item.is_borrowed = " "

    def test_str(self):
        expected = "Item ID: 123, Title: Intermediate programming, Author: Mike, Genre: 1, Is Borrowed: True"
        self.assertEqual(expected,str(self.library_item))
       


