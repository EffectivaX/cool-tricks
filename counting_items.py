'''
@author; Google Jr
@program: counting items
'''


class CountingItems:
    def count_items(self):
        from random import randint
        # old way
        ratings = [randint(1, 10) for _ in range(0, 101)]
        for i in range(1, 6):
            print(f"{i} stars: {ratings.count(i)}")

        #for names as well
        names = ["Andile", "Ayanda", "Zola", "Olwethu", "Nondyebo",
                 "Andile", "Mzie", "Ayanda", "Zola", "Nondyebo", "Andile"]
        for name in set(names):
            print(f"{name}: {names.count(name)}")

        # new way using collections
        from collections import Counter
        ratings_counter = Counter(ratings)
        for rating in ratings_counter:
            print(f"{rating} stars: {ratings_counter[rating]}")


if __name__ == "__main__":
    ci = CountingItems()
    ci.count_items()
