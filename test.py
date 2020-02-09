#!./env/bin/python
import unittest
import os
import re

def get_delimiters(input):
    delims = [',']
    replace = ''
    for match in re.findall(r'(//)(.*)(\n)', input): # Will not run if blank
        (start, delim_token, end) = match
        replace = f'{start}{delim_token}{end}'
        delims = []

        for i in re.split(r'\[|\]',delim_token):
            if i != "":
                delims.append(i)

    return (delims, replace)

def add(input):
    if input == "":
        return 0

    (delimiters, strip) = get_delimiters(input)
    
    input = input.replace(strip,'')
    for d in delimiters:
        input = input.replace(d,',')

    numbers = re.split(r'\n|,', input)
    sum = 0
    for n in numbers:
        if n != '':
            sum += int(n)
    return sum

class StringCalculatorTests(unittest.TestCase):

    def test_empty(self):
        """Given "" should return 0"""
        actual = add('')
        self.assertEqual(actual,0)
    
    def test_1(self):
        """Given "1" should return 1"""
        actual = add('1')
        self.assertEqual(actual, 1)

    def test_1_and_2(self):
        """Given "1,2" should return 3"""
        actual = add('1,2')
        self.assertEqual(actual, 3)
    
    def test_1_newline_2_and_3(self):
        """Given "1\\n2,3" should return 6"""
        actual = add('1\n2,3')
        self.assertEqual(actual, 6)

    def test_1_defined_delimiter_semicolon(self):
        """Given "//;\\n1;2" should return 3"""
        actual = add('//;\n1;2')
        self.assertEqual(actual, 3)
    
    def test_defined_delimiter_multicharacter_semicolon(self):
        """Given "//[***]\\n1***2***3" should return 6"""
        actual = add('//[***]\n1***2***3')
        self.assertEqual(actual, 6)

    def test_defined_delimiter_multicharacter_semicolon(self):
        """Given " //[*][%]\\n1*2%3" should return 6"""
        actual = add('//[*][%]\n1*2%3')
        self.assertEqual(actual, 6)

   
    

if __name__ == '__main__':
    unittest.main()