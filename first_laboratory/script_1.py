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
    :return: the matrix for encoding/decoding
    """
    text_str = text_str.strip()
    text_str += ' ' * (n - len(text_str) % n)

    return [list(text_str[line*5:line*5+5]) for line in range(len(text_str)//n)]


def make_text(matrix: list[list]) -> str:
    """
        This function converts the encoded/decoded matrix into a string
    :param matrix: the encoded/decoded matrix
    :return: the line from encoded/decoded matrix
    """
    return ''.join([''.join([matrix[ind_c][ind_l]
                             for ind_c in range(len(matrix))])
                    for ind_l in range(len(matrix))])


def encoding(matrix: list[list], k1: list, k2: list) -> list[list]:
    """
        This function encodes the text according to the matrix
    :param matrix: the input origin matrix
    :param k1: params for columns
    :param k2: params for lines
    :return: the encoded matrix
    """
    encoding_matrix = list()

    for line in range(len(k2)):
        encoding_matrix.append(list())
        for column in range(len(k1)):
            encoding_matrix[line].append(matrix[k2[line]-1][k1[column]-1])

    return encoding_matrix


def decoding(matrix: list[list], k1: list, k2: list) -> list[list]:
    """
        This function decoding the text according to the matrix
    :param matrix: the input origin matrix
    :param k1: params for columns
    :param k2: params for lines
    :return: the decoded matrix
    """
    decoding_matrix = list()

    for line in range(len(k2)):
        decoding_matrix.append(list())
        for column in range(len(k1)):
            decoding_matrix[line].append(matrix[k2[line]-1][k1[column]-1])

    return decoding_matrix


# main script
with open("input.txt", 'r', encoding='utf-8') as input_file:
    text = input_file.read()
with open("config.json", 'r') as config_file:
    params = json.load(config_file)

print('---Input text---')
print(text)
print('\n-------------------------\n')

origin_matrix = make_matrix(text)
print('---Origin matrix---')
for line in origin_matrix:
    print(line)
print('\n-------------------------\n')

enc_matrix = encoding(origin_matrix, params['k1'], params['k2'])
enc_text = make_text(enc_matrix)
print('---Encoding text---')
print(enc_text)
print('---Matrix encoding---')
print(enc_matrix)
print('\n-------------------------\n')

print('matrix decoding')
print('decoding')
m = encoding(make_matrix(enc_text), params['k1'], params['k2'])
print(m)
