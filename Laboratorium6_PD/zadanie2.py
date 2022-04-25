"""
Program encrypts or decrypts given string using Vigenere cipher
"""


def check(text):
    if not type(text) is str:
        raise ValueError("Podane dane to nie tekst!")
    if not text:
        raise ValueError("Brak danych!")
    for letter in text:
        if not ((ord(letter) >=65 and ord(letter) <= 90) or letter==' '):
            raise ValueError("Dane spoza zakresu!")
    return "POPRAWNE"

def encrypt_vigenere(key, text):
    check(key)
    check(text)
    new_text = ''
    key_id = 0
    for letter in text:
        if letter != ' ':
            letter = vigenere_letter_encrypt(key[key_id], letter)
            if key_id+1 >= len(key):
                key_id=0
            else:
                key_id+=1
        new_text += letter
    return new_text


def decrypt_vigenere(key, text):
    check(key)
    check(text)
    new_text = ''
    key_id = 0
    for letter in text:
        if letter != ' ':
            letter = vigenere_letter_decrypt(key[key_id], letter)
            if key_id+1 >= len(key):
                key_id=0
            else:
                key_id+=1
        new_text += letter
    return new_text


def vigenere_letter_encrypt(key_letter, plain_letter):
    key_value = ord(key_letter)-65
    plain_value = ord(plain_letter)-65
    value = key_value + plain_value
    value = value%26
    value +=65
    return chr(value)


def vigenere_letter_decrypt(key_letter, cipher_letter):
    key_value = ord(key_letter)-65
    cipher_value = ord(cipher_letter)-65
    value = cipher_value - key_value
    if value < 0:
        value = 26 + value
    value +=65
    return chr(value)
