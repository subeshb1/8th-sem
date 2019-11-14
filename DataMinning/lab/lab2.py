transactions = [
  ['A', 'B', 'C', 'E'],
  ['E', 'F', 'A'],
  ['B', 'E', 'B'],
  ['B', 'C', 'F'],
]

def merge_array_of_arrays(arrs):
  new_arr = []
  for arr in arrs:
    new_arr = new_arr + arr
  return new_arr


def support_count(items, transaction):
  support_count = {}
  for item in items:
    if item not in support_count:
      support_count[item] = 0
    for transaction in transactions:
      if item in transaction:
        support_count[item] += 1
  return support_count


item_set = set(merge_array_of_arrays(transactions))

print(support_count(item_set, transactions))