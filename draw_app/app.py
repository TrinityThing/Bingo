import json
from flask import Flask, redirect, request, render_template, url_for
from drawer.draw import Drawer
from draw_app.models.points import PointsContainer

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for("draw_html"))


@app.route('/draw/')
def draw_html():
    return render_template("draw.html", items=global_drawer.draw())


@app.route('/draw/api/daily')
def draw():
    new_draw = global_drawer.draw()
    return json.dumps(new_draw)


@app.route('/draw/api/players/<string:player_name>/points', methods=['GET', 'POST'])
def add_points_by_name(player_name):
    if request.method == 'GET':
        points_container = PointsContainer()
        points_container.set_players_and_options(global_drawer.draw())

        player_points = points_container.get_points(player_name)
        return json.dumps({player_name: player_points})
    elif request.method == 'POST':
        # TODO(kaj): Handle correctness of request

        action = request.get_json(force=True)['action']

        points_container = PointsContainer()
        points_container.set_players_and_options(global_drawer.draw())

        if action == 'add':
            points_container.add_point_to_player(player_name)
        elif action == 'reset':
            points_container.reset_points(player_name)
        else:
            raise Exception('Incorrect request')

        player_points = points_container.get_points(player_name)
        return json.dumps({player_name: player_points})
    else:
        raise Exception('This template is gone. 405')


global_drawer = Drawer(['Kaju', 'Adi', 'Mariaczi', 'Karol', 'Śto'])
