'''
@author: Google Jr
@program: list compression
'''

class ListCompressor:
    def example1(self):
        """
        Example 1: Square of Numbers
        
        This function returns a list of squares of numbers from 0 to 10.

        >>> lc = ListCompressor()
        >>> lc.example1()
        [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        """
        numbers = [i ** 2 for i in range(0, 11)]
        return numbers

    def example2(self):
        """
        Example 2: First Letters of Names
        
        This function returns a list of the first letters of names.

        >>> lc = ListCompressor()
        >>> lc.example2()
        ['A', 'M', 'A', 'Z', 'O', 'N']
        """
        names = ["Andile", "Mzie", "Ayanda", "Zola", "Olwethu", "Nondyebo"]
        first_letters = [name[0] for name in names]
        return first_letters

    def example3(self):
        """
        Example 3: Double Even Numbers
        
        This function returns a list of doubled even numbers from 0 to 10.

        >>> lc = ListCompressor()
        >>> lc.example3()
        [0, 4, 8, 12, 16, 20]
        """
        numbers = [i * 2 for i in range(0, 11) if i % 2 == 0]
        return numbers

    def example4(self):
        """
        Example 4: Double Even Numbers, Triple Odd Numbers
        
        This function returns a list where even numbers are doubled and odd numbers are tripled from 0 to 10.

        >>> lc = ListCompressor()
        >>> lc.example4()
        [0, 3, 4, 9, 8, 15, 12, 21, 16, 27, 20]
        """
        numbers = [i * 2 if i % 2 == 0 else i * 3 for i in range(0, 11)]
        return numbers

    def example5(self):
        """
        Example 5: Double Even Numbers, Triple Divisible by 3
        
        This function returns a list where even numbers are doubled and numbers divisible by 3 are tripled from 0 to 10.

        >>> lc = ListCompressor()
        >>> lc.example5()
        [0, 9, 12, 27]
        """
        numbers = [i * 2 if i % 2 == 0 else i * 3 for i in range(0, 11) if i % 3 == 0]
        return numbers

    def example6(self):
        """
        Example 6: Double Even Numbers, Triple Divisible by 3 and 2
        
        This function returns a list where even numbers are doubled and numbers divisible by both 3 and 2 are tripled from 0 to 10.

        >>> lc = ListCompressor()
        >>> lc.example6()
        [0, 12]
        """
        numbers = [i * 2 if i % 2 == 0 else i * 3 for i in range(0, 11) if i % 3 == 0 and i % 2 == 0]
        return numbers

    def example7(self):
        """
        Example 7: Numbers Divisible by 12
        
        This function returns a list of numbers from 1 to 100 that are divisible by 12.

        >>> lc = ListCompressor()
        >>> lc.example7()
        [12, 24, 36, 48, 60, 72, 84, 96]
        """
        numbers = [i for i in range(1, 101) if i % 12 == 0]
        return numbers


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    lc = ListCompressor()
    print("Example 1:", lc.example1())
    print("Example 2:", lc.example2())
    print("Example 3:", lc.example3())
    print("Example 4:", lc.example4())
    print("Example 5:", lc.example5())
    print("Example 6:", lc.example6())
    print("Example 7:", lc.example7())
