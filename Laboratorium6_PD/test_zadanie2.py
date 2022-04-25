from zadanie2 import encrypt_vigenere, check, decrypt_vigenere, vigenere_letter_decrypt, vigenere_letter_encrypt
import pytest


def test_encrypt_empty():
    with pytest.raises(ValueError):
        encrypt_vigenere('K', '')


def test_encrypt():
    assert encrypt_vigenere('TAJNE', 'TO JEST BARDZO TAJNY TEKST') == 'MO SRWM BJEHSO CNNGY CROLT'


def test_encrypt_vigenere_spaces():
    assert encrypt_vigenere('ASFF', '   ') == '   '


def test_encrypt_vigenere_one_letter():
    assert encrypt_vigenere('KOT', 'G') == 'Q'


def test_encrypt_both_empty():
    with pytest.raises(ValueError):
        encrypt_vigenere('','')


def test_encrypt_wrong_values():
    with pytest.raises(ValueError):
        encrypt_vigenere('1234555','KOrras')


def test_decrypt_empty():
    with pytest.raises(ValueError):
        decrypt_vigenere('K', '')


def test_decrypt():
    assert decrypt_vigenere('TAJNE', 'MO SRWM BJEHSO CNNGY CROLT') == 'TO JEST BARDZO TAJNY TEKST'


def test_decrypt_vigenere_spaces():
    assert decrypt_vigenere('ASFF', '   ') == '   '


def test_decrypt_vigenere_one_letter():
    assert decrypt_vigenere('KOT', 'Q') == 'G'


def test_decrypt_both_empty():
    with pytest.raises(ValueError):
        decrypt_vigenere('','')


def test_decrypt_wrong_values():
    with pytest.raises(ValueError):
        decrypt_vigenere('1234555','KOrras')

def test_check_normal():
    assert check("DANE") == 'POPRAWNE'


def test_check_empty():
    with pytest.raises(ValueError):
        check('')

def test_check_wrong():
    with pytest.raises(ValueError):
        check('123')


def test_check_wrong2():
    with pytest.raises(ValueError):
        check(123)


def test_vigenere_letter_encrypt():
    assert vigenere_letter_encrypt('J','T') == 'C'


def test_vigenere_letter_decrypt():
    assert vigenere_letter_decrypt('J','C') == 'T'