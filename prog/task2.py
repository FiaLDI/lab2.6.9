#!usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':

    dictionary = {
        0:"zero",
        1:"one",
        2:"two",
        3:"three",
        4:"four",
        5:"five",
        6:"six",
        7:"seven"
    }

    reversed_dictionary = {
        value: key 
        for key, value in dictionary.items()
    }

    print(reversed_dictionary)