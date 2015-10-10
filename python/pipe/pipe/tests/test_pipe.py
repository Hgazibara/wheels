import unittest

import pipe.pipe
import fakes


class TestPipe(unittest.TestCase):
    def test_add_returns_sequence_sum(self):
        sequence = fakes.get_sequence()
        self.assertEqual(sequence | pipe.pipe.add(), fakes.get_sequence_sum())


if __name__ == '__main__':
    unittest.main()
