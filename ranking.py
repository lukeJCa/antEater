import random
from collections import Counter
from treys import Evaluator, Card

# Define the ranks and suits
ranks = '23456789TJQKA'
suits = 'cdhs'
deck = [r + s for r in ranks for s in suits]

# Function to deal a poker hand
def deal_hand(num_players, hole_cards, known_community_cards):
    deck_copy = deck.copy()
    for card in hole_cards + known_community_cards:
        deck_copy.remove(card)

    hands = [hole_cards]
    for _ in range(num_players - 1):
        hand = random.sample(deck_copy, 2)
        hands.append(hand)
        for card in hand:
            deck_copy.remove(card)
    
    community_cards = known_community_cards + random.sample(deck_copy, 5 - len(known_community_cards))
    return hands, community_cards

def card_str_to_int(card_str):
    return Card.new(card_str)

def evaluate_hands(hands, community_cards):
    evaluator = Evaluator()
    board = [card_str_to_int(card) for card in community_cards]
    hand_strengths = []

    for hand in hands:
        player_hand = [card_str_to_int(card) for card in hand]
        hand_strength = evaluator.evaluate(board, player_hand)
        hand_strengths.append(hand_strength)
    
    winning_strength = min(hand_strengths)
    winners = [i for i, strength in enumerate(hand_strengths) if strength == winning_strength]

    return winners, winning_strength

# Simulate a number of poker games
def simulate_poker(num_players, hole_cards, known_community_cards = [], num_simulations = 100):
    wins = 0
    for _ in range(num_simulations):
        hands, community_cards = deal_hand(num_players, hole_cards, known_community_cards)
        winners, winning_strength = evaluate_hands(hands, community_cards)
        if 0 in winners:
            wins += 1
    return wins / num_simulations * 100

# Example usage
#hands = [['As', 'Kd'], ['9h', '9d'], ['2c', '2d']]
#community_cards = ['2h', '2s', '3c', '3d', '4s']

num_players = 7
hole_cards = ['Qs', 'Ac']
known_community_cards = ['8d', '4d', '7c']
print(simulate_poker(num_players, hole_cards, known_community_cards))


