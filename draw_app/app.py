import json
from flask import Flask, request, render_template
from drawer.draw import Drawer
from drawer.points import PointsContainer

app = Flask(__name__)


@app.route('/draw/rest')
def draw():
    new_draw = global_drawer.draw()
    return json.dumps(new_draw)


@app.route('/')
@app.route('/draw/')
def draw_html():
    return render_template("draw.html", items=json.loads(draw()))


@app.route('/draw/rest/addPoints', methods=['POST'])
def add_points_by_name():
    if request.method == 'POST':
        """ Example usage:
            curl -d '{"player":"Kaju"}' -X POST http://localhost:5000/draw/rest/addPoints
        """
        # TODO(kaj): Handle correctness of request
        points_container = PointsContainer()
        points_container.set_players_and_options(global_drawer.draw())

        player = request.get_json(force=True)['player']
        points_container.add_point_to_player(player)

        player_points = points_container.get_points(player)

        return json.dumps({"Actual Points": player_points})
    else:
        raise Exception('This templates is gone. 405')


global_drawer = Drawer(['Kaju', 'Adi', 'Mariaczi', 'Karol', 'Śto'])
