# test_string_utils.py

import pytest
from string_utils import reverse_words, count_vowels, is_palindrome


# -------------------------
# reverse_words 测试
# -------------------------
def test_reverse_words_normal():
    assert reverse_words("hello world") == "world hello"

def test_reverse_words_single_word():
    assert reverse_words("hello") == "hello"

def test_reverse_words_invalid_type():
    with pytest.raises(TypeError):
        reverse_words(123)


# -------------------------
# count_vowels 测试
# -------------------------
def test_count_vowels_normal():
    assert count_vowels("hello") == 2

def test_count_vowels_empty():
    assert count_vowels("") == 0

def test_count_vowels_invalid_type():
    with pytest.raises(TypeError):
        count_vowels(None)


# -------------------------
# is_palindrome 测试
# -------------------------
def test_is_palindrome_true():
    assert is_palindrome("A man a plan a canal Panama") is True

def test_is_palindrome_false():
    assert is_palindrome("hello") is False

def test_is_palindrome_invalid_type():
    with pytest.raises(TypeError):
        is_palindrome(12345)
