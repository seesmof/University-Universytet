import os

current_dir: str = os.path.dirname(os.path.abspath(__file__))


class Constants:
    ROOT_DIR: str = os.path.join(current_dir, "..")
