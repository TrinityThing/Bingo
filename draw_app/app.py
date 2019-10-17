import json
from flask import Flask, request
from drawer.draw import Drawer
from points_container.PointsContainer import PointsContainer

app = Flask(__name__)

@app.route('/draw/rest')
def draw():
    new_draw = global_drawer.draw()
    return json.dumps(new_draw)

@app.route('/draw/rest/addPoints', methods=['POST'])
def addPoinstByName():
    if request.method == 'POST':
        """ Example usage:
            curl -d '{"player":"Kaju", "player2":"Malcin"}' -X POST http://localhost:5000/draw/rest/addPoints
        """
        pointsContainer = PointsContainer()
        pointsContainer.setPlayersAndOptions(global_drawer.draw())

        player = request.get_json(force=True)['player']
        pointsContainer.addPointToPlayer(player)

        playerPoints = pointsContainer.getPoints(player)

        return json.dumps({"Actual Points": playerPoints})
    else:
        raise Exception('This view is gone. 405')

global_drawer = Drawer(['Kaju', 'Adi', 'Mariaczi', 'Karol', 'Sito'])