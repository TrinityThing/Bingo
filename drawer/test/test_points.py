import unittest
from drawer.points import PointsContainer


class PointsContainerTestCase(unittest.TestCase):

    def test_create_points_container(self):
        self.assertTrue(PointsContainer() is not None)

    def test_add_points(self):
        pointsContainer = PointsContainer()
        pointsContainer.set_players_and_options({"Kaj": "Op1"})
        pointsContainer.add_point_to_player("Kaj")
        self.assertEqual(pointsContainer.get_points("Kaj"), 1)

    def test_add_negative_points(self):
        pointsContainer = PointsContainer()
        pointsContainer.set_players_and_options({"Kaj": "Op1"})
        self.assertRaises(ValueError, pointsContainer.add_point_to_player, "Kaj", -1)

    def test_add_points_to_unexisting_player(self):
        pointsContainer = PointsContainer()
        self.assertRaises(Exception, pointsContainer.add_point_to_player, "Kaj", -1)

    def test_add_points_by_quote(self):
        pointsContainer = PointsContainer()
        pointsContainer.set_players_and_options({"Kaj": "Op1"})
        pointsContainer.add_point_by_quote("Op1")
        self.assertEqual(pointsContainer.get_points("Kaj"), 1)

    def test_add_points_by_not_existing_quote(self):
        pointsContainer = PointsContainer()
        pointsContainer.set_players_and_options({"Kaj": "Op1"})
        pointsContainer.add_point_by_quote("Op2")
        self.assertEqual(pointsContainer.get_points("Kaj"), 0)

    def test_add_points_with_many_players(self):
        pointsContainer = PointsContainer()
        pointsContainer.set_players_and_options({"Kaj": "Op1", "Kaj3": "Op3", "Kaj2": "Op2", })
        pointsContainer.add_point_by_quote("Op2")
        self.assertEqual(pointsContainer.get_points("Kaj"), 0)
        self.assertEqual(pointsContainer.get_points("Kaj2"), 1)
        self.assertEqual(pointsContainer.get_points("Kaj3"), 0)


if __name__ == '__main__':
    unittest.main()
