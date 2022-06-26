from order import Order
from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order: Order):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.set_paid_status()


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.set_paid_status()


class BlikPaymentProcessor(PaymentProcessor):
    def __init__(self, blik_code: str):
        self.blik_code = blik_code

    def pay(self, order):
        print("Processing blik payment type")
        print(f"Verifying blik code: {self.blik_code}")
        order.set_paid_status()
