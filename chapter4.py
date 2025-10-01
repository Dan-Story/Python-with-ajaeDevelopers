# 집합(Set)
# union, intersection, difference, symmetric.difference
# issubset, issuperset, isdisjoint
# add, update, remove
# 사전(Dictionary)
# dict, keys, values, items, get, clear, pop

#1
# x = {1, 2, 3, 4, 5}
# y = {3, 4, 5, 6, 7}
# print(x & y)
# print(x.intersection(y))

#2
# x = {10, 20, 30}
# x.add(40)
# print(x)

#3
# x = {10, 20, 30, 40}
# print(max(x))

#4
# x = {5, 10, 15}
# y = {5, 10, 15, 20}
# print(x<=y)
# print(x.issubset(y))

#5
# x = {'a': 1, 'b': 2, 'c': 3}
# print(x['b'])

#6
# x = {'a': 1, 'b': 2, 'c': 3}
# x['d'] = 4
# print(x)

#7
# x = {'a': 1, 'b': 2, 'c': 3}
# print('d' in x)

#8
# x = {1, 2, 3}
# x.add(4)
# print(x)

#9
# x = {'x': 10, 'y': 20, 'z': 30}
# del x['y']
# print(x)

# x = {'x': 10, 'y': 20, 'z': 30}
# x.pop('y')
# print(x)

#10
# x = {'a': 1, 'b': 2, 'c': 3}
# x['d'] = 4
# print(x)