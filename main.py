from order import Order
from payment import BlikPaymentProcessor, CreditPaymentProcessor, DebitPaymentProcessor


def main():
    order = Order()
    order.add_item("Keyboard", 1, 50)
    order.add_item("SSD", 2, 150)
    order.add_item("USB cable", 3, 5)

    print(order.total_price())

    processor = DebitPaymentProcessor("123456")
    processor.pay(order)

    processor = CreditPaymentProcessor("123456")
    processor.pay(order)

    processor = BlikPaymentProcessor("1234")
    processor.pay(order)


if __name__ == '__main__':
    main()
