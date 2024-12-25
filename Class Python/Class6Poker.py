import random

# 定義撲克牌數值和花色
suits = ["♠", "♥", "♦", "♣"]  # 黑桃、紅心、方塊、梅花
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

def generate_hand():
    """
    隨機生成一手 5 張撲克牌。
    """
    deck = [f"{value}{suit}" for value in values for suit in suits]
    random.shuffle(deck)
    return deck[:5]

def analyze_hand(hand):
    """
    分析手牌是否為一對、順子、葫蘆、鐵支或同花順。
    :param hand: 5 張撲克牌組成的列表
    :return: 牌型的名稱
    """
    # 提取數值和花色
    card_values = [card[:-1] for card in hand]
    card_suits = [card[-1] for card in hand]

    # 將數值轉換為可排序的數字列表
    value_order = {v: i for i, v in enumerate(values)}
    card_ranks = sorted([value_order[v] for v in card_values])

    # 檢查是否為同花
    is_flush = len(set(card_suits)) == 1

    # 檢查是否為順子
    is_straight = all(card_ranks[i] + 1 == card_ranks[i + 1] for i in range(len(card_ranks) - 1))
    if card_ranks == [0, 1, 2, 3, 12]:  # 處理 A, 2, 3, 4, 5 的特殊順子情況
        is_straight = True

    # 檢查數值的出現次數
    from collections import Counter
    value_counts = Counter(card_values).values()

    if is_flush and is_straight:
        return "同花順"
    elif 4 in value_counts:
        return "鐵支"
    elif 3 in value_counts and 2 in value_counts:
        return "葫蘆"
    elif is_straight:
        return "順子"
    elif 2 in value_counts:
        return "一對"
    else:
        return "其他"

def main():
    """
    主函式：產生撲克牌並檢測牌型。
    """
    hand = generate_hand()
    print("抽到的手牌: ", hand)
    result = analyze_hand(hand)
    print("牌型: ", result)

if __name__ == "__main__":
    main()
