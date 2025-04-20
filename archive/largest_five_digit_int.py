def solution(digits: str) -> int:
    max_val = 0
    for i in range(len(digits) - 4):
        current = int(digits[i:i+5])
        if current > max_val:
            max_val = current
    return max_val

print(solution('1234567898765'))
print(solution('731674765'))
