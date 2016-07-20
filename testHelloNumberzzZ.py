#!/usr/bin/env python3

import unittest
import helloNumberzZ


class TestHelloNumberzZ(unittest.TestCase):
    def setUp(self):
        pass

    def test_add_numberzZ(self):
        int1 = 2
        int2 = 3

        self.assertEqual(helloNumberzZ.add_numberz(int1, int2), 5)

if __name__ == '__main__':
    unittest.main()
