# Author: Abhash Sharma
# Course: CS 325, Fall 2020
# HW 4, 4
# program takes a .txt file written as such:
# Line 1: total activities
# Line 2: activity 1, start time, finish time
# ...
# and outputs in the terminal the following:
# Set 1
# Number of activities selected =
# Activities:
# Set 2
# ...

# Citation: Portions of the code from HW1, HW2, and HW3

def print_to_terminal(array, set_num):
    """prints to terminal"""
    # convert integer array to string
    string_array = ' '.join([str(x) for x in array])
    print("Set", set_num)
    print("Number of activities selected =", len(array))
    print("Activities:", string_array)

def last_to_start(array):
    """takes in an array of activities with ascending finish time
    schedules as many activities that can be completed within a given time"""
    n = len(array) - 1
    A = [array[n][0]]
    i = n
    for m in range(n, -1, -1):
        if array[m][2] <= array[i][1]:
            A.append(array[m][0])
            i = m
    return A

# insert sort function from HW1
def insertsort(array):
    """takes in an unsorted array and returns a sorted array
    uses insertion sort algorithm to sort"""
    length = len(array)
    # Citation: pseudocode from introduction to algorithms (Corman et al)
    for j in range(1, length):
        key = array[j]
        i = j-1
        while i >= 0 and array[i][2] > key[2]:
            array[i+1] = array[i]
            i = i-1
        array[i+1] = key
    return array

def get_int_clear_line(file_name):
    """processes a text file, clears that line, and returns the number on that line"""
    return file_name.readline().strip()

# process file to obtain necessary data
with open('act.txt', 'r') as infile:
    # keep a tally of the total sets of activity in file
    output_set = 1

    while True:
        # a list of list of activity number, start time, and finish time
        act_array = []

        # get the total activities in each case
        tot_act = get_int_clear_line(infile)

        # stops processing file when end of file is reached
        if tot_act == "":
            break

        # iterate through all the activities
        for k in range(int(tot_act)):
            A, S, F = map(int, infile.readline().strip().split())
            act_array.append([A, S, F])

        # sort them according to finish time (in ascending order)
        sorted_act_array = insertsort(act_array)

        # run last_to_start algorithm
        act_sch = last_to_start(sorted_act_array)[::-1]

        # print pertinent data to terminal
        print_to_terminal(act_sch, output_set)

        # increase tally of set
        output_set += 1