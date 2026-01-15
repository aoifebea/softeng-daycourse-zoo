# tiger.py

from .animal import Animal


class Tiger(Animal):
    def __init__(self, name="tiger"):
        super().__init__(name, species="Cat")

    def sound(self):
        return "meows and raws"

    def action(self):
        return "prowls around, pounces to attack."

