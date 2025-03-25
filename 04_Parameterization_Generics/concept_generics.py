# # def maximum_int(a: int, b: int) -> int:
# #     return a if a > b else b

# # def maximum_float(a: float, b: float) -> float:
# #     return a if a > b else b

# # def maximum_str(a: str, b: str) -> str:
# #     return a if  a > b else b

# # print(maximum_int(1, 2))
# # print(maximum_float(1.0, 2.0))
# # print(maximum_str('a', 'b'))

from typin import TypeVar

T = TypeVar('T')

def maximum(a: T, b: T) -> T:
