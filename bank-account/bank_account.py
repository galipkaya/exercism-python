from threading import Lock

OPEN = "open"
CLOSED = "closed"


class BankAccount:
    def __init__(self):
        self.balance = 0
        self.status = CLOSED
        self.lock = Lock()

    def get_balance(self):
        if self.status == CLOSED:
            raise ValueError("account closed")
        return self.balance

    def open(self):
        if self.status == OPEN:
            raise ValueError("account already opened")
        self.status = OPEN

    def deposit(self, amount):
        if self.status == CLOSED:
            raise ValueError("account closed")
        if amount < 0:
            raise ValueError("amount cannot be negative")
        self.lock.acquire()
        self.balance += amount
        self.lock.release()

    def withdraw(self, amount):
        if self.status == CLOSED:
            raise ValueError("account closed")
        if amount < 0:
            raise ValueError("amount cannot be negative")
        if amount > self.balance:
            raise ValueError("amount cannot be greater than balance")
        self.lock.acquire()
        self.balance -= amount
        self.lock.release()

    def close(self):
        if self.status == CLOSED:
            raise ValueError("account already opened")
        self.status = CLOSED
        self.balance = 0
