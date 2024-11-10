"""
Laboratory work 2
This file contains a script demonstrating the encryption of a string from
input.txt in encrypted.txt and decryption in decrypted.txt
"""


# dependencies
import json


def encoding(text: str, key: str, alphabet: str) -> str:
    """
        This function encodes the text according to the key and alphabet
    :param text: the input origin text
    :param key: the key for encoding
    :param alphabet: the alphabet of the language
    :return: the encoded text
    """
    encoding_text = list()
    for ind in range(len(text)):
        encoding_text.append(
            alphabet[(alphabet.find(text[ind]) +
                      alphabet.find(key[ind % len(key)])) % len(alphabet)])
    return ''.join(encoding_text)


def decoding(text: str, key: str, alphabet: str) -> str:
    """
        This function decoding the text according to the key and alphabet
    :param text: the input origin text
    :param key: the key for encoding
    :param alphabet: the alphabet of the language
    :return: the decoded text
    """
    decoding_text = list()
    for ind in range(len(text)):
        decoding_text.append(
            alphabet[(alphabet.find(text[ind]) + len(alphabet) -
                      alphabet.find(key[ind % len(key)])) % len(alphabet)])
    return ''.join(decoding_text)


# main script
with open("input.txt", 'r', encoding='utf-8') as input_file:
    input_text = input_file.read()
with open("config.json", 'r') as config_file:
    params = json.load(config_file)

print('\n---Input text---')
print(input_text)
print('\n-------------------------\n')

enc_text = encoding(input_text, "LEMON", params['alphabet'])
print('---Encoding text---')
print(enc_text)
print('\n-------------------------\n')

dec_text = decoding(enc_text, "LEMON", params['alphabet'])
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
