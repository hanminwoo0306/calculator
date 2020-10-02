# -*- coding: utf-8 -*- 

age = input('당신의 나이는? : ')
month_money = input('월 생활비는? : ')
year_money = int(month_money) * 12
CAGR = float(input('연복리 수익률(%)는? : '))
i = int(input('물가상승률(%)은? : '))
n = int(input('은퇴까지 얼마나 더 일할 수 있나요? (일할 수 있는 남은 햇수): '))

# print((1 + i/100) ** n)

budget = int((year_money * (1 + i/100)**n) / (CAGR/100 - i/100))
budget_uk = round(budget / 100000000, 1)
# print(budget_uk)

print('-'*20)
# print('당신의 나이는: ' + str(age))
# print('당신의 월 생활비는: ' + str(month_money))
# print('당신의 년 생활비는: ' + str(year_money))
# print('당신의 연복리 수익률(%)은: ' + str(CAGR) + '%')
# print('물가상승률(%)은: ' + str(i) + '%')
# print('은퇴까지 일할 수 있는 기간(연): ' + str(n))
# print('-'*20)
print('당신의 은퇴 자금은: ' + str(budget))
print('당신의 은퇴 자금은: 약' + str(budget_uk) + '억원')

# 주석을 추가합니다.
# 주석을 제거합니다.