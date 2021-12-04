import sys
file = "sample.txt" if len(sys.argv) == 2 and sys.argv[1] == "-d" else "input.txt"
lines = open(file, "r").readlines()

draws = list(map(int, lines[0].rstrip().split(',')))

class Board:
    name = ""
    rows = []
    cols = []
    last_draw = None

    def __init__(self, name, rows):
        self.name, self.rows = name, rows
        self.cols = list(map(list, zip(*rows)))

    def has_won(self):
        return not(all(self.rows) and all(self.cols))
    
    def play(self, number):
        self.last_draw = number
        for line in self.rows + self.cols:
            if number in line:
                line.remove(number)
        return number

    def score(self):
        return self.last_draw * sum(map(sum, self.rows))
    
    def print(self):
        print(self.name)
        print("rows:")
        for row in self.rows:
            print(" ".join(map(str, row)))
        print("cols:")
        for col in self.cols:
            print(" ".join(map(str, col)))

def load_boards():
    boards = list()
    for i in range(int(len(lines) / 6)):
        rows = [list(map(int, line.split())) for line in lines[2 + i * 6: 7 + i * 6]]
        boards.append(Board("Board %d" % (i+1), rows))
    return boards

def ex1():
    boards = load_boards()
    for draw in draws:
        for board in boards:
            board.play(draw)
            if board.has_won():
                return board.score()

def ex2():
    boards = load_boards()
    for draw in draws:
        boards = list(filter(lambda b: not(b.has_won()), boards))
        for board in boards:
            board.play(draw)
            if board.has_won() and len(boards) == 1:
                return board.score()

print("ex1 : %d" % ex1())
print("ex2 : %d" % ex2())


