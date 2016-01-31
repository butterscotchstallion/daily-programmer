#!/usr/bin/env python
# -*- coding: utf-8 -*-
from disemvoweler import Disemvoweler


class TestDisemvoweler:
    def test_disemvowel_cymbal(self):
        """
        Test 1
        """
        disem = Disemvoweler()
        voweled_input = "two drums and a cymbal fall off a cliff"
        expected = "twdrmsndcymblfllffclff"
        actual = disem.disemvowel(voweled_input)

        assert expected == actual["output"]
        assert "ouaaaaoai" == actual["diff_chars"]

    def test_disemvowel_psychokinesis(self):
        """
        Test 2
        """
        disem = Disemvoweler()
        psychokinesis = "all those who believe in psychokinesis raise my hand"
        expected = "llthswhblvnpsychknssrsmyhnd"
        actual = disem.disemvowel(psychokinesis)

        assert expected == actual["output"]
        assert "aoeoeieeioieiaiea" == actual["diff_chars"]

    def test_disemvowel_outstanding_field(self):
        """
        Test 3
        """
        disem = Disemvoweler()
        field = "did you hear about the excellent farmer who was outstanding in his field"
        expected = "ddyhrbtthxcllntfrmrwhwststndngnhsfld"
        actual = disem.disemvowel(field)

        assert expected == actual["output"]
        assert "ioueaaoueeeeaeoaouaiiiie" == actual["diff_chars"]
