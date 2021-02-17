import copy
from src import utils


class NotValidActionError(Exception):
    pass


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
ROWS = 7
COLS = 11


class BuffaloChess:
    """
    B: Buffalo
    N: Background
    H: Hunter
    D: Dog
    """

    TURN_B = 1
    TURN_H = -1

    BUFFALO_REWARD = 100
    HUNTER_REWARD = -100

    def __init__(self):
        self.reset()
        self.turn = self.TURN_B

    def render(self):
        # Replace all N to blank
        return

    def reset(self):
        """Restart game"""
        self.state = copy.deepcopy(MAP)
        self.turn = self.TURN_B  # Buffalo start first
        self.done = False

    def is_done(self) -> (bool, int):
        """Check is game state is terminal.
        Returns bool with reward depending on who won

        Returns:
            bool: Game state is terminal
        """
        # if any buffalo reached to the end
        if "B" in self.state[6]:
            return True, self.BUFFALO_REWARD

        # maybe all buffaloes cannot move
        # contains all buffalo hunted
        actions = self.get_possible_moves(self.TURN_B)
        if len(actions) == 0:
            return True, self.HUNTER_REWARD

        return False, 0

    def step(self, action: str):
        """Take an action for the game. Returns observation after action.

        Args:
            action (str): String format action "1A4B"

        Returns:
            tuple: observation(np.array), reward(int), done(bool), info(dict)
        """

        # check if valid turn
        # check if valid movement
        if not action in self.get_possible_moves(self.turn):
            raise NotValidActionError

        # move if able
        self.move(action)
        # next turn
        self.next_turn()

        # check game is done
        done, reward = self.is_done()

        # s, r, d, _
        return self.state, reward, done, {}

    def next_turn(self):
        if self.turn == self.TURN_B:
            self.turn = self.TURN_H
        else:
            self.turn = self.TURN_B

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

    def get_possible_moves(self, turn) -> list:
        """Returns all possible actions in string format

        Args:
            turn (bool): True if Buffalo's turn, else False. If None,
                         return all possible actions
        Returns:
            actions (list): Contains string format actions
        """
        markers = []
        # check turn
        # if buffalo's, append B to markers
        if turn == self.TURN_B or turn == None:
            markers.append("B")
        # if hunter's append H, D to markers
        elif turn == self.TURN_H or turn == None:
            markers.append("H")
            markers.append("D")

        actions = []
        # loop all state
        for r in range(ROWS):
            for c in range(COLS):
                if self.state[r][c] in markers:
                    actions += self.get_actions(r, c)
        return actions

    def get_actions(self, r, c) -> list:
        """Returns all possible move from position

        Returns:
            actions(list): contains action in string format
        """
        actions = []
        # buffalo
        if self.state[r][c] == "B" and self.state[r + 1][c] == "N":
            # movement -> (+1, 0)
            action = utils.to_str(r, c, r + 1, c)
            actions.append(action)

        # hunter
        dirs = [-1, 0, 1]
        if self.state[r][c] == "H":
            for dr in dirs:
                for dc in dirs:
                    if dr == 0 and dc == 0:
                        continue

                    if all(
                        [
                            0 <= r + dr < ROWS,
                            0 <= c + dc < COLS,
                        ]
                    ):
                        if not self.state[r + dr][c + dc] != "D":  # only if B or N
                            continue

                        action = utils.to_str(r, c, r + dr, c + dc)
                        actions.append(action)

        if self.state[r][c] == "D":
            for dr in dirs:
                for dc in dirs:
                    if dr == 0 and dc == 0:
                        continue

                    next_r = r
                    next_c = c
                    while True:
                        if all(
                            [
                                0 <= next_r + dr < ROWS,
                                0 <= next_c + dc < COLS,
                            ]
                        ):
                            # only if empty
                            if not self.state[next_r + dr][next_c + dc] == "N":
                                break
                            action = utils.to_str(r, c, next_r + dr, next_c + dc)
                            actions.append(action)
                            next_r = next_r + dr
                            next_c = next_c + dc
                        else:
                            break

        return actions
