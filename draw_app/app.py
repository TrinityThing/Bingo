import codecs
import configparser
import json
import sys
import os
from flask import Flask, request
from drawer.draw import Drawer
from drawer.points import PointsContainer

app = Flask(__name__)


@app.route('/draw/rest')
def draw():
    new_draw = global_drawer.draw()
    return json.dumps(new_draw)


@app.route('/draw/rest/addPoints', methods=['POST'])
def addPoinstByName():
    if request.method == 'POST':
        """ Example usage:
            curl -d '{"player":"Kaju"}' -X POST http://localhost:5000/draw/rest/addPoints
        """
        #TODO(kaj): Handle correctness of request
        points_container = PointsContainer()
        points_container.set_players_and_options(global_drawer.draw())

        player = request.get_json(force=True)['player']
        points_container.add_point_to_player(player)

        player_points = points_container.get_points(player)

        return json.dumps({"Actual Points": player_points})
    else:
        raise Exception('This view is gone. 405')


def get_config():
    parser = configparser.ConfigParser(allow_no_value=True)
    parser.optionxform = str

    cfg_path = os.getenv("DRAW_APP_CONFIG_FILE", "config.ini")
    cfg_file = codecs.open(cfg_path, "r", "utf8")
    parser.read_file(cfg_file)

    required_sections = ["names", "options"]
    if not all(item in parser.sections() for item in required_sections):
        sys.exit("Error: Missing [names] or [options] section in config file")

    names = parser.options("names")
    options = parser.options("options")
    if len(names) > len(options):
        sys.exit("Error: More players than available options")

    return names, options


player_names, bingo_options = get_config()
global_drawer = Drawer(player_names, bingo_options)
