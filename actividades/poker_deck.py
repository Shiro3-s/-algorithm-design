import random

class cards:
    number_cards = list(range(1,14)) #up to 53
    cards_club = ["h","c","d","s"] #hearts, cloves, diamonds and spades

class deck:
    def trigger_deck():
        deck_list = []  #the list where all cards are 
        for card_club in cards.cards_club:
            for number in cards.number_cards:
                deck_list.append(f"{number}{card_club}")
        random.shuffle(deck_list)
        return deck_list

my_deck = deck.trigger_deck()
print(len(my_deck))