# testes/test_errors.py
import pytest
from src.user_auth import UserAuth

def test_valid_email():
    auth = UserAuth()
    assert auth.is_valid_email('test@example.com')

# def test_invalid_email():
#     auth = UserAuth()
#     assert auth.is_valid_email('userexample.com')

# def test_invalid_emails():    
#     invalid_emails = [
#         "userexample.com",        # Missing @
#         "@domain.com",            # Missing local part
#         "user@.com",              # Invalid domain
#         "user@domain",            # Missing TLD
#         "user@domain.c",          # TLD too short
#         "user@domain.toolongtld", # TLD too long
#     ]
#     for email in invalid_emails:
#         assert not auth.is_valid_email(email)