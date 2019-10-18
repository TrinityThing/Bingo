import sys

from datetime import date
from random import Random


class Drawer:
    """ This comes when you are tired of your entire life """

    def __init__(self, players: list, options: list = None):
        """
        :arg players array of players Eg. ["p1", "p2"]
        :arg options array of possibilities to be draw
        """
        self.__players = players
        self.__options = options
        if self.__options is None: self.__options = self.__generate_options()

    def draw(self):
        n_players = len(self.__players)
        shuffled = self.__shuffle_pack(n_players)
        items = {p: o for p, o in zip(self.__players, shuffled)}

        return items

    def __shuffle_pack(self, n_players):
        generator = Random(self.__generate_daily_seed())
        shuffled = generator.sample(self.__options, k=n_players)
        return shuffled

    def __generate_daily_seed(self):
        current_date = date.today()
        return current_date.toordinal()

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


def main(argv):
    drawer = Drawer(argv)
    print(drawer.draw())


if __name__ == "__main__":
    sys.exit(main(["Kaj", "Adi", "Karol", "Sito", "Małcin"]))
