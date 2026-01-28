# Test suite for BankAccount class using pytest

import pytest
from main import BankAccount


def test_deposit_increases_balance():
    account = BankAccount()
    account.deposit(100)
    assert account.balance == 100


def test_withdraw_more_than_balance_raises_error():
    account = BankAccount(50)
    with pytest.raises(ValueError):
        account.withdraw(100)


def test_initial_balance_is_zero():
    account = BankAccount()
    assert account.balance == 0
