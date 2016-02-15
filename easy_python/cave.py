from random import choice, shuffle

class Cave:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.here = []
        self.tunnels = []

    def tunnels_to(self,cave):
        self.tunnels.append(cave)
#        cave.tunnels.append(self)

    def __repr__(self):
        return "<Cave " + self.name + ">"

cave_names = [ "Arched caven", "A", "B", "C", "D", "E" ]

def create_caves():
    shuffle(cave_names)
    caves = [Cave(cave_names[0], cave_names[1])]
    for name in cave_names[1:]:
        new_cave = Cave(name, name)
        eligible_caves = [Cave for cave in caves if len(cave.tunnels) < 3 ]
        new_cave.tunnels_to(choice(eligible_caves))
        caves.append(new_cave)
    return caves

print cave_names

if __name__ == '__main__':
    for cave in create_caves():
        print cave.name, "=>", cave.tunnels

