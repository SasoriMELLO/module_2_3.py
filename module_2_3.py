my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
while True:
    number = int(input('Введите число'))
    if number>0:
        print(number)
    if number==0:
        continue
    if number<0:
        break
