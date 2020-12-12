import re
contains = {}
for line in open("day7_input.txt","r" ):
    # bright indigo bags contain 4 shiny turquoise bags, 3 wavy yellow bags.
    m = re.split(" bags contain ", line.strip())
    bags = m[1].replace(" bags", '').replace(".", '').replace(" bag", '').replace('no other', '0 other'). split(', ')
    pairs = [bag.split(' ', maxsplit=1) for bag in bags]
    children = [(int(child[0]), child[1]) for child in pairs]
    contains[m[0]] = children
#print(contains)
    
def find_parents(child):
    parents = set()
    for k,v in contains.items():
        if child in [color for (number, color) in v]:
            parents.add(k)
    parents.discard(child)
    return parents
    
#print(find_parents("shiny gold" ))
    
def get_roots(color, tree):
    parents = find_parents(color)
    tree |= parents
    if len(parents) == 0:
        return tree
    else:
        for p in parents:
            tree |= get_roots(p, tree)
        return tree
    
ancestry = get_roots("shiny gold", set())
print('\n'.join(ancestry))