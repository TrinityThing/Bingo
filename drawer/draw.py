import sys
from random import sample


class Drawer:

    def __init__(self, players, options=None):
        self.__players = players
        self.__options = options
        if self.__options is None:
            self.__options = self.__generate_options()

    def __generate_options(self):
        return ["Rozumiesz",
                "E2E",
                "Ryzyko",
                "Chcę wam pomóc",
                "Capacity",
                "Milestone",
                "Business value",
                "Wspólne rozumienie",
                "Sync",
                "Byłem w supporcie",
                "Legacy Break",
                "Product care",
                "A ja mam pytanie",
                "Impediment",
                "MJE",
                "Top Prio",
                "Delivery",
                "Improvement",
                "Proces",
                "Way of working",
                "Robimy Daily",
                "Mitygacja",
                "Inwestygacja",
                "Value for Money",
                "Definition of Done",
                "Testy Automatyczne",
                "Highlighty"]

    def draw(self):
        n_players = len(self.__players)
        shuffled = sample(self.__options, k=n_players)
        items = {p: o for p, o in zip(self.__players, shuffled)}

        return items


def main(argv):
    drawer = Drawer(argv)
    print(drawer.draw())


if __name__ == "__main__":
    sys.exit(main(["Kaj", "Adi", "Karol", "Sito", "Małcin"]))
