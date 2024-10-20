"""
This file contains a script demonstrating the encryption of a string from
input.txt in encrypted.txt and decryption in decrypted.txt
"""


# dependencies
import json


def make_matrix(text_str: str, n: int = 5) -> list[list]:
    """
        This function converts a string into a matrix of the specified size
    :param text_str: the input line
    :param n: the size of the matrix
    :return: the matrix for encoding
    """
    text_str = text_str.strip()
    text_str += ' ' * (n - len(text_str) % n)

    return [list(text_str[line*5:line*5+5]) for line in range(len(text_str)//n)]


# main script
with open("input.txt", 'r', encoding='utf-8') as input_file:
    text = input_file.read()
with open("config.json", 'r') as config_file:
    params = json.load(config_file)

print(list(text))
r = make_matrix(text)
for l in r:
    print(l)
print(params)
