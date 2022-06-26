from order import Order
from abc import ABC


class PaymentProcessor(ABC):
    @staticmethod
    def pay(order: Order, security_code: str):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    @staticmethod
    def pay(order, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.set_paid_status()


class CreditPaymentProcessor(PaymentProcessor):
    @staticmethod
    def pay(order, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.set_paid_status()
