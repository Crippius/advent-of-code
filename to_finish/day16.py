
# https://adventofcode.com/2021/day/16

hex_dict = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "A":10, "B":11, "C":12, "D":13, "E":14, "F":15}


from day03 import bin_to_dec

def dec_to_bin(dec_num):
    bin_num = ""
    while dec_num != 0:
        bin_num += str(dec_num%2)
        dec_num //= 2
    while len(bin_num) != 4:
        bin_num += "0"
    return bin_num[::-1]



def hex_to_bin(hex_num):
    bin_num = ""
    for i in hex_num:
        bin_num += dec_to_bin(hex_dict[i])
    return bin_num


def version_and_id(input):
    version = bin_to_dec(input[:3])
    id = bin_to_dec(input[3:6])

    return version, id

def literal_value(num):
    bin_num = ""
    while num[0] != "0":

        bin_num += num[1:5]
        num = num[5:]
        
    return bin_to_dec(bin_num)

        

def decode(input, do_parse=False):
    total_versions = 0
    num = 0
    gen = 0
    parse = 0
    while len(input) > 6:
        gen += 1
        print(input, gen)
        version, id = version_and_id(input)
        total_versions += version
        input = input[6:]
        parse = 6

        if id == 4:
            print("ID4")
            bin_num = ""
            while len(input) != 0 and input[0] != "0":
                bin_num += input[1:5]
                input = input[5:]
                parse += 5
            bin_num += input[1:5]
            parse += 5
            input = input[5:]
            num = bin_to_dec(bin_num)

        elif input[0] == "0":
            print("ID0")
            length = bin_to_dec(input[1:16])
            input = input[16:]
            parse += 16
            num = 0

            times = 0
            tmp1, tmp2 = decode(input[:length])
            num += tmp1
            total_versions += tmp2
            input = input[length:] 

        else:
            times = bin_to_dec(input[1:12])
            print("ID1", times)
            input = input[12:]
            parse += 12
            num = 0
            for _ in range(times):
                print(f"iteration n {_+1}")
                tmp1, tmp2, length = decode(input, True)
                num += tmp1
                total_versions += tmp2
                input = input[length:]
                parse += length
        
    print(total_versions, parse)
    if do_parse:
        return num, total_versions, parse        
    return num, total_versions


def decode_mask(input):
    input = hex_to_bin(input)
    return decode(input)

def main():

    input_data = open("day16_input.txt", "r")
    input = input_data.readline()
    print(decode_mask(input))




if __name__ == "__main__":
    main()