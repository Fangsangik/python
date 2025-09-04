# 실습
import time
import csv
import random
import playsound


name = input("이름을 입력하세요: ")
print(f"{name}님, 안녕하세요!")

print("행맨 게임을 시작합니다!")
words = []
with open('./resouces/word_list.csv', 'r') as wr:
    reader = csv.reader(wr)
    next(reader)
    for row in reader :
        words.append(row)

random.shuffle(words)

q = random.choice(words)
word = q[0].strip()  # 단어를 선택하고 양쪽 공백 제거

attempts = 5
guessed_letters = ''

while attempts > 0:
    # 실패 횟수
    failed = 0
    for char in word:
        if char in guessed_letters:
            print(char, end=' ')
        else:
            print("_", end=' ')
            failed += 1

    if failed == 0:
        print(f"축하합니다! {name}님, '{word}'를 맞추셨습니다!")
        break
    print()

    print()
    print('hint : {}',format(q[1].strip()))
    guess = input("한 글자를 추측해 보세요: ")
    guessed_letters += guess

    if guess not in word:
        attempts -= 1
        print(f"틀렸습니다! 남은 기회: {attempts}")

        if attempts == 0:
            print(f"게임 오버! '{word}'가 정답입니다.")


