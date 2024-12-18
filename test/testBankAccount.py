import unittest
from src.BankApp import BankAccount
class BankAccountTest(unittest.TestCase):

    def setUp(self)-> None:
        self.account = BankAccount(balance=1000)

    def test_deposito(self):
        new_balance = self.account.deposit(500)
        assert new_balance == 1500

    def test_withdraw(self):
        new_balance = self.account.withdraw(200)
        assert new_balance == 800

    def test_get_balance(self):
        assert self.account.get_balance() == 1000
