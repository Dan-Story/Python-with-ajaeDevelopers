# a= "Python Program"
# print(a[1], a[-1])

# a = [10, 20, 30, 40, 50]
# print(a[0], a[-1])

# a = [1, 2, 3, 4, 5]
# print(a[1:4])

# a = input("입력: ")
# print(a[1:-1])

# a = input("입력: ")
# print(len(a))

# a = input("입력: ")
# print(a.upper())

# a = input("입력1: ")
# b = input("입력2: ")
# print(b in a)

# a = input("입력: ")
# print(a[::-1])

# a = "Hello, World!"
# print(a[::-1])

# a = "Python is fun"
# print(a.split())

# a = [1, 2, 3, 4, 5]
# a.reverse()
# print(a)

# a = input("입력: ")
# print(a == a[::-1])

# a = [20, 30, 10, 70, 30]
# a.sort()
# a.pop(), a.pop(0)
# print(a)

a = [20, 30, 10, 70, 30]
a.remove(max(a))
a.remove(min(a))
print(a)