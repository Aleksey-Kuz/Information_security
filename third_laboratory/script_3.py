"""
Laboratory work 3
This file contains a script demonstrating the encryption of a string from
input.txt in encrypted.txt and decryption in decrypted.txt
"""


# dependencies
import json


def euclid_search(a: int, b: int) -> int:
    """
        This function implements the Euclid algorithm
    :param a: first number
    :param b: second number
    :return: the largest common divisor
    """
    while a != 0 and b != 0:
        if a >= b:
            a %= b
        else:
            b %= a
    return a if a > b else b


def convert_word_to_numbers(word: str, alphabet: str) -> list:
    """
        This function converts a word into a list of
        ordinal numbers of letters in the alphabet
    :param word: the word for conversion
    :param alphabet: the original alphabet
    :return: list of the numbers
    """
    return [alphabet.find(letter) + 1 for letter in word]


def convert_numbers_to_word(numbers: list, alphabet: str) -> str:
    """
        This function converts a list of ordinal numbers of letters
        in the alphabet into a word
    :param numbers: list of the numbers
    :param alphabet: the original alphabet
    :return: result word
    """
    return ''.join([alphabet[(num - 1) % len(alphabet)] for num in numbers])


def calculate_n(p: int, q: int) -> int:
    """
        This function calculate the parameter n
    :param p: the input parameter p
    :param q: the input parameter q
    :return: result parameter n
    """
    return p * q


def calculate_fn(p: int, q: int) -> int:
    """
        This function calculate the parameter f(n)
    :param p: the input parameter p
    :param q: the input parameter q
    :return: result parameter f(n)
    """
    return (p - 1) * (q - 1)


def calculate_e(fn: int) -> int:
    """
        This function calculate the parameter e
    :param fn: the parameter f(n)
    :return: result parameter f(n)
    """
    e = 2
    while e < fn:
        if euclid_search(e, fn) == 1:
            break
        e += 1
    return e


def calculate_d(e: int, fn: int) -> int:
    """
        This function calculate the parameter d
    :param e: the parameter e
    :param fn: the parameter f(n)
    :return: result parameter d
    """
    d = 1
    while ((d * e) % fn) != 1:
        d += 1
    return d


def encoding(numbers_text: list, open_key: list) -> str:
    """
        This function encodes the text according to the open key
    :param numbers_text: the input origin list of text numbers
    :param open_key: the open key for encoding
    :return: the encoded text at list of numbers format
    """
    encoding_text = list()
    for num in numbers_text:
        encoding_text.append(num ** open_key[0] % open_key[1])
    return encoding_text


def decoding(numbers_text: list, closed_key: list) -> str:
    """
        This function decoding the text according to the closed key
    :param numbers_text: the input origin list of text numbers
    :param closed_key: the open key for encoding
    :return: the encoded text at list of numbers format
    """
    decoding_text = list()
    for num in numbers_text:
        decoding_text.append(num ** closed_key[0] % closed_key[1])
    return decoding_text


# main script
with open("input.txt", 'r', encoding='utf-8') as input_file:
    input_text = input_file.read()
with open("config.json", 'r') as config_file:
    params = json.load(config_file)

print('\n---Input text---')
print(input_text)
print('\n-------------------------\n')

print('---Parameters---')
n = calculate_n(params['p'], params['q'])
fn = calculate_fn(params['p'], params['q'])
e = calculate_e(fn)
d = calculate_d(e, fn)
print(f"p = {params['p']}\n"
      f"q = {params['q']}\n"
      f"n = {n}\n"
      f"f(n) = {fn}\n"
      f"e = {e}\n"
      f"d = {d}\n"
      f"open key = ({e}, {n})\n"
      f"closed key = ({d}, {n})")
print('\n-------------------------\n')

enc_list = convert_word_to_numbers(input_text, params['alphabet'])
enc_list = encoding(enc_list, [e, n])
enc_text = convert_numbers_to_word(enc_list, params['alphabet'])
print('---Encoding text---')
print(enc_text)
print('\n-------------------------\n')

dec_list = decoding(enc_list, [d, n])
dec_text = convert_numbers_to_word(dec_list, params['alphabet'])
print('---Decoding---')
print(dec_text)
print('\n-------------------------\n')

if input_text.strip() == dec_text.strip():
    print('Encoding and decoding completed successfully!')
else:
    print('Encoding and decoding failed!')

with open('encrypted.txt', 'w') as enc_file:
    enc_file.write(enc_text.strip())
with open('decrypted.txt', 'w') as dec_file:
    dec_file.write(dec_text.strip())
