
def all_different(lst):
    for i in lst:
        if lst.count(i) != 1:
            return False
    return True


def get_start(packet, length):
    window_end = length
    while not all_different(packet[window_end-length:window_end]):
        window_end += 1
    return window_end


if __name__ == "__main__":

    fp = open("day06_input.txt", "r")

    packet = fp.readline()

    print(f"The start-of-packet marker is with 4 different characters is after character {get_start(packet, 4)}")

    print(f"The start-of-packet marker is with 14 different characters is after character {get_start(packet, 14)}")

    fp.close()