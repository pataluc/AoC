def parse(data: str) -> list:
    return [line.split(',') for line in data.split('\n\n')]

def part1(names: list, moves: list) -> str:
    pos = 0
    for move in moves:
        if move[0] == 'R':
            pos = min(len(names) - 1, pos + int(move[1]))
        else:
            pos = max(0, pos - int(move[1]))
    return names[pos]

assert(part1(*parse("""Vyrdax,Drakzyph,Fyrryn,Elarzris

R3,L2,R3,L1"""))) == "Fyrryn"

print("Part 1: ", part1(*parse("""Drakhynd,Marther,Tharynn,Fyndgaz,Thalzral,Selkzyth,Ulkkynar,Tharnverax,Ryssvynar,Valynn

L9,R1,L7,R7,L1,R3,L1,R9,L8,R6,L7""")))

def part2(names: list, moves: list) -> str:
    pos = 0
    for move in moves:
        if move[0] == 'R':
            pos += int(move[1:])
        else:
            pos -= int(move[1:])
    return names[pos%len(names)]

assert(part2(*parse("""Vyrdax,Drakzyph,Fyrryn,Elarzris

R3,L2,R3,L1"""))) == "Elarzris"

print("Part 2: ", part2(*parse("""Lornyth,Baljor,Aeorulth,Arakgaz,Ignzral,Selkfal,Vanurath,Wynroth,Fyndynn,Ralpyr,Aelithther,Drakvor,Lazirkyris,Paldrilor,Arakaelor,Gaeronar,Felmarsyron,Aeorfyr,Tarlgnaris,Kazgnar

L11,R11,L13,R8,L6,R10,L11,R18,L19,R8,L5,R15,L5,R19,L5,R19,L5,R8,L5,R6,L6,R12,L7,R17,L5,R18,L18,R9,L15""")))

def part3(names: list, moves: list) -> str:
    for move in moves:
        pos = (int(move[1:]) if move[0] == 'R' else -1*int(move[1:])) % len(names)
        temp = names[pos]
        names[pos] = names[0]
        names[0] = temp
    return names[0]

assert(part3(*parse("""Vyrdax,Drakzyph,Fyrryn,Elarzris

R3,L2,R3,L3"""))) == "Drakzyph"

print("Part 3: ", part3(*parse("""Kaldar,Balthrex,Harnrilor,Pyraris,Glaurzion,Tharjoris,Dalhynd,Dorhal,Igngryph,Malithgaz,Baloryx,Elvarlorath,Ryntal,Felnjor,Quarnvyr,Sylzar,Lithnar,Brynidris,Xaralzris,Cragfeth,Aeldra,Yndxeth,Skarzyth,Pyrlyr,Palthzar,Xendfelix,Fyndulrix,Ryssyth,Lithryn,Rylarwyris

L40,R23,L31,R38,L14,R35,L30,R33,L43,R17,L15,R46,L29,R33,L24,R38,L18,R47,L33,R43,L5,R35,L5,R42,L5,R32,L5,R19,L5,R27,L5,R17,L5,R29,L5,R45,L5,R42,L5,R10,L16,R11,L32,R15,L17,R41,L13,R39,L21,R30,L31,R11,L42,R23,L35,R22,L33,R23,L43""")))