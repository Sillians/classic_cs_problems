"""
A stack is a linear data structure that follows the Last In, First Out (LIFO) principle.
This means that the last element added to the stack is the first one to be removed.
It can be visualized as a pile of plates where you can only add or remove the top plate.
"""

# The import of Generic from the typing module enables Stack to be generic over a particular type in type hints.
# The arbitrary type T is defined in T = TypeVar('T'). T can be any type.
from typing import TypeVar, List, Generic
T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)

# Stacks are perfect stand-ins for the towers in The Towers of Hanoi.
num_discs: int = 3
tower_a: Stack[int] = Stack()
tower_b: Stack[int] = Stack()
tower_c: Stack[int] = Stack()
for i in range(1, num_discs + 1):
    tower_a.push(i)

def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:
    if n == 1:
        end.push(begin.pop())
    else:
        hanoi(begin, temp, end, n - 1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n - 1)


if __name__ == "__main__":
    hanoi(tower_a, tower_c, tower_b, num_discs)
    print(tower_a)
    print(tower_b)
    print(tower_c)

























