import random
secrets = random.randint(1,100)
guesses =  []
print(f"正确数字为：{secrets}")
print("数字范围：1~100")
while True:
    guess = int(input("输入数字:"))
    guesses.append(guess)
    if guess < secrets:
        print("小了")
    elif guess > secrets:
        print("大了")
    else:
        print("对了")
        print(f"猜测轨迹：{guesses}")
        break
