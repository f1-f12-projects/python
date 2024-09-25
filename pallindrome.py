# This program to test whether given String is Pallindrome or not.
# Ignore Spaces and it should be case insesitive
# Eg: Radar, Race car

import f1f12_utils as u
from f1f12_utils import logger

def is_pallindrome (givenString = ""):
    # print ("Geven string is: " + givenString)

    # Remove spaces
    givenString = givenString.replace(" ", "")

    # Get the revese string
    reverseString = givenString[::-1]
    # print ("After removing spaces: " + reverseString)
    
    if reverseString.lower() == givenString.lower():
        return True

    return False


def checkPallindrome():    
    input_strings = ["gadag", "Gadag", "Run nur", "Hello"]
    for input_string in input_strings:    
        # input_string = input ("Enter any string to check for Pallindrome: ")
        msg = input_string + " --> "
        if is_pallindrome(input_string):
            msg += "Pallindrome."
        else:
            msg += "NOT Pallindrome."
        logger.info(msg)

if __name__ == "__main__":
    try:
        u.startProgram()
        checkPallindrome()
    except all as e:
        print ("Some error: " + e)
    finally:
        u.endProgram()