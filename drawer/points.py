import sys


class PointsContainer:

    def set_players_and_options(self, player_and_options: set):
        self.__players_and_options = player_and_options
        self.__add_players()

    def add_point_to_player(self, player: str, points: int = 1):
        if player not in self.__players_and_options: raise Exception("Error")
        if points < 0: raise ValueError("Error")
        self.__players_points[player] += points

    def add_point_by_quote(self, quote: str, points: int = 1):
        players = (p for p, q in self.__players_and_options.items() if q == quote)
        for p in players:
            self.add_point_to_player(p)

    def get_points(self, player: str):
        return self.__players_points[player]

    def __add_players(self):
        self.__players_points = {p: 0 for p in self.__players_and_options.keys()}


