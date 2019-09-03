#!/usr/bin/env python3

from colorama import Fore, Back, Style
import random


def create_deck():
    deck = []
    for i in range(4):
        if i == 0:
            suit = Fore.BLACK + u'\u2660'
        elif i == 1:
            suit = Fore.RED + u'\u2665'
        elif i == 2:
            suit = Fore.BLUE + u'\u2666'
        else:
            suit = Fore.GREEN + u'\u2663'
        for j in range(1,14):
            if j == 1:
                card = "A" + suit
            elif j == 10:
                card = "T" + suit
            elif j == 11:
                card = "J" + suit
            elif j == 12:
                card = "Q" + suit
            elif j == 13:
                card = "K" + suit
            else:
                card = Fore.BLACK + str(j) + suit
            deck.append(card)
    return deck


def main():
    # Create deck of cards
    deck = create_deck()
    # Shuffle deck of cards
    random.shuffle(deck)
    # Deal two cards to each player
    player_one_hand = []
    player_two_hand = []
    for position in range(5):
        player_one_hand.append(deck.pop())
        player_two_hand.append(deck.pop())
    # Print out the hands
    print(Style.RESET_ALL + "Player 1 has:", end=' ')
    for card in player_one_hand:
        print(Back.WHITE + Fore.BLACK + card + Back.BLACK, end=' ')
    print(Style.RESET_ALL + "\nPlayer 2 has:", end=' ')
    for card in player_two_hand:
        print(Back.WHITE + Fore.BLACK + card + Back.BLACK, end=' ')
    print(Style.RESET_ALL + "\n")


if __name__ == "__main__":
    main()
