from account import Account


class MoneyTransfer:
    @staticmethod
    def make_transfer(sender, recipient, amount):
        sender.transfer(recipient, amount)
