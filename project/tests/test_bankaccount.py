import unittest
import sys
import os


p = os.path.dirname(os.path.dirname((os.path.abspath('__file__'))))
if p not in sys.path:
    sys.path.append(p)


class TestBankAccount(unittest.TestCase):

    def _getTarget(self):
        from project.tests.bankaccount import BankAccount
        return BankAccount

    def _makeOne(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def test_construct(self):
        target = self._makeOne()
        self.assertEqual(target._balance, 0)

    def test_deposit(self):
        target = self._makeOne()
        target.deposit(100)
        self.assertEqual(target._balance, 100)

    def test_withdraw(self):
        target = self._makeOne()
        target._balance = 100
        target.withdraw(20)
        self.assertEqual(target._balance, 80)

    def test_get_balance(self):
        target = self._makeOne()
        target.set_balance(500)
        self.assertEqual(target._balance, 500)

    def test_set_balance_not_enough_funds(self):
        target = self._makeOne()
        from project.tests.bankaccount import NotEnoughFundsException
        try:
            target.set_balance(-1)
            self.fail()
        except NotEnoughFundsException:
            pass
