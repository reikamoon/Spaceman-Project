
from Spaceman_Project import *


def test_guessed_words():
    secret_word = "cat"
    letters_guessed = ["c", "a", "t"]
    assert get_guessed_word(secret_word, letters_guessed) == secret_word


def test_is_word_guessed():
    secret_word = "dog"
    letters_guessed = ["d", "o", "t"]
    assert is_word_guessed(secret_word, letters_guessed) == False


def test_is_guess_in_word():
    guess = "guineapig"
    secret_word = "hamster"
    assert is_guess_in_word(guess, secret_word) == False
