# 교재 70p 엡실론 관련 예제
import sys

# 엡실론 출력
print(sys.float_info.epsilon) # 2.220446049250313e-16

# 부동소수점 수의 오차 검사
a = 0.1 + 0.1 + 0.1
b = 0.3
print(a - b)    # 5.551115123125783e-17
if abs(a - b) < sys.float_info.epsilon:
    print("a와 b는 같은 값입니다.")  # 이 코드 출력
else:
    print("a와 b는 다른 값입니다.")
