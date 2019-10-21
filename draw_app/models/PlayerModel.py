from pony.orm import db_session

from draw_app.models.model_configuration import Player


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
