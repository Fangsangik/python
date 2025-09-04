# 실습
import time

name = input("이름을 입력하세요: ")
print(f"{name}님, 안녕하세요!")

print("행맨 게임을 시작합니다!")
word = "python"
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
    guess = input("한 글자를 추측해 보세요: ")
    guessed_letters += guess

    if guess not in word:
        attempts -= 1
        print(f"틀렸습니다! 남은 기회: {attempts}")

        if attempts == 0:
            print(f"게임 오버! '{word}'가 정답입니다.")



