# <========== Imports ===========>

from __future__ import annotations
import sys
import os
import unittest


# <========== Local Imports ===========>
parentdir = os.path.realpath(os.path.join(
    os.path.dirname(__file__), os.pardir))

if parentdir not in sys.path:
    sys.path.insert(1, parentdir)

from TicTacToe import TicTacToe
# <========== Tests ===========>

class Testing(unittest.TestCase):
    def test_constructor(self):
        self.assertEqual(TicTacToe().current_player, 0)
        self.assertEqual(TicTacToe(1).current_player, 1)

        with self.assertRaises(Exception) as context: TicTacToe(2)
        self.assertTrue("the first player must be 0 (player 1) or 1 (player 2)" in str( context.exception))

        with self.assertRaises(Exception) as context: TicTacToe(-1)
        self.assertTrue("the first player must be 0 (player 1) or 1 (player 2)" in str(context.exception))


# <========== Main ==========>
if __name__ == '__main__':
    unittest.main()
