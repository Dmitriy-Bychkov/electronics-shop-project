import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)


    def __repr__(self):
        return f'{self.__name}, {self.price}, {self.quantity}'


    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self, new_name: str):
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            raise Exception('Длина наименования товара больше 10 символов')


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity


    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate


    @classmethod
    def instantiate_from_csv(cls) -> None:
        '''
        класс-метод, инициализирующий экземпляры класса `Item`
        данными из файла _src/items.csv
        '''

        cls.all.clear()

        with open('../src/items.csv', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                cls(row['name'], row['price'], row['quantity'])
                

    @staticmethod
    def string_to_number(number):
        '''
        статический метод, возвращающий число из числа-строки
        '''

        return int(float(number))