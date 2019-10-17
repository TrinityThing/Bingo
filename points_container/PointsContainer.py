import sys


class PointsContainer:

    def __init__(self, argv=None):
        pass

    def setPlayersAndOptions(self, player_and_options: set):
        self.__players_and_options = player_and_options
        self.__addPlayers()

    def addPointToPlayer(self, player: str, points: int = 1):
        if not player in self.__players_and_options: raise Exception("Errror")
        if points < 0: raise ValueError("Errror")
        self.__players_points[player] = self.__players_points[player] + points
        pass

    def addPointByQuote(self, quote: str, points: int = 1):
        players = [p if q == quote else None for p, q in self.__players_and_options.items()]
        for p in players:
            try:
                self.addPointToPlayer(p)
            except:
                pass

    def getPoints(self, player: str):
        return self.__players_points[player]

    def __addPlayers(self):
        self.__players_points = {}
        for player, _ in self.__players_and_options.items():
            self.__players_points[player] = 0


def main(argv):
    return PointsContainer(argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
