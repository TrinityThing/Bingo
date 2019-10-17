import json
from flask import Flask
from drawer.draw import Drawer

app = Flask(__name__)

@app.route('/draw/rest/')
def draw():
    drawer = Drawer(['Kaju', 'Adi', 'Mariaczi', 'Karol', 'Sito'])
    new_draw = drawer.draw()
    return json.dumps(new_draw)