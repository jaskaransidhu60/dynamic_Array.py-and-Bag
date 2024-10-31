# Name: Jaskaran Singh Sidhu
# OSU Email: sidhuja@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 2: Bag ADT
# Description: Implements a Bag ADT using a Dynamic Array.

from dynamic_array import DynamicArray, DynamicArrayException

class Bag:
    def __init__(self, start_bag=None):
        self._da = DynamicArray()
        if start_bag:
            for value in start_bag:
                self.add(value)

    def add(self, value: object) -> None:
        self._da.append(value)

    def remove(self, value: object) -> bool:
        for i in range(self._da.length()):
            if self._da.get_at_index(i) == value:
                for j in range(i, self._da.length() - 1):
                    self._da.set_at_index(j, self._da.get_at_index(j + 1))
                self._da.remove_at_index(self._da.length() - 1)
                return True
        return False

    def count(self, value: object) -> int:
        count =
