from src.item import Item


class MixinLanguages:
    '''
    Миксин-класс для возможности изменения языка
    '''

    def __init__(self, name: str, price: float, quantity: int, language='EN'):
        super().__init__(name, price, quantity)
        self.__language = language

    def change_lang(self):
        '''
        Метод для изменения языков
        '''

        if self.__language == 'EN':
            self.__language = 'RU'
            return self
        else:
            self.__language = 'EN'
            return self

    @property
    def language(self):
        return self.__language


class Keyboard(MixinLanguages, Item):
    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
