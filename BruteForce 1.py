#BruteForce
#카드 두 뭉치에서 각각 하나의 카드를 뽑아 큰 곱을 만들기
def max_product(left_cards, right_cards):
    max=0
    for a in left_cards:
        for b in right_cards:
            if a*b>max:
                max=a*b
    return max



# 테스트
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))