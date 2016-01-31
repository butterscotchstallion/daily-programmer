#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Disemvoweler:
    """
    Removes the vowels and spaces from an input string
    """
    def disemvowel(self, user_input_string):
        chars_to_remove = [" ", "a", "e", "i", "o", "u"]
        output = user_input_string.translate(None, "".join(chars_to_remove))
        diff_chars = []
        output_chars = "".join(output)

        for char in "".join(user_input_string):
            if char != " " and char not in output_chars:
                diff_chars.append(char)

        return {
            "output": output,
            "diff_chars": "".join(diff_chars)
        }
