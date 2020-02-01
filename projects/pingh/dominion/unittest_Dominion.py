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

    def test_Action_card(self):
        #  initialization
        self.setUp()
        card = Dominion.Action_card('Woodcutter', 3, 0, 0, 1, 2)
        self.player.hand.append(card)
        self.player.actions = 0
        self.player.buys = 1
        self.player.purse = 2
        # use function
        card.use(self.player, self.trash)
        self.assertEqual(5, len(self.player.hand))
        self.assertEqual(1, len(self.player.played))
        # augment function
        card.augment(self.player)
        self.assertEqual(0, card.actions)
        self.assertEqual(1, card.buys)
        self.assertEqual(2, card.coins)

        # take 2nd card
        self.player.hand.append(card)
        card.use(self.player, self.trash)
        self.assertEqual(2, len(self.player.played))

    def test_Player(self):
        player = Dominion.Player('Annie')
        # action_balance function
        self.assertEqual(0.0, player.action_balance())

        # calcpoints function
        self.assertEqual(3, player.calcpoints())

        player.deck = [Dominion.Copper()]*9 + [Dominion.Estate()]*4
        self.assertEqual(0.0, player.action_balance())
        # self.assertEqual(6, player.calcpoints())

        # draw function
        card = player.draw()
        self.assertEqual('Copper', card.name)

        # cardsummary function
        summary = player.cardsummary()
        self.assertEqual(5, summary['VICTORY POINTS'])

    def test_gameOver(self):
        #  initialization
        self.setUp()
        res = Dominion.gameover(self.supply)
        self.assertEqual(True, res)


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
