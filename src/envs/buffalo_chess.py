import copy
from src import utils

# Set initial state
MAP = [
    "BBBBBBBBBBB",
    "NNNNNNNNNNN",
    "NNNNNNNNNNN",
    "NNNNNNNNNNN",
    "NNNNNNNNNNN",
    "NNNDDHDDNNN",
    "NNNNNNNNNNN",
]
WIDTH = 7
HEIGHT = 11


class BuffaloChess():
    """
    B: Buffalo
    N: Background
    H: Hunter
    D: Dog
    """
    BUFFALO_REWARD = 1
    HUNTER_REWARD = -1

    def __init__(self):
        self.reset()

    def render(self):
        # Replace all N to blank
        return

    def reset(self):
        """Restart game"""
        self.state = copy.deepcopy(MAP)
        self.turn = 0   # Buffalo start first
        self.done = False

    def is_done(self) -> bool:
        """Return True if game is done, else return False

        Returns:
            bool: Game state is terminal
        """
        # if any buffalo reached to the end
        if "B" in self.state[6]:
            return True

        # if all buffalos hunted
        for row in self.state:
            if "B" in row:
                break

        # maybe all buffaloes cannot move
        actions = self.get_possible_moves(0)
        if len(actions) == 0:
            return True
        return False

    def step(self, action: str):
        """Returns next observation of game state after player action

        Args:
            action (str): String format action "1A4B"

        Returns:
            tuple: observation(np.array), reward(int), done(bool), info(dict)
        """
        # parse action string into array indexes

        # check if valid turn
        # check if valid movement

        # move if able
        # next turn

        # check game is done
        # if done, give reward

    def move(self, action: str):
        """Run forced action

        Args:
            action (str): "1A5B"
        """
        r, c, r_, c_ = utils.to_idx(action)
        marker = self.state[r][c]

        line = list(self.state[r])
        line[c] = "N"
        self.state[r] = "".join(line)

        line = list(self.state[r_])
        line[c_] = marker
        self.state[r_] = "".join(line)

    def is_valid_turn(self, idx, turn) -> bool:
        """Return True if marker move is valid for turn

        Args:
            turn ([type]): [description]

        Returns:
            bool: [description]
        """
        # if turn == 0, marker must be B

        # elif turn == 1, marker must be H or D

        # if None, marker must be B, H, or D

    def get_possible_moves(self, turn) -> list:
        """Returns all possible actions in string format

        Args:
            turn (bool): True if Buffalo's turn, else False. If None,
                         return all possible actions
        Returns:
            actions (list): Contains string format actions
        """
        # check turn
        # if buffalo's, append B to markers
        # if hunter's append H, D to markers
        # if None, append all

        actions = []
        # loop all state
        # for each (r, c), inc
        return actions

    def inc(self, r, c) -> list:
        """Returns all possible move positions

        Returns:
            actions(list): contains action in string format
        """
        actions = []
        # if buffalo
        # only down movement -> (+1, 0)

        # if hunter
        # all direction one step
        # check is inbound
        # able to move if B, N

        # if dog
        # hunter move iterative
        # but not B

        return actions
