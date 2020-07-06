weights_str = input('体重(kg)をカンマ区切りで入力してください: ')
weight_str_list = weights_str.split(',')

weight_list = []
for weight_str in weight_str_list:
    weight = int(weight_str)
    weight_list.append(weight)

height_str = input('身長(cm)を入力してください: ')
height = int(height_str)

for weight in weight_list:
    bmi = weight / (height / 100) ** 2
    if bmi >= 25:
        result = '肥満'
    elif bmi >= 18.5:
        result = '標準体重'
    else:
        result = '痩せ型'
    print(f'身長{height}cm、体重{weight}kgのBMIは{bmi}')
    print(f'判定結果は{result}です。')
