import random
print('Добропожаловать в ULA777')
print('Вам начислен бонус 500')
print('Рулетка')
f=True
a=500

while f:
    b=int(input('введите число на которое ставите='))
    c=int(input('Введите сумму='))
    d=random.randint(0,100)
    if a>c:
        a=a-c
        print(d)
        if a<0:
            f=False
            break
        if a>0:
            if d==b:
                a=a+(c*2)
                print('вы победили')
                print('Выпало число=', d)
            if d != b:
                print('Не повезло')
                print('увас осталось=',a)
                print('Выпало число=', d)
        else:
            print('вы ввели не правильную сумму')
    else:
        print('Увас закончились деньги. Выпало число=', d)
        break
