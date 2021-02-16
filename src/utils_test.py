import unittest
import utils


class TestUtils(unittest.TestCase):
    def test_to_idx(self):
        action = "1B5D"
        got = utils.to_idx(action)
        want = (0, 1, 4, 3)

        self.assertEqual(got, want)

        r, c, r_, c_ = got
        action_rv = utils.to_str(r, c, r_, c_)
        self.assertEqual(action_rv, action)


if __name__ == "__main__":
    unittest.main()