import pytest
from text_processor import TextProcessor


def test_capitalize_text_equal():
    """1. Assert equal - egyenlőség ellenőrzés"""
    processor = TextProcessor()
    result = processor.capitalize_text("hello world")
    assert result == "HELLO WORLD"


def test_capitalize_text_not_equal():
    """2. Assert not equal - nem egyenlő"""
    processor = TextProcessor()
    result = processor.capitalize_text("hello world")
    assert result != "hello world"


def test_reverse_text_in():
    """3. Assert in - benne van"""
    processor = TextProcessor()
    result = processor.reverse_text("hello")
    assert "olleh" in result
    assert "h" in result
    assert "hello" not in result


def test_reverse_text_not_in():
    """4. Assert not in - nincs benne"""
    processor = TextProcessor()
    result = processor.reverse_text("hello")
    assert "hello" not in result
    assert "?" not in result


def test_count_words_isinstance():
    """5. Assert isinstance - típus ellenőrzés"""
    processor = TextProcessor()
    result = processor.count_words("hello")
    assert isinstance(result, str) is False
    assert isinstance(processor.count_words("hello"), str) is False


def test_count_words_greater_less():
    """6. Assert >, <, >=, <= - összehasonlítás"""
    processor = TextProcessor()
    result = processor.count_words("hello")
    result1 = processor.count_words("hello w")
    result2 = processor.count_words("hello wo")

    assert result < result2


def test_count_words_empty_string():
    """7. Üres sztring bemenet ellenőrzése"""
    processor = TextProcessor()
    assert processor.count_words("") == 0
    assert processor.count_words("") <= 0
    assert processor.count_words("") < 1
    assert processor.count_words("") != 1


def test_is_palindrome_true_false():
    """8. Assert True/False - boolean ellenőrzés"""
    processor = TextProcessor()
    assert processor.is_palindrome("anna") == True
    assert processor.is_palindrome("banán") == False
    assert processor.is_palindrome("görög") == True


def test_remove_spaces_multiple_asserts():
    """9. Több assert egy tesztben"""
    processor = TextProcessor()
    assert processor.remove_spaces("Alma körte répa") == "Almakörterépa"
    assert isinstance(processor.remove_spaces("Alma körte répa"), str) is True
    assert processor.remove_spaces("Alma körte répa") is not None