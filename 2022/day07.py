
class Directory():

    def __init__(self, name, prev=None):

        self.prev = prev

        self.name = name

        self.elems = {}
    

    def __str__(self):

        name = self.name
        dir = self.prev
        while dir != "/":
            name = f"{dir.name}/{name}"
            dir = dir.prev
        return name
    
    def size(self):
        
        total = 0
        for i in self.elems.values():
            if type(i) == int:
                total += i
            else:
                total += i.size()
        return total


    def print_dir(self, indent=0):

        if indent == 0:
            print(f'{" "*indent}-{self.prev}')

        for i, j in self.elems.items():
            if type(j) == Directory:
                print(f'{" "*(indent+1)}-{i}')
                j.print_dir(indent+1)
            else:
                print(f'{" "*(indent+1)}{i}: {j}')
    
    def add_items(self, new_item:dict={}):

        for i, j in new_item.items():
            self.elems[i] = j

        
def select_dirs(dir:Directory, which, limit, selected_dirs={}, return_dir_size=False) -> dict:
    if not return_dir_size: # Why the **** did I need to add that???
        selected_dirs = {}

    total = 0
    for i in dir.elems.values():
        if type(i) == int:
            total += i
        else:
            dir_size, selected_dirs = select_dirs(i, which, limit, selected_dirs, return_dir_size=True)
            total += dir_size
    
    if which == "smaller":
        if total <= limit:
            selected_dirs[str(dir)] = total

    elif which == "greater":
        if total >= limit:
            selected_dirs[str(dir)] = total
    
    if return_dir_size == True:
        return total, selected_dirs
    return selected_dirs
    
        


if __name__ == "__main__":

    fp = open("day07_input.txt", "r")

    
    dir = Directory("/", "/")
    
    orig = dir

    fp.readline()
    instr = fp.readline().split()
    while instr != []:

        if instr[0] == "$":
            if instr[1] == "cd":
                if instr[2] == "..":
                    dir = dir.prev
                else:
                    dir = dir.elems[instr[2]]
                
                instr = fp.readline().split()
            
            elif instr[1] == "ls":
                new_items = {}
                file = fp.readline().split()
                while file != [] and file[0] != "$":
                    if file[0] == "dir":
                        new_items[file[1]] = Directory(name=file[1], prev=dir)
                    else:
                        new_items[file[1]] = int(file[0])
                    
                    dir.add_items(new_items)

                    file = fp.readline().split()
                instr = file
        
    print(f"The sum of the total sizes of the directories with sizes of at most 100000 is: {sum(select_dirs(orig, which='smaller', limit=100000).values())}")
    
    print(f"The smallest directory that, when deleted, frees more than 30000000 space has size: {min(select_dirs(orig, which='greater', limit=orig.size()-(70000000-30000000)).values())}")

    fp.close()