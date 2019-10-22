from pony.orm import db_session
from draw_app.models.model_configuration import Player


class PointsContainer:

    def __init__(self):
        self.__points_model = PointsModel()
        self.__players_and_options = None

    def set_players_and_options(self, player_and_options: set):
        self.__players_and_options = player_and_options
        self.__add_players()

    def add_point_to_player(self, player: str, points: int = 1):
        if player not in self.__players_and_options: raise Exception("Error")
        if points < 0: raise ValueError("Error")
        self.__points_model.add_point(player)

    def add_point_by_quote(self, quote: str, points: int = 1):
        players = (p for p, q in self.__players_and_options.items() if q == quote)
        for p in players:
            self.add_point_to_player(p)

    def get_points(self, player: str):
        return self.__points_model.get_points(player)

    def reset_points(self, player: str):
        self.__points_model.reset_points(player)

    def __add_players(self):
        self.__players_points = {p: 0 for p in self.__players_and_options.keys()}
        self.__points_model.add_players_if_not_exists(self.__players_and_options)


class PointsModel:

    @db_session
    def add_players_if_not_exists(self, players_and_options):
        for p in players_and_options.keys():
            if not Player.get(player_name=p):
                Player(player_name=p, points_counter=0)

    @db_session
    def add_point(self, player):
        db_player = Player.get(player_name=player)
        db_player.points_counter += 1

    @db_session
    def reset_points(self, player):
        db_player = Player.get(player_name=player)
        db_player.points_counter = 0

    @db_session
    def get_points(self, player):
        return Player.get(player_name=player).points_counter
