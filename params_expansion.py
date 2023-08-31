'''
@author: Google Jr
@program: parameter expansion
'''

class ParameterExpansion:
    def example1(self):
        # old way
        def add(a, b, c):
            return a + b + c

        print(add(1, 2, 3))

        # new way
        def add(*args):
            return sum(args)

        print(add(1, 2, 3))

    def example2(self):
        # old way
        def add(a, b, c):
            return a + b + c

        numbers = [1, 2, 3]
        print(add(numbers[0], numbers[1], numbers[2]))

        # new way
        def add(*args):
            return sum(args)

        numbers = [1, 2, 3]
        print(add(*numbers))

    

if __name__ == "__main__":
    pe = ParameterExpansion()
    print("Example 1:")
    pe.example1()
    print("Example 2:")
    pe.example2()