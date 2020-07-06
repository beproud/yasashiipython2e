bmi = 22
if bmi >= 25:
    result = '肥満'
elif bmi >= 18.5:
    result = '標準体重'
else:
    result = '痩せ型'
print(f'BMIは{bmi}、判定結果は{result}です。')
