#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pangram import Pangram


class TestPangram:
    def test_is_pangram_fox(self):
        input_string = "The quick brown fox jumps over the lazy dog."
        expected = True
        pangram = Pangram()
        actual = pangram.is_pangram(input_string)

        assert expected == actual["is_pangram"]

    def test_is_pangram_box(self):
        input_string = "Pack my box with five dozen liquor jugs"
        expected = True
        pangram = Pangram()
        actual = pangram.is_pangram(input_string)

        assert expected == actual["is_pangram"]

    def test_is_pangram_sax(self):
        input_string = "Saxophones quickly blew over my jazzy hair"
        expected = False
        pangram = Pangram()
        actual = pangram.is_pangram(input_string)

        assert expected == actual["is_pangram"]

    def test_is_pangram_fax(self):
        input_string = "fax machine"
        expected = False
        pangram = Pangram()
        actual = pangram.is_pangram(input_string)

        assert expected == actual["is_pangram"]
