import sys
file = "sample.txt" if len(sys.argv) == 2 and sys.argv[1] == "-d" else "input.txt"

def file_to_array():
    f = open(file, "r")
    depths = []
    for line in f:
        depths.append(int(line))
    
    return depths

def count_increased(array):
    inc_count = None
    last_value = 0
    for value in array:
        if inc_count is None:
            inc_count = 0
        elif value > last_value:
            inc_count += 1
        
        last_value = value
    return inc_count

def ex1():
    return count_increased(file_to_array())

def ex2():
    depths = file_to_array()
    return count_increased(map(sum, zip(depths, depths[1:], depths[2:])))


print("ex1 : %d" % ex1())
print("ex2 : %d" % ex2())