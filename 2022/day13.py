
def ordered(left, right):
    if type(left) == int and type(right) == int:
        if left == right:
            return False, True

        return left < right, False # {min(left, right)} side is smaller, so inputs are {NOT if left>right} in the right order
    elif type(left) == int:
        left = [left]
    elif type(right) == int:
        right = [right]

    for i in range(min(len(left), len(right))):
        order, continue_checking = ordered(left[i], right[i]) # Compare left[i], right[i]
        if order:
            return True, True
        if not continue_checking:
            return order, False

    if len(left) == len(right):
        return False, True
    elif len(left) < len(right): # LEft side is smaller, so inputs are in the right order
        return True, False
    else: # Right side is smaller, so inputs are NOT in the right order
        return False, False

if __name__ == "__main__":
    fp = open("day13_input.txt", "r")

    list_of_indices = []


    left = fp.readline()
    packets = []
    while left != "":
        right = fp.readline()
        left, right = eval(left), eval(right)
        packets += [left, right]

        if ordered(left, right)[0]:
            list_of_indices.append(len(packets)//2)
        fp.readline()
        left = fp.readline()

    print(f"The sum of the indices of the ordered pairs is: {sum(list_of_indices)}")

    divider_packets = [[[2]], [[6]]]
    packets += divider_packets

    # Bubble Sort 🤢
    for i in range(len(packets)-1):
        for j in range(0, len(packets)-i-1):
            if not ordered(packets[j], packets[j+1])[0]:
                packets[j], packets[j+1] = packets[j+1], packets[j]

    decoder_key = 1
    for i in divider_packets:
        decoder_key *= packets.index(i)+1
    
    print(f"The decoder key for the distress signal is: {decoder_key}")
    


    fp.close()