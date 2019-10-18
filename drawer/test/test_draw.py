import unittest
from drawer.draw import Drawer


class DrawerTestCase(unittest.TestCase):

    def test_doubled_drawing(self):
        local_options = ["Option1", "Option2"]
        drawer = Drawer(["Player1", "Player2"], ["Option1", "Option2"])
        result = drawer.draw()
        for player, option in result.items():
            self.assertTrue(option in local_options)

    def test_simple_drawing(self):
        drawer = Drawer(["Player1"], ["Option1"])
        self.assertEqual({"Player1": "Option1"}, drawer.draw())

    def test_no_options_works(self):
        drawer = Drawer(["Player"])
        self.assertGreater(len(drawer.draw()), 0)

    def test_same_seed_twice(self):
        drawer = Drawer(["Player1", "Player2"], ["Option1", "Option2", "Option3"])
        result = drawer.draw()
        result_second = drawer.draw()
        self.assertEqual(result, result_second)

if __name__ == '__main__':
    unittest.main()
