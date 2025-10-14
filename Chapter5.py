#1
# x = int(input("첫 번째 숫자: "))
# y = int(input("두 번째 숫자: "))
# if x > y:
#     print("첫 번쨰 숫자가 더 큼")
# elif x < y:
#     print("두 번째 숫자가 더 큼")
# else:
#     print("두 숫자는 같음")

#2
# score = int(input("점수: "))
# if score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:
#     grade = "C"
# elif score >= 60:
#     grade = "D"
# else:
#     grade = "F"

# print("학점:", grade)

#3
# x = int(input("숫자: "))
# if x % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")

#4
# x = ["apple", "banana", "cherry"]
# y = input("과일: ")
# if y in x:
#     print("포함됨")
# else:
#     print("포함되지않음")

#5
# x = int(input("첫 번째 점수: "))
# y = int(input("두 번째 점수: "))
# z = (x + y)/2
# if z >= 60:
#     print(f"평균 점수는 {z}점으로 합격")
# else:
#     print(f"평균 점수는 {z}점으로 불합격")

#6
# x = input("")
# if x in "python":
#     print("포함")
# else:
#     print("포함되지 않음")

#7
# x = int(input("첫 번째 숫자: "))
# y = int(input("두 번째 숫자: "))
# if x >= 10 and y >= 10:
#     print("두 숫자 모두 10 이상입니다")
# elif x >= 10 or y >= 10:
#     print("한 숫자만 10 이상입니다")  
# else:
#     print("두 숫자 모두 10 미만입니다")

#8
# x = int(input("연도: "))
# if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0):
#     print("윤년")
# else:
#     print("평년")

#9
# height = float(input("키(미터): "))
# weight = float(int(input("몸무게(킬로그램): ")))
# bmi = weight / (height ** 2)
# if bmi < 18.5:
#     status = "저체중"
# elif bmi < 24.9:
#     status = "정상체중"
# elif bmi < 29.9:
#     status = "과체중"
# else:
#     status = "비만"

# print(f"BMI: {bmi:.1f}")
# print(f"상태: {status}")

#10
# num = int(input("숫자를 입력하세요(1~7): "))
# if num == 1:
#     print("월요일")
# elif num == 2:
#     print("화요일")
# elif num == 3:
#     print("수요일")
# elif num == 4:
#     print("목요일")
# elif num == 5:
#     print("금요일")
# elif num == 6:
#     print("토요일")
# elif num == 7:
#     print("일요일")
# else:
#     print("잘못된 입력")