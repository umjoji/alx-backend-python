# Annotations README

This README file provides an overview of the annotated functions and variables included in this project.

## Task 0: Basic annotations - add

```python
def add(a: float, b: float) -> float:
    return a + b
```

## Task 1: Basic annotations - concat

```python
def concat(str1: str, str2: str) -> str:
    return str1 + str2
```

## Task 2: Basic annotations - floor

```python
def floor(n: float) -> int:
    return int(n)
```

## Task 3: Basic annotations - to_string

```python
def to_str(n: float) -> str:
    return str(n)
```

## Task 4: Define variables

```python
a: int = 1
pi: float = 3.14
i_understand_annotations: bool = True
school: str = "Holberton"
```

## Task 5: Complex types - list of floats

```python
def sum_list(input_list: List[float]) -> float:
    return sum(input_list)
```

## Task 6: Complex types - mixed list

```python
def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    return sum(mxd_lst)
```

## Task 7: Complex types - string and int/float to tuple

```python
def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, v ** 2)
```

## Task 8: Complex types - functions

```python
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiplier_func(num: float) -> float:
        return num * multiplier
    return multiplier_func
```

## Task 9: Let's duck type an iterable object

```python
from typing import Iterable, List

def sum_list(items: Iterable[float]) -> float:
    return sum(items)
```

## Task 10: Duck typing - first element of a sequence

```python
from typing import Sequence, Union

def safe_first_element(lst: Sequence[Union[int, float]]) -> Union[int, float, None]:
    if lst:
        return lst[0]
    else:
        return None
```

## Task 11: More involved type annotations

```python
from typing import Dict, List, Tuple

def map_nested_dict(data: Dict[str, List[Tuple[int, str]]]) -> List[Tuple[str, int]]:
    result = []
    for key, lst in data.items():
        for num, val in lst:
            result.append((val, num))
    return result
```

## Task 12: Type Checking

The code should be validated with mypy to ensure type correctness. Any necessary changes should be made based on mypy's feedback.
