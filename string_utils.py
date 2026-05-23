# string_utils.py

def reverse_words(s: str) -> str:
    """反转单词顺序"""
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    words = s.strip().split()
    return " ".join(reversed(words))


def count_vowels(s: str) -> int:
    """统计元音字母数量"""
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)


def is_palindrome(s: str):
    """判断是否回文（忽略大小写和空格）"""
    if not isinstance(s, str):
        raise TypeError("输入必须是字符串")
    cleaned = "".join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

