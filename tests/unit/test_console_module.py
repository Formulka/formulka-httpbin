# -*- coding: utf-8 -*-
# Copyright (c) 2018 Petr Olah <djangoguru@gmail.com>
#
# this file is part of the project "Petr Olah HTTPBin Client" released under the "MIT" open-source license

from formulka_httpbin.console import ansi_red


def test_ansi_red():
    ("formulka_httpbin.console.ansi_red() should wrap the "
     "given string with ansi the escape code for bold red")

    # Given that I have a string to be colorized in the terminal
    my_string = 'This is my string'

    # When I colorize it
    result = ansi_red(my_string)

    # Then it should be wrapped with the correct ansi color code
    result.should.equal('\033[1;31mThis is my string\033[0m')
