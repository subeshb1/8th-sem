# Sum elements in an array
def _sum(arr):
  sum = 0
  for item in arr:
    sum += item
  return sum

int_array = [1,2,3,4,5]

print(_sum(int_array))

# Find common in array

def common(arr1, arr2):
  arr3 = []
  for item in arr1:
    if item in arr2:
      arr3.append(item)
  return arr3

set1 = ['a','b','c', 'd', 'e']
set2 = ['a','x','b', 'y']
print(common(set1, set2))