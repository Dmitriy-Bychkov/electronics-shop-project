import csv

from src.exceptions import InstantiateCSVError, CSVNotFoundError


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

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return f"{self.name}"

    def __add__(self, other):
        if not issubclass(other.__class__, self.__class__):
            raise ValueError('Сложить можно только экземпляры у классов Item и Phone')
        return int(self.quantity) + int(other.quantity)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: str):
        if len(new_name) > 10:
            raise Exception('Длина наименования товара больше 10 символов')
        self.__name = new_name

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
    def csv_reader(cls, filename):
        '''
        класс-метод, читающий файл и инициализирующий экземпляры
        класса `Item` данными из этого файла, а также содержащий блоки проверок файла CSV
        '''

        try:
            cls.all.clear()

            with open(filename, newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    cls(row['name'], row['price'], row['quantity'])

                    # Запускаем цикл проверок для строк в файле и вызываем соответствующие ошибки
                    if len(row['name']) < 1:
                        raise InstantiateCSVError
                    if int(row['price']) < 1:
                        print('Ошибка: цена товара не может быть равной или меньше нуля')
                    if int(row['quantity']) < 0:
                        print('Ошибка: количество товара не может быть меньше нуля')

                # Проверяем на пустой файл
                if len(cls.all) <= 0:
                    raise InstantiateCSVError

        # Переопределяем стандартные ошибки Python
        except FileNotFoundError:
            raise CSVNotFoundError
        except KeyError:
            raise InstantiateCSVError
        except ValueError:
            raise InstantiateCSVError

    @classmethod
    def instantiate_from_csv(cls) -> None:
        '''
        класс-метод, инициализирующий экземпляры класса `Item`
        данными из файла _src/items.csv и перехватывающий наши ошибки
        '''

        try:
            cls.csv_reader('../src/items.csv')

        # Отлавливаем и принтуем наши кастомные ошибки
        except CSVNotFoundError as ex:
            print(ex.message)
        except InstantiateCSVError as ex:
            print(ex.message)

    @staticmethod
    def string_to_number(number):
        '''
        статический метод, возвращающий число из числа-строки
        '''

        return int(float(number))
