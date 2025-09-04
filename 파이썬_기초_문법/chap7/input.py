"""
사용자 입력
형변환 입력
입출력
기본 타입(str)로 인식
"""
name = input("Enter your name: ")
grade = input("Enter your grade: ")
company = input("Enter your company name: ")

print('name : ', name, 'grade : ', grade, 'company : ', company)

number = input("Enter a number: ")
name = input("Enter your name: ")
print('type of number : ', type(number))

# 형 변환
first_number = int(input("Enter a number: "))
second_number = int(input("Enter another number: "))
total = first_number + second_number
print('total : ', type(total), total)

float_number = float(input("Enter a float number: "))
print('type of float_number : ', type(float_number), float_number)

print('FirstName - {0}, LastName - {1}'.format(input('Enter first name : ') , input('Enter last name : ')))