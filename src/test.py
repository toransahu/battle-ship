"""Test battleship.py module"""

from battleship import Battle


# monkey patching function for get_input()
def monkey_get_input(self):
    self.SIZE_OF_FIELD = '5 E'
    self.NUMBER_OF_SHIPS = 2
    self.TYPES_OF_SHIP = ['Q 1 1 A1 B2', 'P 2 1 D4 C3']
    self.TARGETS_OF_PLAYER1 = 'A1 B2 B2 B3'
    self.TARGETS_OF_PLAYER2 = 'A1 B2 B3 A1 D1 E1 D4 D4 D5 D5'
    self.FIELD1 = []
    self.FIELD2 = []
    return 0


# monkey patching
Battle.get_input = monkey_get_input

battle1 = Battle()


def test_get_input_positive():
    assert battle1.get_input() == 0


def test_pre_process():
    assert battle1.pre_process() == 0


def test_war():
    assert battle1.war() == 0
