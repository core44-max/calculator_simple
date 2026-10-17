from builtins import ZeroDivisionError


def add(x: int, c: int) -> int:
    return x + c
def substrack(x: int, c: int) -> int:
    return x - c
def multiply(x: int, c: int) -> int:
    return x * c
def divide(x: int, c: int) -> int | None:
    try:
        return x // c
    except ZeroDivisionError:
        print("write the correct number")