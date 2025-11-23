#1
# def fn(num):
#     for i in range(1,10):
#         print(f"{num} * {i} = {num*i}")

# fn(int(input("입력: ")))

#2
# def fn(num):
#     return num % 2 == 0

# if fn(int(input("입력: "))):
#     print("짝수")
# else:
#     print("홀수")

#3
# def fn(s1, s2):
#     return s1 if len(s1) >= len(s2) else s2

# x = input("입력: ")
# y = input("입력: ")
# print(fn(x, y))

#4
# x = [1, 2, 3, 4, 5, 6]
# y = list(filter(lambda a: a % 2, x))
# print(y)

# print(list(filter(lambda x: x % 2, [1,2,3,4,5,6])))

#5
def fn(num):
    if num == 1 or num == 2:
        return 1
    else:
        n1, n2 = 1, 1
        n3 = 0
        for i in range(3, num+1):
            n3 = n1 + n2
            n1 = n2
            n2 = n3
        return n3

print(fn(int(input("입력: "))))