# Находим цифру в строке

s = input()
flag = 'Цифр нет'
for c in s:                 # считываем каждый символ
    if c in '0123456789':   # проверяем что содержится в символе
        flag = 'Цифра'
        break
print(flag)


