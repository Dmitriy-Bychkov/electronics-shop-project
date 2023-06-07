class InstantiateCSVError(Exception):
    """Класс-исключение для отлавливания ошибки, если файл поврежден"""

    def __init__(self):
        self.message = 'InstantiateCSVError: Файл item.csv поврежден'


class CSVNotFoundError(InstantiateCSVError):
    """Класс-исключение для отлавливания ошибки, если файл отсутствует"""

    def __init__(self):
        self.message = 'FileNotFoundError: Отсутствует файл item.csv'
