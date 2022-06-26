from order import Order
from payment import pay_debit


def main():
    order = Order()
    order.add_item("Keyboard", 1, 50)
    order.add_item("SSD", 2, 150)
    order.add_item("USB cable", 3, 5)

    print(order.total_price())

    pay_debit(order, "123456")


if __name__ == '__main__':
    main()
