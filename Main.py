from typing import List

def selectionSort(array, size) -> List[int]:
  for i in range len(array):
    min=i
    for j in range(i+1,array[j]):
      if array[min]>array[i]:
        array[min]=array[i]
        array[i]=array[min]
  return array

# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
