
def plus(arg1, arg2):
    return arg1+arg2

def minus(arg1, arg2):
    return arg1-arg2

def mul(arg1, arg2):
    return arg1*arg2

def div(arg1, arg2):
    return arg1/arg2

def equal(arg1, arg2):
    return arg2

class Monkey():

    def __init__(self, name, op="=", factors=("", ""), num=float("+inf")) -> None:
        
        self.name = name

        self.op = op

        self.factors = factors

        self.num = num

    def calculate(self, result_dict):
        
        op_dict = {"+":plus, "-":minus, "*":mul, "/":div, "=":equal}

        arg1, arg2 = (result_dict[arg] for arg in self.factors)
        self.num = op_dict[self.op](arg1, arg2)

        return self.num



def can_get_num(factors, result_dict):

    for factor in factors:
        if result_dict[factor] == float("+inf"):
            return False
    return True

def part1(monkeys, result_dict):
    while result_dict["root"] == float("+inf"):
        
        for monkey in monkeys:
            if monkey.num == float("+inf") and can_get_num(monkey.factors, result_dict):
                result_dict[monkey.name] = monkey.calculate(result_dict)

    print(int(result_dict["root"]))

def get_index(name, monkeys):
    index = 0
    for monkey in monkeys:
        if monkey.name == name:
            return index
        index += 1

def part2(monkeys, result_dict):
    
    for monkey in monkeys:
        if monkey.name == "root":
            monkey.op = "="
        elif monkey.name == "humn":
            monkey.num = float("+inf")
            result_dict[monkey.name] = float("+inf")
    
    new_nums = 1
    while new_nums != 0:
        new_nums = 0
        for monkey in monkeys:
            if monkey.name != "humn" and monkey.num == float("+inf") and can_get_num(monkey.factors, result_dict):
                result_dict[monkey.name] = monkey.calculate(result_dict)
                new_nums += 1

    opposite_dict = {"+":minus, "-":plus, "*":div, "/":mul, "=":equal}
    curr = monkeys[get_index("root", monkeys)]
    while curr.name != "humn":
        arg1, arg2 = (monkeys[get_index(i, monkeys)] for i in curr.factors)

        if arg1.num == float("+inf"):
            unknown, known = (arg1, arg2)
            unknown.num = opposite_dict[curr.op](curr.num, known.num)

        else: 
            unknown, known = (arg2, arg1)
            if curr.op == "-":
                unknown.num = minus(known.num, curr.num)
            elif curr.op == "/":
                unknown.num = div(known.num, curr.num)
            else:
                unknown.num = opposite_dict[curr.op](curr.num, known.num)

        result_dict[unknown.name] = unknown.num
        curr = unknown

    print(int(curr.num))

if __name__ == "__main__":

    fp = open("day21_input.txt", "r")

    part = 2

    monkeys = []
    result_dict = {}

    monkey = fp.readline()
    while monkey != "":
        op, factors, num = "=", ("", ""), float("+inf")
        monkey = monkey.split()
        name = monkey[0][:-1]
        if len(monkey) == 2:
            num = int(monkey[1])
        else:
            op = monkey[2]
            factors = (monkey[1], monkey[3])

        monkeys.append(Monkey(name, op, factors, num))
        result_dict[name] = num
        
        monkey = fp.readline()

    if part == 1:
        part1(monkeys, result_dict)
    else:
        part2(monkeys, result_dict)

    fp.close()