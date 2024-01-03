#!/usr/bin/python3

def remove_char_at(str, n):
    str_copy = str
    if n >= len(str_copy) or n < 0:
        return str_copy
    str_copy = str_copy.replace(str[n], "")
    return str_copy
