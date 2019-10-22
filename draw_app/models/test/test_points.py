import unittest
from draw_app.models.points import PointsContainer


class PointsContainerTestCase(unittest.TestCase):

    def test_create_points_container(self):
        self.assertTrue(PointsContainer() is not None)

    def test_add_points(self):
        points_container = PointsContainer()
        points_container.set_players_and_options({"Kaj": "Op1"})
        points_container.add_point_to_player("Kaj")
        self.assertEqual(points_container.get_points("Kaj"), 1)

    def test_add_negative_points(self):
        points_container = PointsContainer()
        points_container.set_players_and_options({"Kaj": "Op1"})
        self.assertRaises(ValueError, points_container.add_point_to_player, "Kaj", -1)

    def test_add_points_to_unexisting_player(self):
        points_container = PointsContainer()
        self.assertRaises(Exception, points_container.add_point_to_player, "Kaj", -1)

    def test_add_points_by_quote(self):
        points_container = PointsContainer()
        points_container.set_players_and_options({"Kaj": "Op1"})
        points_container.add_point_by_quote("Op1")
        self.assertEqual(points_container.get_points("Kaj"), 1)

    def test_add_points_by_not_existing_quote(self):
        points_container = PointsContainer()
        points_container.set_players_and_options({"Kaj": "Op1"})
        points_container.add_point_by_quote("Op2")
        self.assertEqual(points_container.get_points("Kaj"), 0)

    def test_add_points_with_many_players(self):
        points_container = PointsContainer()
        points_container.set_players_and_options({"Kaj": "Op1", "Kaj3": "Op3", "Kaj2": "Op2", })
        points_container.add_point_by_quote("Op2")
        self.assertEqual(points_container.get_points("Kaj"), 0)
        self.assertEqual(points_container.get_points("Kaj2"), 1)
        self.assertEqual(points_container.get_points("Kaj3"), 0)


if __name__ == '__main__':
    unittest.main()
