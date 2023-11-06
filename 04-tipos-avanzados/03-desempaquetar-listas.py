numeros = [1, 2, 3]

primero, *otros = numeros

print(primero)  # 1
print(otros)  # [2,3]

others_nums = [2, 4, 7, 8, 6]

first, *others, last = others_nums
print(first)
print(others)
print(last)
