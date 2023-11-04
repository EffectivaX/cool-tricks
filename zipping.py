'''
@author: Google Jr
@programs: Zipping in python
'''


class Zipping:
    def example(self):
        tech_ceos = ["Elon Musk", "Jeff Bezos",
                     "Satya Nadella", "Mark Zuckerberg", "Tim Cook"]
        tech_companies = ["Tesla", "Amazon", "Microsoft", "Facebook", "Apple"]
        net_worths = [185, 186, 2, 101, 1]
        zipped = list(zip(tech_ceos, tech_companies, net_worths))

        for ceo in zipped:
            print(f"{ceo[0]} is the CEO of {ceo[1]} and is worth ${ceo[2]} billion")
        return zipped

    def example2(self):
        tech_ceos = ["Elon Musk", "Jeff Bezos",
                     "Satya Nadella", "Mark Zuckerberg", "Tim Cook"]
        tech_companies = ["Tesla", "Amazon", "Microsoft", "Facebook", "Apple"]
        net_worths = [185, 186, 134, 101, 1]
        zipped = list(zip(tech_ceos, tech_companies, net_worths))
        unzipped = list(zip(*zipped))
        return unzipped

    def example3(self):
        tech_ceos = ["Elon Musk", "Sundar Pichai",
                     "Satya Nadella", "Mark Zuckerberg", "Tim Cook"]
        tech_companies = ["Tesla", "Google", "Microsoft", "Facebook", "Apple"]
        net_worths = [185, 5, 134, 101, 1]
        zipped = list(zip(tech_ceos, tech_companies, net_worths))
        unzipped = list(zip(*zipped))
        names, companies, worths = unzipped
        return names, companies, worths


if __name__ == "__main__":
    z = Zipping()
    print("Example 1:", z.example())
    print("Example 2:", z.example2())
    print("Example 3:", z.example3())
