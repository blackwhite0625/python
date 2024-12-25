import random

def number_guess_game():
    """
    幾A幾B遊戲：玩家猜測隨機生成的 4 位數字，給出幾A幾B 的提示。
    """
    # 隨機生成 4 個不重複的數字
    answer = random.sample(range(0, 10), 4)
    print("遊戲開始！隨機生成了一組 4 位不重複的數字。")
    print("輸入 'exit' 可退出遊戲。")

    while True:
        guess = input("請輸入你的猜測（4 個不重複的數字）：")
        if guess.lower() == "exit":
            print("遊戲已退出，再見！")
            break

        if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
            print("輸入不合法，請重新輸入 4 個不重複的數字。")
            continue

        guess = [int(digit) for digit in guess]
        
        # 計算 A 和 B 的數量
        A = sum(1 for i in range(4) if guess[i] == answer[i])
        B = sum(1 for digit in guess if digit in answer) - A

        print(f"結果：{A}A{B}B")

        if A == 4:
            print("恭喜你猜對了！")
            break

if __name__ == "__main__":
    number_guess_game()
