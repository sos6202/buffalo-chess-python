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

    def test_is_done(self):
        pass


if __name__ == "__main__":
    unittest.main()
