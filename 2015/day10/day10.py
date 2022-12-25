def look_and_say(number):
    i = 0
    result = ''
    while i < len(number):
        j = 1
        previous = number[i]
        while i < len(number) - 1 and number[i + 1] == previous:
            i += 1
            j += 1
        i += 1
        result += "%d%s" % (j, previous)
    return result

def solve(data, times):
    result = data
    for _ in range(times):
        result = look_and_say(result)

    return len(result)

assert look_and_say("1211") == "111221"
assert look_and_say("21") == "1211"
assert look_and_say("111221") == "312211"

print("ex1 : %s" % solve("3113322113", 40))

print("ex2 : %s" % solve("3113322113", 50))