FILENAME = "input"

def card_to_int(card):
    # A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2
    if card.isdigit():
        return int(card)
    
    if card == "T":
        return 10
    if card == "J": # JOKER == weakest
        return 1
    if card == "Q":
        return 12
    if card == "K":
        return 13
    if card == "A":
        return 14

def compare_cards(handA, handB):
    for i in range(5):
        cardA_value = card_to_int(handA[i])
        cardB_value = card_to_int(handB[i])

        if cardA_value == cardB_value:
            continue

        return cardA_value > cardB_value

def get_hand_rank(hand):
    # Count cards in hand
    cards = {}
    for c in hand:
        if c in cards:
            cards[c] += 1
        else:
            cards[c] = 1

    jokers = cards.pop("J", 0)
    
    foak = 0
    pairs = 0
    toak = 0
    for amount in cards.values():
        # Five of a kind, where all five cards have the same label: AAAAA
        if amount == 5:
            return 7
        # Four of a kind, where four cards have the same label and one card has a different label: AA8AA
        if amount == 4:
            if jokers == 1:
                return 7
            return 6
        if amount == 3:
            if jokers == 1:
                return 6
            if jokers == 2:
                return 7
            toak = 1
        if amount == 2:
            if jokers == 2:
                return 6
            if jokers == 3:
                return 7
            pairs += 1

    if toak == 1:
        # Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
        if pairs == 1:
            return 5
        # Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
        return 4

    # Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    if pairs == 2:
        if jokers == 1:
            return 5
        return 3

    # One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    if pairs == 1:
        if jokers == 1:
            return 4
        return 2

    if jokers == 5 or jokers == 4:
        return 7
    if jokers == 3:
        return 6
    if jokers == 2:
        return 4
    if jokers == 1:
        return 2

    # High card, where all cards' labels are distinct: 23456
    return 1


def is_hand_higher(handA, handB):
    handA_rank = get_hand_rank(handA)
    handB_rank = get_hand_rank(handB)

    if handA_rank == handB_rank:
        return compare_cards(handA, handB)
    
    return handA_rank > handB_rank

ordered_list = []

with open(FILENAME, "r") as f:
    inputs = f.read().splitlines()

    for input in inputs:
        # parse line
        hand, bid = input.split()

        # insert in list
        for index, hand_info in enumerate(ordered_list):
            if is_hand_higher(hand_info[0], hand):
                ordered_list.insert(index, [hand, int(bid)])
                break
        else:
            # No higher hands in oredered_list (or first hand to be append)
            ordered_list.append([hand, int(bid)])

total_sum = 0
for index, hand_info in enumerate(ordered_list):
    total_sum += hand_info[1] * (index+1)
       
print(f"Total Sum: {total_sum}")