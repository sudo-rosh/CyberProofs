import pytest
from password_checker.checker import (
    check_length,
    check_upper_lower,
    check_numbers,
    check_special_characters,
    rate_password,
)

# ---------------------------
# Tests for check_length
# ---------------------------
def test_check_length_valid():
    assert check_length("Password123!") is True

def test_check_length_invalid():
    assert check_length("abc") is False


# ---------------------------
# Tests for check_upper_lower
# ---------------------------
def test_check_upper_lower_valid():
    assert check_upper_lower("Abcdef") is True

def test_check_upper_lower_no_upper():
    assert check_upper_lower("abcdef") is False

def test_check_upper_lower_no_lower():
    assert check_upper_lower("ABCDEF") is False


# ---------------------------
# Tests for check_numbers
# ---------------------------
def test_check_numbers_valid():
    assert check_numbers("abc123") is True

def test_check_numbers_invalid():
    assert check_numbers("abcdef") is False


# ---------------------------
# Tests for check_special_characters
# ---------------------------
def test_check_special_characters_valid():
    assert check_special_characters("abc!") is True

def test_check_special_characters_invalid():
    assert check_special_characters("abc123") is False


# ---------------------------
# Tests for rate_password
# ---------------------------
def test_rate_password_weak():
    assert rate_password("abc") == 1  # Only lowercase letters

def test_rate_password_medium():
    assert rate_password("Abc123") >= 2  # Has upper, lower, numbers but no special

def test_rate_password_strong():
    assert rate_password("Abc123!") == 4  # Meets all 4 requirements
