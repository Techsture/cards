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


def deal_card(deck):
    card = deck.pop()
    return card


def deal_community_cards(deck):
    community_cards = []
    # Flop
    deal_card(deck)
    for card in range(3):
        community_cards.append(deal_card(deck))
    # Turn
    deal_card(deck)
    community_cards.append(deal_card(deck))
    # River
    deal_card(deck)
    community_cards.append(deal_card(deck))
    return community_cards


def main():
    # Create deck of cards
    deck = create_deck()
    # Shuffle deck of cards
    random.shuffle(deck)
    # Deal two cards to each player
    player_one_hand = []
    player_two_hand = []
    for position in range(2):
        player_one_hand.append(deal_card(deck))
        player_two_hand.append(deal_card(deck))
    # Print out the hands
    print(Style.RESET_ALL + "Player 1 has:", end=' ')
    for card in player_one_hand:
        print(Back.WHITE + Fore.BLACK + card + Back.BLACK, end=' ')
    print(Style.RESET_ALL + "\nPlayer 2 has:", end=' ')
    for card in player_two_hand:
        print(Back.WHITE + Fore.BLACK + card + Back.BLACK, end=' ')
    print(Style.RESET_ALL + "\n")
    community_cards = deal_community_cards(deck)
    print("Community Cards: ", end=' ')
    for card in community_cards:
        print(Back.WHITE + Fore.BLACK + card + Back.BLACK, end=' ')
    print(Style.RESET_ALL + "\n")


if __name__ == "__main__":
    main()
