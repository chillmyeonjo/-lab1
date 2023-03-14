def d():
    from random import randint

    x=0
    while x<3:
        a=int(randint(0,20))
        b=int(randint(0,20))
        y =int(input(print(a,"+",b,"= ")))

        if a+b == y:
            print('Правильно')
        else:
            print('Не верно')
            x=x+1
    if x==3:
        print('Игра окончена')

d()