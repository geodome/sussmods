from typing import Literal, overload, NamedTuple

@overload
def transform(data: str, mode: Literal["split"]) -> list[str]:
    ...

@overload
def transform(data: str, mode: Literal["upper"]) -> str:
    ...

def transform(data: str, mode: Literal["split", "upper"]) -> list[str] | str:
    if mode == "split":
        return data.split()
    else:
        return data.upper()

split_words = transform("hello world", "split")  # Return type is list[str]
split_words[0]  # Type checker is happy

upper_words = transform("hello world", "upper")  # Return type is str
upper_words.lower()  # Type checker is happy

#upper_words.append("!")  # Cannot access attribute "append" for "str"

transform("asdasdasd","upper")

Point = NamedTuple("Point", [('x', int), ('y', int)])

a = Point(x=1,y=2)
print(a)

def root(n: int, threshold:float=0.000001) -> float:
    def fx(x:int|float) -> float:
        return x**2 - n
    a, b = 0, n
    while True:
        mid = (a + b) / 2
        if abs(fx(mid)) <= threshold:
            return mid + threshold
        elif fx(a)*fx(mid) < 0:
            b = mid
        else:
            a = mid

print(root(83)**2)