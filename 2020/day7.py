import sys, re
f = open("%s_input.txt" % sys.argv[0].split('.')[0], "r")


parents_for_children = dict()
children_of_parents = dict()

for line in f:
    (parent_bag, contains) = line.rstrip().split(' bags contain ')

    children_of_parents[parent_bag] = dict()

    for child_bag in contains.replace(' bags', '').replace(' bag', '').replace('no other', '0 other').rstrip('.').split(', '):
        n, child = child_bag.split(' ', 1)
        
        if n != '0':
            children_of_parents[parent_bag][child] = int(n)

        if child not in parents_for_children:
            parents_for_children[child] = [parent_bag]
        elif parent_bag not in parents_for_children[child]:
            parents_for_children[child].append(parent_bag)
        
#print(len(parents_for_children))
#print(parents_for_children['shiny gold'])
        


def up_through(search, parents_for_children, result = set()):
    #print('_________')
    #print('result: ', result)

    if search in parents_for_children:
        #print('parents of %s: ' % search, parents_for_children[search])
        for parent in parents_for_children[search]:     
            if parent not in result: 
                up_through(parent, parents_for_children, result)
                result.add(parent)
    else: 
        #print('%s has no parents' % search)
        result.add(search)

    return result

result = up_through('shiny gold', parents_for_children)

#print('\n'.join(sorted(result)))
print('ex1: %d' % len(result))

def down_through(search, children_of_parents):
    result = 0
    print('_________')
    print('children of %s: ' % search, children_of_parents[search])
    #print('result: ', result)
    for child, number in children_of_parents[search].items():
        if number > 0:
            result += number        
            result += number * down_through(child, children_of_parents)
    return result

result2 = down_through('shiny gold', children_of_parents)

#print('\n'.join(sorted(result)))
print('ex2: %d' % result2)


