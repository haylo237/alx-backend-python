from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiply(value: float) -> float:
        return multiplier * value
    return multiply
