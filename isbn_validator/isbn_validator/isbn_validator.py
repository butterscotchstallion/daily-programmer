#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint


class ISBNValidator:
    """
    Validates an ISBN:
    obtain the sum of 10 times the first digit,
    9 times the second digit, 8 times the third digit...
    all the way till you add 1 times the last digit.
    If the sum leaves no remainder when divided by
    11 the code is a valid ISBN.
    """
    def validate(self, isbn):
        isbn_without_hyphens = isbn.replace("-", "")
        multiplier = 10
        divisor = 11
        isbn_sum = 0

        if len(isbn_without_hyphens) != 10:
            return False

        for char in "".join(isbn_without_hyphens):
            """
            In the case of the check digit, the last digit of the ISBN,
            the upper case X can appear. The method of determining the
            check digit for the ISBN is the modulus 11 with the weighting
            factors 10 to 1. The Roman numeral X is used in lieu of 10
            where ten would occur as a check digit.
            """
            if char == "X":
                digit = 10
            else:
                try:
                    digit = int(char)
                except ValueError:
                    continue

            isbn_sum += digit * multiplier

            if multiplier == 1:
                break
            else:
                multiplier -= 1

        if isbn_sum > 0:
            return isbn_sum % divisor == 0

    def generate(self):
        is_valid = False
        isbn = None

        while not is_valid:
            isbn = "".join([str(randint(0, 9)) for x in range(0, 10)])
            is_valid = self.validate(isbn)

        return isbn
