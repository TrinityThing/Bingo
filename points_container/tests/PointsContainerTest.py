import unittest
from points_container.PointsContainer import PointsContainer

class PointsContainerTestCase(unittest.TestCase):

    def test_create_points_container(self):
        self.assertTrue(PointsContainer() is not None)

    def test_add_points(self):
        pointsContainer = PointsContainer()
        pointsContainer.setPlayersAndOptions({"Kaj": "Op1"})
        pointsContainer.addPointToPlayer("Kaj")
        self.assertEqual(pointsContainer.getPoints("Kaj"), 1)

    def test_add_negative_points(self):
        pointsContainer = PointsContainer()
        pointsContainer.setPlayersAndOptions({"Kaj": "Op1"})
        self.assertRaises(ValueError, pointsContainer.addPointToPlayer, "Kaj", -1)

    def test_add_points_to_unexisting_player(self):
        pointsContainer = PointsContainer()
        self.assertRaises(Exception, pointsContainer.addPointToPlayer, "Kaj", -1)

    def test_add_points_by_quote(self):
        pointsContainer = PointsContainer()
        pointsContainer.setPlayersAndOptions({"Kaj": "Op1"})
        pointsContainer.addPointByQuote("Op1")
        self.assertEqual(pointsContainer.getPoints("Kaj"), 1)

    def test_add_points_by_not_existing_quote(self):
        pointsContainer = PointsContainer()
        pointsContainer.setPlayersAndOptions({"Kaj": "Op1"})
        pointsContainer.addPointByQuote("Op2")
        self.assertEqual(pointsContainer.getPoints("Kaj"), 0)

    def test_add_points_with_many_players(self):
        pointsContainer = PointsContainer()
        pointsContainer.setPlayersAndOptions({"Kaj": "Op1", "Kaj3": "Op3", "Kaj2": "Op2", })
        pointsContainer.addPointByQuote("Op2")
        self.assertEqual(pointsContainer.getPoints("Kaj"), 0)
        self.assertEqual(pointsContainer.getPoints("Kaj2"), 1)
        self.assertEqual(pointsContainer.getPoints("Kaj3"), 0)


if __name__ == '__main__':
    unittest.main()
