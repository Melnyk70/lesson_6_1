# ДЗ 6.1. Діапазон букв
# Користувач вводить через дефіс дві літери, Ваше завдання написати програму, яка повертатиме всі символи між ними включно.
# Жодних перевірок на помилку робити не треба, мінімальне значення завжди менше або дорівнює максимальному.
# Підказка: Використовуйте модуль string , у якому є string.ascii_letters, з усім набором потрібних букв
# Приклад: "a-c" -> abc  "a-a" -> a  "s-H" -> stuvwxyzABCDEFGH  "a-A" -> abcdefghijklmnopqrstuvwxyzA
import string
var_standart=string.ascii_letters
var_str="s-H"
print("\"", var_str, "\" =>", end="")
str_start=var_str[0]
str_end=var_str[-1]
a=var_standart.find(str_start)
b=var_standart.find(str_end)+1
print(var_standart[a:b])
