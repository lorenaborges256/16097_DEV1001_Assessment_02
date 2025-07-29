# testes/test_errors.py
import pytest
from src.user_auth import UserAuth
from src.stock_checker import StockChecker

def test_valid_email():
    auth = UserAuth()
    assert auth.is_valid_email('test@example.com')

def test_find_user_by_email_existing():
    auth = UserAuth()
    auth.users = [
        {"Name": "Lorena", "Email": "lorena@example.com"},
        {"Name": "Carlos", "Email": "carlos@example.com"},
    ]

    result = auth.find_user_by_email("lorena@example.com")
    assert result == {"Name": "Lorena", "Email": "lorena@example.com"}

def test_find_user_by_email_not_existing():
    auth = UserAuth()
    auth.users = [
        {"Name": "Lorena", "Email": "lorena@example.com"},
    ]
    result = auth.find_user_by_email("joana@example.com")
    assert result is None

def test_valid_product():
    checker = StockChecker()
    assert checker.validate_product("Conditioner") is True

def test_invalid_product():
    checker = StockChecker()
    result = checker.validate_product("Face Cream")
    assert result is False
