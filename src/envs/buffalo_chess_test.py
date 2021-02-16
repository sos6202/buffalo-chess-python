import unittest
import copy
from src.envs import buffalo_chess as bc

MAP = [
    "BBBBBBBBBBB",
    "NNNNNNNNNNN",
    "NNNNNNNNNNN",
    "NNNNNNNNNNN",
    "NNNNNNNNNNN",
    "NNNDDHDDNNN",
    "NNNNNNNNNNN",
]


class TestEnv(unittest.TestCase):
    def setUp(self):
        self.map = copy.deepcopy(MAP)

    def test_move(self):
        env = bc.BuffaloChess()
        env.move("1A4B")

        want = [
            "NBBBBBBBBBB",
            "NNNNNNNNNNN",
            "NNNNNNNNNNN",
            "NBNNNNNNNNN",
            "NNNNNNNNNNN",
            "NNNDDHDDNNN",
            "NNNNNNNNNNN",
        ]

        self.assertEqual(env.state, want)

    def test_actions(self):
        env = bc.BuffaloChess()
        state = [
            "NNNNNNNNNNN",
            "NNBBBNNNNNN",
            "NNNNNNNNNNN",
            "NNNNNNBBNNN",
            "NNNNNNNNNNN",
            "NNNNNNNNNBN",
            "NNNNNNNNNNN",
        ]
        env.state = state
        actions = env.get_possible_moves(bc.BuffaloChess.TURN_B)
        self.assertEqual(len(actions), 6)

    def test_is_done(self):
        no_buf = [
            "NNNNNNNNNNN",
            "NNNNNNNNNNN",
            "NNNNNNNNNNN",
            "NHNNNDDDDNN",
            "NNNNNNNNNNN",
            "NNNNNNNNNNN",
            "NNNNNNNNNNN",
        ]

        env = bc.BuffaloChess()
        env.state = no_buf
        done, reward = env.is_done()
        self.assertEqual(done, True)
        self.assertEqual(reward, bc.BuffaloChess.HUNTER_REWARD)

        buf_win = [
            "NNNNNNNNNNN",
            "NNNNNNNNNNN",
            "NNNNNNNNNNN",
            "NNNNNNDDDDN",
            "NNNNNNNNNNN",
            "NNNNNNHNNNN",
            "NBNNNNNNNNN",
        ]

        env.state = buf_win
        done, reward = env.is_done()
        self.assertEqual(done, True)
        self.assertEqual(reward, bc.BuffaloChess.BUFFALO_REWARD)

        no_move = [
            "NNNNNNNNNNN",
            "NNNNNNBNNNN",
            "NNNNNNDNNNN",
            "NNBNNNNNNNN",
            "NNDNNHNNDNN",
            "NNNNNNNNBNN",
            "NNNNNNNNDNN",
        ]
        env.state = no_move
        done, reward = env.is_done()
        self.assertEqual(done, True)
        self.assertEqual(reward, bc.BuffaloChess.HUNTER_REWARD)

        not_done = [
            "NNNNNNNNNNN",
            "NNNNNNNNNNN",
            "NNNNDNDNNNN",
            "NNNNNNNNNNN",
            "NNNNNNBNNNN",
            "NNHNNNDNNBN",
            "NNNNNNNNNNN",
        ]
        env.state = not_done
        done, reward = env.is_done()
        self.assertEqual(done, False)
        self.assertEqual(reward, 0)

    def test_get_actions(self):
        dogs = [
            "NNNNNNNNNNN",
            "NNNNNNNNNNN",
            "NNNNNBNNNNN",
            "NNNNNDNNNNN",
            "NBNNNNNNNBN",
            "NNNNNNNNNNN",
            "NNNNNNNNNNN",
        ]
        env = bc.BuffaloChess()
        env.state = dogs

        want = 12 + 10 + 3
        actions = env.get_actions(3, 5)
        self.assertEqual(want, len(actions))


if __name__ == "__main__":
    unittest.main()
