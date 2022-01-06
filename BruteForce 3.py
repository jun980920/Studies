#건물 사이의 빗물량 구하기
#건물의 높이는 리스트 내 숫자로 표현
def trapping_rain(buildings):
    rain=0
    for i in range(1, len(buildings)-1):
        left_max=max(buildings[:i])
        right_max=max(buildings[i+1:])
        second_big=min(left_max, right_max)
        if second_big>buildings[i]:
            rain+=second_big-buildings[i]
    return rain
# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
