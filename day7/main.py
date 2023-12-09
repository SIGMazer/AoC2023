#!/bin/env python3



def read_input(filename="input"):
    with open(filename, "r") as file:
        return file.read()

HANDS = [
    (line[:5].translate(str.maketrans("TJQKA", "abcde")), int(line[5:]))
    for line in read_input().splitlines()
]

def score(hand):
    return sum(hand.count(c) for c in hand)

def score_wild(hand):
    return max(score(hand.replace("b", c)) for c in "123456789acde")

def part_one():
    scored = ((score(hand), hand, bid) for hand, bid in HANDS)
    return sum(i * bid for i, (*_, bid) in enumerate(sorted(scored), start=1))

def part_two():
    scored = ((score_wild(hand), hand.replace("b", "0"), bid) for hand, bid in HANDS)
    return sum(i * bid for i, (*_, bid) in enumerate(sorted(scored), start=1))


print(part_one())
print(part_two())

