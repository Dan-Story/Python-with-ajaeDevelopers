#1
#<기본>
# x = int(input("출력: "))
# i = 0
# while i <= x:
#     print(i)
#     i += 1

#<최신>
# x = int(input("출력: "))
# i = 0
# while i <= x:
#     print(f"{i}")
#     i += 1

#<구식>
# x = int(input("출력: "))
# i = 0
# while i <= x:
#     print("%d" % i)
#     i += 1

#2
# x = int(input("입력: "))
# for i in range(1, 10):
#     print(f"{x} x {i} = {x*i}")

# x = int(input("입력: "))
# i = 1
# while i<10:
#     print(f"{x} x {i} = {x*i}")
#     i+=1

#3
# x = int(input("입력: "))

# while x > 0:
#     i = x
#     while i >= 0:
#         print(f"{i}")
#         i = i - 1
#     x = int(input("입력: "))

# print("프로그램을 종료합니다")

#4
#<첫번째 코딩이 더 좋음>
# for i in range(2, 10):
#     if i % 2 == 1:
#         continue
#     for j in range(1, 10):
#         print(f"{i} x {j} = {i*j}")

# i = 0
# while i < 8:
#     i = i + 2
#     for j in range(1, 10):
#         print(f"{i} x {j} = {i*j}")

#5
# x = int(input("숫자1: "))
# y = int(input("숫자2: "))
# z = int(input("숫자3: "))

# nums = [x, y, z]
# max_value = max(a)

# print(f"가장 큰 숫자는 {max_value}입니다.")

# """max_value = nums[0]

# for num in nums:
#     if num > max_value:
#         max_value = num"""

#6
# a = [1, 2, 3, 4, 5]
# b = [i*3 for i in a]
# print(b)

#7
x = input("입력: ")
cnt = 0
for i in x:
    for j in "aeiouAEIOU":
        if i==j:
            cnt = cnt + 1

print(cnt)