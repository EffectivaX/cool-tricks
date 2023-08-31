class ParameterExpansion:
    def example1(self):
        '''
        >>> pe = ParameterExpansion()
        >>> pe.example1()
        6
        15
        '''

        # old way
        def add(a, b, c):
            '''
            >>> add(1, 2, 3)
            6
            >>> add(3, 5, 7)
            15
            '''
            return a + b + c

        # new way
        def add(*args):
            '''
            >>> add(1, 2, 3)
            6
            >>> add(3, 5, 7)
            15
            '''
            return sum(args)

        print(add(1, 2, 3))
        print(add(3, 5, 7))

    def example2(self):
        '''
        >>> pe = ParameterExpansion()
        >>> pe.example2()
        6
        12
        '''

        # old way
        def add(a, b, c):
            '''
            >>> numbers = [1, 2, 3]
            >>> add(numbers[0], numbers[1], numbers[2])
            6
            '''
            return a + b + c

        numbers = [1, 2, 3]
        print(add(numbers[0], numbers[1], numbers[2]))

        # new way
        def add(*args):
            '''
            >>> numbers = [6, 2, 4]
            >>> add(*numbers)
            12
            '''
            return sum(args)

        numbers = [6, 2, 4]
        print(add(*numbers))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    pe = ParameterExpansion()
    print("Example 1:")
    pe.example1()
    print("Example 2:")
    pe.example2()
