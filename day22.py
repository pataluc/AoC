deck1 = [1, 10, 28, 29, 13, 11, 35, 7, 43, 8, 30, 25, 4, 5, 17, 32, 22, 39, 50, 46, 16, 26, 45, 38, 21]
deck2 = [19, 40, 2, 12, 49, 23, 34, 47, 9, 14, 20, 24, 42, 37, 48, 44, 27, 6, 33, 18, 15, 3, 36, 41, 31]

def battle1(deck1, deck2):
    i = 0
    while len(deck1) and len(deck2):
        i += 1
        #print("-- Round %i --" % i)
        #print("P1 deck : %s" % ", ".join(map(str, deck1)))
        #print("P2 deck : %s" % ", ".join(map(str, deck2)))

        card1 = deck1.pop(0)
        card2 = deck2.pop(0)
        #print("P1 plays : %i" % card1)
        #print("P2 plays : %i" % card2)

        if card1 > card2:
            #print("P1 wins")
            deck1.append(card1)
            deck1.append(card2)
        else:
            #print("P2 wins")
            deck2.append(card2)
            deck2.append(card1)


    #print("== Post-game results ==")
    #print("P1 deck : %s" % ", ".join(map(str, deck1)))
    #print("P2 deck : %s" % ", ".join(map(str, deck2)))

    return sum([c * (i + 1) for i, c in enumerate(reversed(deck1 + deck2))])

def battle2(deck1, deck2, game = 1):
    sub_game = 0
    previous_rounds = set()
    #print("=== Game %s ===" % game)
    i = 0
    while len(deck1) and len(deck2):
        i += 1
        #print("\n-- Round %d (Game %d) --" % (i, game))
        #print("Player 1's deck: %s" % ", ".join(map(str, deck1)))
        #print("Player 2's deck: %s" % ", ".join(map(str, deck2)))

        if ("%s|%s" % (" ".join(map(str, deck1)), " ".join(map(str, deck2))) in previous_rounds):
            # instant win for P1
            #print("################# Instant WIN for P1 in game %i" % game)
            return ([1], [])
        
        previous_rounds.add("%s|%s" % (" ".join(map(str, deck1)), " ".join(map(str, deck2))))

        card1 = deck1.pop(0)
        card2 = deck2.pop(0)
        #print("Player 1 plays: %i" % card1)
        #print("Player 2 plays: %i" % card2)

        if len(deck1) >= card1 and len(deck2) >= card2:
            #print("Playing a sub-game to determine the winner...")
            sub_game += 1
            d1, d2 = battle2(deck1[:card1].copy(), deck2[:card2].copy(), game + sub_game)
            #print(" ... back to game %d" % game)

            if len(d1):
                #print("Player 1 wins round %d of game %d!" % (i, game))
                deck1.append(card1)
                deck1.append(card2)
            else:
                #print("Player 2 wins round %d of game %d!" % (i, game))
                deck2.append(card2)
                deck2.append(card1)
        else:
            if card1 > card2:
                #print("Player 1 wins round %d of game %d!" % (i, game))
                deck1.append(card1)
                deck1.append(card2)
            else:
                #print("Player 2 wins round %d of game %d!" % (i, game))
                deck2.append(card2)
                deck2.append(card1)

    #print("The winner of game %s is player %d!" % (game, 1 if len(deck1) else 2))
        
    return deck1, deck2

# Ex 1
print("Ex 1: %i" % battle1(deck1.copy(), deck2.copy()))

# Ex 2
battle2(deck1, deck2)

#print("== Post-game results ==")
#print("P1 deck : %s" % ", ".join(map(str, deck1)))
#print("P2 deck : %s" % ", ".join(map(str, deck2)))
print("Ex 2: %i" % sum([c * (i + 1) for i, c in enumerate(reversed(deck1 + deck2))]))