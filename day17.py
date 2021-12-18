
# https://adventofcode.com/2021/day/17

# note: this piece of code is a mixture of 'ostrich programming' and cool mathematical findings, enjoy!   
#                                                   |
#                                                   v
#                              https://en.wikipedia.org/wiki/Ostrich_algorithm

from math import floor, sqrt

def main():
    
    input_data = open("day17_input.txt", "r").readline() # Getting data
    input_data = input_data[input_data.find("x"):] # Starting from the actual datapoints  

    t_x_min = int(input_data[2:input_data.find(".")]) # Finding the extremes in x
    t_x_max = int(input_data[input_data.find(".")+2: input_data.find(",")])

    input_data = input_data[input_data.find("y"):]

    t_y_min = int(input_data[2:input_data.find(".")]) # Finding the y extremes
    t_y_max = int(input_data[input_data.find(".")+2:])
    
    v_y_max = abs(t_y_min)-1 # WHEN the target is negative these conditions work, 
    v_y_min = t_y_min # After the first (and only) step they reach the target, any higher velocity wouldn't enter the target

    # Finding highest point with greatest vertical velocity (Part 1)
    # Since the vertical velocity gets smaller as time goes on because of gravity, similarly to the drag with the horizontal velocity,
    # We can find the highest point by summing all integers from 1 to the initial velocity 'n', and it equals to n*(n+1)/2
    y_max = v_y_max*(v_y_max+1)/2 

    print(f"The highest that can be reached while still hitting the target is: {y_max}\n") # 4950   
    
    v_x_max = t_x_max # Same thing for the maximum horizontal velocity
    v_x_min = floor((1+sqrt(1+4*t_x_min*2))/2) 
    # For the minimal one this (^) is the solution I discovered, here's the explanation:
    # Because of the drag, the horizontal velocity becomes smaller one step at a time, and I found out while writing
    # the code (@ ~ row 82) that the final x position is the sum of all numbers between 1 and the initial horizontal velocity 'n'
    # In my calculus class I found out that this sum can be rewritten as n*(n+1)/2; so to find the minimal velocity to reach
    # the nearest point of the target 'k'we have to solve this equation -> n*(n+1)/2=k -> n**2+n-2k = 0, 
    # after doing the quadratic formula for n (and rounding it down to the integer value) we get our result :) 
    
    # Finding all possible initial velocities that make the probe reach the target
    counter = 0
    for v_y in range(v_y_min, v_y_max+1): # Using our limitations that we conveniently found
        starting_v_y = v_y
        for v_x in range(v_x_min, v_x_max+1):
            v_y = starting_v_y  # Resetting variables 
            x, y = 0, 0

            while x <= t_x_max and y >= t_y_min: # While the probe can still reach the target
                last = (x, y) # Storing the last position before going out range

                x += v_x
                y += v_y
                
                if v_x > 0:
                    v_x -= 1
                v_y -= 1

            x, y = last # If the probe was previously inside the target, increase counter
            if x >= t_x_min and  x <= t_x_max and y >= t_y_min and y <= t_y_max:
                counter += 1
    
    print(f"The number of distinct initial velocity values that reach the target is: {counter}")


# The first, less mathematical, algorithms to find the thresholds for the y (1) and (x) trajectory
# note: only the v_y_min and v_x_min codes are shown
# |
# v
# while not (points[-2] == t_y_min and len([i for i in points[-3:] if i<0]) == 2): # <- Very specific exit conditions
#     v_y_max += 1
#     v_y = v_y_max
#     y = 0
#     while y >= t_y_min:
#         y += v_y
#         if y > y_max:
#             y_max = y
#         v_y -= 1
    
# while x < t_x_min:
#     v_x_min += 1
#     v_x = v_x_min
#     x = 0
#     while v_x != 0:
#         x += v_x
#         v_x -= 1

# | Code used to find maximum height 
# v
# y, y_max = 0, 0
# v_y = v_y_max
# while v_y != 0: 
#     y += v_y
#     if y > y_max:
#         y_max = y
#     v_y -= 1

if __name__ == "__main__":
    main()