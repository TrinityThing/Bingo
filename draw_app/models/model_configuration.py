from pony.orm import PrimaryKey, Required, Optional

from draw_app.settings import db


class Player(db.Entity):
    id = PrimaryKey(int, auto=True)
    player_name = Required(str, unique=True)
    points_counter = Optional(int)


db.generate_mapping(create_tables=True)
