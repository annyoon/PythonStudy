# 동전의 개수와 화폐 단위 입력
n = int(input())
money = list(map(int, input().split()))

# 동전 크기 순으로 정렬
money.sort()

sum = 1
for m in money:
    # 지금까지의 동전 합 + 1보다 다음 동전이 더 크면 break
    if m <= sum:
        sum += m
    else:
        break
        
print(sum)

