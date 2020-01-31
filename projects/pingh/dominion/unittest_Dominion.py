import testUtility
import Dominion
from unittest import TestCase


class TestCard(TestCase):

    def setUp(self):
        # Data setup
        self.players = testUtility.GetPlayers()
        self.nV = testUtility.GetCurses(self.players)
        self.nC = testUtility.GetVictoryCards(self.players)
        self.box = testUtility.GetBoxes(self.nV)
        self.supply_order = testUtility.GetSupplyOrder()

        # Pick n cards from box to be in the supply.
        self.supply = testUtility.GetSupply(self.box, 5, self.players)
        self.trash = []
        self.player = Dominion.Player('Annie')

    def test_init(self):
        # initialize test data
        self.setUp()
        cost = 1
        buypower = 5

        # instantiate the card object
        card = Dominion.Coin_card(self.player.name, cost, buypower)

        # verify that class variables have the expected values
        self.assertEqual('Annie', card.name)
        self.assertEqual(buypower, card.buypower)
        self.assertEqual(cost, card.cost)
        self.assertEqual("coin", card.category)
        self.assertEqual(0, card.vpoints)

    def test_react(self):
        # self.fail()
        pass
