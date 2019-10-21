import json
from flask import Flask, redirect, request, render_template, url_for
from drawer.draw import Drawer
from drawer.points import PointsContainer

app = Flask(__name__)


@app.route('/draw/rest')
def draw():
    new_draw = global_drawer.draw()
    return json.dumps(new_draw)


@app.route('/')
def index():
    return redirect(url_for("draw_html"))


@app.route('/draw/')
def draw_html():
    return render_template("draw.html", items=global_drawer.draw())


@app.route('/draw/rest/<string:player_name>/points/add', methods=['POST'])
def add_points_by_name(player_name):
    if request.method == 'POST':
        # TODO(kaj): Handle correctness of request
        points_container = PointsContainer()
        points_container.set_players_and_options(global_drawer.draw())

        player = player_name
        points_container.add_point_to_player(player)

        player_points = points_container.get_points(player)

        return json.dumps({"Actual Points": player_points})
    else:
        raise Exception('This template is gone. 405')


@app.route('/draw/rest/<string:player_name>/points/reset', methods=['POST'])
def reset_points_by_name(player_name):
    if request.method == 'POST':
        # TODO(kaj): Handle correctness of request
        points_container = PointsContainer()
        points_container.set_players_and_options(global_drawer.draw())

        player = player_name

        points_container.reset_points(player)

        player_points = points_container.get_points(player)

        return json.dumps({"Actual Points": player_points})
    else:
        raise Exception('This template is gone. 405')


global_drawer = Drawer(['Kaju', 'Adi', 'Mariaczi', 'Karol', 'Śto'])
