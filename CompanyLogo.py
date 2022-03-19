import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input("enter string: ")
    char_array = list(s)
    keep_number: list

    for item in range(0, len(char_array)-1):
        if char_array[item] == char_array[item+1]: keep_number[item]
        print(keep_number[item])


    print(char_array)
