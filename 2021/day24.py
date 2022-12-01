
# https://adventofcode.com/2021/day/1

def EOF_check(input): # Small function to check if the program reached the EOF
    return 1 if input != "" else 0

def main():
    input_data = open("day24_input.txt")
    
    for monad in reversed(range(10000000000000, 99999999999999)):
        input_data.seek(0)
        variables = {"w":0, "x":0, "y":0, "z":0}
        print(monad)
        monad = str(monad)
        if "0" in monad:
            continue
        
        punt = 0
        check  = input_data.readline()[:-1]
        while EOF_check(check):
            #print(check)
            check = check.split(" ")
            if len(check) == 2:
                check.append("")
            
            op, var1, var2 = check
            
            if op == "inp":
                variables[var1] = int(monad[punt])
                punt += 1
                
            elif op == "add":
                if var2 in variables:
                    variables[var1] += variables[var2]
                else:
                    variables[var1] += int(var2)
            
            elif op == "mul":
                if var2 in variables:
                    variables[var1] *= variables[var2]
                else:
                    variables[var1] *= int(var2)
            
            elif op == "div":
                if var2 in variables:
                    variables[var1] //= variables[var2]
                else:
                    variables[var1] //= int(var2)
            
            elif op == "mod":
                if var2 in variables:
                    variables[var1] %= variables[var2]
                else:
                    variables[var1] %= int(var2)
            
            elif op == "eql":
                if var2 in variables:
                    variables[var1] = 1 if variables[var1] == variables[var2] else 0
                else:
                    variables[var1] = 1 if variables[var1] == int(var2) else 0

            check = input_data.readline()[:-1]
        
        if variables["z"] == 0:
            print(monad)
            break
        

if __name__ == "__main__":
    main()