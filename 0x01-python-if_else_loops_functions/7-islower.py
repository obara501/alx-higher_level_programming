#!/usr/bin/python3
def islower(c):
    letter = ord(c)
    if letter >= ord("a") and letter <= ord("z"):
        return True
    return False
