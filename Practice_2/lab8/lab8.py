_input = list(map(int,input().split()))
temp = {}
root = -1
for index,value in enumerate(_input):
  if value == root:
    root = index
    continue
  if value not in temp:
    temp[value]=[index]
  else:
    temp[value].append(index)


"""
pesudocode:
  init max_height =1 and queue is root
  while queue not empty:
    i,h <- queue.pop()
    if i not in temp:
      continue
    h <- h +1
    if h > max_height:
      max_height = h
    for v in temp[i]:
      queue.add((v,h))
  return max_height
"""
max_height =1
queue = [(root,max_height)]

while len(queue)>0:
  _index,_height = queue.pop()
  if _index not in temp:
    continue
  _height+=1
  if _height >max_height:
    max_height= _height
  #Get all position of next node in current node
  for _value in temp[_index]:
    queue.append((_value,_height))
print(max_height)