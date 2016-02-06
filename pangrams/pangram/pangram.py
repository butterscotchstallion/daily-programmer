#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Pangram:
    def is_pangram(self, input_string):
        alphabet_letter_count = 26
        letters_used = {}
        input_string_letters = [letter.lower() for letter in "".join(input_string)]

        for letter in input_string_letters:
            if letter == " " or letter == ".":
                continue

            if letter not in letters_used:
                letters_used[letter] = 0

            letters_used[letter] += 1

        number_of_letters_used = len(letters_used.keys())

        return {
            "letters_used": letters_used,
            "is_pangram": number_of_letters_used == alphabet_letter_count
        }
