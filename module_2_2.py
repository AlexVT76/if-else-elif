first=input('Введите первое число: ')
second=input('Введите второе число: ')
third=input('Введите третье число: ')
if first==second==third :
    print(3)
elif first==second or first==third or third==second:
    print(2)
else:
    print(0)
