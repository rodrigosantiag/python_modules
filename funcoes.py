from typing import Any


def somar():
    print("Esta função vai somar valores")


def multi():
    print("Esta função vai multiplicar valores")


def find_index(to_find: list, item: Any) -> int:
    for i, valor in enumerate(to_find):
        if valor == item:
            return i

    return -1
