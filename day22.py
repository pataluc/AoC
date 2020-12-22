init_deck1 = [1, 10, 28, 29, 13, 11, 35, 7, 43, 8, 30, 25, 4, 5, 17, 32, 22, 39, 50, 46, 16, 26, 45, 38, 21]
init_deck2 = [19, 40, 2, 12, 49, 23, 34, 47, 9, 14, 20, 24, 42, 37, 48, 44, 27, 6, 33, 18, 15, 3, 36, 41, 31]

def battle(deck1, deck2, recurse_game = False):
    if recurse_game:
        previous_rounds = set()
    
    while len(deck1) and len(deck2):
        if recurse_game:
            if "%s|%s" % (" ".join(map(str, deck1)), " ".join(map(str, deck2))) in previous_rounds:
                return ([1], []) # instant win for P1
            
            previous_rounds.add("%s|%s" % (" ".join(map(str, deck1)), " ".join(map(str, deck2))))

        card1 = deck1.pop(0)
        card2 = deck2.pop(0)        

        if recurse_game and len(deck1) >= card1 and len(deck2) >= card2:              
            d1, d2 = battle(deck1[:card1].copy(), deck2[:card2].copy(), True)
            if len(d1):
                deck1.append(card1)
                deck1.append(card2)
            else:
                deck2.append(card2)
                deck2.append(card1)
        else:
            if card1 > card2:
                deck1.append(card1)
                deck1.append(card2)
            else:
                deck2.append(card2)
                deck2.append(card1)        
    return deck1, deck2

# Ex 1
r1, r2 = battle(init_deck1.copy(), init_deck2.copy())
print("Ex 1: %i" % sum([c * (i + 1) for i, c in enumerate(reversed(r1 + r2))]))

# Ex 2
r1, r2 = battle(init_deck1, init_deck2, True)
print("Ex 2: %i" % sum([c * (i + 1) for i, c in enumerate(reversed(r1 + r2))]))