class Order:
    def __init__(self, id, title, senders_name, address):
        self.id = id
        self.title = title
        self.senders_name = senders_name
        self.address = address
        self.is_delivered = False

    def order_info(self):
        """Информация о заказе"""
        if self.is_delivered == True:
            Delivery = "Да"
        else:
            Delivery = "Нет"

        order_info = str(f"Заказ №{self.id}\nНаименование: {self.title}\nОтправитель: {self.senders_name}\n"
                         f"Адрес доставки: {self.address}\nДоставлен: {Delivery}\n")
        return order_info

    def delivery(self):
        """Изменение статуса заказа"""
        self.is_delivered = not self.is_delivered
        return self.is_delivered

Order1 = Order (1,"Заказ1","Иванов Иван Иванович","Екатеринбург, Ленина 2")
Order2 = Order (2,"Заказ2","Петров Петр Петрович","Екатеринбург, Ленина 1")

print (Order1.order_info())
print (Order2.delivery())