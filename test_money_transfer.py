import pytest
from account import Account
from moneytransfer import MoneyTransfer


@pytest.fixture
def accounts():
    account1 = Account("123456", 1000)
    account2 = Account("654321", 500)
    return account1, account2


def test_deposit(accounts):
    account1, _ = accounts
    account1.deposit(500)
    assert account1.balance == 1500


def test_withdraw(accounts):
    _, account2 = accounts
    account2.withdraw(200)
    assert account2.balance == 300


def test_transfer(accounts):
    account1, account2 = accounts
    MoneyTransfer.make_transfer(account1, account2, 300)
    assert account1.balance == 700
    assert account2.balance == 800


def test_insufficient_balance(accounts):
    account1, account2 = accounts
    with pytest.raises(ValueError):
        MoneyTransfer.make_transfer(account1, account2, 10000)
