import sys

from car_drive_app.game import Game


def main() -> None:
    track_save_name = sys.argv[1]
    game = Game(track_save_name)
    game.run()