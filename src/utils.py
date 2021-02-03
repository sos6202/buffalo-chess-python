def to_idx(action: str) -> (int, int, int, int):
    """Converts action string to index for game state

    Argument:
        action(str): Input action in string format e.g)"A1B3"
    Returns:
        x, y (int, int): Coordinate of first 2 position
        x_, y_ (int, int): Coordinate of second 2 position
    """

    r, c, r_, c_ = list(action)
    r = int(r) - 1
    c = ord(c) - 65
    r_ = int(r_) - 1
    c_ = ord(c_) - 65

    return r, c, r_, c_


def index_to_action(x, y, x_, y_):
    """Converts index to action in string format

    Args:
        x (int): 
        y (int): 
        x_ (int):
        y_ (int):

    Returns:
        action(str): String format action
    """
