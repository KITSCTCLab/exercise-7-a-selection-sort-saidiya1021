from typing import List

def selectionSort(array, size) -> List[int]:
  array=[size]
  for i in range (len(array)):
    min=i
    for j in range(i+1,len(array)):
      if array[min]>array[j]:
        min=j
    array[i],array[min]=array[min],array[i]
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
