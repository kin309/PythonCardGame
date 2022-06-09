from rectangle import Rectangle
from cardpile import discardpile, deck
from hand import hand
from creature import Creature
from card import *
from random import choice
from playergamelogic import PlayerGameLogic

class Player(Creature, PlayerGameLogic):
    def __init__(self, x=180, y=400, width=100, height=100, colorz=(10,120,30), border=True, border_color=(100,170,100)):
        Creature.__init__(self, 10, x, y, width, height, colorz, border, border_color)
        PlayerGameLogic.__init__(self)

        hand.set_interface()
        for x in range(6):
            deck.add_card(BuyCard())

        self.max_energy = 3
        self.current_energy = 3

        self.selected_card = Card()

    def draw_cards_interface(self):
        self.draw()
        self.draw_interface()
        deck.draw_interface()
        discardpile.draw_interface()
        for card in hand.cards:
            card.interface()
        try:
            self.selected_card.interface()
        except AttributeError:
            pass





player1 = Player()