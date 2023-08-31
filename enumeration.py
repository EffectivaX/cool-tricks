'''
@author: Google Jr
@program: enumerate
'''


class Enumerate:
    def example1(self):
        names = ["Andile", "Ayanda", "Zola", "Olwethu", "Nondyebo"]
        for i, name in enumerate(names):
            # By default, enumerate starts at 0
            print(f"{i}: {name}")

    def example2(self):
        names = ["Andile", "Ayanda", "Zola", "Olwethu", "Nondyebo"]
        for i, name in enumerate(names, start=1):
            # By default, enumerate starts at 0. To start at 1, use start=1
            print(f"{i}: {name}")


if __name__ == "__main__":
    e = Enumerate()
    print("Example 1:")
    e.example1()
    print("Example 2:")
    e.example2()
