# tiger.py

from .animal import Animal


class Tiger(Animal):
    def __init__(self, name="Tiger"):
        super().__init__(name, species="Cat")

    def sound(self):
        return "meow"

    def action(self):
        return "prowls around."

# Testing
def test_tiger():
    assert Tiger().describe() == "Tiger the Cat says meow and prowls around."