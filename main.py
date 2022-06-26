from order import Order
from payment import DebitPaymentProcessor, CreditPaymentProcessor


def main():
    order = Order()
    order.add_item("Keyboard", 1, 50)
    order.add_item("SSD", 2, 150)
    order.add_item("USB cable", 3, 5)

    print(order.total_price())

    processor = DebitPaymentProcessor
    processor.pay(order, "123456")

    processor = CreditPaymentProcessor
    processor.pay(order, "123456")


if __name__ == '__main__':
    main()
