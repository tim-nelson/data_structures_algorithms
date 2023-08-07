import sys

input = sys.stdin.read()
input_lines = input.split('\n')

n = int(input_lines[0])
int_list = [int(x) for x in input_lines[1].split()]

assert(len(int_list) == n)

largest_int = max(int_list)
largest_int_index = int_list.index(largest_int)

int_list.pop(largest_int_index)
second_large_int = max(int_list)


print(largest_int * second_large_int)
