# testes/test_errors.py
import pytest
from src.user_auth import UserAuth
from src.stock_checker import StockChecker
from src.notifier import Notifier
import tempfile
import os



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
    result = checker.validate_product("Shampoo")
    assert result is True

def test_invalid_product():
    checker = StockChecker()
    result = checker.validate_product("Face Cream")
    assert result is False


def test_load_credentials_reads_file_correctly():
    content = "EMAIL=test@example.com\nPASSWORD=abc123"
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as temp:
        temp.write(content)
        temp_filename = temp.name

    notifier = Notifier()
    credentials = notifier.load_credentials(temp_filename)

    os.remove(temp_filename)  # Limpeza pós-teste

    assert credentials == {
        "EMAIL": "test@example.com",
        "PASSWORD": "abc123"
    }
