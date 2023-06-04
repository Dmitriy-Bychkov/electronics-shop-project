from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __str__(self) -> str:
        return f'{self.name}'

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, sim_quantity: int):
        if sim_quantity > 0 and isinstance(sim_quantity, int):
            self.__number_of_sim = sim_quantity
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
