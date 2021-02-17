# 문자열 입력
s = list(map(int, input()))
num = s[0]

# 연산할 숫자가 0이나 1일 경우 덧셈
for i in range(1, len(s)):
    if num < 2 or s[i] < 2:
        num = num + s[i]
    else: # 0이나 1이 아닐 경우 곱셈
        num = num * s[i]
        
print(num)

