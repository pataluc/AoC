import re
from os import path
from sys import argv

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)

class Blueprint:
    def __init__(self, values):
        self.number = int(values[0])
        self.ore_cost_in_ore, self.clay_cost_in_ore, self.obsidian_cost_in_ore, self.obsidian_cost_in_clay, self.geode_cost_in_ore, self.geode_cost_in_obsidian = list(map(int, values[1:]))



def load(file):
    regex = r'Blueprint (\d*): Each ore robot costs (\d*) ore\. Each clay robot costs (\d*) ore\. Each obsidian robot costs (\d*) ore and (\d*) clay\. Each geode robot costs (\d*) ore and (\d*) obsidian\.'
    return [ Blueprint(re.match(regex, line).groups()) for line in open(file_path(file), "r").read().split("\n") ]

def conjugate(value):
    return "robot collects" if value <= 1 else "robots collect"

debug = True
def ex1(data):
    blueprint: Blueprint
    for blueprint in data:
        ore = clay = obsidian = geode = 0
        ore_robots = 1
        clay_robots = obsidian_robots = geode_robots = 0
        building_ore_robot = building_clay_robot = building_obsidian_robot = building_geode_robot = False

        for mn in range(24):
            print("\n== Minute %d ==" % (mn + 1))

            if ore >= blueprint.geode_cost_in_ore and obsidian >= blueprint.geode_cost_in_obsidian:
                ore -= blueprint.geode_cost_in_ore
                obsidian -= blueprint.geode_cost_in_obsidian
                building_geode_robot = True
                print("Spend %d ore and %d obsidian to start building a geode-collecting robot." % (blueprint.geode_cost_in_ore, blueprint.geode_cost_in_obsidian))
            if ore >= blueprint.obsidian_cost_in_ore and clay >= blueprint.obsidian_cost_in_clay:
                ore -= blueprint.obsidian_cost_in_ore
                clay -= blueprint.obsidian_cost_in_clay
                building_obsidian_robot = True
                print("Spend %d ore and %d clay to start building a obsidian-collecting robot." % (blueprint.obsidian_cost_in_ore, blueprint.obsidian_cost_in_clay))
            if ore >= blueprint.clay_cost_in_ore:
                ore -= blueprint.clay_cost_in_ore
                building_clay_robot = True
                print("Spend %d ore to start building a clay-collecting robot." % blueprint.clay_cost_in_ore)
            if ore >= blueprint.ore_cost_in_ore:
                ore -= blueprint.ore_cost_in_ore
                building_ore_robot = True
                print("Spend %d ore to start building a ore-collecting robot." % blueprint.ore_cost_in_ore)

            ore += ore_robots
            print("%d ore-collecting %s %d ore; you now have %d ore." % (ore_robots, conjugate(ore_robots), ore_robots, ore))

            if clay_robots:
                clay += clay_robots
                print("%d clay-collecting %s %d clay; you now have %d clay." % (clay_robots, conjugate(clay_robots), clay_robots, clay))
            if obsidian_robots:
                obsidian += obsidian_robots
                print("%d obsidian-collecting %s %d obsidian; you now have %d obsidian." % (obsidian_robots, conjugate(obsidian_robots), obsidian_robots, obsidian))
            if geode_robots:
                geode += geode_robots
                print("%d geode-collecting %s %d geode; you now have %d geode." % (geode_robots, conjugate(geode_robots), geode_robots, geode))

            if building_ore_robot:
                ore_robots += 1
                print("The new ore-collecting robot is ready; you now have %d of them." % ore_robots)
                building_ore_robot = False
            if building_clay_robot:
                clay_robots += 1
                print("The new clay-collecting robot is ready; you now have %d of them." % clay_robots)
                building_clay_robot = False
            if building_obsidian_robot:
                obsidian_robots += 1
                print("The new obsidian-collecting robot is ready; you now have %d of them." % obsidian_robots)
                building_obsidian_robot = False
            if building_geode_robot:
                geode_robots += 1
                print("The new geode-collecting robot is ready; you now have %d of them." % geode_robots)
                building_geode_robot = False

        print("you now have %d geodes" % geode)
        exit()



    return

def ex2(data):
    return

sample = load("sample.txt")
# print(sample)
assert ex1(sample) == 33

data = load("input.txt")
print("ex1 : %s" % ex1(data))


assert ex2(sample) == 56000011
print("ex2 : %s" % ex2(data))
