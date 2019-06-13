
class node:
    def __init__(self, taken=[], value=0, room=0, estim=0):
        self.taken = taken
        self.value = value
        self.room  = room
        self.estim = estim


class Algorithms:
    def __init__(self, items, capacity):
        self.items = items
        self.capacity = capacity

    # items are sorted by value/weight   
    def sort_vw(self):
        self.items = sorted(self.items, key=lambda k: k.value/k.weight , reverse=True)

    # Estimate max_value
    def get_estimate(self):
        self.sort_vw()
        capacity = self.capacity
        value = 0
        for item in self.items:
            if capacity >= item.weight:
                capacity -= item.weight
                value += item.value
            else:
                value += 1.0 * capacity * item.value / item.weight
                break
        return value

    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    def greedy(self):
        self.sort_vw()
        estimation = self.get_estimate()
        len_i = len(self.items)
        
        ans_taken = None
        ans_value = 0
        taken = [0] * len_i

        for i in range(len_i):
            value = 0
            weight = 0
            for j in range(i, len_i):
                item = self.items[j]
                if weight + item.weight <= self.capacity:
                    taken[item.index] = 1
                    value += item.value
                    weight += item.weight
            if value > ans_value:
                ans_value = value
                if ans_value == estimation:
                    return ans_value, taken
                ans_taken = taken
            taken = [0] * len_i
        return ans_value, ans_taken

    # Dynamic Programming
    def db(self):
        capacity = self.capacity
        len_i = len(self.items)
        table = [ [0] * (capacity+1) for i in range(len_i) ]

        # print(self.estimation, 'Start Dynamic Programming...')
        for i in range(len_i):
            item = self.items[i]
            for j in range(item.weight):
                table[i][j] = table[i-1][j]
            for j in range(item.weight, capacity+1):
                table[i][j] = max(table[i-1][j-item.weight] + item.value, table[i-1][j])
        
        ans_value = table[-1][-1]
        ans_taken = [0] * len_i
        # Find the taken series.
        for j in range(i, -1, -1):
            if table[j-1][capacity] != table[j][capacity] or j == 0:
                capacity -= self.items[j].weight
                ans_taken[j] = 1
                if capacity == 0:
                    break
        return ans_value, ans_taken

    # Branch and Bound
    def bb(self):
        len_i = len(self.items)
        taken = []
        ans_value = 0
        history = [[[[], 0, self.capacity, self.get_estimate()]]]

        for i in range(len_i):
            # [ TAKEN, VALUE, ROOM, ESTIMATION_LEFT ]
            item = self.items[i]
            new_layer = []
            for j in range(i): 
                pass
            for parent in history[i]:
                if parent[2] >= item.weight: # Select the item
                    new_value = parent[1] + item.value
                    new_taken = parent[0] + [1]
                    new_layer.append([new_taken, new_value, parent[2]-item.weight, parent[3] ])
                    if new_value > ans_value:
                        ans_value = new_value
                        taken = new_taken
                if parent[3] > item.value: # Not select the item
                    new_layer.append([parent[0]+[0] , parent[1], parent[2], parent[3]-item.value ])
            history.append(new_layer)
            # print(history)

        # # i is the times of mistakes (not selected items)
        # for i in range(len_i): 
        #     item = items[i]
        #     value = item.value
        #     pass
        ans_taken = [0] * len_i
        for i in range(len(taken)):
            ans_taken[ self.items[i].index ] = 1
        
        return ans_value, ans_taken