import testUtility
import Dominion
from unittest import TestCase

class test_Action_card(TestCase):

    def test_init(self):
        card = Dominion.Action_card('Woodcutter', 3, 0, 0, 1, 2)
        self.assertEqual(0, card.actions)
        self.assertEqual(0, card.cards)
        self.assertEqual(1, card.buys)
        self.assertEqual(2, card.coins)

    def test_use(self):
        player = Dominion.Player('Annie')
        trash = []
        card = Dominion.Action_card('Woodcutter', 3, 0, 0, 1, 2)
        player.hand.append(card)

        card.use(player, trash)

        self.assertEqual(5, len(player.hand))
        self.assertEqual(1, len(player.played))

    def test_augment(self):
        player = Dominion.Player('Annie')
        player.actions = 0
        player.buys = 1
        player.purse = 2
        card = Dominion.Action_card('Woodcutter', 3, 0, 0, 1, 2)

        card.augment(player)

        self.assertEqual(0, card.actions)
        self.assertEqual(1, card.buys)
        self.assertEqual(2, card.coins)

    def test_react(self):
        # self.fail()
        pass

class Test_Player(TestCase):

    def test_action_balance(self):
        player = Dominion.Player('Annie')
        player.deck = [Dominion.Copper()] * 1
        player.hand = [Dominion.Copper()] * 1
        self.assertEqual(0.0, player.action_balance())

        player.deck = [Dominion.Thief()]*1
        player.hand = [Dominion.Thief()] * 1
        self.assertEqual(-70.0, player.action_balance())

    def test_calcpoints(self):
        player = Dominion.Player('Annie')
        player.deck = [Dominion.Copper()] * 1
        player.hand = [Dominion.Copper()] * 1
        self.assertEqual(0, player.calcpoints())

        player.deck = [Dominion.Gardens()] * 1
        player.hand = [Dominion.Gardens()] * 1
        self.assertEqual(0, player.calcpoints())

    def test_draw(self):
        player = Dominion.Player('Annie')
        player.deck = [Dominion.Gardens()] * 1
        player.hand = []
        card = player.draw()
        self.assertEqual('Gardens', card.name)

        player.deck = []
        player.hand = []
        player.discard = [Dominion.Gardens()] * 1
        card = player.draw()
        self.assertEqual(0, len(player.deck))

        player.deck = []
        player.hand = []
        player.discard = []
        card = player.draw()
        self.assertIsNone(card)

    def test_cardsummary(self):
        player = Dominion.Player('Annie')
        player.deck = [Dominion.Gardens()] * 1 + [Dominion.Copper()] * 1

        summary = player.cardsummary()

        self.assertEqual(1, summary['Gardens'])

    def test_react(self):
        # self.fail()
        pass

class GameOver(TestCase):

    def test_gameOver(self):
        players = ["Annie"]
        box = {}
        supply = testUtility.GetSupply(box, 5, players)
        res = Dominion.gameover(supply)
        self.assertEqual(True, res)

        box["Province"] = [Dominion.Province()] * 1
        supply = testUtility.GetSupply(box, 5, players)
        res = Dominion.gameover(supply)
        self.assertEqual(False, res)

        box["Woodcutter"] = []
        box["Smithy"] = []
        box["Laboratory"] = []
        supply = testUtility.GetSupply(box, 5, players)
        res = Dominion.gameover(supply)
        self.assertEqual(True, res)


    def test_react(self):
        # self.fail()
        pass

# class TestCard(TestCase):

    # def setUp(self):
    #     # Data setup
    #     self.players = testUtility.GetPlayers()
    #     self.nV = testUtility.GetCurses(self.players)
    #     self.nC = testUtility.GetVictoryCards(self.players)
    #     self.box = testUtility.GetBoxes(self.nV)
    #     self.supply_order = testUtility.GetSupplyOrder()
    #
    #     # Pick n cards from box to be in the supply.
    #     self.supply = testUtility.GetSupply(self.box, 5, self.players)
    #     self.trash = []
    #
    #     self.player = Dominion.Player('Annie')

    # def test_init(self):
    #     # initialize test data
    #     self.setUp()
    #     cost = 1
    #     buypower = 5
    #
    #     # instantiate the card object
    #     card = Dominion.Coin_card(self.player.name, cost, buypower)
    #
    #     # verify that class variables have the expected values
    #     self.assertEqual('Annie', card.name)
    #     self.assertEqual(buypower, card.buypower)
    #     self.assertEqual(cost, card.cost)
    #     self.assertEqual("coin", card.category)
    #     self.assertEqual(0, card.vpoints)

    # def test_react(self):
    #     # self.fail()
    #     pass