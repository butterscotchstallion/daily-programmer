#!/usr/bin/env python
# -*- coding: utf-8 -*-
from isbn_validator import ISBNValidator


class TestISBNValidator:
    def test_isbn_validate_valid_isbn(self):
        expected = True
        isbn = "0-7475-3269-9"
        isbn_validator = ISBNValidator()
        actual = isbn_validator.validate(isbn)

        assert expected == actual

    def test_isbn_validate_invalid_isbn(self):
        expected = False
        isbn = "0-7475-3269-meow"
        isbn_validator = ISBNValidator()
        actual = isbn_validator.validate(isbn)

        assert expected == actual

    def test_isbn_validate_x_isbn(self):
        expected = False
        isbn = "0-7475-3269-X"
        isbn_validator = ISBNValidator()
        actual = isbn_validator.validate(isbn)

        assert expected == actual

    def test_isbn_generate_isbn(self):
        expected = True
        isbn_validator = ISBNValidator()
        generated_isbn = isbn_validator.generate()
        is_valid = isbn_validator.validate(generated_isbn)

        assert expected == is_valid
