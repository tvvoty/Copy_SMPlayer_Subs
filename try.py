import pyperclip
import re


def convert_sub_timestamp_to_miliseconds(seconds, miliseconds):
    return miliseconds + (seconds * 1000)


print(convert_sub_timestamp_to_miliseconds(8633, 024000))
