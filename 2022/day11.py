from day01 import best_n

class Monkey():

    def __init__(self, id, starting_items, operation, divisible_by, throw_to, worry=1):

        self.id = id

        self.items = starting_items

        self.orig = list(tuple(starting_items))

        self.operation = operation

        self.divisible_by = divisible_by
        
        self.throw_to = throw_to

        self.worry = 0

        self.mcm = 0

        self.times_inspected = 0

    def inspect(self, obj):
        self.times_inspected += 1
        old = obj
        new = eval(self.operation) # Worry level becomes {new}.
        return new

    def inspect_items(self):

        items_to_throw = []
        for obj in self.items:
            worry_level = self.inspect(obj) # Monkey {id} inspects an item with a worry level of {obj}.
            worry_level //= self.worry # Monkey {id} gets bored with item. Worry level is divided by {worry} to {worry_level}.
            worry_level %= self.mcm
            to = self.throw_to[not (worry_level % self.divisible_by)] # Current worry level is {'' if not (worry_level % divisible_by) else 'not'} divisible by {divisible_by}.
            items_to_throw.append((to, worry_level)) # Item with worry level {worry_level} is thrown to monkey {to}.
        
        self.items = []
        return items_to_throw

    def add_item(self, obj):

        self.items += [obj]

    def reset_inspect_count(self):
        self.times_inspected = 0
        self.items = self.orig


if __name__ == "__main__":

    fp = open("day11_input.txt", "r")


    monkeys = []
    mcm = 1

    string = fp.readline()
    while string != "":
        id = int(string.split()[-1][:-1])                                                      # Monkey {id}:
        starting_items = [int(i.strip(",")) for i in fp.readline().split()[2:]]                #  Starting items: {starting_items}
        operation = fp.readline()[19:-1]                                                       #  Operation: {operation}
        divisible_by = int(fp.readline().split()[-1])                                          #  Test: divisible by {divisible_by}
        throw_to = {True:int(fp.readline().split()[-1]), False:int(fp.readline().split()[-1])} #   If true: throw to monkey {throw_to[True]}
        fp.readline() # filler line                                                            #   If false: throw to monkey {throw_to[False]}
        
        monkeys.append(Monkey(id, starting_items, operation, divisible_by, throw_to))
        mcm *= divisible_by
        
        string = fp.readline()

    parts = [(3, 20), (1, 10_000)] # (worry_divisor, number_of_rounds)
    for part in parts:
        worry, rounds = part
        for round in range(rounds):
            for monkey in monkeys:
                monkey.worry = worry
                monkey.mcm = mcm

                items_to_throw = monkey.inspect_items()

                for to, obj in items_to_throw:
                    monkeys[to].add_item(obj)

        most_active = best_n([monkey.times_inspected for monkey in monkeys], 2)
        
        print(f"The level of monkey business after {rounds} rounds (worry = {worry}) is: {most_active[0]*most_active[1]}")

        for monkey in monkeys:
            monkey.reset_inspect_count()

    fp.close()