from solid import Order


def main():
    order = Order()
    order.add_item("Keyboard", 1, 50)
    order.add_item("SSD", 2, 150)
    order.add_item("USB cable", 3, 5)

    print(order.total_price())
    order.pay("debit", "123456")


if __name__ == '__main__':
    main()
