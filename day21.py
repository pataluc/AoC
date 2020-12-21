import sys
import re

lines = list(map(str.rstrip, open("%s_input.txt" % sys.argv[0].split('.')[0], "r").readlines()))

ingredients_allergens = dict()
allergens_ingredients = dict()

for line in lines:
    ingredients, allergens = re.findall('(.*) \(contains (.*)\)', line)[0]
    for ingredient in ingredients.split(" "):
        if ingredient not in ingredients_allergens:
            ingredients_allergens[ingredient] = set(allergens.split(", "))
        else:
            ingredients_allergens[ingredient] = ingredients_allergens[ingredient].intersection(set(allergens.split(", ")))

    for allergen in allergens.split(", "):
        if allergen not in allergens_ingredients:
            allergens_ingredients[allergen] = set(ingredients.split(" "))
        else:
            allergens_ingredients[allergen] = allergens_ingredients[allergen].intersection(set(ingredients.split(" ")))

contains_allergen = set()
for a in allergens_ingredients.values():
    contains_allergen |= set(a)

no_allergens = ingredients_allergens.keys() - contains_allergen

count = 0
for ingredient in no_allergens:
    for line in lines:
        line_ingredients = line.split(" (")[0].split(" ")
        count += line_ingredients.count(ingredient)

print("Ex 1: %d, no allergens: " % count, no_allergens)


def solve(allergens_ingredients, result = dict()):
    #print(result)
    for allergen, ingredients in allergens_ingredients.items():
        #print(ingredients - set(result.values()))
        if len(ingredients - set(result.values())) == 1:
            ingredient = (ingredients - set(result.values())).pop()
            result[allergen] = ingredient
            #print("%s contains %s" % (ingredient, allergen))

    if len(result) != len(allergens_ingredients):
        return solve(allergens_ingredients, result)
    else:
        return result
    
    #for allergen, ingredients in allergens_ingredients.items():
    #    f
#
    #    print(allergen)
    #    print(ingredients)

allergenic = solve(allergens_ingredients)

print("Ex 2: %s" % ",".join(list(map(lambda a: allergenic[a], sorted(allergenic.keys())))))
#print(ingredients_allergens)
