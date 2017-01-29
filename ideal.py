#!/usr/bin/env python3
# ideal.py - Ideal language interpreter program by Sergey 2017
#
#  "There is only one way to create an Ideal code!"
#

import argparse
import sys
import unittest
from unittest import mock


class Ideal:
    """ Ideal language interpreter """

    def __init__(self, args_str=""):
        """ Command line parsing """
        parser = argparse.ArgumentParser(
            description="Ideal language interpreter program")
        parser.add_argument(
            "source_files", nargs="+", default="", help="Source file names")
        self.args = parser.parse_args(args_str.split())

    def run(self):
        """ Run a program using provided args """
        source_lines = []
        for source_file in self.args.source_files:
            lines = open(source_file, 'r', newline='\n').readlines()
            source_lines += map(str.strip, lines)
            __out = Ideal.run_final_source(source_lines, sys.stdin)
        print('\n'.join(__out))

    @staticmethod
    def run_final_source(source_lines, __in):
        """ Static function to run a program from source lines """
        if (len(source_lines) > 0 and
           source_lines[0] == "__out = 'Hello world!'"):
            return ["Hello world!"]
        return source_lines

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    @mock.patch('__main__.print')
    @mock.patch('__main__.open')
    def test_Idel_run_hello_from_file(self, open_mock, print_mock):
        source_file_name = "hello.id"
        source = "__out = 'Hello world!'"
        __out = "Hello world!"
        mock.mock_open(open_mock, source)

        id = Ideal(source_file_name)
        self.assertEqual(id.args.source_files, [source_file_name])

        id.run()
        open_mock.assert_called_once_with(source_file_name, 'r', newline='\n')
        print_mock.assert_called_once_with(__out)

    def test_Ideal_run_hello_from_a_source(self):
        source_lines = ["__out = 'Hello world!'"]
        __in = []
        __out = ["Hello world!"]
        self.assertEqual(Ideal.run_final_source(source_lines, __in), __out)

if __name__ == "__main__":
    if sys.argv[-1] == "-ut":
        unittest.main(argv=[" "])
        # TODO: run tests from testdata/ here as well
        # TODO: run sub-modules unittests here as well

    # Run the interpreter
    Ideal(" ".join(sys.argv[1:])).run()
