import pytest
from app import slugify

def test_basic_phrase():
    assert slugify("Hello World") == "hello-world"

def test_multiple_punctuation():
    assert slugify("Hello, world!!! How_are you?") == "hello-world-how-are-you"

def test_string_with_emojis():
    assert slugify("Python is 👍 cool!") == "python-is-cool"
