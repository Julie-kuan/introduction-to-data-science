# -*- coding: utf-8 -*-
"""W4_A105260051_官廷樺.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1K1Wx4tanWcdetKpIZm8z_6cS6FAtA9c_

將目前的攝氏氣溫轉換為華氏氣溫
Fahrenheit = Celsius × 9/5 + 32
"""

current_celsiu = 28
current_fahrenheit = current_celsiu * 9 / 5 + 32
print(current_fahrenheit)

"""將目前的華氏氣溫轉換為攝氏氣溫
Celsius = (Fahrenheit − 32) × 5/9
"""

current_fahrenheit = 82.4
current_celsiu = (current_fahrenheit - 32) * 5 / 9
print(current_celsiu)

"""計算俠客歐尼爾巔峰時期的 BMI 身體質量指
數
NBA 史上最偉大的中鋒之一「柴油引擎」俠客歐尼爾（Shaquille O’Neal）巔峰時期的身高為 216 公分、體重為 147 公斤。
"""

shaq_height = 2.16
shaq_weight = 147
shaq_bmi = shaq_weight / shaq_height**2
print(shaq_bmi)

"""隨堂練習：What did Ross say?
Let's put aside the fact that you "accidentally" pick up my grandmother's ring.
"""

ross_said = """Let's put aside the fact that you "accidentally" pick up my grandmother's ring."""
print(ross_said)

"""隨堂練習：
讓使用者輸入城市名稱與天氣，並印出「我在OOO，天氣OOO」
"""

city = input("請輸入你在的城市")
 weather = input("請輸入你目前的天氣")

print("我在{}，天氣{}".format(city, weather))

"""隨堂練習： 球員 BMI 與過重判斷

以 input() 函數請使用者輸入球員姓名、身高與體重

計算球員的 BMI 並且印出

超過 30 代表過重，請印出判斷結果
"""

player_name = input("請輸入球員姓名")
height = input("請輸入球員的身高(cm)")
weight = input("請輸入球員的體重(kg)")

height = int(height)
weight = int(weight)
player_bmi = weight / (height/100)**2
print(player_bmi)

player_bmi = float(player_bmi) 
print("{}的身體質量指數為：{:.2f}".format(player_name, player_bmi))
print("{}是否過重：{}".format(player_name, player_bmi > 30))