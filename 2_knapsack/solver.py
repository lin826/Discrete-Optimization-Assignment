#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
from algo import Algorithms
Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        # if int(parts[1]) <= capacity:
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    # TODO: Constraind Programming
    def CP():
        pass

    # TODO: Local Search
    def LS():
        pass

    # TODO: Mixed Integer Programming
    def MIP():
        pass



    algo = Algorithms(items=items, capacity=capacity)
    if len(items) > 50:
        ans_value, ans_taken = algo.greedy()
    else:
        ans_value, ans_taken = algo.bb()

    def return_ans(ans_value, ans_taken):
        # prepare the solution in the specified output format
        output_data = str(ans_value) + ' ' + str(0) + '\n'
        output_data += ' '.join(map(str, ans_taken))
        return output_data
    return return_ans(ans_value, ans_taken)


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

