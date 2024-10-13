# ДЗ 6.1. Діапазон букв
import string
var_standart=string.ascii_letters
var_str="s-H"
print("\"", var_str, "\" =>", end="")
str_start=var_str[0]
str_end=var_str[-1]
a=var_standart.find(str_start)
b=var_standart.find(str_end)+1
print(var_standart[a:b])
