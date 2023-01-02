
from day09 import sign

class CircularList():

    def __init__(self, lst:list) -> None:
        self.ref = {i:num for i, num in enumerate(lst)}
        self.lst = [i for i in self.ref.keys()]
        self.order = tuple(self.lst)
        self.len = len(self.lst)
        self.zero_ref = lst.index(0)
        self.zero = self.zero_ref

    def move(self, i):
        index = self.lst.index(i)
        steps = self.ref[i]%(self.len-1)

        if steps+index > (self.len-1):
            steps -= self.len-1

        if steps < 0:
            self.lst = self.lst[:index+steps] + [i] + self.lst[index+steps:index] + self.lst[index+1:]
        else:
            self.lst = self.lst[:index] + self.lst[index+1:index+steps+1] + [i] + self.lst[index+steps+1:]

    def update_zero(self):
        self.zero = self.lst.index(self.zero_ref)

    def encrypt(self):
        for i in self.order:
            self.move(i)
        self.update_zero()


if __name__ == "__main__":
    
    fp = open("day20_input.txt", "r")
    
    lst = []
    
    num = fp.readline()
    while num != "":   
        lst.append(int(num))
        num = fp.readline()

    part1 = CircularList(lst)
    
    part1.encrypt()

    coords = 0
    for offset in (1000, 2000, 3000):
        pos = (part1.zero+offset)%part1.len
        coords += part1.ref[part1.lst[pos]] 

    print(coords)

    decryption_key = 811589153
    part2 = CircularList([i*decryption_key for i in lst])

    for _ in range(10):
        part2.encrypt()
    
    coords = 0
    for offset in (1000, 2000, 3000):
        pos = (part2.zero+offset)%part2.len
        coords += part2.ref[part2.lst[pos]] 

    print(coords)


    fp.close()