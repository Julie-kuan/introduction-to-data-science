# -*- coding: utf-8 -*-
"""W6-A105260051-官廷樺.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rFFOVAU_jh4il4nxwTkVfPMhbL7uD2qO

隨堂練習 : 判斷身分證字號的尾數是否為奇數
"""

id_last_digit = input("請輸入您的身分證字號的尾數 : ")
id_last_digit = int(id_last_digit)
print(id_last_digit)
print(type(id_last_digit))
modulo = id_last_digit % 2
ans =modulo == 1
print(ans)

