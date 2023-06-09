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

    def test_constructor(self: Testing):
        self.assertEqual(TicTacToe().current_player, 0)
        self.assertEqual(TicTacToe(1).current_player, 1)

        with self.assertRaises(Exception) as context: TicTacToe(2)
        self.assertTrue("the first player must be 0 (player 1) or 1 (player 2)" in str( context.exception))

        with self.assertRaises(Exception) as context: TicTacToe(-1)
        self.assertTrue("the first player must be 0 (player 1) or 1 (player 2)" in str(context.exception))

        with self.assertRaises(Exception) as context: TicTacToe(-2)

    def test_set_target(self: Testing):
        t: TicTacToe = TicTacToe()

        self.assertTrue(t.set_target(1))
        self.assertEqual(t.__str__(), "['X' ' ' ' ']\n[' ' ' ' ' ']\n[' ' ' ' ' ']\n")
        self.assertEqual(t.current_player, 1)

        self.assertTrue(t.set_target(2))
        self.assertEqual(t.__str__(), "['X' 'O' ' ']\n[' ' ' ' ' ']\n[' ' ' ' ' ']\n")
        self.assertEqual(t.current_player, 0)

        self.assertFalse(t.set_target(1))
        self.assertEqual(t.__str__(), "['X' 'O' ' ']\n[' ' ' ' ' ']\n[' ' ' ' ' ']\n")
        self.assertEqual(t.current_player, 0)

        t: TicTacToe = TicTacToe()
        for i in range(1,10): t.set_target(i)
        self.assertEqual(t.__str__(), "['X' 'O' 'X']\n['O' 'X' 'O']\n['X' 'X' 'X']\n")
        self.assertEqual(t.current_player, 0)


    def test_is_full(self: Testing):
        t: TicTacToe = TicTacToe()
        for i in range(1, 9):
            t.set_target(i)
            self.assertFalse(t.is_full())

        t.set_target(9)
        self.assertTrue(t.is_full())

    def test_is_player_win(self: Testing):
        t: TicTacToe = TicTacToe()
        self.assertFalse(t.is_player_win())

        t.set_target(1)
        t.set_target(4)
        t.set_target(2)
        t.set_target(5)
        t.set_target(3)
        self.assertTrue(t.is_player_win())

        t: TicTacToe = TicTacToe()
        t.set_target(1)
        t.set_target(2)
        t.set_target(4)
        t.set_target(5)
        t.set_target(7)
        self.assertTrue(t.is_player_win())

        t: TicTacToe = TicTacToe()
        t.set_target(1)
        t.set_target(2)
        t.set_target(5)
        t.set_target(6)
        t.set_target(9)
        self.assertTrue(t.is_player_win())

        t: TicTacToe = TicTacToe()
        t.set_target(3)
        t.set_target(2)
        t.set_target(5)
        t.set_target(6)
        t.set_target(7)
        self.assertTrue(t.is_player_win())
# <========== Main ==========>
if __name__ == '__main__':
    unittest.main()
