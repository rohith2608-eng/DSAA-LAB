class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

class Node:
    def __init__(self, level, profit, bound, weight):
        self.level = level
        self.profit = profit
        self.bound = bound
        self.weight = weight

def bound(u, n, W, arr):
    if u.weight >= W:
        return 0
    profit_bound = u.profit
    j = u.level + 1
    totweight = u.weight
    while j < n and totweight + arr[j].weight <= W:
        totweight += arr[j].weight
        profit_bound += arr[j].value
        j += 1
    if j < n:
        profit_bound += (W - totweight) * arr[j].value / arr[j].weight
    return profit_bound

def knapsack(W, arr, n):
    arr.sort(key=lambda x: x.value / x.weight, reverse=True)
    queue = []
    u = Node(-1, 0, 0, 0)
    v = Node(-1, 0, 0, 0)
    u.bound = bound(u, n, W, arr)
    queue.append(u)
    max_profit = 0
    while queue:
        u = queue.pop(0)
        if u.level == -1:
            v.level = 0
        if u.level == n - 1:
            continue
        v.level = u.level + 1
        v.weight = u.weight + arr[v.level].weight
        v.profit = u.profit + arr[v.level].value
        if v.weight <= W and v.profit > max_profit:
            max_profit = v.profit
        v.bound = bound(v, n, W, arr)
        if v.bound > max_profit:
            queue.append(Node(v.level, v.profit, v.bound, v.weight))
        v.weight = u.weight
        v.profit = u.profit
        v.bound = bound(v, n, W, arr)
        if v.bound > max_profit:
            queue.append(Node(v.level, v.profit, v.bound, v.weight))
    return max_profit

W = 10
arr = [Item(40, 2), Item(50, 3.14), Item(100, 1.98), Item(95, 5), Item(30, 3)]
n = len(arr)

print("Maximum profit is", knapsack(W, arr, n))
