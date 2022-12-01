
# https://adventofcode.com/2021/day/20

# todo: optimize code (now it takes about 20s to complete 50 iterations)

from day03 import bin_to_dec

def sharp_to_dec(string): # Transforms a string that contains '#' and '.' into a number
    bin_num = ["0" if i=="." else "1" for i in string] # (ex. '##..#.' -> 32+16+0+0+2+0 = 50)
    return bin_to_dec(bin_num)

def EOF_check(input): # Small function to check if the program reached the EOF
    return 1 if input != "" and input != "\n" else 0

def ENHANCE(image, classification): # ENHANCES the image with the correct classification
    
    new_image = [] # Where the new image is stored

    for row in range(len(image)):
        new_row = "" # Where every new line is stored
        for col in range(len(image[0])):

            if col == 0 or col == len(image[0])-1 or row == 0 or row == len(image)-1: # If it's in the extremes,
                sharp_num = image[0][0:3]+image[1][0:3]+image[2][0:3] # Do as the top left 3x3 square does

            else: # Otherwise get the three lines of the 3x3 matrix around the value
                sharp_num = image[row-1][col-1:col+2]+image[row][col-1:col+2]+image[row+1][col-1:col+2]

            num = sharp_to_dec(sharp_num) # Convert it to a number
            new_row += classification[num] # Add a '#' or a '.' to the new row depending on the classification
        
        new_image.append(new_row)
    
    return new_image, new_image[0][0] # Return the new image and how the background acts (top left character)



def ENLARGE(image, back): # ENLARGES the image, adding 3 new characters at every extreme

    new_image = [] # Where the larger image is going to be stored
    
    for _ in range(3): # Adding three 'background' characters to the top
        new_image.append(back*len(image[0])+6*back)
    for i in image: # Around every line
        new_image.append(back*3+i+back*3)
    for _ in range(3): # And at the end
        new_image.append(back*len(image[0])+6*back)
    
    return new_image



def main():

    input_data = open("day20_input.txt", "r")

    image_algorithm = input_data.readline() # Getting the algorithm
    image = []

    input_data.readline()
    check = input_data.readline()
    while EOF_check(check): # Filling image with all the characters
        image.append(check[:-1])
        check = input_data.readline()

    back = "." # Initially the background is filled with '.'s

    for gen in range(50): 
        image = ENLARGE(image, back) # ENLARGING AND ENHANCING IMAGE 
        image, back = ENHANCE(image, image_algorithm)

        if gen == 1: # (For part 1), count number of '#' after two iterations
            counter = 0
            for i in image:
                for j in i:
                    if j == "#":
                        counter += 1
            print(f"The number of '#' after 2 enhancements is: {counter}\n") # 5395

    counter = 0 # (For part 2), count number of '#' after fifty iterations
    for i in image:
        for j in i:
            if j == "#":
                counter += 1
    print(f"The number of '#' after 50 enhancements is: {counter}") # 17584



if __name__ == "__main__":
    main()