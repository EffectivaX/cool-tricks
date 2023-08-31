'''
@author: Google Jr
@program: type annotation
'''


class TypeAnnotation:
    def example1(self):
        def add(a: int, b: int) -> int:
            return a + b

        print(add(1, 2))

        def add(a: int, b: int) -> int:
            return a + b

        print(add(1, 2))

        def multiply(a: int, b: int) -> int:
            return a * b

        print(multiply(2, 3))

        def divide(a: int, b: int) -> float:
            return a / b

        print(divide(2, 3))

    def example2(self):
        # using strings this time
        def what_is_better(a: str, b: str) -> str:
            return f"{a} is better than {b}"

        print(what_is_better("Python", "Java"))


if __name__ == "__main__":
    ta = TypeAnnotation()
    print("Example 1:")
    ta.example1()
    print("Example 2:")
    ta.example2()
