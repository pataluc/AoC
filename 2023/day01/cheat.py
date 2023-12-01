
from os import path
from sys import argv
import regex as re

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)


def load(file):
    return open(file_path(file), "r").read().rstrip()
stringData = load("input.txt")
lines = stringData.splitlines()

#with open('ex_input.txt') as f:
#    lines = [line.rstrip() for line in f]

submitA=False
submitB=False

def main():
    print("The solution for part 1 is: {0}".format(part1Solution(lines)))
    if submitA == True:
        print("Submitting solution A to AoC:")
        # submit(part1Solution(lines), part="a", day=1, year=2023)
    print("The solution for part 2 is: {0}".format(part2Solution(lines)))
    if submitB == True:
        print("Submitting solution B to AoC:")
        # submit(part2Solution(lines), part="b", day=1, year=2023)

def readDigits(d):
    return d.replace("one", "1").replace("two", "2").replace("three", "3").replace("four", "4")\
        .replace("five", "5").replace("six", "6").replace("seven", "7").replace("eight", "8").replace("nine", "9")

def part1Solution(lines):
    total=0
    for line in lines:
         nums=re.findall(r'\d', line)
         number=nums[0]+nums[-1]
         total=total+int(number)     
    return total

def part2Solution(lines):
    total=0
    for line in lines:
        digits = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line, overlapped=True)
        
        # print(line)
        nums=re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line, overlapped=True)
        wordNums = {'one': "1",
                    'two': "2",
                    'three': "3",
                    'four': "4",
                    'five': "5",
                    'six': "6",
                    'seven': "7",
                    'eight': "8",
                    'nine': "9",
                   }
 
        if nums[0] in wordNums:
            firstNum=wordNums[nums[0]]
        else:
            firstNum=nums[0]

        if nums[-1] in wordNums:
            lastNum=wordNums[nums[-1]]
        else:
            lastNum=nums[-1]

        firstLast=int(firstNum+lastNum)
        my = int(readDigits(digits[0]) + readDigits(digits[-1]))
        if firstLast != my:
            print(line, firstLast, my)
        total=total+firstLast
        
    return total

if __name__ == "__main__":
    main()