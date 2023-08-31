'''
@author: Google Jr
@program: list compression
'''

class ListCompressor:
    def example1(self):
        numbers = [i ** 2 for i in range(0, 11)]
        return numbers

    def example2(self):
        names = ["Andile", "Mzie", "Ayanda", "Zola", "Olwethu", "Nondyebo"]
        first_letters = [name[0] for name in names]
        return first_letters

    def example3(self):
        numbers = [i * 2 for i in range(0, 11) if i % 2 == 0]
        return numbers

    def example4(self):
        numbers = [i * 2 if i % 2 == 0 else i * 3 for i in range(0, 11)]
        return numbers

    def example5(self):
        numbers = [i * 2 if i % 2 == 0 else i * 3 for i in range(0, 11) if i % 3 == 0]
        return numbers

    def example6(self):
        numbers = [i * 2 if i % 2 == 0 else i * 3 for i in range(0, 11) if i % 3 == 0 and i % 2 == 0]
        return numbers

    def example7(self):
        numbers = [i for i in range(1, 101) if i % 12 == 0]
        return numbers


if __name__ == "__main__":
    lc = ListCompressor()
    print("Example 1:", lc.example1()) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    print("Example 2:", lc.example2()) # ['A', 'M', 'A', 'Z', 'O', 'N']
    print("Example 3:", lc.example3()) # [0, 4, 8, 12, 16, 20]
    print("Example 4:", lc.example4()) # [0, 3, 4, 9, 8, 15, 12, 21, 16, 27, 20]
    print("Example 5:", lc.example5()) # [0, 9, 12, 21, 24, 33, 36, 45, 48, 57, 60]
    print("Example 6:", lc.example6()) # [0, 12, 24, 36, 48, 60]
    print("Example 7:", lc.example7()) # [12, 24, 36, 48, 60, 72, 84, 96]

