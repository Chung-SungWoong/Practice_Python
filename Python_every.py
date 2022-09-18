"""
# 1. Node

from platform import node

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
 
node1 = Node(1)
head = node

def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)
    
add(5)

print(node1.next.data)

"""

"""
2.map and filter
test_str = "ABCDEF"

test_map = map(lambda x: x.lower().test_str)
test_filter = filter(lambda x: x.lower().test_str)

print("문자열 map: ", list(test_map))
print("문자열 filter: ",list(test_filter))
"""
"""
3. List comprehension

test_list = [1,2,3,4,5,1]
lc = [x * 2 for x in test_list]
print(lc)
word = "ABCDEF"
double_word = [i*2 for i in word]
print(double_word)
test = ["Ab",'Bc','FFF']
lower = [x.lower() for x in test]
print(lower)

test_list = set(test_list)
test_list = list(test_list)
print(test_list)
"""
"""
test_list = [1,2,3,4,5]
test_map = map(lambda x: x * 2, test_list)
print(test_map)
print(list(test_map))

test_map2 = map(lambda x: x ** 2, test_list)
print(list(test_map2))
"""
"""
check = [-5,1,0,5,4,-6]
positive = list(filter(lambda x: x > 0,check))
zero = list(filter(lambda x: x == 0, check))
negative = list(filter(lambda x: x < 0, check))

print(format(len(positive)/len(check),".06f"))
print(format(len(zero)/len(check),"0.6f"))
print(format(len(negative)/len(check),"0.06f"))
"""

