from order import Order


def pay_debit(order: Order, security_code: str) -> None:
    print("Processing debit payment type")
    print(f"Verifying security code: {security_code}")
    order.set_paid_status()


def pay_credit(order, security_code: str) -> None:
    print("Processing credit payment type")
    print(f"Verifying security code: {security_code}")
    order.set_paid_status()
