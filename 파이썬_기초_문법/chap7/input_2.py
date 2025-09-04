# int형으로 인식 되어 있는 중 -> String 값으로 input 값을 넣었을때

# 예외 처리
# try:
#     n = int(input("Enter a number: "))
#     print("You entered:", n)
# except ValueError as e:
#     print("Invalid input! Please enter a valid number.")

# 올바른 값을 입력 완료 지속
# while True:
while True:
    try:
        n = int(input("Enter a number: "))
        print("You entered:", n)
        break  # 올바른 값을 입력하면 반복 종료
    except ValueError as e:
        print("Invalid input! Please enter a valid number.")