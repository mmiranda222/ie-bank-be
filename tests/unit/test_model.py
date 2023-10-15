from iebank_api.models import Account
import pytest


def test_create_account():
    """
    GIVEN a Account model
    WHEN a new Account is created
    THEN check the name, account_number, balance, currency, status and created_at fields are defined correctly
    """
    account = Account('John Doe', 'Spain', '€')
    assert account.name == 'John Doe'
    assert account.country == 'Spain'
    assert account.currency == '€'
    assert account.account_number != None
    assert account.balance == 0.0
    assert account.status == 'Active'

def test_account_initial_balance():
    """
    GIVEN an account model
    WHEN an account is created
    THEN check that the initial balance is set to 0
    """
    account = Account('John Doe', 'Spain', '€')
    assert account.balance == 0.0

    account.balance = 100.0
    assert account.balance == 100.0

def test_account_status():
    """
    GIVEN an account model
    WHEN an account is created
    THEN check that the status is active
    """
    account = Account('John Doe', 'Spain', '€')
    assert account.status == "Active"

def update_account_status():
    """
    GIVEN an account model
    WHEN an account is inactive
    THEN check that the status is inactive
    """
    account = Account('John Doe', 'Spain', '€')
    account.status = "Inactive"
    assert account.status == "Inactive"

def test_account_currency_set():
    """
    GIVEN an account model
    WHEN an account is created
    THEN check that the currency is set correctly
    """
    account = Account('John Doe', 'Spain', '€')
    assert account.currency == "€"

def test_account_country_set():
    """
    GIVEN an account model
    WHEN an account is created
    THEN check that the country is set correctly
    """
    account = Account('John Doe', 'Spain', '€')
    # Then
    assert account.country == "Spain"